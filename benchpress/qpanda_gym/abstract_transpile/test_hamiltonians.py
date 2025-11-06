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
"""Test Hamiltonians against abstract backend topologies"""

import pytest
from pyqpanda3.transpilation import *
from benchpress.utilities.io import input_circuit_properties, output_circuit_properties
from benchpress.utilities.io.hamiltonians import generate_hamiltonian_circuit
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.config import Configuration
from benchpress.utilities.backends import FlexibleBackend
from benchpress.utilities.validation import circuit_validator


from benchpress.workouts.abstract_transpile.hamlib_hamiltonians import (
    HAM_TOPO,
    HAM_TOPO_NAMES,
    WorkoutAbstractHamiltonians,
)

OPTIMIZATION_LEVEL = Configuration.options["qpanda"]["optimization_level"]
basic_gates = ['X1','RZ','CZ']

@benchpress_test_validation
class TestWorkoutAbstractHamiltonians(WorkoutAbstractHamiltonians):
    @pytest.mark.parametrize("circ_and_topo", HAM_TOPO, ids=HAM_TOPO_NAMES)
    def test_hamiltonians(self, benchmark, circ_and_topo):
        prog = generate_hamiltonian_circuit(
            circ_and_topo[0].pop("ham_hamlib_hamiltonian"), benchmark
        )
        input_circuit_properties(prog, benchmark)
        backend = FlexibleBackend(len(prog.qubits()), layout=circ_and_topo[1])
        topo = backend.configuration().coupling_map
        pm = Transpiler()
        @benchmark
        def result():
            atf_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL, basic_gates)
            return atf_prog


        benchmark.extra_info.update(circ_and_topo[0])
        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)
