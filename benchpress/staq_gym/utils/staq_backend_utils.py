from typing import Iterable

from pystaq import Device
from qiskit.providers import BackendV2
from qiskit.transpiler import CouplingMap

from benchpress.qiskit_gym.utils.qiskit_backend_utils import get_qiskit_bench_backend
from benchpress.utilities.backends import FlexibleBackend


def _get_staq_device(
    num_qubits: int,
    coupling_map: CouplingMap | Iterable[Iterable[int]],
    one_q_errors: None | dict[int, float] = None,
    two_q_errors: None | dict[tuple[int, int], float] = None,
) -> Device:
    """Creates a Staq Device from specified number of qubits, coupling map,
        and gate errors (one- and two-qubit).

    Args:
        num_qubits (int): Number of qubits in the device.
        coupling_map (CouplingMap | Iterable[Iterable[int, int]]): Coupling
            map of the device.
        one_q_errors (None | dict[int, float]): Single qubit gate errors.
        two_q_errors (None | dict[tuple[int, int], float]): Two qubit gate errors.

    Returns:
        dev (Device): A Pystaq Device object.
    """
    if one_q_errors is None:
        one_q_errors = {}

    if two_q_errors is None:
        two_q_errors = {}

    dev = Device(num_qubits)

    for q0, q1 in coupling_map:
        gate_error = two_q_errors.get((q0, q1), 0)
        dev.add_edge(q0, q1, fidelity=1 - gate_error, directed=True)

    for q in range(num_qubits):
        gate_error = one_q_errors.get(q, 0)
        dev.set_fidelity(q, 1 - gate_error)

    return dev


def _get_backend_data(
    backend: BackendV2 | FlexibleBackend,
) -> tuple[int, CouplingMap, dict[int, float], dict[tuple[int, int], float]]:
    """Extracts information from an IBM backend object that are necessary
        for creating Pystaq Device.

    Args:
        backend (BackendV2 | FlexibleBackend): An IBM device object.
            It can be a fake backend or real backend or a custom `FlexibleBackend`.

    Returns:
        num_qubits (int): Number of qubits in the backend.
        coupling_map (CouplingMap): Coupling map of the backend.
        one_q_errors (dict[int, float]): Single qubit gate errors.
        two_q_errors (dict[tuple[int, int], float]): Two qubit gate errors.
    """
    target = backend.target
    num_qubits = target.num_qubits
    coupling_map = target.build_coupling_map()

    one_q_errors = {q: target["sx"][(q,)].error for q in range(num_qubits)}

    two_q_errors = {(q0, q1): target["cz"][(q0, q1)].error for q0, q1 in coupling_map}

    return num_qubits, coupling_map, one_q_errors, two_q_errors


def get_staq_bench_backend(backend_name: str) -> Device:
    """Creates a pystaq Device from a Qiskit backend. Pystaq Device only
        understands number of qubits, coupling map, and optional 2-qubit and
        1-qubit gate errors. It does not have a notion of fixed basis gates.

    Args:
        backend_name (str): Name of the backend.

    Returns:
        dev (Device): Pystaq Device object.
    """
    backend = get_qiskit_bench_backend(backend_name=backend_name)
    num_qubits, coupling_map, one_q_errors, two_q_errors = _get_backend_data(backend)

    return _get_staq_device(
        num_qubits=num_qubits,
        coupling_map=coupling_map,
        one_q_errors=one_q_errors,
        two_q_errors=two_q_errors,
    )


class StaqFlexibleBackend:
    """Flexible backend object for Staq gym. Due nature of the Staq package,
    this flexible backend does not ingerits from and modifies Pystaq Device
    obejct. Instead, it creates a Pystaq Device object from a FlexibleBackend
    with specified number of qubits and layout (coupling map) using the
    `get_staq_flexible_backend` method
    """

    def __init__(self, min_qubits, layout="square"):
        self._backend = FlexibleBackend(min_qubits, layout=layout)

    def __repr__(self):
        out = f"<StaqFlexibleBackend(num_qubits={self._backend.num_qubits}, "
        out += f"layout='{self._backend._layout}', "
        out += "basis_gates=['U3', 'CX']>"
        return out

    def get_staq_flexible_backend(self):
        (num_qubits, coupling_map, one_q_errors, two_q_errors) = _get_backend_data(
            self._backend
        )

        return _get_staq_device(
            num_qubits=num_qubits,
            coupling_map=coupling_map,
            one_q_errors=one_q_errors,
            two_q_errors=two_q_errors,
        )
