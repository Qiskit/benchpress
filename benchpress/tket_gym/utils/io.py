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

from pytket import Qubit, Circuit
from pytket.qasm import circuit_from_qasm
from pytket._tket.pauli import Pauli, QubitPauliString
from pytket.utils import QubitPauliOperator, gen_term_sequence_circuit

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


def qubit_pauli_operator_from_qiskit(sparse_pauli_op):
    """Convert Qiskit SparsePauliOp to pytket QubitPauliOperator."""
    tk_qpop = {}
    input_qs = [Qubit(q) for q in range(sparse_pauli_op.num_qubits)]
    tket_p = {"I": Pauli.I, "X": Pauli.X, "Y": Pauli.Y, "Z": Pauli.Z}
    for (pauli_term, c) in sparse_pauli_op.to_list():
        tk_qpop[QubitPauliString(input_qs, [tket_p[p] for p in pauli_term])] = c
    return QubitPauliOperator(tk_qpop)


def tket_hamiltonian_circuit(sparse_op, label=None, evo_time=1):
    qc = Circuit(sparse_op.num_qubits)
    # `gen_term_sequence_circuit` assumes a default evolution time of pi/2, hence we multiply a prefactor
    tket_op = qubit_pauli_operator_from_qiskit(sparse_op*evo_time*2/pi)
    return gen_term_sequence_circuit(tket_op, qc)
  
  
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
