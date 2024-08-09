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
"""Test summit benchmarks"""

from qiskit.circuit.library import EfficientSU2

from qiskit_transpiler_service.transpiler_service import TranspilerService

from benchpress.config import Configuration
from benchpress.qiskit_gym.circuits import bv_all_ones
from benchpress.utilities.io import (qasm_circuit_loader, input_circuit_properties,
                                     output_circuit_properties)
from benchpress.utilities.validation import circuit_validator
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceTranspile100Q
from benchpress.qiskit_gym.circuits import trivial_bvlike_circuit

BACKEND = Configuration.backend()
TWO_Q_GATE = BACKEND.two_q_gate_type
OPTIMIZATION_LEVEL = Configuration.options["qiskit"]["optimization_level"]

TRANS_SERVICE = TranspilerService(
    coupling_map=list(BACKEND.coupling_map.get_edges()),
    qiskit_transpile_options={"basis_gates": BACKEND.operation_names},
    ai=True,
    optimization_level=OPTIMIZATION_LEVEL,
    timeout=3600,
)


@benchpress_test_validation
class TestWorkoutDeviceTranspile100Q(WorkoutDeviceTranspile100Q):
    def test_QFT_100_transpile(self, benchmark):
        """Compile 100Q QFT circuit against target backend"""
        circuit = qasm_circuit_loader(
            Configuration.get_qasm_dir("qft") + "qft_N100.qasm", benchmark
        )

        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, BACKEND)

    def test_QV_100_transpile(self, benchmark):
        """Compile 10Q QV circuit against target backend"""
        circuit = qasm_circuit_loader(
            Configuration.get_qasm_dir("qv") + "qv_N100_12345.qasm", benchmark
        )

        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, BACKEND)

    def test_circSU2_89_transpile(self, benchmark):
        """Compile 89Q circSU2 circuit against target backend"""
        circuit = EfficientSU2(89, reps=3, entanglement="circular")
        input_circuit_properties(circuit, benchmark)
        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, BACKEND)

    def test_circSU2_100_transpile(self, benchmark):
        """Compile 100Q circSU2 circuit against target backend"""
        circuit = EfficientSU2(100, reps=3, entanglement="circular")
        input_circuit_properties(circuit, benchmark)
        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, BACKEND)

    def test_BV_100_transpile(self, benchmark):
        """Compile 100Q BV circuit against target backend"""
        circuit = bv_all_ones(100)
        input_circuit_properties(circuit, benchmark)
        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, BACKEND)

    def test_square_heisenberg_100_transpile(self, benchmark):
        """Compile 100Q square-Heisenberg circuit against target backend"""
        circuit = qasm_circuit_loader(
            Configuration.get_qasm_dir("square-heisenberg")
            + "square_heisenberg_N100.qasm",
            benchmark,
        )

        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, BACKEND)

    def test_QAOA_100_transpile(self, benchmark):
        """Compile 100Q QAOA circuit against target backend"""
        circuit = qasm_circuit_loader(
            Configuration.get_qasm_dir("qaoa") + "qaoa_barabasi_albert_N100_3reps.qasm",
            benchmark,
        )

        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, BACKEND)

    def test_BVlike_simplification_transpile(self, benchmark):
        """Transpile a BV-like circuit that should collapse down
        into a single X and Z gate on a target device
        """
        circuit = trivial_bvlike_circuit(100)
        input_circuit_properties(circuit, benchmark)
        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, BACKEND)

    def test_clifford_100_transpile(self, benchmark):
        """Compile 10Q Clifford circuit against target backend"""
        circuit = qasm_circuit_loader(
            Configuration.get_qasm_dir("clifford") + "clifford_100_12345.qasm",
            benchmark,
        )

        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, BACKEND)
