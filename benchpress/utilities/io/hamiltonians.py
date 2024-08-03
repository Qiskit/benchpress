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
import json
import os

from qiskit.quantum_info import SparsePauliOp

from benchpress.config import Configuration


def generate_hamiltonian_circuit(sparse_op, benchmark):
    """Generate a Trotter circuit of a requested Hamiltonian and record the import time

    sparse_op (SparsePauliOp): Input top-level dir
    benchmark (Benchmark): Benchmark class to record info to

    Returns:
        The circuit instance for the corresponding SDK
    """
    gym_name = Configuration.gym_name
    if gym_name in ["qiskit", "qiskit-transpiler-service"]:
        from benchpress.qiskit_gym.utils.io import qiskit_hamiltonian_circuit

        circuit = qiskit_hamiltonian_circuit(sparse_op)
    elif gym_name == "tket":
        from benchpress.tket_gym.utils.io import tket_hamiltonian_circuit

        circuit = tket_hamiltonian_circuit(sparse_op)
    elif gym_name == "bqskit":
        from benchpress.bqskit_gym.utils.io import bqskit_hamiltonian_circuit

        circuit = bqskit_hamiltonian_circuit(sparse_op)
    else:
        raise ValueError(f"Unknown gym name {gym_name}")
    return circuit


def dump_hamiltonians_to_qasm(fn):
    ham_records = json.load(open(fn, "r"))
    for h in ham_records:
        terms = h.pop("ham_hamlib_hamiltonian_terms")
        coefficients = h.pop("ham_hamlib_hamiltonian_coefficients")
        h["ham_hamlib_hamiltonian"] = SparsePauliOp(terms, coefficients)

    output_dir = fn[:-2] + os.sep
    os.makedirs(output_dir, exist_ok=True)

    from benchpress.qiskit_gym.utils.io import qiskit_hamiltonian_circuit
    from qiskit import qasm2

    for ham in ham_records:
        qc = qiskit_hamiltonian_circuit(ham["ham_hamlib_hamiltonian"])
        fn = "".join(
            c if c.isalnum() else "_"
            for c in "ham_"
            + ham["ham_problem"]
            + "_"
            + ham["ham_instance"][1:-1].replace("ham_", "").replace("ham", "")
        )
        qasm2.dump(qc, output_dir + fn + ".qasm")
        print("dumped", fn)


if __name__ == "__main__":
    dump_hamiltonians_to_qasm(
        Configuration.get_hamiltonian_dir("hamlib") + "100_representative.json"
    )
