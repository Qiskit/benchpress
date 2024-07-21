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

import os
import pytest

from benchpress.config import Configuration
from benchpress.utilities.io import qasm_circuit_loader
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceFeynman

BACKEND = Configuration.backend()
TWO_Q_GATE = BACKEND.two_q_gate_type
OPTIMIZATION_LEVEL = Configuration.options["tket"]["optimization_level"]


def pytest_generate_tests(metafunc):
    directory = Configuration.get_qasm_dir("feynman")
    file_list = [x for x in os.listdir(directory) if x.endswith(".qasm")]
    metafunc.parametrize("filename", file_list)


@benchpress_test_validation
class TestWorkoutDeviceTranspile100Q(WorkoutDeviceFeynman):
    def test_feynman_transpile(self, benchmark, filename):
        """Compile a feynman benchmark qasm file against a target device"""
        circuit = qasm_circuit_loader(
            f"{Configuration.get_qasm_dir('feynman')}{filename}", benchmark
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

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(TWO_Q_GATE)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(TWO_Q_GATE)
        assert result
