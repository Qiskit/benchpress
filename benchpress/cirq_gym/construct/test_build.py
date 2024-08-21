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
from benchpress.utilities.io import output_circuit_properties
from benchpress.config import Configuration
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.build import WorkoutCircuitConstruction

from benchpress.cirq_gym.circuits import (
    cirq_QV,
    multi_control_circuit,
    dtc_unitary,
    cirq_circSU2,
    cirq_random_clifford,
)

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

        output_circuit_properties(result, "MatrixGate", benchmark)
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

        output_circuit_properties(result, "ZZPowGate", benchmark)
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
            with open(
                Configuration.get_qasm_dir("qv") + "qv_N100_12345.qasm", "r"
            ) as file:
                data = file.read()
            out = circuit_from_qasm(data)
            return out

        output_circuit_properties(result, "CXPowGate", benchmark)
        assert len(list(result.findall_operations_with_gate_type(cirq.Rz))) == 120000
        assert len(list(result.findall_operations_with_gate_type(cirq.Rx))) == 80000
        assert (
            len(list(result.findall_operations_with_gate_type(cirq.CNotPowGate)))
            == 15000
        )

    def test_bigint_qasm2_import(self, benchmark):
        """QASM import with bigint"""

        @benchmark
        def result():
            with open(
                Configuration.get_qasm_dir("bigint") + "bigint.qasm", "r"
            ) as file:
                data = file.read()
            out = circuit_from_qasm(data)
            return out

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
            out = cirq_circSU2(N, 4)
            return out

        output_circuit_properties(result, "CXPowGate", benchmark)
        assert len(cirq.parameter_names(result)) == 1000

    def test_param_circSU2_100_bind(self, benchmark):
        """Measures an SDKs ability to bind 1000 parameters
        to efficient SU2 circuit over 100Q with circular
        entanglement and 4 repetitions.
        """
        N = 100
        qc = cirq_circSU2(N, 4)
        assert len(cirq.parameter_names(qc)) == 1000

        @benchmark
        def result():
            # Here we put parameter dict building in the timing as it is
            # a required step for binding
            param_names = cirq.parameter_names(qc)
            vals = np.linspace(0, 2 * np.pi, len(param_names))
            param_dict = dict(zip(param_names, vals))
            out = cirq.resolve_parameters(qc, param_dict)
            return out

        output_circuit_properties(result, "CXPowGate", benchmark)
        assert len(cirq.parameter_names(result)) == 0

    def test_clifford_build(self, benchmark):
        """Measures an SDKs ability to build a 100Q
        random Clifford circuit from scratch.
        """

        @benchmark
        def result():
            cirq_random_clifford(100, seed=SEED)
            return True

        assert result
