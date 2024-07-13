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

from benchpress.config import Configuration
from benchpress.utilities.io import get_qasmbench_circuits

TOPOLOGY_NAMES = Configuration.options['general']['abstract_topologies']


def qasmbench_parameters(size):
    qasm_dir = Configuration.get_qasm_dir(f"qasmbench-{size}")
    circuits, names = get_qasmbench_circuits(qasm_dir)

    circs_and_topo = []
    test_ids = []
    for idx, circ in enumerate(circuits):
        for topo_name in TOPOLOGY_NAMES:
            circs_and_topo.append((circ, topo_name))
            test_ids.append(names[idx]+'-'+topo_name)
    return circs_and_topo, test_ids

SMALL_CIRC_TOPO, SMALL_NAMES = qasmbench_parameters('small')
MEDIUM_CIRC_TOPO, MEDIUM_NAMES = qasmbench_parameters('medium')
LARGE_CIRC_TOPO, LARGE_NAMES = qasmbench_parameters('large')

@pytest.mark.benchmark(group="Transpile - Abstract")
class WorkoutAbstractQasmBenchSmall:
    @pytest.mark.parametrize( "circ_and_topo", SMALL_CIRC_TOPO, ids=SMALL_NAMES)  
    @pytest.mark.skip(reason="Not implemented")
    def test_QASMBench_small(self, benchmark, circ_and_topo):
        """Abstract transpilation for qasmbench small"""
        pass


@pytest.mark.benchmark(group="Transpile - Abstract")
class WorkoutAbstractQasmBenchMedium:
    @pytest.mark.parametrize( "circ_and_topo", MEDIUM_CIRC_TOPO, ids=MEDIUM_NAMES)  
    @pytest.mark.skip(reason="Not implemented")
    def test_QASMBench_medium(self, benchmark, circ_and_topo):
        """Abstract transpilation for qasmbench medium"""
        pass


@pytest.mark.benchmark(group="Transpile - Abstract")
class WorkoutAbstractQasmBenchLarge:
    @pytest.mark.parametrize( "circ_and_topo", LARGE_CIRC_TOPO, ids=LARGE_NAMES)  
    @pytest.mark.skip(reason="Not implemented")
    def test_QASMBench_large(self, benchmark, circ_and_topo):
        """Abstract transpilation for qasmbench large"""
        pass
