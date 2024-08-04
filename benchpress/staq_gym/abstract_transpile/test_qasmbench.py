"""Test qasmbench against abstract backend topologies"""

import subprocess

import pytest
from qiskit import QuantumCircuit

from benchpress.config import Configuration
from benchpress.utilities.io import qasm_circuit_loader, output_circuit_properties
from benchpress.utilities.validation import circuit_validator
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

# Truncating OPTIMIZATION_LEVEL to max 2
# OPTIMIZATION_LEVEL=3 uses a `--cnot-resynthesis` flag
# that removes qubit connectivity
OPTIMIZATION_LEVEL = 2 if OPTIMIZATION_LEVEL > 2 else OPTIMIZATION_LEVEL

LAYOUT = Configuration.options["staq"]["layout"]
MAPPING = Configuration.options["staq"]["mapping"]
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
        backend = StaqFlexibleBackend(circuit.num_qubits, circ_and_topo[1])
        staq_backend = backend.get_staq_flexible_backend()
        device = staq_device(backend=staq_backend)

        @benchmark
        def result():
            out = subprocess.run(
                RUN_ARGS_COMMON + ["-m", "--device", device, input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        output_circuit_properties(result, "cx", benchmark)
        assert circuit_validator(result, backend)


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchMedium(WorkoutAbstractQasmBenchMedium):
    @pytest.mark.parametrize("circ_and_topo", MEDIUM_CIRC_TOPO, ids=MEDIUM_NAMES)
    def test_QASMBench_medium(self, benchmark, circ_and_topo, staq_device):
        input_qasm_file = circ_and_topo[0]
        circuit = qasm_circuit_loader(input_qasm_file, benchmark)
        backend = StaqFlexibleBackend(circuit.num_qubits, circ_and_topo[1])
        staq_backend = backend.get_staq_flexible_backend()
        device = staq_device(backend=staq_backend)

        @benchmark
        def result():
            out = subprocess.run(
                RUN_ARGS_COMMON + ["-m", "--device", device, input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        output_circuit_properties(result, "cx", benchmark)
        assert circuit_validator(result, backend)


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchLarge(WorkoutAbstractQasmBenchLarge):
    @pytest.mark.parametrize("circ_and_topo", LARGE_CIRC_TOPO, ids=LARGE_NAMES)
    def test_QASMBench_large(self, benchmark, circ_and_topo, staq_device):
        input_qasm_file = circ_and_topo[0]
        circuit = qasm_circuit_loader(input_qasm_file, benchmark)
        backend = StaqFlexibleBackend(circuit.num_qubits, circ_and_topo[1])
        staq_backend = backend.get_staq_flexible_backend()
        device = staq_device(backend=staq_backend)

        @benchmark
        def result():
            out = subprocess.run(
                RUN_ARGS_COMMON + ["-m", "--device", device, input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        output_circuit_properties(result, "cx", benchmark)
        assert circuit_validator(result, backend)
