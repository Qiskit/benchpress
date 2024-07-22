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

def tket_circuit_validation(circuit, backend):
    """Validate that input circuit matches gate set
    and topology of target backend

    Parameters:
        circuit (QuantumCircuit): Input circuit
        backend (BackendV2): Target backend
    """

    return backend.valid_circuit(circuit)
