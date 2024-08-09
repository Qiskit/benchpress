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
"""Test transpilation against a device"""
import json
import pytest
from qiskit.quantum_info import SparsePauliOp

from qiskit_transpiler_service.transpiler_service import TranspilerService

from benchpress.config import Configuration
from benchpress.utilities.io import input_circuit_properties, output_circuit_properties
from benchpress.utilities.io.hamiltonians import generate_hamiltonian_circuit
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceHamlibHamiltonians
from benchpress.utilities.validation import circuit_validator

BACKEND = Configuration.backend()
TWO_Q_GATE = BACKEND.two_q_gate_type
OPTIMIZATION_LEVEL = Configuration.options["qiskit"]["optimization_level"]

TRANS_SERVICE = TranspilerService(
    coupling_map=list(BACKEND.coupling_map.get_edges()),
    qiskit_transpile_options={"basis_gates": BACKEND.operation_names},
    ai=True,
    optimization_level=OPTIMIZATION_LEVEL,
    timeout=3600,
)


def pytest_generate_tests(metafunc):
    directory = Configuration.get_hamiltonian_dir("hamlib")
    ham_records = json.load(open(directory + "100_representative.json", "r"))
    for h in ham_records:
        terms = h.pop("ham_hamlib_hamiltonian_terms")
        coefficients = h.pop("ham_hamlib_hamiltonian_coefficients")
        h["ham_hamlib_hamiltonian"] = SparsePauliOp(terms, coefficients)
    metafunc.parametrize(
        "hamiltonian_info", ham_records, ids=lambda x: "ham_" + x["ham_instance"][1:-1]
    )


@benchpress_test_validation
class TestWorkoutDeviceHamlibHamiltonians(WorkoutDeviceHamlibHamiltonians):

    def test_hamlib_hamiltonians_transpile(self, benchmark, hamiltonian_info):
        """Transpile a Hamiltonian against a target device"""
        if hamiltonian_info["ham_qubits"] > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")

        circuit = generate_hamiltonian_circuit(
            hamiltonian_info.pop("ham_hamlib_hamiltonian"), benchmark
        )
        input_circuit_properties(circuit, benchmark)

        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        benchmark.extra_info.update(hamiltonian_info)
        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, BACKEND)
