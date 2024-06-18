"""
Fake Torino device (133 qubit).
"""

# This is here because the import path differs between Qiskit 1.0 and earlier versions
import os

try:
    from qiskit_ibm_runtime.fake_provider.fake_backend import FakeBackendV2
except ImportError:
    from qiskit.providers.fake_provider.fake_backend import FakeBackendV2


class FakeTorino(FakeBackendV2):
    """A fake 133 qubit backend."""

    dirname = os.path.dirname(__file__)  # type: ignore
    conf_filename = "conf_torino.json"  # type: ignore
    props_filename = "props_torino.json"  # type: ignore
    backend_name = "fake_torino"  # type: ignore
