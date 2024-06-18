# This code is part of Qiskit.
#
# (C) Copyright IBM 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""Test circuit manipulation"""
import pytest
import numpy as np
from bqskit import Circuit, MachineModel, compile
from bqskit.compiler import Compiler
from bqskit.ir.gates import (
    CNOTGate,
    IdentityGate,
    XGate,
    YGate,
    ZGate,
    ControlledGate,
    CZGate,
    RXGate,
    RYGate,
    RZGate,
    SqrtXGate,
    XGate,
)

from benchpress.config import Config
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.manipulate import WorkoutCircuitManipulate
from benchpress.utilities.args import get_args

args = get_args(filename=Config.get_args_file())

TWIRLING_SETS = {
    "CNOTGate": [
        [IdentityGate(), ZGate(), ZGate(), ZGate()],
        [IdentityGate(), XGate(), IdentityGate(), XGate()],
        [IdentityGate(), YGate(), ZGate(), YGate()],
        [IdentityGate(), IdentityGate(), IdentityGate(), IdentityGate()],
        [ZGate(), XGate(), ZGate(), XGate()],
        [ZGate(), YGate(), IdentityGate(), YGate()],
        [ZGate(), IdentityGate(), ZGate(), IdentityGate()],
        [ZGate(), ZGate(), IdentityGate(), ZGate()],
        [XGate(), YGate(), YGate(), ZGate()],
        [XGate(), IdentityGate(), XGate(), XGate()],
        [XGate(), ZGate(), YGate(), YGate()],
        [XGate(), XGate(), XGate(), IdentityGate()],
        [YGate(), IdentityGate(), YGate(), XGate()],
        [YGate(), ZGate(), XGate(), YGate()],
        [YGate(), XGate(), YGate(), IdentityGate()],
        [YGate(), YGate(), XGate(), ZGate()],
    ],
    "CZGate": [
        [IdentityGate(), ZGate(), IdentityGate(), ZGate()],
        [IdentityGate(), XGate(), ZGate(), XGate()],
        [IdentityGate(), YGate(), ZGate(), YGate()],
        [IdentityGate(), IdentityGate(), IdentityGate(), IdentityGate()],
        [ZGate(), XGate(), IdentityGate(), XGate()],
        [ZGate(), YGate(), IdentityGate(), YGate()],
        [ZGate(), IdentityGate(), ZGate(), IdentityGate()],
        [ZGate(), ZGate(), ZGate(), ZGate()],
        [XGate(), YGate(), YGate(), XGate()],
        [XGate(), IdentityGate(), XGate(), ZGate()],
        [XGate(), ZGate(), XGate(), IdentityGate()],
        [XGate(), XGate(), YGate(), YGate()],
        [YGate(), IdentityGate(), YGate(), ZGate()],
        [YGate(), ZGate(), YGate(), IdentityGate()],
        [YGate(), XGate(), XGate(), YGate()],
        [YGate(), YGate(), XGate(), XGate()],
    ],
}


@benchpress_test_validation
class TestWorkoutCircuitManipulate(WorkoutCircuitManipulate):
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q QV
        circuit
        """
        circuit = Circuit.from_file(
            Config.get_qasm_dir("dtc") + "dtc_100_cx_12345.qasm"
        )

        @benchmark
        def result():
            twirled_circuit = direct_twirl(circuit)
            return twirled_circuit

        assert result
        assert 4 * circuit.gate_counts[CNOTGate()] == (
            result.gate_counts[XGate()]
            + result.gate_counts[YGate()]
            + result.gate_counts[ZGate()]
            + result.gate_counts[IdentityGate()]
        )

    @pytest.mark.xfail(
        reason="Runs out of memory (128GB RAM) for 16Q MCX gate", run=False
    )
    def test_multi_control_decompose(self, benchmark):
        """Decompose a multi-control gate into the
        basis [rx, ry, rz, cz]
        """
        N = 16
        mcx = ControlledGate(gate=XGate(), num_controls=N - 1)
        circ = Circuit(num_qudits=N)
        circ.append_gate(mcx(), list(range(N)))
        model = MachineModel(
            num_qudits=N, gate_set={RXGate(), RYGate(), RZGate(), CZGate()}
        )

        @benchmark
        def result():
            out_circuit = compile(
                circ,
                model=model,
                optimization_level=args["bqskit_optimization_level"],
                max_synthesis_size=N,
                compiler=Compiler(),
                seed=0,
            )
            return out_circuit

        benchmark.extra_info["gate_count_2q"] = result.gate_counts[CZGate()]
        assert result

    def test_QV100_basis_change(self, benchmark):
        """Change a QV100 circuit basis from [rx, ry, rz, cx]
        to [sx, x, rz, cz]
        """
        qasm_file = Config.get_qasm_dir("qv") + "qv_N100_12345.qasm"
        circ = Circuit.from_file(qasm_file)

        model = MachineModel(
            num_qudits=circ.num_qudits,
            gate_set={SqrtXGate(), XGate(), RZGate(), CZGate()},
        )

        @benchmark
        def result():
            out = compile(
                input=circ,
                model=model,
                optimization_level=args["bqskit_optimization_level"],
                compiler=Compiler(),
                seed=0,
            )
            return out

        assert result


def direct_twirl(input_circ, twirled_gate="CNOTGate", seed=None):
    new_circ = Circuit(input_circ.num_qudits)
    RNG = np.random.default_rng(seed)
    twirling_set = TWIRLING_SETS[twirled_gate]
    for op in input_circ:
        if op.gate.name == "CNOTGate":
            q0, q1 = op.location
            twirl_idx = RNG.integers(0, 16)
            twirl_gates = twirling_set[twirl_idx]

            new_circ.append_gate(twirl_gates[0], [q0])
            new_circ.append_gate(twirl_gates[1], [q1])
            new_circ.append(op)
            new_circ.append_gate(twirl_gates[2], [q0])
            new_circ.append_gate(twirl_gates[3], [q1])
        else:
            new_circ.append(op)

    return new_circ
