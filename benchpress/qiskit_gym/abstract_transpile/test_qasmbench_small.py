"""Test summit benchmarks"""
import pytest
from qiskit import QuantumCircuit, transpile

from benchpress.config import Configuration
from benchpress.utilities.io import get_qasmbench_circuits


qasm_dir = Configuration.get_qasm_dir("qasmbench-small")
circuits, names = get_qasmbench_circuits(qasm_dir)


args = get_args(filename=Config.get_args_file())
backend = get_backend(backend_name=args["backend_name"], bench_name="qiskit")

class TestQASMBenchMedium:
    @pytest.mark.parametrize( "qasm_str", circuits, ids=names)  
    def test_QASMBench_large(self, benchmark, qasm_str):
        circuit = QuantumCircuit.from_qasm_file(qasm_str)
        @benchmark
        def result():
            trans_qc = transpile(
                circuit, backend, optimization_level=args["optimization_level"]
            )
            return trans_qc
        benchmark.extra_info["gate_count_2q"] = result.count_ops().get("cz", 0)
        benchmark.extra_info["depth_2q"] = result.depth(
            filter_function=lambda x: x.operation.name == "cz"
        )
        assert result
