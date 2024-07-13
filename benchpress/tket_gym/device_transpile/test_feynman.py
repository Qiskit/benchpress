"""Test summit benchmarks"""

import os
import pytest
from pytket.circuit import OpType
from pytket.qasm import circuit_from_qasm

from benchpress.config import Configuration
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceFeynman

BACKEND = Configuration.backend()
OPTIMIZATION_LEVEL = Configuration.options["tket"]["optimization_level"]


def pytest_generate_tests(metafunc):
    directory = Configuration.get_qasm_dir("feynman")
    file_list = [x for x in os.listdir(directory) if x.endswith(".qasm")]
    metafunc.parametrize("filename", file_list)


@benchpress_test_validation
class TestWorkoutDeviceTranspile100Q(WorkoutDeviceFeynman):
    def test_feynman_transpile(self, benchmark, filename):
        """Compile a feynman benchmark qasm file against a target device"""
        circuit = circuit_from_qasm(
            f"{Configuration.get_qasm_dir('feynman')}{filename}"
        )
        if circuit.n_qubits > BACKEND.backend_info.n_nodes:
            pytest.skip("Circuit too large for given backend.")
        pm = BACKEND.default_compilation_pass(optimisation_level=OPTIMIZATION_LEVEL)

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            pm.apply(new_circ)
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result
