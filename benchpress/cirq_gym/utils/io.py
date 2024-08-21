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
import cirq
from cirq.contrib.qasm_import import circuit_from_qasm


def cirq_qasm_loader(qasm_file, benchmark):
    """Loads a QASM file and measures the import time

    Parameters:
        qasm_file (str): The QASM file
        benchmark (Benchmark): The class holding the benchmark instance

    Returns:
        Circuit: A Cirq circuit instance
    """
    start = perf_counter()
    with open(qasm_file, "r") as f:
        qasm_str = "".join(f.readlines())
    circuit = circuit_from_qasm(qasm_str)
    stop = perf_counter()
    benchmark.extra_info["qasm_load_time"] = stop - start
    benchmark.extra_info["input_num_qubits"] = cirq.num_qubits(circuit)
    return circuit


def cirq_input_circuit_properties(circuit, benchmark):
    """Get cirq output circuit statistics

    Parameters:
        circuit (Circuit): Input Cirq circuit
        benchmark : The benchmark object
    """
    benchmark.extra_info["input_num_qubits"] = cirq.num_qubits(circuit)


def cirq_output_circuit_properties(circuit, two_qubit_gate, benchmark):
    """Get cirq output circuit statistics

    Parameters:
        circuit (Circuit): Input Cirq circuit
        two_qubit_gate: A 2Q gate , e.g. 'CXPowGate', 'MatrixGate', or 'CZPowGate'
        benchmark : The benchmark object
    """

    twoq_gates = []
    count_ops = {}

    for item in circuit.all_operations():
        item_name = type(item.gate).__name__
        if item_name == two_qubit_gate:
            twoq_gates.append(item)
        if item_name in count_ops:
            count_ops[item_name] += 1
        else:
            count_ops[item_name] = 1

    benchmark.extra_info["output_num_qubits"] = cirq.num_qubits(circuit)
    benchmark.extra_info["output_circuit_operations"] = count_ops
    benchmark.extra_info["output_gate_count_2q"] = len(twoq_gates)
    # https://quantumcomputing.stackexchange.com/questions/9302/computing-circuit-depth-in-cirq
    benchmark.extra_info["output_depth_2q"] = len(cirq.Circuit(twoq_gates))
