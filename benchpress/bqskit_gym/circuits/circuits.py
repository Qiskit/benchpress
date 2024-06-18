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
"""Test circuit generation"""

import numpy as np
import pytest
from bqskit.ir import Circuit
from bqskit.ir.gates import (
    CNOTGate,
    ConstantUnitaryGate,
    ControlledGate,
    HGate,
    MeasurementPlaceholder,
    RXGate,
    RYGate,
    RZGate,
    RZZGate,
    XGate,
    ZGate,
)
from bqskit.qis.unitary import UnitaryMatrix
from scipy import stats
from sympy import Symbol


def bqskit_QV(num_qubits, depth=None, seed=None):
    """Construct QV circuit

    Parameters:
        width (int): Number of qubits
        depth (int): Number of QV layers
        seed (int): RNG seed, default=None

    Returns:
        Circuit: QV circuit
    """
    RNG = np.random.default_rng(seed=seed)
    out = Circuit(num_qudits=num_qubits)
    depth = depth or num_qubits
    width = int(np.floor(num_qubits / 2))
    perm_0 = np.arange(num_qubits)
    for _ in range(depth):
        perm = RNG.permutation(perm_0)
        for w in range(width):
            su4 = stats.unitary_group.rvs(4, random_state=RNG)
            unitary = UnitaryMatrix(input=su4)
            gate = ConstantUnitaryGate(utry=unitary)
            physical_qubits = int(perm[2 * w]), int(perm[2 * w + 1])
            out.append_gate(gate, [physical_qubits[0], physical_qubits[1]])
    return out


def bqskit_circSU2(width, num_reps=3):
    """Efficient SU2 circuit with circular entanglement
    and using Ry and Rz 1Q-gates'

    Parameters:
        width (int): Number of qubits in circuit
        num_reps (int): Number of repetitions, default = 3

    Returns:
        Circuit: Output circuit
    """
    out = Circuit(width)
    counter = 0
    for qubit in range(0, width):
        out.append_gate(RYGate(), qubit)
        out.append_gate(RZGate(), qubit)

        counter += 1
    counter += width

    for _ in range(num_reps):
        out.append_gate(CNOTGate(), [width - 1, 0])
        for qubit in range(width - 1):
            out.append_gate(CNOTGate(), [qubit, qubit + 1])

        for qubit in range(width):
            out.append_gate(RYGate(), qubit)
            out.append_gate(RZGate(), qubit)
            counter += 1
        counter += width
    return out


def dtc_unitary(num_qubits, g=0.95, seed=12345):
    rng = np.random.default_rng(seed=seed)

    qc = Circuit(num_qubits)

    for i in range(num_qubits):
        qc.append_gate(RXGate(), i, params=[g * np.pi])

    for i in range(0, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        qc.append_gate(RZZGate(), [i, i + 1], params=[phi])

    for i in range(1, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        qc.append_gate(RZZGate(), [i, i + 1], params=[phi])

    # Longitudinal fields for disorder
    for i in range(num_qubits):
        h = rng.uniform(low=-np.pi, high=np.pi)
        qc.append_gate(RZGate(), i, params=[h])

    return qc


def multi_control_circuit(num_qubits):
    out = Circuit(num_qubits)
    out.append_gate(XGate(), 0)
    for i in range(1, num_qubits):
        gate = ControlledGate(gate=XGate(), num_controls=i)
        out.append_gate(gate, range(i + 1))

    return out


def bqskit_bv_all_ones(N):
    """A circuit to generate a BV circuit over N
    qubits for an all-ones bit-string

    Parameters:
        N (int): Number of qubits in circuit

    Returns:
        Circuit: BV circuit
    """
    out = Circuit(N)
    out.append_gate(XGate(), [N - 1])
    out.append_gate(HGate(), [N - 1])
    for kk in range(N - 1):
        out.append_gate(HGate(), [kk])
        out.append_gate(CNOTGate(), [kk, N - 1])
        out.append_gate(HGate(), [kk])

    creg = ("meas", N)
    measurements = {qubit: ("meas", qubit) for qubit in range(N)}
    meas_op = MeasurementPlaceholder([creg], measurements)
    out.append_gate(meas_op, range(N))
    return out


def trivial_bvlike_circuit(N):
    """A trivial circuit that should boil down
    to just a X and Z gate since they commute out

    Parameters:
        N (int): Number of qubits

    Returns:
        Circuit: Output circuit
    """
    qc = Circuit(N)
    for kk in range(N - 1):
        qc.append_gate(CNOTGate(), [kk, N - 1])
    qc.append_gate(XGate(), [N - 1])
    qc.append_gate(ZGate(), [N - 2])
    for kk in range(N - 2, -1, -1):
        qc.append_gate(CNOTGate(), [kk, N - 1])
    return qc
