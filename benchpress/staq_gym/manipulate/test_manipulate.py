"""Test circuit manipulation"""

import subprocess

import pytest
from qiskit import QuantumCircuit, qasm2

from benchpress.config import Configuration
from benchpress.qiskit_gym.circuits import multi_control_circuit
from benchpress.workouts.manipulate import WorkoutCircuitManipulate
from benchpress.workouts.validation import benchpress_test_validation

OPTIMIZATION_LEVEL = Configuration.options["staq"]["optimization_level"]


@benchpress_test_validation
class TestWorkoutCircuitManipulate(WorkoutCircuitManipulate):
    @pytest.mark.skip(reason="No circuit building and manipulation in staq.")
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q QV
        circuit
        """
        pass

    @pytest.mark.skip(
        reason="staq QASM parser does not undersatnd p and c3sqrtx gates."
    )
    def test_multi_control_decompose(self, benchmark, tmp_path_factory):
        """Decompose a multi-control gate into the basis [U3, CX]"""
        circ = multi_control_circuit(16)
        base_temp_dir = tmp_path_factory.getbasetemp()
        input_qasm_file = "multi_controlled_not_16.qasm"
        qasm2.dump(circ, base_temp_dir / input_qasm_file)

        @benchmark
        def result():
            out = subprocess.run(
                ["staq", "-S", f"-O{OPTIMIZATION_LEVEL}", "-c", input_qasm_file],
                capture_output=True,
                text=True,
            )

            return QuantumCircuit.from_qasm_str(out.stdout)

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cx", 0)
        assert result

    @pytest.mark.skip(reason="No transformation to arbitrary basis in staq.")
    def test_QV100_basis_change(self, benchmark):
        """Change a QV100 circuit basis from [rx, ry, rz, cx]
        to [sx, x, rz, cz]
        """
        pass


@benchpress_test_validation
class TestWorkoutDAGManipulate(WorkoutCircuitManipulate):
    @pytest.mark.skip(reason="No circuit building and manipulation in staq.")
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q QV
        circuit
        """
        pass
