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
"""QASMbench utilities"""

from benchpress.config import Configuration


def output_circuit_properties(circuit, two_qubit_gate, benchmark):
    """Return circuit statistics

    circuit : Input quantum circuit
    two_qubit_gate : Target two-qubit gate
    benchmark (Benchmark): Benchmark class to record info to

    """
    gym_name = Configuration.gym_name
    if gym_name in ["qiskit", "qiskit-transpiler-service"]:
        from benchpress.qiskit_gym.utils.io import qiskit_output_circuit_properties
        qiskit_output_circuit_properties(circuit, two_qubit_gate, benchmark)
    
    elif gym_name == "tket":
        from benchpress.tket_gym.utils.io import tket_output_circuit_properties
        tket_output_circuit_properties(circuit, two_qubit_gate, benchmark)
    
    elif gym_name == "bqskit":
        from benchpress.bqskit_gym.utils.io import bqskit_output_circuit_properties
        bqskit_output_circuit_properties(circuit, two_qubit_gate, benchmark)

    elif gym_name == "staq":
        from benchpress.staq_gym.utils.io import staq_output_circuit_properties
        staq_output_circuit_properties(circuit, two_qubit_gate, benchmark)
    else:
        raise Exception(f'Unsupported gym name {gym_name}')
