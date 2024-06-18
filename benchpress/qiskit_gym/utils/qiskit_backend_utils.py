import json
import os

# This is here because the import path differs between Qiskit 1.0 and earlier versions
try:
    import qiskit_ibm_runtime.fake_provider.backends as fake_backends
except ImportError:
    import qiskit.providers.fake_provider.backends as fake_backends
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.providers.models.backendconfiguration import QasmBackendConfiguration
from qiskit.providers.models.backendproperties import BackendProperties
from .fake_backends import FakeTorino


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
    "fake_torino": FakeTorino,
    "fake_toronto_v2": fake_backends.FakeTorontoV2,
    "fake_valencia_v2": fake_backends.FakeValenciaV2,
    "fake_vigo_v2": fake_backends.FakeVigoV2,
    "fake_washington_v2": fake_backends.FakeWashingtonV2,
    "fake_yorktown_v2": fake_backends.FakeYorktownV2,
    # BackendV1 Backends
    "fake_almaden": fake_backends.FakeAlmaden,
    "fake_armonk": fake_backends.FakeArmonk,
    "fake_athens": fake_backends.FakeAthens,
    "fake_belem": fake_backends.FakeBelem,
    "fake_boeblingen": fake_backends.FakeBoeblingen,
    "fake_bogota": fake_backends.FakeBogota,
    "fake_brooklyn": fake_backends.FakeBrooklyn,
    "fake_burlington": fake_backends.FakeBurlington,
    "fake_cairo": fake_backends.FakeCairo,
    "fake_cambridge": fake_backends.FakeCambridge,
    "fake_cambridge_alternative_basis": fake_backends.FakeCambridgeAlternativeBasis,
    "fake_casablanca": fake_backends.FakeCasablanca,
    "fake_essex": fake_backends.FakeEssex,
    "fake_guadalupe": fake_backends.FakeGuadalupe,
    "fake_hanoi": fake_backends.FakeHanoi,
    "fake_jakarta": fake_backends.FakeJakarta,
    "fake_johannesburg": fake_backends.FakeJohannesburg,
    "fake_kolkata": fake_backends.FakeKolkata,
    "fake_lagos": fake_backends.FakeLagos,
    "fake_lima": fake_backends.FakeLima,
    "fake_london": fake_backends.FakeLondon,
    "fake_manhattan": fake_backends.FakeManhattan,
    "fake_manila": fake_backends.FakeManila,
    "fake_melbourne": fake_backends.FakeMelbourne,
    "fake_montreal": fake_backends.FakeMontreal,
    "fake_mumbai": fake_backends.FakeMumbai,
    "fake_nairobi": fake_backends.FakeNairobi,
    "fake_ouresne": fake_backends.FakeOurense,
    "fake_paris": fake_backends.FakeParis,
    "fake_poughkeepsie": fake_backends.FakePoughkeepsie,
    "fake_quito": fake_backends.FakeQuito,
    "fake_rochester": fake_backends.FakeRochester,
    "fake_rome": fake_backends.FakeRome,
    "fake_rueschlikon": fake_backends.FakeRueschlikon,
    "fake_santiago": fake_backends.FakeSantiago,
    "fake_singapore": fake_backends.FakeSingapore,
    "fake_sydney": fake_backends.FakeSydney,
    "fake_tenerife": fake_backends.FakeTenerife,
    "fake_tokyo": fake_backends.FakeTokyo,
    "fake_toronto": fake_backends.FakeToronto,
    "fake_valencia": fake_backends.FakeValencia,
    "fake_vigo": fake_backends.FakeVigo,
    "fake_washington": fake_backends.FakeWashington,
    "fake_yorktown": fake_backends.FakeYorktown,
}


def get_qiskit_bench_backend(backend_name):
    if "fake" in backend_name:
        return STR_TO_IBM_FAKE_BACKEND[backend_name]()
    elif "ibm" in backend_name:
        service = QiskitRuntimeService()
        return service.get_backend(backend_name)
    else:
        raise ValueError(f"Backend name {backend_name} not recognized.")


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
