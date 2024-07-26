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
import copy
import json

import pytest
from qiskit.quantum_info import SparsePauliOp

from benchpress.config import Configuration

TOPOLOGY_NAMES = Configuration.options["general"]["abstract_topologies"]


def hamlib_parameters():
    directory = Configuration.get_hamiltonian_dir("hamlib")
    ham_records = json.load(open(directory + "100_representative.json", 'r'))
    for h in ham_records:
        terms = h.pop('ham_hamlib_hamiltonian_terms')
        coefficients = h.pop('ham_hamlib_hamiltonian_coefficients')
        h['ham_hamlib_hamiltonian'] = SparsePauliOp(terms, coefficients)

    hams_and_topo = []
    test_ids = []
    for idx, ham in enumerate(ham_records):
        for topo_name in TOPOLOGY_NAMES:
            hams_and_topo.append((copy.copy(ham), topo_name))
            test_ids.append("ham_" + ham['ham_instance'][1:-1] + "-" + topo_name)
    return hams_and_topo, test_ids


HAM_TOPO, HAM_TOPO_NAMES = hamlib_parameters()


@pytest.mark.benchmark(group="Transpile - Abstract")
class WorkoutAbstractHamiltonians:
    @pytest.mark.parametrize("circ_and_topo", HAM_TOPO, ids=HAM_TOPO_NAMES)
    @pytest.mark.skip(reason="Not implemented")
    def test_hamiltonians(self, benchmark, circ_and_topo):
        """Abstract transpilation for Hamiltonians"""
        pass
