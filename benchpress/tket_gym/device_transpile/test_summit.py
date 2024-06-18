"""Test summit benchmarks"""

from pytket.circuit import OpType
from pytket.qasm import circuit_from_qasm

from benchpress.config import Config
from benchpress.tket_gym.circuits import tket_bv_all_ones, tket_circSU2
from benchpress.utilities.args import get_args
from benchpress.utilities.backends import get_backend

from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceTranspile100Q
from benchpress.tket_gym.circuits import trivial_bvlike_circuit

args = get_args(filename=Config.get_args_file())
backend = get_backend(backend_name=args["backend_name"], bench_name="tket")


@benchpress_test_validation
class TestWorkoutDeviceTranspile100Q(WorkoutDeviceTranspile100Q):
    def test_QFT_100_transpile(self, benchmark):
        """Compile 100Q QFT circuit against target backend"""
        circuit = circuit_from_qasm(Config.get_qasm_dir("qft") + "qft_N100.qasm")

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            backend.default_compilation_pass().apply(new_circ)
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result

    def test_QV_100_transpile(self, benchmark):
        """Compile 10Q QV circuit against target backend"""
        circuit = circuit_from_qasm(Config.get_qasm_dir("qv") + "qv_N100_12345.qasm")

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            backend.default_compilation_pass().apply(new_circ)
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result

    def test_circSU2_100_transpile(self, benchmark):
        """Compile 100Q circSU2 circuit against target backend"""
        circuit = tket_circSU2(100, 3)

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            backend.default_compilation_pass().apply(new_circ)
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result

    def test_BV_100_transpile(self, benchmark):
        """Compile 100Q BV circuit against target backend"""
        circuit = tket_bv_all_ones(100)

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            backend.default_compilation_pass().apply(new_circ)
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result

    def test_square_heisenberg_100_transpile(self, benchmark):
        """Compile 100Q square-Heisenberg circuit against target backend"""
        circuit = circuit_from_qasm(
            Config.get_qasm_dir("square-heisenberg") + "square_heisenberg_N100.qasm"
        )

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            backend.default_compilation_pass().apply(new_circ)
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result

    def test_QAOA_100_transpile(self, benchmark):
        """Compile 100Q QAOA circuit against target backend"""
        circuit = circuit_from_qasm(
            Config.get_qasm_dir("qaoa") + "qaoa_barabasi_albert_N100_3reps.qasm"
        )

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            backend.default_compilation_pass().apply(new_circ)
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result

    def test_BVlike_simplification_transpile(self, benchmark):
        """Transpile a BV-like circuit that should collapse down
        into a single X and Z gate on a target device
        """
        circuit = trivial_bvlike_circuit(100)

        @benchmark
        def result():
            new_circ = circuit.copy()
            backend.default_compilation_pass().apply(new_circ)
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result
