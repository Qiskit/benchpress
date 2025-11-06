import random
from scipy import stats
import numpy as np
from pyqpanda3.core import *

# num_qubit_pool = 100
# qubit_vec = [pq.Qubit(i) for i in range(0, num_qubit_pool)]


def qpanda_QV(num_qubits, depth=None, seed=12345):
    """Construct QV circuit

    Parameters:
        width (int): Number of qubits
        depth (int): Number of QV layers
        seed (int): RNG seed, default=None

    Returns:
        Circuit: QV circuit
    """
    if depth is None:
        depth = num_qubits
    return QProg(QV(num_qubits,depth,seed))


def qpanda_circSU2(width, num_reps=3):
    """Efficient SU2 circuit with circular entanglement
    and using Ry and Rz 1Q-gates'

    Parameters:
        width (int): Number of qubits in circuit
        num_reps (int): Number of repetitions, default = 3

    Returns:
        Circuit: Output circuit
    """
    num_params = 2 * width * (num_reps + 1)

    params = [random.uniform(-3.1415926, 3.1415926) for kk in range(num_params)]

    out = QCircuit(width)
    counter = 0
    for qubit in range(0, width):
        out << RY(qubit, params[counter])
        out << RZ(qubit, params[counter + width])
        counter += 1
    counter += width

    for _ in range(num_reps):
        out << CNOT(width - 1, 0)
        for qubit in range(width - 1):
            out << CNOT(qubit, qubit + 1)

        for qubit in range(width):
            out << RY(qubit, params[counter])
            out << RZ(qubit, params[counter + width])
            counter += 1
        counter += width
    return QProg(out)


def qpanda_circSU2_vqc(width, num_reps):
    ### params 的形状为（2,width,num_reps)
    from pyqpanda3.vqcircuit import VQCircuit
    import pyqpanda3.vqcircuit as VQC
    from pyqpanda3.core import CNOT
    """Efficient SU2 circuit with circular entanglement
    and using Ry and Rz 1Q-gates'
    """
    vqc = VQCircuit()
    vqc.set_Param([2,width,num_reps],["tmp","qbit","rep"])

    for qubit in range(0, width):
        vqc << RY(qubit, vqc.Param([0,qubit,0]))
        vqc << RZ(qubit, vqc.Param([1,qubit,0]))

    for rep in range(num_reps-1):
        vqc << CNOT(width-1,0)
        for qubit in range(width - 1):
            vqc << CNOT(qubit, qubit + 1)

        for qubit in range(width):
            vqc << RY(qubit, vqc.Param([0,qubit,rep+1]))
            vqc << RZ(qubit, vqc.Param([1,qubit,rep+1]))
    return vqc

def dtc_unitary(num_qubits, g=0.95, seed=12345):
    rng = np.random.default_rng(seed=seed)

    qc = QCircuit(num_qubits)

    for i in range(num_qubits):
        qc << RX(i, g * np.pi)

    for i in range(0, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        qc << RZZ(i + 1, i, 2 * phi)
    for i in range(1, num_qubits - 1, 2):
        phi = rng.uniform(low=np.pi / 16, high=3 * np.pi / 16)
        qc << RZZ(i + 1, i, 2 * phi)

    # Longitudinal fields for disorder
    for i in range(num_qubits):
        h = rng.uniform(low=-np.pi, high=np.pi)
        qc << RZ(i, h * np.pi)
    return qc


def multi_control_circuit(num_qubits):
    sub = QCircuit(1)
    sub << X(0)
    out = QCircuit(num_qubits)
    sub = sub.control([kk for kk in range(1, num_qubits)])
    out << sub
    return QProg(out)


def qpanda_bv_all_ones(N):
    """A circuit to generate a BV circuit over N
    qubits for an all-ones bit-string

    Parameters:
        N (int): Number of qubits in circuit

    Returns:
        Circuit: BV circuit
    """
    out = QCircuit(N)
    out << X(N - 1)
    out << H(N - 1)
    for kk in range(N - 1):
        out << H(kk)
        out << CNOT(kk, N - 1)
        out << H(kk)
        # out << Measure(kk], kk])
    return QProg(out)


def trivial_bvlike_circuit(N):
    """A trivial circuit that should boil down
    to just a X and Z gate since they commute out

    Parameters:
        N (int): Number of qubits

    Returns:
        Circuit: Output circuit
    """
    qc = QCircuit(N)
    for kk in range(N - 1):
        qc << CNOT(kk, N - 1)
    qc << X(N - 1)
    qc << Z(N - 2)
    for kk in range(N - 2, -1, -1):
        qc << CNOT(kk, N - 1)
    return QProg(qc)


def qpanda_random_clifford(num_qubits, num_gates=None, seed=None):
    """Construct a random clifford circuit

    Parameters:
        num_qubits (int): Number of qubits
        num_gates (int): Number of gates
        seed (int): RNG seed, default=None

    Returns:
        Circuit: random Clifford circuit
    """
    RNG = np.random.default_rng(seed=seed)
    out = QCircuit(num_qubits)
    num_gates = num_gates or 10 * num_qubits * num_qubits
    gates = ["cx", "cz", "cy", "swap", "x", "y", "z", "s", "sdg", "h"]

    for _ in range(num_gates):
        gate = gates[RNG.integers(len(gates))]

        if gate == "cx":
            qubits = RNG.choice(num_qubits, 2, replace=False)
            out << CNOT(qubits[0], qubits[1])
        elif gate == "cy":
            qubits = RNG.choice(num_qubits, 2, replace=False)
            out << Y(qubits[1]).control(qubits[0])
        elif gate == "cz":
            qubits = RNG.choice(num_qubits, 2, replace=False)
            out << Z(qubits[1]).control(qubits[0])
        elif gate == "swap":
            qubits = RNG.choice(num_qubits, 2, replace=False)
            out << SWAP(qubits[0], qubits[1])

        elif gate == "x":
            qubit = RNG.integers(num_qubits)
            out << X(qubit)
        elif gate == "y":
            qubit = RNG.integers(num_qubits)
            out << Y(qubit)
        elif gate == "z":
            qubit = RNG.integers(num_qubits)
            out << Z(qubit)
        elif gate == "h":
            qubit = RNG.integers(num_qubits)
            out << H(qubit)
        elif gate == "s":
            qubit = RNG.integers(num_qubits)
            out << S(qubit)
        elif gate == "sdg":
            qubit = RNG.integers(num_qubits)
            out << S(qubit).dagger()

    return QProg(out)


if __name__ == '__main__':
    num_qubit = 10
    qpanda_random_clifford(num_qubit)
    qpanda_QV(num_qubit, num_qubit)
    trivial_bvlike_circuit(num_qubit)
    qpanda_bv_all_ones(num_qubit)
    multi_control_circuit(num_qubit)
    dtc_unitary(num_qubit)
    qpanda_circSU2(num_qubit)
    qpanda_circSU2_vqc(num_qubit,1)
