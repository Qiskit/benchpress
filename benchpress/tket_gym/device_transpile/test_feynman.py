"""Test summit benchmarks"""

import os
from pytket.circuit import OpType
from pytket.qasm import circuit_from_qasm

from benchpress.config import Config
from benchpress.utilities.args import get_args
from benchpress.utilities.backends import get_backend
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceFeynman

args = get_args(filename=Config.get_args_file())
backend = get_backend(backend_name=args["backend_name"], bench_name="tket")


def pytest_generate_tests(metafunc):
    directory = Config.get_qasm_dir("feynman")
    file_list = [x for x in os.listdir(directory) if x.endswith(".qasm")]
    metafunc.parametrize("filename", file_list)


@benchpress_test_validation
class TestWorkoutDeviceTranspile100Q(WorkoutDeviceFeynman):
    def test_feynman_transpile(self, benchmark, filename):
        """Compile a feynman benchmark qasm file against a target device"""
        circuit = circuit_from_qasm(f"{Config.get_qasm_dir('feynman')}{filename}")
        if circuit.n_qubits > backend.backend_info.n_nodes:
            pytest.skip("Circuit too large for given backend.")

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            backend.default_compilation_pass().apply(new_circ)
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result
