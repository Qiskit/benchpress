"""Test circuit manipulation"""

from qiskit import QuantumCircuit
from qiskit.circuit import pauli_twirl_2q_gates
from qiskit.passmanager import PropertySet
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

from benchpress.config import Configuration
from benchpress.utilities.io import qasm_circuit_loader
from benchpress.qiskit_gym.circuits import multi_control_circuit
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.manipulate import WorkoutCircuitManipulate


@benchpress_test_validation
class TestWorkoutCircuitManipulate(WorkoutCircuitManipulate):
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q QV
        circuit
        """
        circuit = qasm_circuit_loader(
            Configuration.get_qasm_dir("dtc") + "dtc_100_cx_12345.qasm", benchmark
        )
        assert benchmark(pauli_twirl_2q_gates, circuit)

    def test_multi_control_decompose(self, benchmark):
        """Decompose a multi-control gate into the
        basis [rx, ry, rz, cz]
        """
        translate = generate_preset_pass_manager(
            1, basis_gates=["rx", "ry", "rz", "cz"]
        ).translation
        circ = multi_control_circuit(16)

        @benchmark
        def result():
            translate.property_set = PropertySet()
            out = translate.run(circ)
            return out

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        assert result

    def test_QV100_basis_change(self, benchmark):
        """Change a QV100 circuit basis from [rx, ry, rz, cx]
        to [sx, x, rz, cz]
        """
        translate = generate_preset_pass_manager(
            1, basis_gates=["sx", "x", "rz", "cz"]
        ).translation
        circ = qasm_circuit_loader(
            Configuration.get_qasm_dir("qv") + "qv_N100_12345.qasm", benchmark
        )

        @benchmark
        def result():
            translate.property_set = PropertySet()
            out = translate.run(circ)
            return out

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        assert result

    def test_random_clifford_decompose(self, benchmark):
        """Decompose a random clifford into
        basis [rz, sx, x, cz]
        """
        translate = generate_preset_pass_manager(
            1, basis_gates=["rz", "sx", "x", "cz"]
        ).translation
        cliff_circ = QuantumCircuit.from_qasm_file(
            Configuration.get_qasm_dir("clifford") + "clifford_20_12345.qasm"
        )
        from qiskit.quantum_info import Clifford

        cliff = Clifford(cliff_circ)
        circ = cliff.to_circuit()

        @benchmark
        def result():
            translate.property_set = PropertySet()
            out = translate.run(circ)
            return out

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result
