"""Test qasmbench against abstract backend topologies"""

import pytest

from bqskit import Circuit, compile
from bqskit.compiler import Compiler
from bqskit.ir.gates import CNOTGate, CXGate, CZGate
from benchpress.bqskit_gym.utils.bqskit_backend_utils import ECRGate
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.config import Configuration
from benchpress.bqskit_gym.utils.bqskit_backend_utils import BqskitFlexibleBackend

from benchpress.workouts.abstract_transpile import (
    WorkoutAbstractQasmBenchSmall,
    WorkoutAbstractQasmBenchMedium,
    WorkoutAbstractQasmBenchLarge,
)
from benchpress.workouts.abstract_transpile.qasmbench import (
    SMALL_CIRC_TOPO,
    SMALL_NAMES,
    MEDIUM_CIRC_TOPO,
    MEDIUM_NAMES,
    LARGE_CIRC_TOPO,
    LARGE_NAMES,
)
#BACKEND = Configuration.backend()
OPTIMIZATION_LEVEL = Configuration.options["bqskit"]["optimization_level"]


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchSmall(WorkoutAbstractQasmBenchSmall):
    @pytest.mark.parametrize("circ_and_topo", SMALL_CIRC_TOPO, ids=SMALL_NAMES)
    def test_QASMBench_small(self, benchmark, circ_and_topo):
        circuit = Circuit.from_file(circ_and_topo[0])
        BACKEND = BqskitFlexibleBackend(circuit.num_qudits, circ_and_topo[1])
        compiler = Compiler()
        @benchmark
        def result():
            new_circ = compile(
                circuit,
                model=BACKEND,
                optimization_level=OPTIMIZATION_LEVEL,
                compiler=compiler,
            )
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.gate_counts[CZGate()]
        benchmark.extra_info["depth_2q"] = result.multi_qudit_depth
        assert result


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchMedium(WorkoutAbstractQasmBenchMedium):
    @pytest.mark.parametrize("circ_and_topo", MEDIUM_CIRC_TOPO, ids=MEDIUM_NAMES)
    def test_QASMBench_medium(self, benchmark, circ_and_topo):
        circuit = Circuit.from_file(circ_and_topo[0])
        BACKEND = BqskitFlexibleBackend(circuit.num_qudits, circ_and_topo[1])
        compiler = Compiler()
        @benchmark
        def result():
            new_circ = compile(
                circuit,
                model=BACKEND,
                optimization_level=OPTIMIZATION_LEVEL,
                compiler=compiler,
            )
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.gate_counts[CZGate()]
        benchmark.extra_info["depth_2q"] = result.multi_qudit_depth
        assert result


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchLarge(WorkoutAbstractQasmBenchLarge):
    @pytest.mark.parametrize("circ_and_topo", LARGE_CIRC_TOPO, ids=LARGE_NAMES)
    def test_QASMBench_large(self, benchmark, circ_and_topo):
        circuit = Circuit.from_file(circ_and_topo[0])
        BACKEND = BqskitFlexibleBackend(circuit.num_qudits, circ_and_topo[1])
        compiler = Compiler()
        @benchmark
        def result():
            new_circ = compile(
                circuit,
                model=BACKEND,
                optimization_level=OPTIMIZATION_LEVEL,
                compiler=compiler,
            )
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.gate_counts[CZGate()]
        benchmark.extra_info["depth_2q"] = result.multi_qudit_depth
        assert result





