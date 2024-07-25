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
import pytest


@pytest.mark.benchmark(group="Transpile - Device")
class WorkoutDeviceTranspile100Q:
    @pytest.mark.skip(reason="Not implimented")
    def test_QFT_100_transpile(self, benchmark):
        """Transpile a Quantum Fourier Transform (QFT) 100 circuit against a target device"""
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_QV_100_transpile(self, benchmark):
        """Transpile a Quantum Volume (QV) 100 circuit against a target device"""
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_circSU2_100_transpile(self, benchmark):
        """Transpile a SU2 circuit with circular entanglement against a target device"""
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_BV_100_transpile(self, benchmark):
        """Transpile a 100Q Berstein-Vazirani (BV) circuit with an all-ones bit-string
        against a target device
        """
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_square_heisenberg_100_transpile(self, benchmark):
        """Transpile a 100Q Heisenberg Hamiltonian matching a square topology
        against a target device
        """
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_QAOA_100_transpile(self, benchmark):
        """Transpile a 100Q QAOA circuit with 3 repetitions derived from
        a random Barabasi-Albert graph to a target device
        """
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_BVlike_simplification_transpile(self, benchmark):
        """Transpile a BV-like circuit that should collapse down
        into a single X and Z gate on a target device
        """
        pass

    @pytest.mark.skip(reason="Not implimented")
    def test_clifford_100_transpile(self, benchmark):
        """Transpile a Clifford 100 circuit against a target device"""
        pass
