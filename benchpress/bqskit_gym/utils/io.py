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
from time import perf_counter
from math import pi

from bqskit import Circuit
from bqskit.ext import qiskit_to_bqskit
from benchpress.qiskit_gym.utils.io import qiskit_hamiltonian_circuit


def bqskit_qasm_loader(qasm_file, benchmark):
    """Loads a QASM file and measures the import time

    Parameters:
        qasm_file (str): The QASM file
        benchmark (Benchmark): The class holding the benchmark instance

    Returns:
        Circuit: A BQSKit circuit instance
    """
    start = perf_counter()
    circuit = Circuit.from_file(qasm_file)
    stop = perf_counter()
    benchmark.extra_info["qasm_load_time"] = stop - start
    benchmark.extra_info["input_num_qubits"] = circuit.num_qudits
    return circuit


def bqskit_hamiltonian_circuit(sparse_op, label=None, evo_time=1):
    # BQSKit uses qiskit to construct a Trotter circuit, see https://github.com/BQSKit/bqskit-tutorial/blob/d04b4c40180c26ef81a8927663679fa085efc053/hubbard/hubbard.py#L135
    # hence we also use it here. Note that we must decompose the returned circuit here because BQSKit
    # will complain about the n-qubit PauliBoxes inside the circuit returned by `qk_ham_circuit`
    return qiskit_to_bqskit(
        qiskit_hamiltonian_circuit(sparse_op, label, evo_time).decompose().decompose()
    )


def bqskit_input_circuit_properties(circuit, benchmark):
    benchmark.extra_info["input_num_qubits"] = circuit.num_qudits


def bqskit_output_circuit_properties(circuit, two_qubit_gate, benchmark):
    ops = {}
    for op in circuit.operations():
        if op.gate.name in ops:
            ops[op.gate.name] += 1
        else:
            ops[op.gate.name] = 1
    benchmark.extra_info["output_num_qubits"] = circuit.num_qudits
    benchmark.extra_info["output_circuit_operations"] = ops
    benchmark.extra_info["output_gate_count_2q"] = circuit.gate_counts.get(
        two_qubit_gate, 0
    )
    benchmark.extra_info["output_depth_2q"] = circuit.multi_qudit_depth
