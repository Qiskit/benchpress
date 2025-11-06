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
"""Test qasmbench against abstract backend topologies"""

from benchpress.config import Configuration
from benchpress.utilities.backends import FlexibleBackend
from benchpress.workouts.abstract_transpile.qasmbench import (
    SMALL_CIRC_TOPO,
    SMALL_NAMES,
    MEDIUM_CIRC_TOPO,
    MEDIUM_NAMES,
    LARGE_CIRC_TOPO,
    LARGE_NAMES,
)

OPTIMIZATION_LEVEL = Configuration.options["qiskit"]["optimization_level"]

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
"""Test qasmbench against abstract backend topologies"""
import pytest
from pyqpanda3.core import QProg
from pyqpanda3.transpilation import *
from benchpress.utilities.io import qasm_circuit_loader, output_circuit_properties
from benchpress.utilities.validation import circuit_validator
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.config import Configuration

from benchpress.workouts.abstract_transpile import (
    WorkoutAbstractQasmBenchSmall,
    WorkoutAbstractQasmBenchMedium,
    WorkoutAbstractQasmBenchLarge,
)

OPTIMIZATION_LEVEL = Configuration.options["qpanda"]["optimization_level"]
basic_gates = ['X1','RZ','CZ']

@benchpress_test_validation
class TestWorkoutAbstractQasmBenchSmall(WorkoutAbstractQasmBenchSmall):
    @pytest.mark.parametrize("circ_and_topo", SMALL_CIRC_TOPO, ids=SMALL_NAMES)
    def test_QASMBench_small(self, benchmark, circ_and_topo):
        prog = qasm_circuit_loader(circ_and_topo[0], benchmark)
        backend = FlexibleBackend(len(prog.qubits()), layout=circ_and_topo[1])
        topo = backend.configuration().coupling_map
        pm = Transpiler()

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchMedium(WorkoutAbstractQasmBenchMedium):
    @pytest.mark.parametrize("circ_and_topo", MEDIUM_CIRC_TOPO, ids=MEDIUM_NAMES)
    def test_QASMBench_medium(self, benchmark, circ_and_topo):
        prog = qasm_circuit_loader(circ_and_topo[0], benchmark)
        backend = FlexibleBackend(len(prog.qubits()), layout=circ_and_topo[1])
        topo = backend.configuration().coupling_map
        pm = Transpiler()

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchLarge(WorkoutAbstractQasmBenchLarge):
    @pytest.mark.parametrize("circ_and_topo", LARGE_CIRC_TOPO, ids=LARGE_NAMES)
    def test_QASMBench_large(self, benchmark, circ_and_topo):
        prog = qasm_circuit_loader(circ_and_topo[0], benchmark)
        backend = FlexibleBackend(len(prog.qubits()), layout=circ_and_topo[1])
        topo = backend.configuration().coupling_map
        pm = Transpiler()

        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL, basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)
