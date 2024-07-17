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
import subprocess

import numpy as np
import pytest
from qiskit import QuantumCircuit, qasm2
from qiskit.circuit.library import EfficientSU2

from benchpress.config import Configuration
from benchpress.qiskit_gym.circuits import bv_all_ones, trivial_bvlike_circuit
from benchpress.workouts.device_transpile import WorkoutDeviceTranspile100Q
from benchpress.workouts.validation import benchpress_test_validation


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


@pytest.fixture(scope="session")
def staq_device(backend, tmp_path_factory):
    device_file = tmp_path_factory.getbasetemp() / "device.json"
    with open(device_file, "w") as f:
        f.write(str(backend))

    return device_file


# Staq transpiles a circuit by reading it from a `.qasm` file only.
# Also, Staq does not have circuit building (and manipulation) features.
# Therefore, some test circuits are created using Qiskit, and then,
# `QuantumCircuit` objects are saved as `.qasm` in a temporary directory
# from pytest.TempPathFactory.

# Staq reads a device specification (connectivity and error rates) from
# a `.json` file. 
# 
@benchpress_test_validation
class TestWorkoutDeviceTranspile100Q(WorkoutDeviceTranspile100Q):
    @pytest.mark.xfail(
        reason="Error: libc++abi: terminating due to uncaught exception of type "
        "std::out_of_range: stoi: out of range",
        run=False,
    )
    def test_QFT_100_transpile(self, benchmark, staq_device):
        """Compile 100Q QFT circuit against target backend"""
        qasm_file = "qft_N100.qasm"
        input_qasm_file = Configuration.get_qasm_dir("qft") + qasm_file

        @benchmark
        def result():
            out = subprocess.run(
                RUN_ARGS_COMMON + ["-m", "--device", staq_device, input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        # load output QASM as a QuantumCircuit to get statistics as
        # staq does not have built-in utilities for such
        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cx", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cx"
        )
        assert result

    def test_QV_100_transpile(self, benchmark, staq_device):
        """Compile 100Q QV circuit against target backend"""
        qasm_file = "qv_N100_12345.qasm"
        input_qasm_file = Configuration.get_qasm_dir("qv") + qasm_file

        @benchmark
        def result():
            out = subprocess.run(
                RUN_ARGS_COMMON + ["-m", "--device", staq_device, input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        # load output QASM as a QuantumCircuit to get statistics as
        # staq does not have built-in utilities for such
        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cx", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cx"
        )
        assert result

    def test_circSU2_100_transpile(self, benchmark, tmp_path_factory, staq_device):
        """Compile 100Q circSU2 circuit against target backend"""
        circuit = EfficientSU2(100, reps=3, entanglement="circular")

        # staq works on qasm files only & qasm files need bounded params
        num_parameters = circuit.num_parameters
        np.random.seed(0)
        params = np.random.uniform(low=0.1, high=np.pi, size=num_parameters)
        circuit.assign_parameters(parameters=params, inplace=True)

        base_temp_dir = tmp_path_factory.getbasetemp()
        input_qasm_file = base_temp_dir / "circ.qasm"
        qasm2.dump(circuit, input_qasm_file)

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

    def test_BV_100_transpile(self, benchmark, tmp_path_factory, staq_device):
        """Compile 100Q BV circuit against target backend"""
        circuit = bv_all_ones(100)

        base_temp_dir = tmp_path_factory.getbasetemp()
        input_qasm_file = base_temp_dir / "circ.qasm"
        qasm2.dump(circuit, input_qasm_file)

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

    def test_square_heisenberg_100_transpile(self, benchmark, staq_device):
        """Compile 100Q square-Heisenberg circuit against target backend"""
        qasm_file = "square_heisenberg_N100.qasm"
        input_qasm_file = Configuration.get_qasm_dir("square-heisenberg") + qasm_file

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

    def test_QAOA_100_transpile(self, benchmark, staq_device):
        """Compile 100Q QAOA circuit against target backend"""
        qasm_file = "qaoa_barabasi_albert_N100_3reps.qasm"
        input_qasm_file = Configuration.get_qasm_dir("qaoa") + qasm_file

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

    def test_BVlike_simplification_transpile(
        self, benchmark, tmp_path_factory, staq_device
    ):
        """Transpile a BV-like circuit that should collapse down
        into a single X and Z gate on a target device
        """
        circuit = trivial_bvlike_circuit(100)

        base_temp_dir = tmp_path_factory.getbasetemp()
        input_qasm_file = base_temp_dir / "trivial_bvlike_100.qasm"
        qasm2.dump(circuit, input_qasm_file)

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
