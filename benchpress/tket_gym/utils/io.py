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
from pytket.qasm import circuit_from_qasm


def tket_qasm_loader(qasm_file, benchmark):
    """Loads a QASM file and measures the import time

    Parameters:
        qasm_file (str): The QASM file
        benchmark (Benchmark): The class holding the benchmark instance

    Returns:
        Circuit: A Tket circuit instance
    """
    start = perf_counter()
    circuit = circuit_from_qasm(qasm_file)
    stop = perf_counter()
    benchmark.extra_info["qasm_load_time"] = stop - start
    benchmark.extra_info["input_num_qubits"] = circuit.n_qubits
    return circuit


def tket_output_circuit_properties(circuit, two_qubit_gate, benchmark):
    ops = {}
    for command in circuit.get_commands():
        if command.op.type in ops:
            ops[command.op.type] += 1
        else:
            ops[command.op.type] = 1
    benchmark.extra_info["circuit_operations"] = ops
    benchmark.extra_info["gate_count_2q"] = circuit.n_gates_of_type(two_qubit_gate)
    benchmark.extra_info["depth_2q"] = circuit.depth_by_type(two_qubit_gate)
