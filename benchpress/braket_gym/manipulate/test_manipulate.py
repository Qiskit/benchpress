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

from braket.circuits import Circuit, Gate, Instruction
from braket.circuits.moments import Moments

from benchpress.config import Configuration
from benchpress.utilities.io import qasm_circuit_loader
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.manipulate import WorkoutCircuitManipulate
from benchpress.braket_gym.circuits import braket_QV


CNOT_twirling_gates = [
    (Gate.I(), Gate.I(), Gate.I(), Gate.I()),
    (Gate.I(), Gate.X(), Gate.I(), Gate.X()),
    (Gate.I(), Gate.Y(), Gate.Z(), Gate.Y()),
    (Gate.I(), Gate.Z(), Gate.Z(), Gate.Z()),
    (Gate.Y(), Gate.I(), Gate.Y(), Gate.X()),
    (Gate.Y(), Gate.X(), Gate.Y(), Gate.I()),
    (Gate.Y(), Gate.Y(), Gate.X(), Gate.Z()),
    (Gate.Y(), Gate.Z(), Gate.X(), Gate.Y()),
    (Gate.X(), Gate.I(), Gate.X(), Gate.X()),
    (Gate.X(), Gate.X(), Gate.X(), Gate.I()),
    (Gate.X(), Gate.Y(), Gate.Y(), Gate.Z()),
    (Gate.X(), Gate.Z(), Gate.Y(), Gate.Y()),
    (Gate.Z(), Gate.I(), Gate.Z(), Gate.I()),
    (Gate.Z(), Gate.X(), Gate.Z(), Gate.X()),
    (Gate.Z(), Gate.Y(), Gate.I(), Gate.Y()),
    (Gate.Z(), Gate.Z(), Gate.I(), Gate.Z()),
]


def _twirl_single_CNOT_gate(op):
    if op.operator.name != "CNot":
        return op

    A, B, C, D = random.choice(CNOT_twirling_gates)
    control_qubit, target_qubit = op.target
    return [
        Instruction(A, control_qubit),
        Instruction(B, target_qubit),
        op,
        Instruction(C, control_qubit),
        Instruction(D, target_qubit),
    ]


def cx_twirl(circuit):
    new_moments = Moments()
    for op in circuit.instructions:
        new_moments.add(_twirl_single_CNOT_gate(op))

    new_circ = Circuit()
    new_circ._moments = new_moments
    return new_circ


@benchpress_test_validation
class TestWorkoutCircuitManipulate(WorkoutCircuitManipulate):
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q DTC
        circuit
        """
        # Unlike other SDKs, the QASM importer is a bit flaky so build a new circuit
        circuit = braket_QV(100, seed=12345)

        @benchmark
        def result():
            out = cx_twirl(circuit)
            return out

        assert result
