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

def bqskit_circuit_validation(circuit, backend):
    """Validate that input circuit matches gate set
    and topology of target backend

    Parameters:
        circuit (QuantumCircuit): Input circuit
        backend (MachineModel): Target backend
    """
    circuit_ops = set(item.name for item in circuit.gate_counts.keys())
    backend_ops = set(item.name for item in backend.gate_set)
    # Add barrier to backend ops
    backend_ops.add('barrier')
    backend_ops.add('measurement')
    diff_set = set(circuit_ops).difference(backend_ops)
    if diff_set:
        raise Exception(f'Circuit has gates outside backend basis set {diff_set}')

    edges = backend.coupling_graph
    for item in circuit.operations():
        if item.gate == backend.two_q_gate_type:
            if item.location not in edges:
                raise Exception(f'2Q gate edge {item.location} not in backend topology')
    return True
