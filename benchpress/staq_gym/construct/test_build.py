"""Test circuit generation"""

import pytest

from benchpress.workouts.build import WorkoutCircuitConstruction
from benchpress.workouts.validation import benchpress_test_validation


@benchpress_test_validation
class TestWorkoutCircuitConstruction(WorkoutCircuitConstruction):
    @pytest.mark.xfail(
        reason="No circuit building and manipulation in staq.", run=False
    )
    def test_QV100_build(self, benchmark):
        """Measures an SDKs ability to build a 100Q
        QV circit from scratch.
        """
        pass

    @pytest.mark.xfail(
        reason="No circuit building and manipulation in staq.", run=False
    )
    def test_DTC100_set_build(self, benchmark):
        """Measures an SDKs ability to build a set
        of 100Q DTC circuits out to 100 layers of
        the underlying unitary
        """
        pass

    @pytest.mark.xfail(
        reason="No circuit building and manipulation in staq.", run=False
    )
    def test_multi_control_circuit(self, benchmark):
        """Measures an SDKs ability to build a circuit
        with a multi-controlled X-gate
        """
        pass

    @pytest.mark.xfail(
        reason="No circuit building and manipulation in staq.", run=False
    )
    def test_param_circSU2_100_build(self, benchmark):
        """Measures an SDKs ability to build a
        parameterized efficient SU2 circuit with circular entanglement
        over 100Q utilizing 4 repetitions.  This will yield a
        circuit with 1000 parameters
        """
        pass

    @pytest.mark.xfail(
        reason="No circuit building and manipulation in staq.", run=False
    )
    def test_param_circSU2_100_bind(self, benchmark):
        """Measures an SDKs ability to bind 1000 parameters
        to efficient SU2 circuit over 100Q with circular
        entanglement and 4 repetitions.
        """
        pass

    @pytest.mark.xfail(reason="No qasm importing in staq", run=False)
    def test_QV100_qasm2_import(self, benchmark):
        """QASM import of QV100 circuit"""
        pass
