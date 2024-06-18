"""Test circuit manipulation"""

import numpy as np

from qiskit import QuantumCircuit
from qiskit.converters import circuit_to_dag, dag_to_circuit
from qiskit.circuit import CircuitInstruction, Qubit, library
from qiskit.dagcircuit import DAGCircuit
from qiskit.passmanager import PropertySet
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

from benchpress.config import Config
from benchpress.qiskit_gym.circuits import multi_control_circuit
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.manipulate import WorkoutCircuitManipulate


# These are all singletons.
GATES = {
    "id": library.IGate(),
    "x": library.XGate(),
    "y": library.YGate(),
    "z": library.ZGate(),
    "cx": library.CXGate(),
    "cz": library.CZGate(),
}
TWIRLING_SETS_NAMES = {
    "cx": [
        ["id", "z", "z", "z"],
        ["id", "x", "id", "x"],
        ["id", "y", "z", "y"],
        ["id", "id", "id", "id"],
        ["z", "x", "z", "x"],
        ["z", "y", "id", "y"],
        ["z", "id", "z", "id"],
        ["z", "z", "id", "z"],
        ["x", "y", "y", "z"],
        ["x", "id", "x", "x"],
        ["x", "z", "y", "y"],
        ["x", "x", "x", "id"],
        ["y", "id", "y", "x"],
        ["y", "z", "x", "y"],
        ["y", "x", "y", "id"],
        ["y", "y", "x", "z"],
    ],
    "cz": [
        ["id", "z", "id", "z"],
        ["id", "x", "z", "x"],
        ["id", "y", "z", "y"],
        ["id", "id", "id", "id"],
        ["z", "x", "id", "x"],
        ["z", "y", "id", "y"],
        ["z", "id", "z", "id"],
        ["z", "z", "z", "z"],
        ["x", "y", "y", "x"],
        ["x", "id", "x", "z"],
        ["x", "z", "x", "id"],
        ["x", "x", "y", "y"],
        ["y", "id", "y", "z"],
        ["y", "z", "y", "id"],
        ["y", "x", "x", "y"],
        ["y", "y", "x", "x"],
    ],
}
TWIRLING_SETS = {
    key: [[GATES[name] for name in twirl] for twirl in twirls]
    for key, twirls in TWIRLING_SETS_NAMES.items()
}


def _dag_from_twirl(gate_2q, twirl):
    dag = DAGCircuit()
    # or use QuantumRegister - doesn't matter
    qubits = (Qubit(), Qubit())
    dag.add_qubits(qubits)
    dag.apply_operation_back(twirl[0], (qubits[0],), (), check=False)
    dag.apply_operation_back(twirl[1], (qubits[1],), (), check=False)
    dag.apply_operation_back(gate_2q, qubits, (), check=False)
    dag.apply_operation_back(twirl[2], (qubits[0],), (), check=False)
    dag.apply_operation_back(twirl[3], (qubits[1],), (), check=False)
    return dag


TWIRLING_DAGS = {
    key: [_dag_from_twirl(GATES[key], twirl) for twirl in twirls]
    for key, twirls in TWIRLING_SETS.items()
}


@benchpress_test_validation
class TestWorkoutCircuitManipulate(WorkoutCircuitManipulate):
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q QV
        circuit
        """
        circuit = QuantumCircuit.from_qasm_file(
            Config.get_qasm_dir("dtc") + "dtc_100_cx_12345.qasm"
        )
        assert benchmark(circuit_twirl, circuit)

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
        circ = QuantumCircuit.from_qasm_file(
            Config.get_qasm_dir("qv") + "qv_N100_12345.qasm"
        )

        @benchmark
        def result():
            translate.property_set = PropertySet()
            out = translate.run(circ)
            return out

        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        assert result


@benchpress_test_validation
class TestWorkoutDAGManipulate(WorkoutCircuitManipulate):
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q QV
        circuit
        """
        circuit = QuantumCircuit.from_qasm_file(
            Config.get_qasm_dir("dtc") + "dtc_100_cx_12345.qasm"
        )

        def setup():
            return (circuit_to_dag(circuit),), {}

        assert benchmark.pedantic(dag_twirl, setup=setup, rounds=4)


def circuit_twirl(qc, twirled_gate="cx", seed=None):
    rng = np.random.default_rng(seed)
    twirl_set = TWIRLING_SETS.get(twirled_gate, [])

    out = qc.copy_empty_like()
    for instruction in qc.data:
        if instruction.operation.name != twirled_gate:
            out._append(instruction)
        else:
            # We could also scan through `qc` outside the loop to know how many
            # twirled gates we'll be dealing with, and RNG the integers ahead of
            # time - that'll be faster depending on what percentage of gates are
            # twirled, and how much the Numpy overhead is.
            twirls = twirl_set[rng.integers(len(twirl_set))]
            control, target = instruction.qubits
            out._append(CircuitInstruction(twirls[0], (control,), ()))
            out._append(CircuitInstruction(twirls[1], (target,), ()))
            out._append(instruction)
            out._append(CircuitInstruction(twirls[2], (control,), ()))
            out._append(CircuitInstruction(twirls[3], (target,), ()))
    return out


def dag_twirl(dag, twirled_gate="cx", seed=None):
    # This mutates `dag` in place.
    rng = np.random.default_rng(seed)
    twirl_set = TWIRLING_DAGS.get(twirled_gate, [])
    twirled_gate_op = GATES[twirled_gate].base_class

    to_twirl = dag.op_nodes(twirled_gate_op)
    twirl_indices = rng.integers(len(twirl_set), size=(len(to_twirl),))

    for index, op_node in zip(twirl_indices, to_twirl):
        dag.substitute_node_with_dag(op_node, twirl_set[index])
    return dag
