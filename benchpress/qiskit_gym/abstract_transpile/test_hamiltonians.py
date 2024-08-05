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

from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

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

OPTIMIZATION_LEVEL = Configuration.options["qiskit"]["optimization_level"]


@benchpress_test_validation
class TestWorkoutAbstractHamiltonians(WorkoutAbstractHamiltonians):
    @pytest.mark.parametrize("circ_and_topo", HAM_TOPO, ids=HAM_TOPO_NAMES)
    def test_hamiltonians(self, benchmark, circ_and_topo):
        circuit = generate_hamiltonian_circuit(
            circ_and_topo[0].pop("ham_hamlib_hamiltonian"), benchmark
        )
        input_circuit_properties(circuit, benchmark)
        backend = FlexibleBackend(circuit.num_qubits, circ_and_topo[1])
        TWO_Q_GATE = backend.two_q_gate_type
        pm = generate_preset_pass_manager(
            optimization_level=OPTIMIZATION_LEVEL, backend=backend
        )

        @benchmark
        def result():
            trans_qc = pm.run(circuit)
            return trans_qc

        benchmark.extra_info.update(circ_and_topo[0])
        output_circuit_properties(result, TWO_Q_GATE, benchmark)
        assert circuit_validator(result, backend)
