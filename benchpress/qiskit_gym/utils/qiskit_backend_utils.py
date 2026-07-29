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

# This is here because the import path differs between Qiskit 1.0 and earlier versions
try:
    import qiskit_ibm_runtime.fake_provider as fake_provider
    from qiskit_ibm_runtime.fake_provider.fake_backend import FakeBackendV2
except ImportError:
    import qiskit.providers.fake_provider as fake_provider
    from qiskit.providers.fake_provider.fake_backend import FakeBackendV2
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime.models.backend_configuration import QasmBackendConfiguration
from qiskit_ibm_runtime.models.backend_properties import BackendProperties

from benchpress.config import POSSIBLE_2Q_GATES


def _regularize_fake_backend_name(name):
    """Regularize a fake-backend name so different spellings map to the same key.

    Lower-cases the string and strips underscores so that, e.g., both
    ``"fake_almaden_v2"`` and ``"FakeAlmadenV2"`` resolve to the same backend,
    and ``"fake_torino"`` and ``"FakeTorino"`` (which has no ``V2`` variant)
    both point to ``FakeTorino``.
    """
    return name.lower().replace("_", "")


def _discover_fake_backends():
    """Discover every fake backend provided by ``qiskit_ibm_runtime.fake_provider``.

    Rather than hardcoding a dictionary that must be updated whenever
    a new fake backend is added to ``qiskit_ibm_runtime``, this collects every
    `FakeBackendV2` subclass at import time in a dictionary.
    The key is the regularized fake backend name, and the value is a FakeBackend object.
    """
    backends = {}
    for name in dir(fake_provider):
        obj = getattr(fake_provider, name)
        if (
            isinstance(obj, type)
            and issubclass(obj, FakeBackendV2)
            and obj is not FakeBackendV2
        ):
            backends[_regularize_fake_backend_name(name)] = obj
    return backends


_FAKE_BACKENDS = _discover_fake_backends()


def get_ibm_fake_backend(backend_name):
    """Return a fresh fake-backend instance for ``backend_name``.

    The name is regularized so it becomes case- and underscore-insensitive. A backend can be
    requested using either its snake_case name (e.g., ``"fake_almaden_v2"``,
    ``"fake_torino"``) or its class name (``"FakeAlmadenV2"``, ``"FakeTorino"``).

    Raises:
        KeyError: if no fake backend matches ``backend_name``.
    """
    key = _regularize_fake_backend_name(backend_name)
    try:
        backend_cls = _FAKE_BACKENDS[key]
    except KeyError:
        raise KeyError(
            f"Fake backend {backend_name!r} not found in "
            f"{fake_provider.__name__}. Available backends: "
            f"{sorted(b.__name__ for b in _FAKE_BACKENDS.values())}"
        )
    return backend_cls()


def get_qiskit_bench_backend(backend_name):
    lowered_name = backend_name.lower()
    if "fake" in lowered_name:
        backend = get_ibm_fake_backend(backend_name)
    elif "ibm" in lowered_name:
        service = QiskitRuntimeService()
        backend = service.get_backend(backend_name)
    else:
        raise ValueError(f"Backend name {backend_name} not recognized.")

    op_names = backend.operation_names
    twoq_gates = list(set(op_names).intersection(POSSIBLE_2Q_GATES))
    if len(twoq_gates) > 1:
        raise Exception("Only one 2Q gate type is currently supported")
    elif len(twoq_gates) == 0:
        raise Exception(f"No gate in {POSSIBLE_2Q_GATES} found!")
    setattr(backend, "two_q_gate_type", twoq_gates[0])
    return backend


def extend_ibm_fake_backend(fake_backend):
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
