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
    import qiskit_ibm_runtime.fake_provider.backends as fake_backends
except ImportError:
    import qiskit.providers.fake_provider.backends as fake_backends
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime.models.backend_configuration import QasmBackendConfiguration
from qiskit_ibm_runtime.models.backend_properties import BackendProperties

from benchpress.config import POSSIBLE_2Q_GATES

STR_TO_IBM_FAKE_BACKEND = {
    # BackendV2 Backends
    "fake_almaden_v2": fake_backends.FakeAlmadenV2,
    "fake_armonk_v2": fake_backends.FakeArmonkV2,
    "fake_athens_v2": fake_backends.FakeAthensV2,
    "fake_auckland": fake_backends.FakeAuckland,
    "fake_belem_v2": fake_backends.FakeBelemV2,
    "fake_boeblingen_v2": fake_backends.FakeBoeblingenV2,
    "fake_bogota_v2": fake_backends.FakeBogotaV2,
    "fake_brooklyn_v2": fake_backends.FakeBrooklynV2,
    "fake_burlington_v2": fake_backends.FakeBurlingtonV2,
    "fake_cairo_v2": fake_backends.FakeCairoV2,
    "fake_cambridge_v2": fake_backends.FakeCambridgeV2,
    "fake_casablanca_v2": fake_backends.FakeCasablancaV2,
    "fake_essex_v2": fake_backends.FakeEssexV2,
    "fake_geneva_v2": fake_backends.FakeGeneva,
    "fake_guadalupe_v2": fake_backends.FakeGuadalupeV2,
    "fake_hanoi_v2": fake_backends.FakeHanoiV2,
    "fake_jakarta_v2": fake_backends.FakeJakartaV2,
    "fake_hohannesburg_v2": fake_backends.FakeJohannesburgV2,
    "fake_kolkata_v2": fake_backends.FakeKolkataV2,
    "fake_lagos_v2": fake_backends.FakeLagosV2,
    "fake_lima_v2": fake_backends.FakeLimaV2,
    "fake_london_v2": fake_backends.FakeLondonV2,
    "fake_manhattan_v2": fake_backends.FakeManhattanV2,
    "fake_manila_v2": fake_backends.FakeManilaV2,
    "fake_melbourne_v2": fake_backends.FakeMelbourneV2,
    "fake_montreal_v2": fake_backends.FakeMontrealV2,
    "fake_mumbai_v2": fake_backends.FakeMumbaiV2,
    "fake_nairobi_v2": fake_backends.FakeNairobiV2,
    "fake_oslo_v2": fake_backends.FakeOslo,
    "fake_ourense_v2": fake_backends.FakeOurenseV2,
    "fake_paris_v2": fake_backends.FakeParisV2,
    "fake_perth": fake_backends.FakePerth,
    "fake_prague": fake_backends.FakePrague,
    "fake_poughkeepsie_v2": fake_backends.FakePoughkeepsieV2,
    "fake_quito_v2": fake_backends.FakeQuitoV2,
    "fake_rochester_v2": fake_backends.FakeRochesterV2,
    "fake_rome_v2": fake_backends.FakeRomeV2,
    "fake_santiago_v2": fake_backends.FakeSantiagoV2,
    "fake_sherbrooke": fake_backends.FakeSherbrooke,
    "fake_singapore_v2": fake_backends.FakeSingaporeV2,
    "fake_sydney_v2": fake_backends.FakeSydneyV2,
    "fake_torino": fake_backends.FakeTorino,
    "fake_toronto_v2": fake_backends.FakeTorontoV2,
    "fake_valencia_v2": fake_backends.FakeValenciaV2,
    "fake_vigo_v2": fake_backends.FakeVigoV2,
    "fake_washington_v2": fake_backends.FakeWashingtonV2,
    "fake_yorktown_v2": fake_backends.FakeYorktownV2,
}


def get_qiskit_bench_backend(backend_name):
    if "fake" in backend_name:
        backend = STR_TO_IBM_FAKE_BACKEND[backend_name]()
    elif "ibm" in backend_name:
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
