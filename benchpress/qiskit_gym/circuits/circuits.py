"""Test circuit generation"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library.standard_gates import XGate


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
    qc = QuantumCircuit(num_qubits)

    # X rotation by g*pi on all qubits (simulates imperfect periodic flips)
    for i in range(num_qubits):
        qc.rx(g * np.pi, i)

    # Ising interaction (only couples adjacent spins with random coupling strengths)
    for i in range(0, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        qc.rzz(2 * phi, i, i + 1)
    for i in range(1, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        qc.rzz(2 * phi, i, i + 1)

    # Longitudinal fields for disorder
    for i in range(num_qubits):
        h = rng.uniform(low=-np.pi, high=np.pi)
        qc.rz(h * np.pi, i)

    return qc


def multi_control_circuit(num_qubits):
    """A circuit with multi-control X-gates

    Parameters:
        N (int): Number of qubits

    Returns:
        QuantumCircuit: Output circuit
    """
    gate = XGate()
    out = QuantumCircuit(num_qubits)
    out.compose(gate, range(gate.num_qubits), inplace=True)
    for _ in range(num_qubits - 1):
        gate = gate.control()
        out.compose(gate, range(gate.num_qubits), inplace=True)
    return out


def bv_all_ones(N):
    """A circuit to generate a BV circuit over N
    qubits for an all-ones bit-string

    Parameters:
        N (int): Number of qubits

    Returns:
        QuantumCircuit: Output circuit
    """
    qc = QuantumCircuit(N, N - 1)
    qc.x(N - 1)
    qc.h(range(N))
    qc.cx(range(N - 1), N - 1)
    qc.h(range(N - 1))
    qc.measure(range(N - 1), range(N - 1))
    return qc


def trivial_bvlike_circuit(N):
    """A trivial circuit that should boil down
    to just a X and Z gate since they commute out

    Parameters:
        N (int): Number of qubits

    Returns:
        QuantumCircuit: Output circuit
    """
    qc = QuantumCircuit(N)
    for kk in range(N - 1):
        qc.cx(kk, N - 1)
    qc.x(N - 1)
    qc.z(N - 2)
    for kk in range(N - 2, -1, -1):
        qc.cx(kk, N - 1)
    return qc


def random_clifford_circuit(num_qubits, seed=12345):
    """Generate a random clifford circuit
    Parameters:
        num_qubits (int): Number of qubits
        seed (int): Optional. Seed the random number generator, default=12345

    Returns:
        QuantumCircuit: Clifford circuit
    """
    # This code is used to generate the QASM file
    from qiskit.circuit.random import random_clifford_circuit
    gates = ["cx", "cz", "cy", "swap", "x", "y", "z", "s", "sdg", "h"]
    qc = random_clifford_circuit(num_qubits, gates=gates, num_gates=10 * num_qubits * num_qubits, seed=seed)
    return qc
