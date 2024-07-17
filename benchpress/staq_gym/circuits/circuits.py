"""Test circuit generation"""


def dtc_unitary(num_qubits, g=0.95, seed=12345):
    """Generate a Floquet unitary for DTC evolution
    Parameters:
        num_qubits (int): Number of qubits
        g (float): Optional. Parameter controlling amount of x-rotation, default=0.95
        seed (int): Optional. Seed the random number generator, default=12345
    """
    raise NotImplementedError("staq does not support circuit creation.")


def multi_control_circuit(num_qubits):
    """A circuit with multi-control X-gates

    Parameters:
        N (int): Number of qubits
    """
    raise NotImplementedError("staq does not support circuit creation.")


def bv_all_ones(N):
    """A circuit to generate a BV circuit over N
    qubits for an all-ones bit-string

    Parameters:
        N (int): Number of qubits
    """
    raise NotImplementedError("staq does not support circuit creation.")


def trivial_bvlike_circuit(N):
    """A trivial circuit that should boil down
    to just a X and Z gate since they commute out

    Parameters:
        N (int): Number of qubits
    """
    raise NotImplementedError("staq does not support circuit creation.")
