from benchpress.qiskit_gym.utils.qiskit_backend_utils import get_qiskit_bench_backend
from benchpress.utilities.backends import FlexibleBackend
from pystaq import Device


def get_staq_bench_backend(backend_name: str) -> Device:
    """Creates a pystaq Device from a Qiskit backend. Pystaq Device only
        understands number of qubits, coupling map, and optional 2-qubit and
        1-qubit gate errors. It does not have a notion of basis gates as it
        transpiles any circuit into {U3, CX} set only.
    
    Args:
        backend_name (str): Name of the backend.

    Returns:
        dev (Device): Pystaq Device object.
    """
    backend = get_qiskit_bench_backend(backend_name=backend_name)
    target = backend.target
    num_qubits = target.num_qubits
    dev = Device(num_qubits)

    coupling_map = target.build_coupling_map()
    for q0, q1 in coupling_map:
        gate_error = target["cz"][(q0, q1)].error
        dev.add_edge(q0, q1, fidelity=1 - gate_error, directed=True)

    for q in range(num_qubits):
        gate_error = target["sx"][(q,)].error
        dev.set_fidelity(q, 1 - gate_error)

    return dev

class StaqFlexibleBackend(Device):
    """Modifies Tket's `IBMQBackend` class to accept FlexibleBackends
    (`ExtendedIBMFakeBackend` to be precise) for offline compilation.
    The new class only uses `_get_backend_info` and `default_compilation_pass`
    methods of the parent class `IBMQBackend` as offline compilation only needs
    these two methods. Accessing other methods of the parent class will raise
    `NotImplementedError`.
    """

    def __init__(self, min_qubits, layout="square"):
        self._backend = FlexibleBackend(min_qubits, layout=layout)
        self._backend_info = self._get_backend_info(self._backend.configuration(), None)
        config = self._backend.configuration()
        self._max_per_job = getattr(config, "max_experiments", 1)
        gate_set = _tk_gate_set(self._backend.configuration())
        self._primitive_gates = _get_primitive_gates(gate_set)
        self._supports_rz = OpType.Rz in self._primitive_gates

    def __repr__(self):
        out = f"<TketFlexibleBackend(num_qubits={self._backend.num_qubits}, "
        out += f"layout='{self._backend._layout}', "
        out += f"basis_gates={self._backend._basis_gates}>"
        return out

    def available_devices(self):
        raise NotImplementedError(f"Not implemented for fake backends")

    def process_circuits(self, **kwargs: Any) -> None:
        raise NotImplementedError(f"Not implemented for fake backends")

    def _retrieve_job(self, **kwargs: Any) -> None:
        raise NotImplementedError(f"Not implemented for fake backends")

    def cancel(self, **kwargs: Any) -> None:
        raise NotImplementedError(f"Not implemented for fake backends")

    def circuit_status(self, **kwargs: Any) -> CircuitStatus:
        raise NotImplementedError(f"Not implemented for fake backends")

    def get_result(self, **kwargs: Any) -> None:
        raise NotImplementedError(f"Not implemented for fake backends")
