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
"""Basic circuit validation"""

def qiskit_circuit_validation(circuit, backend):
    """Validate that input circuit matches gate set
    and topology of target backend

    Parameters:
        circuit (QuantumCircuit): Input circuit
        backend (BackendV2): Target backend
    """
    circuit_ops = set(circuit.count_ops().keys())
    backend_ops = set(backend.operation_names)
    # Add barrier to backend ops
    backend_ops.add('barrier')
    diff_set = set(circuit_ops).difference(backend_ops)
    if diff_set:
        raise Exception(f'Circuit has gates outside backend basis set {diff_set}')

    cmap = backend.coupling_map
    if cmap.graph.num_edges() < cmap.graph.num_nodes() * (cmap.graph.num_nodes()-1):
        edges = set(cmap.get_edges())
        for gate in circuit.get_instructions(backend.two_q_gate_type):
            _edge = (circuit.find_bit(gate.qubits[0]).index,
                    circuit.find_bit(gate.qubits[1]).index)
            if _edge not in edges:
                raise Exception(f'2Q gate edge {_edge} not in backend topology')
    return True
