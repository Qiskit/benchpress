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
    """Get the file dirs and names from a dir
    of QASMbench files and record load time to benchmark

    qasm_file (str): Input top-level dir
    benchmark (Benchmark): Benchmark class to record info to

    Returns:
        tuple: list of QASM file src strings and list of names
    """
    gym_name = Configuration.gym_name
    if gym_name in ["qiskit", "qiskit-transpiler-service"]:
        from benchpress.qiskit_gym.utils.io import qiskit_qasm_loader

        circuit = qiskit_qasm_loader(qasm_file, benchmark)
    return circuit
