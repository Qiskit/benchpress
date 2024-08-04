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


def staq_circuit_validation(circuit, backend):
    """Validate that input circuit matches the
      topology of target backend

    Parameters:
        circuit (QuantumCircuit): Input circuit
        backend (BackendV2): Target backend
    """
    try:
        cmap = backend._backend.coupling_map
    except:
        cmap = backend.coupling_map
    if cmap.graph.num_edges() < cmap.graph.num_nodes() * (cmap.graph.num_nodes() - 1):
        edges = set(cmap.get_edges())
        for gate in circuit.get_instructions("cx"):
            _edge = (
                circuit.find_bit(gate.qubits[0]).index,
                circuit.find_bit(gate.qubits[1]).index,
            )
            if _edge not in edges:
                raise Exception(f"2Q gate edge {_edge} not in backend topology")
    return True
