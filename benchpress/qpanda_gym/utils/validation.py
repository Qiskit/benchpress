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
import pyqpanda3 as pq3

def qpanda_circuit_validation(circuit, backend):
    """Validate that input circuit matches gate set
    and topology of target backend

    Parameters:
        circuit (QuantumCircuit): Input circuit
        backend (BackendV2): Target backend
    """
    ops = circuit.gate_operations(False)
    arch_map = dict()
    for edge in backend:
        u, v = edge
        if u not in arch_map:
            arch_map[u] = []
        if v not in arch_map:
            arch_map[v] = []

        arch_map[u].append(v)
        arch_map[v].append(u)
    #return pq3.transpilation.check_mapping(ops,arch_map)
    for op in ops:
        qubits = op.qubits()
        if len(qubits) > 1:
            if qubits[1] in arch_map[qubits[0]]:
                continue
            else:
                raise Exception(f"2Q gate {op.name()}edge {qubits} not in backend topology")
    return True
