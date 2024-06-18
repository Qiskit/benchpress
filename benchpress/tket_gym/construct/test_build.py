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
"""Test circuit generation"""
import numpy as np
from pytket.circuit import Circuit, OpType
from pytket.qasm import circuit_from_qasm

from benchpress.tket_gym.circuits import (
    tket_circSU2,
    tket_QV,
    dtc_unitary,
    multi_control_circuit,
)

from benchpress.config import Config
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.build import WorkoutCircuitConstruction

SEED = 12345


@benchpress_test_validation
class TestWorkoutCircuitConstruction(WorkoutCircuitConstruction):
    def test_QV100_build(self, benchmark):
        """Measures an SDKs ability to build a 100Q
        QV circit from scratch.
        """

        @benchmark
        def result():
            tket_QV(100, 100, seed=SEED)
            return True

        assert result

    def test_DTC100_set_build(self, benchmark):
        """Measures an SDKs ability to build a set
        of 100Q DTC circuits out to 100 layers of
        the underlying unitary
        """
        max_cycles = 100
        num_qubits = 100

        @benchmark
        def result():
            initial_state = Circuit(num_qubits)
            circs = [initial_state]
            dtc_circuit = dtc_unitary(num_qubits)
            for tt in range(max_cycles):
                qc = circs[tt].copy()
                qc.append(dtc_circuit)
                circs.append(qc)
            return circs[-1]

        assert result.n_gates_of_type(OpType.ZZPhase) == 9900

    def test_multi_control_circuit(self, benchmark):
        """Measures an SDKs ability to build a circuit
        with a multi-controlled X-gate
        """
        ITER_CIRCUIT_WIDTH = 16

        @benchmark
        def result():
            out = multi_control_circuit(ITER_CIRCUIT_WIDTH)
            return True

        assert result

    def test_param_circSU2_100_build(self, benchmark):
        """Measures an SDKs ability to build a
        parameterized efficient SU2 circuit with circular entanglement
        over 100Q utilizing 4 repetitions.  This will yield a
        circuit with 1000 parameters
        """
        N = 100

        @benchmark
        def result():
            out = tket_circSU2(N, 4)
            return out

        assert len(result.free_symbols()) == 1000

    def test_param_circSU2_100_bind(self, benchmark):
        """Measures an SDKs ability to bind 1000 parameters
        to efficient SU2 circuit over 100Q with circular
        entanglement and 4 repetitions.
        """
        N = 100
        qc = tket_circSU2(N, 4)
        assert len(qc.free_symbols()) == 1000

        @benchmark
        def result():
            # Here we put parameter dict building in the timing as it is
            # a required step for binding
            params_dict = {}
            vals = np.linspace(0, 2 * np.pi, len(qc.free_symbols()))
            for idx, param in enumerate(qc.free_symbols()):
                params_dict[param] = vals[idx]
            out = qc.copy()
            out.symbol_substitution(params_dict)
            return out

        assert len(result.free_symbols()) == 0

    def test_QV100_qasm2_import(self, benchmark):
        """QASM import of QV100 circuit"""

        @benchmark
        def result():
            out = circuit_from_qasm(Config.get_qasm_dir("qv") + "qv_N100_12345.qasm")
            return out

        assert result.n_gates_of_type(OpType.Rz) == 120000
        assert result.n_gates_of_type(OpType.Rx) == 80000
        assert result.n_gates_of_type(OpType.CX) == 15000
