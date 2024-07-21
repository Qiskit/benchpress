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


def qasm_circuit_loader(qasm_file, benchmark):
    """Load the requested QASM circuit and record the import time

    qasm_file (str): Input top-level dir
    benchmark (Benchmark): Benchmark class to record info to

    Returns:
        The circuit instance for the corresponding SDK
    """
    gym_name = Configuration.gym_name
    if gym_name in ["qiskit", "qiskit-transpiler-service"]:
        from benchpress.qiskit_gym.utils.io import qiskit_qasm_loader

        circuit = qiskit_qasm_loader(qasm_file, benchmark)
    elif gym_name == 'tket':
        from benchpress.tket_gym.utils.io import tket_qasm_loader

        circuit = tket_qasm_loader(qasm_file, benchmark)

    elif gym_name == 'bqskit':
        from benchpress.bqskit_gym.utils.io import bqskit_qasm_loader

        circuit = bqskit_qasm_loader(qasm_file, benchmark)
    
    elif gym_name == 'cirq':
        from benchpress.cirq_gym.utils.io import cirq_qasm_loader

        circuit = cirq_qasm_loader(qasm_file, benchmark)
    return circuit
