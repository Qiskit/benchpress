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

from qiskit_ibm_runtime import QiskitRuntimeService

from benchpress.config import POSSIBLE_2Q_GATES
from benchpress.qiskit_gym.utils.qiskit_backend_utils import get_ibm_fake_backend


def get_qpanda_bench_backend(backend_name):
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
