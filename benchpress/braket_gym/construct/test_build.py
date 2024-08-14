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

from benchpress.config import Configuration
from benchpress.utilities.io import qasm_circuit_loader, output_circuit_properties
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.build import WorkoutCircuitConstruction

from benchpress.braket_gym.circuits import braket_QV, braket_circSU2, dtc_unitary
from braket.circuits import Circuit

SEED = 12345


@benchpress_test_validation
class TestWorkoutCircuitConstruction(WorkoutCircuitConstruction):
    def test_QV100_build(self, benchmark):
        """Measures an SDKs ability to build a 100Q
        QV circit from scratch.
        """

        @benchmark
        def result():
            out = braket_QV(100, 100)
            return out

        output_circuit_properties(result, "Unitary", benchmark)
        assert True

    def test_DTC100_set_build(self, benchmark):
        """Measures an SDKs ability to build a set
        of 100Q DTC circuits out to 100 layers of
        the underlying unitary
        """
        max_cycles = 100
        num_qubits = 100

        @benchmark
        def result():
            initial_state = Circuit()
            circs = [initial_state.copy()]
            dtc_circuit = dtc_unitary(num_qubits)
            for tt in range(max_cycles):
                qc = circs[tt].copy()
                qc += dtc_circuit
                circs.append(qc)
            return circs[-1]

        output_circuit_properties(result, "ZZ", benchmark)
        assert result

    def test_multi_control_circuit(self, benchmark):
        """Measures an SDKs ability to build a circuit
        with a multi-controlled X-gate
        """
        ITER_CIRCUIT_WIDTH = 16

        @benchmark
        def result():
            out = Circuit()
            out.x(0)
            for kk in range(ITER_CIRCUIT_WIDTH):
                out.x(kk + 1, control=range(kk + 1))
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
            out = braket_circSU2(N, 4)
            return out

        output_circuit_properties(result, "CNot", benchmark)
        assert len(result.parameters) == 1000

    def test_param_circSU2_100_bind(self, benchmark):
        """Measures an SDKs ability to bind 1000 parameters
        to efficient SU2 circuit over 100Q with circular
        entanglement and 4 repetitions.
        """
        N = 100
        qc = braket_circSU2(N, 4)

        @benchmark
        def result():
            # Here we put parameter dict building in the timing
            # as it is required for binding
            params_dict = {}
            vals = np.linspace(0, 2 * np.pi, len(qc.parameters))
            for idx, param in enumerate(qc.parameters):
                params_dict[param.name] = vals[idx]
            out = qc.make_bound_circuit(params_dict)
            return out

        output_circuit_properties(result, "CNot", benchmark)
        assert result.parameters == set()

    def test_QV100_qasm2_import(self, benchmark):
        """QASM import of QV100 circuit"""

        @benchmark
        def result():
            circuit = qasm_circuit_loader(
                Configuration.get_qasm_dir("qv") + "qv_N100_12345.qasm", benchmark
            )
            return circuit

        output_circuit_properties(result, "CNot", benchmark)
        assert result

    def test_bigint_qasm2_import(self, benchmark):
        """QASM import of circuit with bigint"""

        @benchmark
        def result():
            circuit = qasm_circuit_loader(
                Configuration.get_qasm_dir("bigint") + "bigint.qasm", benchmark
            )
            return circuit

        assert result
