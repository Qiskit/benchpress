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
from __future__ import annotations

import numpy as np
from bqskit import MachineModel
from bqskit.ext.qiskit.models import _basis_gate_str_to_bqskit_gate
from bqskit.ir.gates.constantgate import ConstantGate
from bqskit.ir.gates.qubitgate import QubitGate
from bqskit.qis.unitary.unitarymatrix import UnitaryMatrix

from benchpress.config import POSSIBLE_2Q_GATES
from benchpress.utilities.backends.flexible_backend import FlexibleBackend
from benchpress.qiskit_gym.utils.qiskit_backend_utils import (
    STR_TO_IBM_FAKE_BACKEND,
    extend_ibm_fake_backend,
    get_qiskit_bench_backend,
)


class ECRGate(ConstantGate, QubitGate):
    """The Echoed Cross Resonance gate.

    The ECR gate is given by the following unitary:

    .. math::

        \\sqrt(2)\\begin{pmatrix}
        0 & 0 & 1 & i \\\\
        0 & 0 & i & 1 \\\\
        1 & -i & 0 & 0 \\\\
        -i & 1 & 0 & 0 \\\\
        \\end{pmatrix}
    """

    _num_qudits = 2
    _qasm_name = "ecr"
    _utry = UnitaryMatrix(
        np.sqrt(1 / 2)
        * np.array(
            [
                [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 1.0j],
                [0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 1.0j, 1.0 + 0.0j],
                [1.0 + 0.0j, 0.0 - 1.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 - 1.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
            ]
        ),
    )


def BqskitFlexibleBackend(min_qubits, layout="square", basis_gates=None):
    """Returns a MachineModel for a FlexibleBackend that is compatible with Bqskit
    Parameters:
        min_qubits (int): Minimum desired number of qubits
        layout (str): Target qubit topology.  Options are 'heavy-hex', 'linear',
                      'square', 'torus', or 'tree'
        basis_gates (list): Supported basis gates.  If none supplied, defaults to the global
                            default set
    Returns:
        MachineModel: Mode representing flexible backend in Bqskit
    """
    flex_backend = FlexibleBackend(min_qubits, layout=layout, basis_gates=basis_gates)
    model = _get_bqskit_machine_model(flex_backend)
    possible_gates = _basis_gate_str_to_bqskit_gate(POSSIBLE_2Q_GATES)
    twoq_gates = list(model.gate_set.intersection(possible_gates))
    if len(twoq_gates) > 1:
        raise Exception('Only one 2Q gate type is currently supported')
    elif len(twoq_gates) == 0:
        raise Exception(f'No gate in {possible_gates} found!')
    setattr(model, "two_q_gate_type", twoq_gates[0])
    return model


def _get_bqskit_machine_model(backend):
    """Create a machine model for a IBM Backend."""
    config = backend.configuration()
    num_qudits = config.n_qubits
    basis_gates = config.basis_gates
    gate_set = _basis_gate_str_to_bqskit_gate(basis_gates=basis_gates)
    if "ecr" in basis_gates:
        gate_set.add(ECRGate())
    if config.coupling_map:
        coupling_map = list({tuple(sorted(e)) for e in config.coupling_map})
    else:
        coupling_map = None
    model = MachineModel(num_qudits, coupling_map, gate_set)  # type: ignore
    possible_gates = _basis_gate_str_to_bqskit_gate(POSSIBLE_2Q_GATES)
    twoq_gates = list(model.gate_set.intersection(possible_gates))
    if len(twoq_gates) > 1:
        raise Exception('Only one 2Q gate type is currently supported')
    elif len(twoq_gates) == 0:
        raise Exception(f'No gate in {possible_gates} found!')
    setattr(model, "two_q_gate_type", twoq_gates[0])
    return model


def get_bqskit_bench_backend(backend_name: str):
    """Utility for creating a backend compatible with BQSKIT compilation.
    It takes a Qiskit backend name, either a fake backend name
    (e.g., `"fake_sherbrooke"`) or real hardware name (e.g., `"ibm_sherbrooke"`).

    Parameters:
        backend_name (str): Name of the backend.

    Returns:
        A backend (Model) of `MachineModel` object compatible with BQSKIT.
    """
    if "fake" in backend_name:
        ibm_fake_backend = STR_TO_IBM_FAKE_BACKEND[backend_name]()
        backend = extend_ibm_fake_backend(ibm_fake_backend)
    elif "ibm" in backend_name:
        backend = get_qiskit_bench_backend(backend_name)
    else:
        raise ValueError(f"Backend name {backend_name} not recognized.")

    return _get_bqskit_machine_model(backend=backend)
