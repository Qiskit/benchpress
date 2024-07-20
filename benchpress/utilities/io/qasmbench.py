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

import os


def get_qasmbench_circuits(qasm_dir):
    """Get the file dirs and names from a dir
    of QASMbench files

    qasm_dir (str): Input top-level dir

    Returns:
        tuple: list of QASM file src strings and list of names
    """
    qasm_files = []
    qasm_names = []
    for root, _, files in os.walk(qasm_dir):
        for file in files:
            if file.endswith(".qasm") and "transpiled" not in file:
                qasm_files.append(os.path.join(root, file))
                qasm_names.append(file.split(".")[0])
    return qasm_files, qasm_names
