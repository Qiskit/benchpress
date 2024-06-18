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
from braket.circuits import Circuit, FreeParameter
from scipy import stats


def braket_circSU2(width, num_reps=3):
    """Efficient SU2 circuit with circular entanglement
    and using Ry and Rz 1Q-gates'

    Parameters:
        width (int): Number of qubits in circuit
        num_reps (int): Number of repetitions, default = 3

    Returns:
        Circuit: Output circuit
    """
    num_params = 2 * width * (num_reps + 1)
    params = [FreeParameter(f"x_{kk}") for kk in range(num_params)]

    out = Circuit()
    counter = 0
    for qubit in range(0, width):
        out.ry(qubit, params[counter])
        out.rz(qubit, params[counter + width])
        counter += 1
    counter += width

    for _ in range(num_reps):
        out.cnot(width - 1, 0)
        for qubit in range(width - 1):
            out.cnot(qubit, qubit + 1)

        for qubit in range(width):
            out.ry(qubit, params[counter])
            out.rz(qubit, params[counter + width])
            counter += 1
        counter += width
    return out


def braket_QV(width, depth=None, seed=None):
    """Construct QV circuit

    Parameters:
        width (int): Number of qubits
        depth (int): Number of QV layers
        seed (int): RNG seed, default=None

    Returns:
        Circuit: QV circuit
    """
    RNG = np.random.default_rng(seed=seed)
    out = Circuit()
    depth = depth or width
    num_2q = int(np.floor(width / 2))
    perm_0 = np.arange(width)
    for _ in range(depth):
        perm = RNG.permutation(perm_0)
        for w in range(num_2q):
            su4 = stats.unitary_group.rvs(4, random_state=RNG)
            physical_qubits = int(perm[2 * w]), int(perm[2 * w + 1])
            out.unitary(matrix=su4, targets=[physical_qubits[0], physical_qubits[1]])
    return out


def dtc_unitary(num_qubits, g=0.95, seed=None):
    """DTC unitary

    Parameters:
        num_qubits (int): Width of circuit
        g (float): Roatation about x-axis
        seed (int): RNG seed, default=None

    Returns:
        Circuit : DTC circuit
    """
    rng = np.random.default_rng(seed=seed)

    qc = Circuit()
    for i in range(num_qubits):
        qc.rx(i, g * np.pi)
    for i in range(0, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        qc.zz(i, i + 1, 2 * phi)
    for i in range(1, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        qc.zz(i, i + 1, 2 * phi)

    for i in range(num_qubits):
        h = rng.uniform(low=-np.pi, high=np.pi)
        qc.rz(i, h * np.pi)
    return qc
