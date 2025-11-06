"""Test summit benchmarks"""
from pyqpanda3.transpilation import *
import pytest
from benchpress.config import Configuration
from benchpress.utilities.io import (
    qasm_circuit_loader,
    input_circuit_properties,
    output_circuit_properties,
)
from benchpress.utilities.validation import circuit_validator

from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.device_transpile import WorkoutDeviceTranspile100Q
from benchpress.qpanda_gym.circuits import qpanda_bv_all_ones, qpanda_circSU2, trivial_bvlike_circuit, qpanda_QV

BACKEND = Configuration.backend()
TWO_Q_GATE = BACKEND.two_q_gate_type
OPTIMIZATION_LEVEL = Configuration.options["qpanda"]["optimization_level"]
basic_gates = ['X1','RZ','CZ']

@benchpress_test_validation
class TestWorkoutDeviceTranspile100Q(WorkoutDeviceTranspile100Q):
    def test_QFT_100_transpile(self, benchmark):
        """Compile 100Q QFT circuit against target backend"""

        prog = qasm_circuit_loader(
            Configuration.get_qasm_dir("qft") + "qft_N100.qasm", benchmark
        )

        if len(prog.qubits()) > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")
        pm = Transpiler()
        topo = BACKEND.configuration().coupling_map


        @benchmark
        def result():
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)

    def test_QV_100_transpile(self, benchmark):
        """Compile 10Q QV circuit against target backend"""
        prog = qpanda_QV(100, 100, seed=12345)
        if len(prog.qubits()) > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")
        pm = Transpiler()
        topo = BACKEND.configuration().coupling_map

        @benchmark
        def result():
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)

    def test_circSU2_89_transpile(self, benchmark):
        """Compile 89Q circSU2 circuit against target backend"""
        prog = qpanda_circSU2(89, 3)
        input_circuit_properties(prog, benchmark)
        if len(prog.qubits()) > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")
        pm = Transpiler()
        topo = BACKEND.configuration().coupling_map
        @benchmark
        def result():
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)

    def test_circSU2_100_transpile(self, benchmark):
        """Compile 100Q circSU2 circuit against target backend"""
        prog = qpanda_circSU2(100, 3)
        input_circuit_properties(prog, benchmark)
        if len(prog.qubits()) > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")
        pm = Transpiler()
        topo = BACKEND.configuration().coupling_map

        @benchmark
        def result():
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)

    def test_BV_100_transpile(self, benchmark):
        """Compile 100Q BV circuit against target backend"""
        prog = qpanda_bv_all_ones(100)
        input_circuit_properties(prog, benchmark)
        if len(prog.qubits()) > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")
        pm = Transpiler()
        topo = BACKEND.configuration().coupling_map

        @benchmark
        def result():
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)

    def test_square_heisenberg_100_transpile(self, benchmark):
        """Compile 100Q square-Heisenberg circuit against target backend"""
        prog = qasm_circuit_loader(
            Configuration.get_qasm_dir("square-heisenberg")
            + "square_heisenberg_N100.qasm",
            benchmark,
        )
        if len(prog.qubits()) > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")
        pm = Transpiler()
        topo = BACKEND.configuration().coupling_map


        @benchmark
        def result():
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)

    def test_QAOA_100_transpile(self, benchmark):
        """Compile 100Q QAOA circuit against target backend"""
        prog = qasm_circuit_loader(
            Configuration.get_qasm_dir("qaoa") + "qaoa_barabasi_albert_N100_3reps.qasm",
            benchmark,
        )
        if len(prog.qubits()) > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")
        pm = Transpiler()
        topo = BACKEND.configuration().coupling_map


        @benchmark
        def result():
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)

    def test_BVlike_simplification_transpile(self, benchmark):
        """Transpile a BV-like circuit that should collapse down
        into a single X and Z gate on a target device
        """
        prog = trivial_bvlike_circuit(100)
        input_circuit_properties(prog, benchmark)
        if len(prog.qubits()) > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")
        pm = Transpiler()
        topo = BACKEND.configuration().coupling_map

        @benchmark
        def result():
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)

    def test_clifford_100_transpile(self, benchmark):
        """Compile 100Q Clifford circuit against target backend"""
        prog = qasm_circuit_loader(
            Configuration.get_qasm_dir("clifford") + "clifford_100_12345.qasm",
            benchmark,
        )

        if len(prog.qubits()) > BACKEND.num_qubits:
            pytest.skip("Circuit too large for given backend.")
        pm = Transpiler()
        topo = BACKEND.configuration().coupling_map

        @benchmark
        def result():
            aft_prog = pm.transpile(prog, topo, {}, OPTIMIZATION_LEVEL,basic_gates)
            return aft_prog

        output_circuit_properties(result, '2Q_GATE', benchmark)
        assert circuit_validator(result, topo)
