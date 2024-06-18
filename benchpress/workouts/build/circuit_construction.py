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


"""Test basic circuit construction"""
import pytest

@pytest.mark.benchmark(group="Circuit construction")
class WorkoutCircuitConstruction:
    @pytest.mark.skip(reason="Not implimented")
    def test_QV100_build(self, benchmark):
        """Measures an SDKs ability to build a 100Q
        QV circit from scratch.
        """
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_DTC100_set_build(self, benchmark):
        """Measures an SDKs ability to build a set
        of 100Q DTC circuits out to 100 layers of
        the underlying unitary
        """
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_multi_control_circuit(self, benchmark):
        """Measures an SDKs ability to build a circuit
        with a multi-controlled X-gate
        """
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_param_circSU2_100_build(self, benchmark):
        """Measures an SDKs ability to build a
        parameterized efficient SU2 circuit with circular entanglement
        over 100Q utilizing 4 repetitions.  This will yield a
        circuit with 1000 parameters
        """
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_param_circSU2_100_bind(self, benchmark):
        """Measures an SDKs ability to bind 1000 parameters
        to efficient SU2 circuit over 100Q with circular
        entanglement and 4 repetitions.
        """
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_QV100_qasm2_import(self, benchmark):
        """Gather metrics on an SDKs import of a
        QV100 circuit from a QASM2 file
        """
        pass
