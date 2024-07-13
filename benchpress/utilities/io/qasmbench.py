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
