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
from qiskit import QuantumCircuit


def qiskit_qasm_loader(qasm_file, benchmark):
    start = perf_counter()
    circuit = QuantumCircuit.from_qasm_file(qasm_file)
    stop = perf_counter()
    benchmark.extra_info["qasm_load_time"] = stop - start
    benchmark.extra_info["input_num_qubits"] = circuit.num_qubits
    return circuit


def qiskit_output_circuit_properties(circuit, two_qubit_gate, benchmark):
    benchmark.extra_info["circuit_operations"] = circuit.count_ops()
    benchmark.extra_info["gate_count_2q"] = circuit.count_ops().get(two_qubit_gate, 0)
    benchmark.extra_info["depth_2q"] = circuit.depth(
            filter_function=lambda x: x.operation.name == two_qubit_gate
        )