"""Test qasmbench against abstract backend topologies"""

import subprocess

import pytest
from qiskit import QuantumCircuit

from benchpress.config import Configuration
from benchpress.utilities.io import qasm_circuit_loader
from benchpress.staq_gym.utils.staq_backend_utils import StaqFlexibleBackend
from benchpress.workouts.abstract_transpile import (
    WorkoutAbstractQasmBenchLarge,
    WorkoutAbstractQasmBenchMedium,
    WorkoutAbstractQasmBenchSmall,
)
from benchpress.workouts.abstract_transpile.qasmbench import (
    LARGE_CIRC_TOPO,
    LARGE_NAMES,
    MEDIUM_CIRC_TOPO,
    MEDIUM_NAMES,
    SMALL_CIRC_TOPO,
    SMALL_NAMES,
)
from benchpress.workouts.validation import benchpress_test_validation

OPTIMIZATION_LEVEL = Configuration.options["staq"]["optimization_level"]

LAYOUT = Configuration.options["staq"]["layout"]
MAPPING = Configuration.options["staq"]["mapping"]
RUN_ARGS_COMMON = [
    "staq",
    "-S",
    f"-O{OPTIMIZATION_LEVEL}",
    "-c",
    "-l",
    LAYOUT,
    "-M",
    MAPPING,
    "-f",
    "qasm",
]

# `cc` and `qft` circuits throw 'stoi: out of range' error.
# So, those tests will be marked as `skip`
mark_large_tests = ("cc", "qft")
reason = (
    "libc++abi: terminating due to uncaught exception of type "
    "std::out_of_range: stoi: out of range"
)

LARGE_CIRC_TOPO_MARKED = [
    (
        pytest.param(circ_and_topo, marks=pytest.mark.skip(reason=reason), id=name)
        if name.startswith(mark_large_tests)
        else circ_and_topo
    )
    for circ_and_topo, name in zip(LARGE_CIRC_TOPO, LARGE_NAMES)
]


@pytest.fixture(scope="session")
def staq_device(tmp_path_factory):
    def _staq_device(backend):
        device_file = tmp_path_factory.getbasetemp() / "device.json"
        with open(device_file, "w") as f:
            f.write(str(backend))

        return device_file

    return _staq_device


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchSmall(WorkoutAbstractQasmBenchSmall):
    @pytest.mark.parametrize("circ_and_topo", SMALL_CIRC_TOPO, ids=SMALL_NAMES)
    def test_QASMBench_small(self, benchmark, circ_and_topo, staq_device):
        input_qasm_file = circ_and_topo[0]
        circuit = qasm_circuit_loader(input_qasm_file, benchmark)
        backend = StaqFlexibleBackend(
            circuit.num_qubits, circ_and_topo[1]
        ).get_staq_flexible_backend()
        device = staq_device(backend=backend)

        @benchmark
        def result():
            out = subprocess.run(
                RUN_ARGS_COMMON + ["-m", "--device", device, input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cx", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cx"
        )
        assert result


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchMedium(WorkoutAbstractQasmBenchMedium):
    @pytest.mark.parametrize("circ_and_topo", MEDIUM_CIRC_TOPO, ids=MEDIUM_NAMES)
    def test_QASMBench_medium(self, benchmark, circ_and_topo, staq_device):
        input_qasm_file = circ_and_topo[0]
        circuit = qasm_circuit_loader(input_qasm_file, benchmark)
        backend = StaqFlexibleBackend(
            circuit.num_qubits, circ_and_topo[1]
        ).get_staq_flexible_backend()
        device = staq_device(backend=backend)

        @benchmark
        def result():
            out = subprocess.run(
                RUN_ARGS_COMMON + ["-m", "--device", device, input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cx", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cx"
        )
        assert result


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchLarge(WorkoutAbstractQasmBenchLarge):
    @pytest.mark.parametrize("circ_and_topo", LARGE_CIRC_TOPO_MARKED, ids=LARGE_NAMES)
    def test_QASMBench_large(self, benchmark, circ_and_topo, staq_device):
        input_qasm_file = circ_and_topo[0]
        circuit = qasm_circuit_loader(input_qasm_file, benchmark)
        backend = StaqFlexibleBackend(
            circuit.num_qubits, circ_and_topo[1]
        ).get_staq_flexible_backend()
        device = staq_device(backend=backend)

        @benchmark
        def result():
            out = subprocess.run(
                RUN_ARGS_COMMON + ["-m", "--device", device, input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cx", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cx"
        )
        assert result
