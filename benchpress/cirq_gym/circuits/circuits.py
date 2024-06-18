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

"""Cirq circuit generation"""

import numpy as np
import cirq


def cirq_QV(num_qubits, depth, seed=None):
    """Generates a model circuit with the given number of qubits and depth.

    The generated circuit consists of `depth` layers of random qubit
    permutations followed by random two-qubit gates that are sampled from the
    Haar measure on SU(4).

    Args:
        num_qubits: The number of qubits in the generated circuit.
        depth: The number of layers in the circuit.
        seed: Random state or random state seed.

    Returns:
        The generated circuit.
    """
    # Setup the circuit and its qubits.
    qubits = cirq.LineQubit.range(num_qubits)
    circuit = cirq.Circuit()
    random_state = cirq.value.parse_random_state(seed)

    # For each layer.
    for _ in range(depth):
        # Generate uniformly random permutation Pj of [0...n-1]
        perm = random_state.permutation(num_qubits)

        # For each consecutive pair in Pj, generate Haar random SU(4)
        # Decompose each SU(4) into CNOT + SU(2) and add to Ci
        for k in range(0, num_qubits - 1, 2):
            permuted_indices = [int(perm[k]), int(perm[k + 1])]
            special_unitary = cirq.testing.random_special_unitary(4, random_state=seed)

            # Convert the decomposed unitary to Cirq operations and add them to
            # the circuit.
            circuit.append(
                cirq.MatrixGate(special_unitary).on(
                    qubits[permuted_indices[0]], qubits[permuted_indices[1]]
                )
            )
    return circuit


def multi_control_circuit(N):
    qreg = cirq.LineQubit.range(N)
    qc = cirq.Circuit()

    for kk in range(N):
        gate = cirq.ControlledGate(sub_gate=cirq.X, num_controls=kk)
        qc.append(gate(*[qreg[ii] for ii in range(kk + 1)]))
    return qc


def dtc_unitary(num_qubits, g=0.95, seed=12345):
    """Generate a Floquet unitary for DTC evolution
    Parameters:
        num_qubits (int): Number of qubits
        g (float): Optional. Parameter controlling amount of x-rotation, default=0.95
        seed (int): Optional. Seed the random number generator, default=12345

    Returns:
        QuantumCircuit: Unitary operator
    """
    rng = np.random.default_rng(seed=seed)
    qc = cirq.Circuit()
    qreg = cirq.LineQubit.range(num_qubits)

    ops = []
    # X rotation by g*pi on all qubits (simulates imperfect periodic flips)
    for i in range(num_qubits):
        ops.append(cirq.Rx(rads=g * np.pi).on(qreg[i]))

    moment1 = cirq.Moment(ops)

    ops = []
    # Ising interaction (only couples adjacent spins with random coupling strengths)
    for i in range(0, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        ops.append(
            cirq.ZZPowGate(exponent=4 * phi / np.pi, global_shift=-0.5).on(
                qreg[i], qreg[i + 1]
            )
        )

    moment2 = cirq.Moment(ops)
    ops = []
    for i in range(1, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        ops.append(
            cirq.ZZPowGate(exponent=4 * phi / np.pi, global_shift=-0.5).on(
                qreg[i], qreg[i + 1]
            )
        )
    moment3 = cirq.Moment(ops)

    ops = []
    # Longitudinal fields for disorder
    for i in range(num_qubits):
        h = rng.uniform(low=-np.pi, high=np.pi)
        ops.append(cirq.Rz(rads=h * np.pi).on(qreg[i]))

    moment4 = cirq.Moment(ops)

    qc.append([moment1, moment2, moment3, moment4])

    return qc
