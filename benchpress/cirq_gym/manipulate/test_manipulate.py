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
"""Test circuit manipulation"""
import random
import numpy as np

import cirq
from cirq.contrib.qasm_import import circuit_from_qasm

from benchpress.config import Config
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.manipulate import WorkoutCircuitManipulate


CNOT_twirling_gates = [
    (cirq.I, cirq.I, cirq.I, cirq.I),
    (cirq.I, cirq.X, cirq.I, cirq.X),
    (cirq.I, cirq.Y, cirq.Z, cirq.Y),
    (cirq.I, cirq.Z, cirq.Z, cirq.Z),
    (cirq.Y, cirq.I, cirq.Y, cirq.X),
    (cirq.Y, cirq.X, cirq.Y, cirq.I),
    (cirq.Y, cirq.Y, cirq.X, cirq.Z),
    (cirq.Y, cirq.Z, cirq.X, cirq.Y),
    (cirq.X, cirq.I, cirq.X, cirq.X),
    (cirq.X, cirq.X, cirq.X, cirq.I),
    (cirq.X, cirq.Y, cirq.Y, cirq.Z),
    (cirq.X, cirq.Z, cirq.Y, cirq.Y),
    (cirq.Z, cirq.I, cirq.Z, cirq.I),
    (cirq.Z, cirq.X, cirq.Z, cirq.X),
    (cirq.Z, cirq.Y, cirq.I, cirq.Y),
    (cirq.Z, cirq.Z, cirq.I, cirq.Z),
]


def _twirl_single_CNOT_gate(op):
    if op.gate != cirq.CNOT:
        return op

    A, B, C, D = random.choice(CNOT_twirling_gates)
    control_qubit, target_qubit = op.qubits
    return [
        A.on(control_qubit),
        B.on(target_qubit),
        op,
        C.on(control_qubit),
        D.on(target_qubit),
    ]


@benchpress_test_validation
class TestWorkoutCircuitManipulate(WorkoutCircuitManipulate):
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q QV
        circuit
        """
        with open(Config.get_qasm_dir("dtc") + "dtc_100_cx_12345.qasm", "r") as file:
            circ_data = file.read().replace("\n", "")
        circuit = circuit_from_qasm(circ_data)

        @benchmark
        def result():
            twirled_circuit = circuit.map_operations(_twirl_single_CNOT_gate)
            return twirled_circuit

        assert result
