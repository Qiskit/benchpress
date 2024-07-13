"""Test qasmbench against abstract backend topologies"""
import pytest

from pytket.circuit import OpType
from pytket.qasm import circuit_from_qasm

from benchpress.workouts.validation import benchpress_test_validation
from benchpress.config import Configuration
from benchpress.tket_gym.utils.tket_backend_utils import TketFlexibleBackend

from benchpress.workouts.abstract_transpile import (WorkoutAbstractQasmBenchSmall,
                                                    WorkoutAbstractQasmBenchMedium,
                                                    WorkoutAbstractQasmBenchLarge)
from benchpress.workouts.abstract_transpile.qasmbench import (SMALL_CIRC_TOPO, SMALL_NAMES,
                                                              MEDIUM_CIRC_TOPO, MEDIUM_NAMES,
                                                              LARGE_CIRC_TOPO, LARGE_NAMES)

OPTIMIZATION_LEVEL = Configuration.options['tket']["optimization_level"]


@benchpress_test_validation
class TestWorkoutAbstractOpenQasmSmall(WorkoutAbstractQasmBenchSmall):
    @pytest.mark.parametrize( "circ_and_topo", SMALL_CIRC_TOPO, ids=SMALL_NAMES)  
    def test_QASMBench_small(self, benchmark, circ_and_topo):
        circuit = circuit_from_qasm(circ_and_topo[0])
        backend = TketFlexibleBackend(circuit.n_qubits, circ_and_topo[1])
        pm = backend.default_compilation_pass(optimisation_level=OPTIMIZATION_LEVEL)
        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            pm.apply(new_circ)
            return new_circ
        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result


@benchpress_test_validation
class TestWorkoutAbstractOpenQasmMedium(WorkoutAbstractQasmBenchMedium):
    @pytest.mark.parametrize( "circ_and_topo", MEDIUM_CIRC_TOPO, ids=MEDIUM_NAMES)  
    def test_QASMBench_medium(self, benchmark, circ_and_topo):
        circuit = circuit_from_qasm(circ_and_topo[0])
        backend = TketFlexibleBackend(circuit.n_qubits, circ_and_topo[1])
        pm = backend.default_compilation_pass(optimisation_level=OPTIMIZATION_LEVEL)
        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            pm.apply(new_circ)
            return new_circ
        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result


@benchpress_test_validation
class TestWorkoutAbstractOpenQasmLarge(WorkoutAbstractQasmBenchLarge):
    @pytest.mark.parametrize( "circ_and_topo", LARGE_CIRC_TOPO, ids=LARGE_NAMES)  
    def test_QASMBench_large(self, benchmark, circ_and_topo):
        circuit = circuit_from_qasm(circ_and_topo[0])
        backend = TketFlexibleBackend(circuit.n_qubits, circ_and_topo[1])
        pm = backend.default_compilation_pass(optimisation_level=OPTIMIZATION_LEVEL)
        @benchmark
        def result():
            # Need to make a copy as the compilation is done in-place
            new_circ = circuit.copy()
            pm.apply(new_circ)
            return new_circ
        benchmark.extra_info["gate_count_2q"] = result.n_gates_of_type(OpType.CZ)
        benchmark.extra_info["depth_2q"] = result.depth_by_type(OpType.CZ)
        assert result
