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
import os
import pytest
from pyqpanda3.transpilation import *
from benchpress.config import Configuration
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceFeynman
from benchpress.utilities.io import qasm_circuit_loader, output_circuit_properties
from benchpress.utilities.validation import circuit_validator

BACKEND = Configuration.backend()
TWO_Q_GATE = BACKEND.two_q_gate_type
OPTIMIZATION_LEVEL = Configuration.options["qpanda"]["optimization_level"]
basic_gates = ['X1','RZ','CZ']

def pytest_generate_tests(metafunc):
    directory = Configuration.get_qasm_dir("feynman")
    file_list = [x for x in os.listdir(directory) if x.endswith(".qasm")]
    metafunc.parametrize("filename", file_list)


@benchpress_test_validation
class TestWorkoutDeviceFeynman(WorkoutDeviceFeynman):

    def test_feynman_transpile(self, benchmark, filename):
        """Transpile a feynman benchmark qasm file against a target device"""
        prog = qasm_circuit_loader(
            f"{Configuration.get_qasm_dir('feynman')}{filename}", benchmark
        )

        if len(prog.qubits()) > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")
        pm = Transpiler()
        topo = BACKEND.configuration().coupling_map
        # print(topo)

        @benchmark
        def result():
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)
