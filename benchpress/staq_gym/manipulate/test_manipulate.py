"""Test circuit manipulation"""

import os

import pytest
from qiskit import QuantumCircuit, qasm2

from benchpress.config import Config
from benchpress.qiskit_gym.circuits import multi_control_circuit
from benchpress.workouts.manipulate import WorkoutCircuitManipulate
from benchpress.workouts.validation import benchpress_test_validation


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
        """Decompose a multi-control gate into the
        basis [U3, CX]
        """
        circ = multi_control_circuit(16)
        base_temp_dir = tmp_path_factory.getbasetemp()
        qasm_file = "multi_controlled_not_16.qasm"
        qasm2.dump(circ, base_temp_dir / qasm_file)

        @benchmark
        def result():
            out_file = base_temp_dir / f"temp_{qasm_file}"
            os.system(f"staq -S -O2 -o {out_file} -f qasm {base_temp_dir / qasm_file}")

            return out_file

        result = QuantumCircuit.from_qasm_file(result)
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
