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
from braket.circuits import Circuit


def braket_qasm_loader(qasm_file, benchmark):
    """Loads a QASM file and measures the import time

    https://github.com/amazon-braket/amazon-braket-sdk-python/blob/bbdbfa64cd63ae1b035a48c3eaa6485f43309c60/src/braket/circuits/circuit.py#L1263

    Parameters:
        qasm_file (str): The QASM file
        benchmark (Benchmark): The class holding the benchmark instance

    Returns:
        Circuit: A Braket circuit instance
    """
    start = perf_counter()
    with open(qasm_file, "r") as file:
        data = file.read()
    circuit = Circuit.from_ir(data)
    stop = perf_counter()
    benchmark.extra_info["qasm_load_time"] = stop - start
    benchmark.extra_info["input_num_qubits"] = circuit.qubit_count
    return circuit


def braket_input_circuit_properties(circuit, benchmark):
    """Get cirq output circuit statistics

    Parameters:
        circuit (Circuit): Input Cirq circuit
        benchmark : The benchmark object
    """
    benchmark.extra_info["input_num_qubits"] = circuit.qubit_count


def braket_output_circuit_properties(circuit, two_qubit_gate, benchmark):
    """Get cirq output circuit statistics

    Parameters:
        circuit (Circuit): Input Cirq circuit
        two_qubit_gate: A 2Q gate name, e.g.
        benchmark : The benchmark object
    """
    count_ops = {}
    for item in circuit.instructions:
        name = item.operator.name
        if name in count_ops:
            count_ops[name] += 1
        else:
            count_ops[name] = 1
    benchmark.extra_info["output_num_qubits"] = circuit.qubit_count
    benchmark.extra_info["output_circuit_operations"] = count_ops
    benchmark.extra_info["output_gate_count_2q"] = count_ops.get(two_qubit_gate, 0)
    benchmark.extra_info["output_depth_2q"] = None
