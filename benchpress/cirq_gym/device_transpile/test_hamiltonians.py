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
from benchpress.config import Configuration
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceHamlibHamiltonians



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
        pytest.skip("Not implimented")
