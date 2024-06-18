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

import numpy as np
import os
import pytest
import numpy as np

from pytket.circuit import OpType
from pytket.qasm import circuit_from_qasm
from pytket.tailoring import PauliFrameRandomisation
from pytket.predicates import CompilationUnit
from pytket.passes import DecomposeMultiQubitsCX, DecomposeBoxes
from pytket.passes import SequencePass, auto_rebase_pass


from benchpress.tket_gym.circuits import multi_control_circuit
from benchpress.config import Config
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.manipulate import WorkoutCircuitManipulate


@benchpress_test_validation
class TestWorkoutCircuitManipulate(WorkoutCircuitManipulate):
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q QV
        circuit
        """
        circuit = circuit_from_qasm(
            Config.get_qasm_dir("dtc") + "dtc_100_cx_12345.qasm"
        )
        PauliTwirling = PauliFrameRandomisation()

        @benchmark
        def result():
            twirled_circuit = PauliTwirling.sample_circuits(circuit, 1)
            return twirled_circuit

        assert result

    def test_multi_control_decompose(self, benchmark):
        """Decompose a multi-control gate into the
        basis [rx, ry, rz, cz]
        """
        seqpass = SequencePass(
            [
                DecomposeBoxes(),
                DecomposeMultiQubitsCX(),
                auto_rebase_pass({OpType.Rx, OpType.Ry, OpType.Rz, OpType.CZ}),
            ]
        )
        circ = multi_control_circuit(16)

        @benchmark
        def result():
            cu = CompilationUnit(
                circ.copy()
            )  # Copy is needed because modifications are in-place
            seqpass.apply(cu)
            return cu.circuit

        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        assert result

    def test_QV100_basis_change(self, benchmark):
        """Change a QV100 circuit basis from [rx, ry, rz, cx]
        to [sx, x, rz, cz]
        """
        seqpass = SequencePass(
            [
                DecomposeBoxes(),
                DecomposeMultiQubitsCX(),
                auto_rebase_pass({OpType.SX, OpType.X, OpType.Rz, OpType.CZ}),
            ]
        )
        circ = circuit_from_qasm(Config.get_qasm_dir("qv") + "qv_N100_12345.qasm")

        @benchmark
        def result():
            cu = CompilationUnit(
                circ.copy()
            )  # Copy is needed because modifications are in-place
            seqpass.apply(cu)
            return cu.circuit

        assert result
