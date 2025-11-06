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
import os
from qiskit import QuantumCircuit, qasm2
from qiskit.circuit.library import PauliEvolutionGate
from time import perf_counter
from pyqpanda3.intermediate_compiler import *

def qpanda_qasm_loader(qasm_file, benchmark):
    start = perf_counter()
    prog = convert_qasm_file_to_qprog(qasm_file)

    stop = perf_counter()
    benchmark.extra_info["qasm_load_time"] = stop - start
    benchmark.extra_info["input_num_qubits"] = len(prog.qubits())
    return prog


def qpanda_hamiltonian_circuit(sparse_op, label=None, evo_time=1):
    qc = QuantumCircuit(sparse_op.num_qubits)
    qc.append(
        PauliEvolutionGate(sparse_op, time=evo_time, label=label),
        qargs=range(sparse_op.num_qubits),
    )
    qc = qc.decompose().decompose()
    qasm = qasm2.dumps(qc)
    return convert_qasm_string_to_qprog(qasm)


def qpanda_input_circuit_properties(circuit, benchmark):
    benchmark.extra_info["input_num_qubits"] = len(circuit.qubits())


def qpanda_output_circuit_properties(circuit, two_qubit_gate, benchmark):
    benchmark.extra_info["output_num_qubits"] = len(circuit.qubits())
    benchmark.extra_info["output_circuit_operations"] = circuit.count_ops(False)
    if two_qubit_gate == '2Q_GATE':
        benchmark.extra_info["output_gate_count_2q"] = len(circuit.gate_operations(True))
    else:
        benchmark.extra_info["output_gate_count_2q"] = circuit.count_ops(False).get(
            two_qubit_gate, 0
        )
    benchmark.extra_info["output_depth_2q"] = circuit.depth(True)

