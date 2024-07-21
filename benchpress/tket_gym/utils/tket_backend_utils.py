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
import json
import os
from typing import Any

from pytket.backends import CircuitStatus
from pytket.circuit import OpType
from pytket.extensions.qiskit.backends.ibm import IBMQBackend, _get_primitive_gates
from pytket.extensions.qiskit.qiskit_convert import _tk_gate_set
from qiskit.providers.models.backendconfiguration import QasmBackendConfiguration
from qiskit.providers.models.backendproperties import BackendProperties

from benchpress.config import POSSIBLE_2Q_GATES
from benchpress.utilities.backends import FlexibleBackend
from benchpress.qiskit_gym.utils.qiskit_backend_utils import STR_TO_IBM_FAKE_BACKEND


POSSIBLE_TKET_GATES = [
    getattr(OpType, gate_str.upper()) for gate_str in POSSIBLE_2Q_GATES
]


def _extend_ibm_fake_backend(fake_backend) -> "IBMFakeBackend":
    """The function takes a specific fake backend class such as `FakeSherbrooke and
    extends the class with two new methods. namely, `configuration` and `properties`
    to make the fake backends compatible with Tket.

    Tket uses `IBMBackend.configuration()` and `IBMBackend.properties()` methods to
    fetch necessary information for its `default_compilation_pass`. Currently, IBM's
    `FakeBackendV2` objects do not have those methods. This function extends the
    `FakeBackendV2` class with these two methods necessary for Tket.

    Parameters:
        fake_backend (): A specific `FakeBackendV2` class such as `FakeSherbrooke`.

    Returns:
        The `ExtendedIBMFakeBackend` class.
    """

    def configuration() -> QasmBackendConfiguration:
        conf_file = os.path.join(fake_backend.dirname, fake_backend.conf_filename)
        with open(conf_file, "r") as f:
            data = json.load(f)
        # TODO: Replace with `PulseBackendConfiguration`
        return QasmBackendConfiguration.from_dict(data)

    def properties() -> BackendProperties:
        props_file = os.path.join(fake_backend.dirname, fake_backend.props_filename)
        with open(props_file, "r") as f:
            data = json.load(f)
        return BackendProperties.from_dict(data)

    setattr(fake_backend, "configuration", configuration)
    setattr(fake_backend, "properties", properties)

    return fake_backend


class TketFakeIBMQBackend(IBMQBackend):
    """Modifies Tket's `IBMQBackend` class to accept Qiskit fake backends
    (`ExtendedIBMFakeBackend` to be precise) for offline compilation.
    The new class only uses `_get_backend_info` and `default_compilation_pass`
    methods of the parent class `IBMQBackend` as offline compilation only needs
    these two methods. Accessing other methods of the parent class will raise
    `NotImplementedError`.
    """

    def __init__(self, fake_backend: "FakeBackend"):
        self._backend = fake_backend
        self._backend_info = self._get_backend_info(
            config=self._backend.configuration(), props=self._backend.properties()
        )
        config = self._backend.configuration()
        self._max_per_job = getattr(config, "max_experiments", 1)
        gate_set = _tk_gate_set(self._backend.configuration())
        self._primitive_gates = _get_primitive_gates(gate_set)
        self._supports_rz = OpType.Rz in self._primitive_gates

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


class TketFlexibleBackend(IBMQBackend):
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
        self.two_q_gate_type = getattr(OpType, self._backend.two_q_gate_type.upper())

    def __repr__(self):
        out = f"<TketFlexibleBackend(num_qubits={self._backend.num_qubits}, "
        out += f"layout='{self._backend._layout}', "
        out += f"basis_gates={self._primitive_gates}>"
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


def get_tket_bench_backend(backend_name: str):
    """Utility for creating a backend compatible with tKet compilation.
    It takes a Qiskit backend name, either a fake backend (e.g., `"fake_sherbrooke"`)
    or real hardware (e.g., `"ibm_sherbrooke"`).

    Parameters:
        backend_name (str): Name of the backend.

    Returns:
        A backend of either custom `TketFakeIBMQBackend` or tKet's built-in
        `IBMQBackend` object compatible with tKet.
    """
    if "fake" in backend_name:
        ibm_fake_backend = STR_TO_IBM_FAKE_BACKEND[backend_name]()
        extended_ibm_fake_backend = _extend_ibm_fake_backend(ibm_fake_backend)
        backend = TketFakeIBMQBackend(extended_ibm_fake_backend)
    elif "ibm" in backend_name:
        backend = IBMQBackend(backend_name)
    else:
        raise ValueError(f"Backend name {backend_name} not recognized.")
    twoq_gates = list(backend.backend_info.gate_set.intersection(POSSIBLE_TKET_GATES))
    if len(twoq_gates) > 1:
        raise Exception("Only one 2Q gate type is currently supported")
    elif len(twoq_gates) == 0:
        raise Exception(f"No gate in {POSSIBLE_TKET_GATES} found!")
    setattr(backend, "two_q_gate_type", twoq_gates[0])
    return backend
