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
import sys

from benchpress.qpanda_gym.circuits.circuits import qpanda_QV, qpanda_circSU2_vqc
from benchpress.qpanda_gym.circuits import (
    qpanda_circSU2,
    qpanda_QV,
    qpanda_random_clifford,
    dtc_unitary,
    multi_control_circuit,
)

from benchpress.config import Configuration
from benchpress.utilities.io import output_circuit_properties
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.build import WorkoutCircuitConstruction
import pyqpanda3.core as pq_core
from pyqpanda3.intermediate_compiler import * 
SEED = 12345


@benchpress_test_validation
class TestWorkoutCircuitConstruction(WorkoutCircuitConstruction):
    def test_QV100_build(self, benchmark):
        """Measures an SDKs ability to build a 100Q
        QV circuit from scratch.
        """

        @benchmark
        def result():
            out = qpanda_QV(100, 100, seed=SEED)
            return out

        output_circuit_properties(result, 'Oracle', benchmark)
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
            initial_state = pq_core.QCircuit(num_qubits)
            circs = [initial_state]
            dtc_circuit = dtc_unitary(num_qubits)
            for tt in range(max_cycles):
                qc = circs[tt]
                qc << dtc_circuit
                circs.append(qc)
            return circs[-1]

        output_circuit_properties(result, 'RZZ', benchmark)
        assert result

    def test_clifford_build(self, benchmark):
        """Measures an SDKs ability to build a 100Q
        Clifford circuit from scratch.
        """

        @benchmark
        def result():
            out = qpanda_random_clifford(100, seed=SEED)
            return out

        assert result

    def test_multi_control_circuit(self, benchmark):
        """Measures an SDKs ability to build a circuit
        with a multi-controlled X-gate
        """
        ITER_CIRCUIT_WIDTH = 16

        @benchmark
        def result():
            out = multi_control_circuit(ITER_CIRCUIT_WIDTH)
            return out

        assert True

    def test_param_circSU2_100_build(self, benchmark):
        """Measures an SDKs ability to build a
        parameterized efficient SU2 circuit with circular entanglement
        over 100Q utilizing 4 repetitions.  This will yield a
        circuit with 1000 parameters
        """
        N = 100

        @benchmark
        def result():
            out = qpanda_circSU2(N, 4)
            return out

        output_circuit_properties(result, 'CNOT', benchmark)
        assert result

    def test_param_circSU2_100_bind(self, benchmark):
        """Measures an SDKs ability to bind 1000 parameters
        to efficient SU2 circuit over 100Q with circular
        entanglement and 4 repetitions.
        """
        N = 100
        qc = qpanda_circSU2_vqc(N, 4)
        assert True

        @benchmark
        def result():
            # Here we put parameter dict building in the timing as it is
            # a required step for binding
            tmp = 2
            width = N
            num_resp = 5
            qcircuit_num = 1
            params = np.random.uniform(-3.1415926, 3.1415926, size=[qcircuit_num, tmp, width, num_resp])
            vqres = qc(params)
            return vqres.at([0])

        output_circuit_properties(result, 'CNOT', benchmark)
        assert result

    def test_QV100_qasm2_import(self, benchmark):
        """QASM import of QV100 circuit"""

        @benchmark
        def result():

            out = convert_qasm_file_to_qprog(
                Configuration.get_qasm_dir("qv") + "qv_N100_12345.qasm"
            )
            return out

        output_circuit_properties(result, 'CNOT', benchmark)
        assert result.count_ops(False).get('CNOT') == 15000

    def test_bigint_qasm2_import(self, benchmark):
        """QASM import circuit with bigint"""

        @benchmark
        def result():
            out = convert_qasm_file_to_qprog(
                Configuration.get_qasm_dir("bigint") + "bigint.qasm"
            )
            return out

        output_circuit_properties(result, "CNOT", benchmark)
        assert result
