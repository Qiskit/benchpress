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
from sympy import Symbol
from pytket.circuit import Unitary2qBox, Circuit, QControlBox, CircBox
from scipy import stats


def tket_QV(num_qubits, depth=None, seed=None):
    """Construct QV circuit

    Parameters:
        width (int): Number of qubits
        depth (int): Number of QV layers
        seed (int): RNG seed, default=None

    Returns:
        Circuit: QV circuit
    """
    RNG = np.random.default_rng(seed=seed)
    out = Circuit(num_qubits)
    depth = depth or num_qubits
    width = int(np.floor(num_qubits / 2))
    perm_0 = np.arange(num_qubits)
    for _ in range(depth):
        perm = RNG.permutation(perm_0)
        for w in range(width):
            su4 = stats.unitary_group.rvs(4, random_state=RNG)
            physical_qubits = int(perm[2 * w]), int(perm[2 * w + 1])
            out.add_unitary2qbox(
                Unitary2qBox(su4), physical_qubits[0], physical_qubits[1]
            )
    return out


def tket_circSU2(width, num_reps=3):
    """Efficient SU2 circuit with circular entanglement
    and using Ry and Rz 1Q-gates'

    Parameters:
        width (int): Number of qubits in circuit
        num_reps (int): Number of repetitions, default = 3

    Returns:
        Circuit: Output circuit
    """
    num_params = 2 * width * (num_reps + 1)

    params = [Symbol(f"x_{kk}") for kk in range(num_params)]

    out = Circuit(width)
    counter = 0
    for qubit in range(0, width):
        out.Ry(params[counter], qubit)
        out.Rz(params[counter + width], qubit)
        counter += 1
    counter += width

    for _ in range(num_reps):
        out.CX(width - 1, 0)
        for qubit in range(width - 1):
            out.CX(qubit, qubit + 1)

        for qubit in range(width):
            out.Ry(params[counter], qubit)
            out.Rz(params[counter + width], qubit)
            counter += 1
        counter += width
    return out


def dtc_unitary(num_qubits, g=0.95, seed=12345):
    rng = np.random.default_rng(seed=seed)

    qc = Circuit(num_qubits)

    for i in range(num_qubits):
        qc.Rx(g * np.pi, i)

    for i in range(0, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        qc.ZZPhase(2 * phi, i, i + 1)
    for i in range(1, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        qc.ZZPhase(2 * phi, i, i + 1)

    # Longitudinal fields for disorder
    for i in range(num_qubits):
        h = rng.uniform(low=-np.pi, high=np.pi)
        qc.Rz(h * np.pi, i)
    return qc


def multi_control_circuit(num_qubits):
    sub = Circuit(1)
    sub.X(0)
    sub_box = CircBox(sub)

    out = Circuit(num_qubits)
    out.add_circbox(sub_box, [0])

    for kk in range(1, num_qubits):
        sub_box = QControlBox(sub_box, 1)
        out.add_qcontrolbox(sub_box, range(kk + 1))
    return out


def tket_bv_all_ones(N):
    """A circuit to generate a BV circuit over N
    qubits for an all-ones bit-string

    Parameters:
        N (int): Number of qubits in circuit

    Returns:
        Circuit: BV circuit
    """
    out = Circuit(N, N)
    out.X(N - 1)
    out.H(N - 1)
    for kk in range(N - 1):
        out.H(kk)
        out.CX(kk, N - 1)
        out.H(kk)
        out.Measure(kk, kk)
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
        qc.CX(kk, N - 1)
    qc.X(N - 1)
    qc.Z(N - 2)
    for kk in range(N - 2, -1, -1):
        qc.CX(kk, N - 1)
    return qc
