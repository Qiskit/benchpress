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
import json
import os
import subprocess

import pytest
from qiskit import QuantumCircuit

from benchpress.config import Configuration
from benchpress.utilities.io import qasm_circuit_loader, output_circuit_properties
from benchpress.utilities.validation import circuit_validator
from benchpress.workouts.device_transpile import WorkoutDeviceFeynman
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.qiskit_gym.utils.qiskit_backend_utils import get_qiskit_bench_backend

QISKIT_BACKEND = get_qiskit_bench_backend(
    Configuration.options["general"]["backend_name"]
)
BACKEND = Configuration.backend()
LAYOUT = Configuration.options["staq"]["layout"]
MAPPING = Configuration.options["staq"]["mapping"]
OPTIMIZATION_LEVEL = Configuration.options["staq"]["optimization_level"]

# Truncating OPTIMIZATION_LEVEL to max 2
# OPTIMIZATION_LEVEL=3 uses a `--cnot-resynthesis` flag
# that removes qubit connectivity
OPTIMIZATION_LEVEL = 2 if OPTIMIZATION_LEVEL > 2 else OPTIMIZATION_LEVEL

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
    def _staq_device(backend):
        device_file = tmp_path_factory.getbasetemp() / "device.json"
        with open(device_file, "w") as f:
            f.write(str(backend))

        return device_file

    return _staq_device


@benchpress_test_validation
class TestWorkoutDeviceFeynman(WorkoutDeviceFeynman):

    def test_feynman_transpile(self, benchmark, filename, staq_device):
        """Transpile a feynman benchmark qasm file against a target device"""
        device = staq_device(backend=BACKEND)
        # Pystaq Device does not have an attribute for number of qubits in the device
        # Therefore, we have to load the device json file and get the length of "qubits"
        with open(device, "r") as jf:
            dev = json.load(jf)
        num_qubits = len(dev["qubits"])
        input_qasm_file = f"{Configuration.get_qasm_dir('feynman')}{filename}"

        circuit = qasm_circuit_loader(input_qasm_file, benchmark)
        if circuit.num_qubits > num_qubits:
            pytest.skip("Circuit too large for given backend.")

        @benchmark
        def result():
            out = subprocess.run(
                RUN_ARGS_COMMON + ["-m", "--device", device, input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        output_circuit_properties(result, "cx", benchmark)
        assert circuit_validator(result, QISKIT_BACKEND)
