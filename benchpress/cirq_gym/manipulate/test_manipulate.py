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
import random

import cirq
from cirq import ops, protocols
from cirq.transformers.analytical_decompositions import two_qubit_to_cz
from cirq.transformers.target_gatesets import compilation_target_gateset
from typing import Any, Dict, Sequence, Type, Union

from benchpress.utilities.io import qasm_circuit_loader
from benchpress.config import Configuration
from benchpress.utilities.io import output_circuit_properties
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.manipulate import WorkoutCircuitManipulate
from benchpress.cirq_gym.circuits import multi_control_circuit


CNOT_twirling_gates = [
    (cirq.I, cirq.I, cirq.I, cirq.I),
    (cirq.I, cirq.X, cirq.I, cirq.X),
    (cirq.I, cirq.Y, cirq.Z, cirq.Y),
    (cirq.I, cirq.Z, cirq.Z, cirq.Z),
    (cirq.Y, cirq.I, cirq.Y, cirq.X),
    (cirq.Y, cirq.X, cirq.Y, cirq.I),
    (cirq.Y, cirq.Y, cirq.X, cirq.Z),
    (cirq.Y, cirq.Z, cirq.X, cirq.Y),
    (cirq.X, cirq.I, cirq.X, cirq.X),
    (cirq.X, cirq.X, cirq.X, cirq.I),
    (cirq.X, cirq.Y, cirq.Y, cirq.Z),
    (cirq.X, cirq.Z, cirq.Y, cirq.Y),
    (cirq.Z, cirq.I, cirq.Z, cirq.I),
    (cirq.Z, cirq.X, cirq.Z, cirq.X),
    (cirq.Z, cirq.Y, cirq.I, cirq.Y),
    (cirq.Z, cirq.Z, cirq.I, cirq.Z),
]


def _twirl_single_CNOT_gate(op):
    if op.gate != cirq.CNOT:
        return op

    A, B, C, D = random.choice(CNOT_twirling_gates)
    control_qubit, target_qubit = op.qubits
    return [
        A.on(control_qubit),
        B.on(target_qubit),
        op,
        C.on(control_qubit),
        D.on(target_qubit),
    ]


class IBMTargetGateset(compilation_target_gateset.TwoQubitCompilationTargetGateset):
    """Modified from

    https://github.com/quantumlib/Cirq/blob/2975d10912acd4183838f5c1ddba8f278faedb2a/
    cirq-core/cirq/transformers/target_gatesets/cz_gateset.py#L27
    """

    def __init__(
        self,
        *,
        atol: float = 1e-8,
        allow_partial_czs: bool = False,
        additional_gates: Sequence[
            Union[Type["cirq.Gate"], "cirq.Gate", "cirq.GateFamily"]
        ] = (),
        preserve_moment_structure: bool = True,
    ) -> None:
        """Initializes IBMTargetGateset"""
        super().__init__(
            ops.CZ,
            ops.XPowGate(exponent=0.5),
            ops.X,
            ops.Rz,
            ops.MeasurementGate,
            ops.GlobalPhaseGate,
            *additional_gates,
            name="IBMTargetGateset",
            preserve_moment_structure=preserve_moment_structure,
        )
        self.additional_gates = tuple(
            g if isinstance(g, ops.GateFamily) else ops.GateFamily(gate=g)
            for g in additional_gates
        )
        self._additional_gates_repr_str = ", ".join(
            [ops.gateset._gate_str(g, repr) for g in additional_gates]
        )
        self.atol = atol
        self.allow_partial_czs = allow_partial_czs

    def _decompose_two_qubit_operation(self, op: "cirq.Operation", _) -> "cirq.OP_TREE":
        if not protocols.has_unitary(op):
            return NotImplemented
        return two_qubit_to_cz.two_qubit_matrix_to_cz_operations(
            op.qubits[0],
            op.qubits[1],
            protocols.unitary(op),
            allow_partial_czs=self.allow_partial_czs,
            atol=self.atol,
        )

    def __repr__(self) -> str:
        return (
            f"cirq.IBMTargetGateset("
            f"atol={self.atol}, "
            f"allow_partial_czs={self.allow_partial_czs}, "
            f"additional_gates=[{self._additional_gates_repr_str}]"
            f")"
        )

    def _value_equality_values_(self) -> Any:
        return self.atol, self.allow_partial_czs, frozenset(self.additional_gates)

    def _json_dict_(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {
            "atol": self.atol,
            "allow_partial_czs": self.allow_partial_czs,
        }
        if self.additional_gates:
            d["additional_gates"] = list(self.additional_gates)
        return d

    @classmethod
    def _from_json_dict_(cls, atol, allow_partial_czs, additional_gates=(), **kwargs):
        return cls(
            atol=atol,
            allow_partial_czs=allow_partial_czs,
            additional_gates=additional_gates,
        )


@benchpress_test_validation
class TestWorkoutCircuitManipulate(WorkoutCircuitManipulate):
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q QV
        circuit
        """
        circuit = qasm_circuit_loader(
            Configuration.get_qasm_dir("dtc") + "dtc_100_cx_12345.qasm", benchmark
        )

        @benchmark
        def result():
            twirled_circuit = circuit.map_operations(_twirl_single_CNOT_gate)
            return twirled_circuit

        assert result

    def test_QV100_basis_change(self, benchmark):
        """Change a QV100 circuit basis from [rx, ry, rz, cx]
        to [sx, x, rz, cz]
        """
        circ = qasm_circuit_loader(
            Configuration.get_qasm_dir("qv") + "qv_N100_12345.qasm", benchmark
        )

        @benchmark
        def result():
            out = cirq.optimize_for_target_gateset(circ, gateset=IBMTargetGateset())
            return out

        output_circuit_properties(result, "CXPowGate", benchmark)
        assert result

    def test_multi_control_decompose(self, benchmark):
        """Decompose a multi-control gate into the
        basis [rx, ry, rz, cz]

        Note:
            This basis works by default in Cirq.  However,
            there are extra _* operations as well.  Will
            calling this passing regardless.
        """
        circ = multi_control_circuit(16)

        @benchmark
        def result():
            out = cirq.optimize_for_target_gateset(circ)
            return out

        output_circuit_properties(result, "CZPowGate", benchmark)
        assert result

    def test_random_clifford_decompose(self, benchmark):
        """Decompose a random clifford into
        basis [rz, sx, x, cz]
        """
        circuit = qasm_circuit_loader(
            Configuration.get_qasm_dir("clifford") + "clifford_20_12345.qasm", benchmark
        )

        @benchmark
        def result():
            out = cirq.optimize_for_target_gateset(circuit, gateset=IBMTargetGateset())
            return out

        output_circuit_properties(result, "CZPowGate", benchmark)
        assert result
