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
import subprocess

import pytest
from qiskit import QuantumCircuit

from benchpress.config import Configuration
from benchpress.staq_gym.utils.staq_backend_utils import get_staq_device_file
from benchpress.workouts.device_transpile import WorkoutDeviceFeynman
from benchpress.workouts.validation import benchpress_test_validation

# staq-gym uses Qiskit backend to create a compatible device JSON file.
BACKEND = Configuration.backend()
LAYOUT = Configuration.options["staq"]["layout"]
MAPPING = Configuration.options["staq"]["mapping"]
OPTIMIZATION_LEVEL = Configuration.options["staq"]["optimization_level"]

RUN_ARGS_COMMON = [
    "staq",
    "-S",
    f"-O{OPTIMIZATION_LEVEL}",
    "-l",
    LAYOUT,
    "-M",
    MAPPING,
    "-f",
    "qasm",
]


def pytest_generate_tests(metafunc):
    directory = Configuration.get_qasm_dir("feynman")
    file_list = [x for x in os.listdir(directory) if x.endswith(".qasm")]
    metafunc.parametrize("filename", file_list)


@pytest.fixture(scope="session")
def staq_device(tmp_path_factory):
    dev_file = get_staq_device_file(
        target=BACKEND.target, tmp_path_factory=tmp_path_factory
    )

    return dev_file


@benchpress_test_validation
class TestWorkoutDeviceFeynman(WorkoutDeviceFeynman):

    def test_feynman_transpile(self, benchmark, filename, staq_device):
        """Transpile a feynman benchmark qasm file against a target device"""
        input_qasm_file = f"{Configuration.get_qasm_dir('feynman')}{filename}"

        circuit = QuantumCircuit.from_qasm_file(input_qasm_file)
        if circuit.num_qubits > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")

        @benchmark
        def result():
            out = subprocess.run(
                RUN_ARGS_COMMON + ["-m", "--device", staq_device, input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cx", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cx"
        )
        assert result
