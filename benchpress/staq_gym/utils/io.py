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


def staq_input_circuit_properties(circuit, benchmark):
    benchmark.extra_info["input_num_qubits"] = circuit.num_qubits


def staq_output_circuit_properties(circuit, two_qubit_gate, benchmark):
    benchmark.extra_info["output_num_qubits"] = circuit.num_qubits
    benchmark.extra_info["output_circuit_operations"] = circuit.count_ops()
    benchmark.extra_info["output_gate_count_2q"] = circuit.count_ops().get("cx", 0)
    benchmark.extra_info["output_depth_2q"] = circuit.depth(
        filter_function=lambda x: x.operation.name == "cx"
    )
