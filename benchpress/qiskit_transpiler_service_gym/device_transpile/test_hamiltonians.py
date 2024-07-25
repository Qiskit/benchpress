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
import pickle
import pytest

from qiskit_transpiler_service.transpiler_service import TranspilerService

from benchpress.config import Configuration
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
)



def pytest_generate_tests(metafunc):
    directory = Configuration.get_hamiltonian_dir("hamlib")
    ham_records = pickle.load(open(directory+"100_representative.p", 'rb'))
    metafunc.parametrize("hamiltonian_info", ham_records,
                         ids=lambda x: "ham_" + x['ham_instance'][1:-1])


@benchpress_test_validation
class TestWorkoutDeviceHamlibHamiltonians(WorkoutDeviceHamlibHamiltonians):

    def test_hamlib_hamiltonians_transpile(self, benchmark, hamiltonian_info):
        """Transpile a Hamiltonian against a target device"""
        if hamiltonian_info['ham_qubits'] > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")

        circuit = generate_hamiltonian_circuit(hamiltonian_info.pop('ham_hamlib_hamiltonian'), benchmark)

        @benchmark
        def result():
            trans_qc = TRANS_SERVICE.run(circuit)
            return trans_qc

        benchmark.extra_info.update(hamiltonian_info)
        benchmark.extra_info["gate_count_2q"] = result.count_ops().get(TWO_Q_GATE, 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == TWO_Q_GATE
        )
        assert circuit_validator(result, BACKEND)