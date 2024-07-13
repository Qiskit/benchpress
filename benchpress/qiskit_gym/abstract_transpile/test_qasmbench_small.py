"""Test summit benchmarks"""
import pytest

from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

from benchpress.workouts.validation import benchpress_test_validation
from benchpress.config import Configuration
from benchpress.utilities.backends import FlexibleBackend

from benchpress.workouts.abstract_transpile import (WorkoutAbstractQasmBenchSmall,
                                                    WorkoutAbstractQasmBenchMedium,
                                                    WorkoutAbstractQasmBenchLarge)
from benchpress.workouts.abstract_transpile.qasmbench import (SMALL_CIRC_TOPO, SMALL_NAMES,
                                                              MEDIUM_CIRC_TOPO, MEDIUM_NAMES,
                                                              LARGE_CIRC_TOPO, LARGE_NAMES)


BACKEND = Configuration.backend()
OPTIMIZATION_LEVEL = Configuration.options['qiskit']["optimization_level"]


@benchpress_test_validation
class TestWorkoutAbstractOpenQasmSmall(WorkoutAbstractQasmBenchSmall):
    @pytest.mark.parametrize( "circ_and_topo", SMALL_CIRC_TOPO, ids=SMALL_NAMES)  
    def test_QASMBench_small(self, benchmark, circ_and_topo):
        circuit = QuantumCircuit.from_qasm_file(circ_and_topo[0])
        backend = FlexibleBackend(circuit.num_qubits, circ_and_topo[1])
        pm = generate_preset_pass_manager(optimization_level=OPTIMIZATION_LEVEL,
                                          backend=backend)
        @benchmark
        def result():
            trans_qc = pm.run(circuit)
            return trans_qc
        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result


@benchpress_test_validation
class TestWorkoutAbstractOpenQasmMedium(WorkoutAbstractQasmBenchMedium):
    @pytest.mark.parametrize( "circ_and_topo", MEDIUM_CIRC_TOPO, ids=MEDIUM_NAMES)  
    def test_QASMBench_medium(self, benchmark, circ_and_topo):
        circuit = QuantumCircuit.from_qasm_file(circ_and_topo[0])
        backend = FlexibleBackend(circuit.num_qubits, circ_and_topo[1])
        pm = generate_preset_pass_manager(optimization_level=OPTIMIZATION_LEVEL,
                                          backend=backend)
        @benchmark
        def result():
            trans_qc = pm.run(circuit)
            return trans_qc
        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result


@benchpress_test_validation
class TestWorkoutAbstractOpenQasmLarge(WorkoutAbstractQasmBenchLarge):
    @pytest.mark.parametrize( "circ_and_topo", LARGE_CIRC_TOPO, ids=LARGE_NAMES)  
    def test_QASMBench_large(self, benchmark, circ_and_topo):
        circuit = QuantumCircuit.from_qasm_file(circ_and_topo[0])
        backend = FlexibleBackend(circuit.num_qubits, circ_and_topo[1])
        pm = generate_preset_pass_manager(optimization_level=OPTIMIZATION_LEVEL,
                                          backend=backend)
        @benchmark
        def result():
            trans_qc = pm.run(circuit)
            return trans_qc
        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result
