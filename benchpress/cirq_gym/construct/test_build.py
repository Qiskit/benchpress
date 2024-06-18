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
import cirq
from cirq.contrib.qasm_import import circuit_from_qasm

from benchpress.config import Config
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.build import WorkoutCircuitConstruction

from benchpress.cirq_gym.circuits import cirq_QV, multi_control_circuit, dtc_unitary

SEED = 12345


@benchpress_test_validation
class TestWorkoutCircuitConstruction(WorkoutCircuitConstruction):
    def test_QV100_build(self, benchmark):
        """Measures an SDKs ability to build a 100Q
        QV circit from scratch.
        """

        @benchmark
        def result():
            out = cirq_QV(100, 100, seed=12345)
            return out

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
            initial_state = cirq.Circuit()
            dtc_circuit = dtc_unitary(num_qubits, g=0.95, seed=SEED)

            circs = [initial_state]
            for tt in range(max_cycles):
                qc = circs[tt].copy()
                qc += dtc_circuit
                circs.append(qc)
            return circs[-1]

        assert True

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

    def test_QV100_qasm2_import(self, benchmark):
        """QASM import of QV100 circuit"""

        @benchmark
        def result():
            with open(Config.get_qasm_dir("qv") + "qv_N100_12345.qasm", "r") as file:
                data = file.read()
            out = circuit_from_qasm(data)
            return out

        assert len(list(result.findall_operations_with_gate_type(cirq.Rz))) == 120000
        assert len(list(result.findall_operations_with_gate_type(cirq.Rx))) == 80000
        assert (
            len(list(result.findall_operations_with_gate_type(cirq.CNotPowGate)))
            == 15000
        )
