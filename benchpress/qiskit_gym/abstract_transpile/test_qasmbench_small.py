"""Test summit benchmarks"""
import pytest
from qiskit import QuantumCircuit
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

from benchpress.config import Configuration
from benchpress.utilities.io import get_qasmbench_circuits
from benchpress.utilities.backends import FlexibleBackend

BACKEND = Configuration.backend()
OPTIMIZATION_LEVEL = Configuration.options['qiskit']["optimization_level"]
TOPOLOGY_NAMES = ['heavy-hex', 'square', 'linear']

qasm_dir = Configuration.get_qasm_dir("qasmbench-small")
circuits, names = get_qasmbench_circuits(qasm_dir)

circs_and_topo = []
test_ids = []
for idx, circ in enumerate(circuits):
    for topo_name in TOPOLOGY_NAMES:
        circs_and_topo.append((circ, topo_name))
        test_ids.append(names[idx]+'-'+topo_name)




class TestQASMBenchSmall:
    @pytest.mark.parametrize( "circ_and_topo", circs_and_topo, ids=test_ids)  
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
