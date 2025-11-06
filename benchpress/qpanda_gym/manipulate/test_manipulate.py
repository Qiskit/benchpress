"""Test circuit manipulation"""
import numpy as np

from benchpress.config import Configuration
from benchpress.utilities.io import qasm_circuit_loader
from benchpress.qpanda_gym.circuits import multi_control_circuit
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.manipulate import WorkoutCircuitManipulate
import pyqpanda3.transpilation as pq
from pyqpanda3.core import *

basic_gates = ['X1','RZ','CZ']
@benchpress_test_validation
class TestWorkoutCircuitManipulate(WorkoutCircuitManipulate):
    def test_DTC100_twirling(self, benchmark):
        """Perform Pauli-twirling on a 100Q QV
        circuit
        """
        circuit = qasm_circuit_loader(
            Configuration.get_qasm_dir("dtc") + "dtc_100_cx_12345.qasm", benchmark
        )

        @benchmark
        def result():
            twirled_circuit = direct_twirl(circuit,'CNOT',12345)
            return twirled_circuit

        assert result
        assert 4 * circuit.count_ops(False).get('CNOT') == (
                result.count_ops(False).get('X')
                + result.count_ops(False).get('Y')
                + result.count_ops(False).get('Z')
                + result.count_ops(False).get('I')
        )

    def test_multi_control_decompose(self, benchmark):
        """Decompose a multi-control gate into the
        basis [rx, ry, rz, cz]
        """
        # translate = generate_preset_pass_manager(
        #     1, basis_gates=["rx", "ry", "rz", "cz"]
        # ).translation
        circ = multi_control_circuit(16)

        @benchmark
        def result():
            # translate.property_set = PropertySet()
            out = pq.decompose(circ,basic_gates)
            return out

        benchmark.extra_info["gate_count_2q"] = result.count_ops(True).get("CZ", 0)
        assert result

    def test_QV100_basis_change(self, benchmark):
        """Change a QV100 circuit basis from [rx, ry, rz, cx]
        to [sx, x, rz, cz]
        """
        circ = qasm_circuit_loader(
            Configuration.get_qasm_dir("qv") + "qv_N100_12345.qasm", benchmark
        )

        @benchmark
        def result():
            out = pq.decompose(circ,basic_gates)
            return out

        benchmark.extra_info["gate_count_2q"] = result.count_ops(True).get("CZ", 0)
        assert result

    def test_random_clifford_decompose(self, benchmark):
        """Decompose a random clifford into
        basis [rz, sx, x, cz]
        """

        cliff_circ = qasm_circuit_loader(
            Configuration.get_qasm_dir("clifford") + "clifford_20_12345.qasm", benchmark
        )

        @benchmark
        def result():
            out = pq.decompose(cliff_circ,basic_gates)
            return out

        benchmark.extra_info["gate_count_2q"] = result.count_ops(True).get("CZ", 0)
        benchmark.extra_info["depth_2q"] = result.depth(True)
        assert result
