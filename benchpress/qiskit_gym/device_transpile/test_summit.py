"""Test summit benchmarks"""

import pytest
from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import EfficientSU2
from qiskit.transpiler.passes import StarPreRouting
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

from benchpress.config import Config
from benchpress.qiskit_gym.circuits import bv_all_ones
from benchpress.utilities.args import get_args
from benchpress.utilities.backends import get_backend

from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceTranspile100Q
from benchpress.qiskit_gym.circuits import trivial_bvlike_circuit

args = get_args(filename=Config.get_args_file())
backend = get_backend(backend_name=args["backend_name"], bench_name="qiskit")


@benchpress_test_validation
class TestWorkoutDeviceTranspile100Q(WorkoutDeviceTranspile100Q):
    def test_QFT_100_transpile(self, benchmark):
        """Compile 100Q QFT circuit against target backend"""
        circuit = QuantumCircuit.from_qasm_file(
            Config.get_qasm_dir("qft") + "qft_N100.qasm"
        )

        pm = generate_preset_pass_manager(args["optimization_level"], backend)
        pm.init.append(StarPreRouting())

        @benchmark
        def result():
            trans_qc = pm.run(circuit)
            return trans_qc

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result

    def test_QV_100_transpile(self, benchmark):
        """Compile 10Q QV circuit against target backend"""
        circuit = QuantumCircuit.from_qasm_file(
            Config.get_qasm_dir("qv") + "qv_N100_12345.qasm"
        )

        @benchmark
        def result():
            trans_qc = transpile(
                circuit, backend, optimization_level=args["optimization_level"]
            )
            return trans_qc

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result

    def test_circSU2_100_transpile(self, benchmark):
        """Compile 100Q circSU2 circuit against target backend"""
        circuit = EfficientSU2(100, reps=3, entanglement="circular")

        @benchmark
        def result():
            trans_qc = transpile(
                circuit, backend, optimization_level=args["optimization_level"]
            )
            return trans_qc

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result

    def test_BV_100_transpile(self, benchmark):
        """Compile 100Q BV circuit against target backend"""
        circuit = bv_all_ones(100)

        @benchmark
        def result():
            trans_qc = transpile(
                circuit, backend, optimization_level=args["optimization_level"]
            )
            return trans_qc

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result

    def test_square_heisenberg_100_transpile(self, benchmark):
        """Compile 100Q square-Heisenberg circuit against target backend"""
        circuit = QuantumCircuit.from_qasm_file(
            Config.get_qasm_dir("square-heisenberg") + "square_heisenberg_N100.qasm"
        )

        @benchmark
        def result():
            trans_qc = transpile(
                circuit, backend, optimization_level=args["optimization_level"]
            )
            return trans_qc

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result

    def test_QAOA_100_transpile(self, benchmark):
        """Compile 100Q QAOA circuit against target backend"""
        circuit = QuantumCircuit.from_qasm_file(
            Config.get_qasm_dir("qaoa") + "qaoa_barabasi_albert_N100_3reps.qasm"
        )

        @benchmark
        def result():
            trans_qc = transpile(
                circuit, backend, optimization_level=args["optimization_level"]
            )
            return trans_qc

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result

    def test_BVlike_simplification_transpile(self, benchmark):
        """Transpile a BV-like circuit that should collapse down
        into a single X and Z gate on a target device
        """
        circuit = trivial_bvlike_circuit(100)

        @benchmark
        def result():
            trans_qc = transpile(
                circuit, backend, optimization_level=args["optimization_level"]
            )
            return trans_qc

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result
