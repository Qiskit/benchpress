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
"""Test transpilation against a device"""
import os
import pytest
from bqskit import Circuit, compile
from bqskit.compiler import Compiler
from bqskit.ir.gates import CNOTGate, CXGate, CZGate
from benchpress.bqskit_gym.utils.bqskit_backend_utils import ECRGate

from benchpress.config import Configuration
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceFeynman


BACKEND = Configuration.backend()
TWO_Q_GATE = BACKEND.two_q_gate_type
OPTIMIZATION_LEVEL = Configuration.options["bqskit"]["optimization_level"]
compiler = Compiler()


def pytest_generate_tests(metafunc):
    directory = Configuration.get_qasm_dir("feynman")
    file_list = [x for x in os.listdir(directory) if x.endswith(".qasm")]
    metafunc.parametrize("filename", file_list)


@benchpress_test_validation
class TestWorkoutDeviceFeynman(WorkoutDeviceFeynman):

    def test_feynman_transpile(self, benchmark, filename):
        """Transpile a feynman benchmark qasm file against a target device"""
        circuit = Circuit.from_file(
            f"{Configuration.get_qasm_dir('feynman')}{filename}"
        )
        if circuit.num_qudits > BACKEND.num_qudits:
            pytest.skip("Circuit too large for given backend.")

        @benchmark
        def result():
            new_circ = compile(
                circuit,
                model=BACKEND,
                optimization_level=OPTIMIZATION_LEVEL,
                compiler=compiler,
            )
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.gate_counts[TWO_Q_GATE]
        benchmark.extra_info["depth_2q"] = result.multi_qudit_depth
        assert result
