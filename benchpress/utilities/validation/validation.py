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

from benchpress.config import Configuration


def circuit_validator(circuit, backend):
    """Validate a circuit matches the gate set and
    topology of the target backend
    
    Parameters:
        circuit : Input circuit
        backend : Target backend
    """
    gym_name = Configuration.gym_name
    if gym_name in ["qiskit", "qiskit-transpiler-service"]:
        from benchpress.qiskit_gym.utils.validation import qiskit_circuit_validation

        qiskit_circuit_validation(circuit, backend)
    elif gym_name in ["tket"]:
        from benchpress.tket_gym.utils.validation import tket_circuit_validation

        tket_circuit_validation(circuit, backend)
    
    elif gym_name in ["bqskit"]:
        from benchpress.bqskit_gym.utils.validation import bqskit_circuit_validation

        bqskit_circuit_validation(circuit, backend)
    else:
        raise ValueError(f"Unknown gym name {gym_name}")
    return circuit
