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
class WorkoutDeviceFeynman:

    @pytest.mark.skip(reason="Not implemented")
    def test_feynman_transpile(self, benchmark, filename):
        """Transpile a Quantum Fourier Transform (QFT) 100 circuit against a target device"""
        pass
