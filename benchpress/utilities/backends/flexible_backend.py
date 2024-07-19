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

import math
import scipy.optimize as opt
import rustworkx as rx

from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.providers.models.backendconfiguration import QasmBackendConfiguration
from qiskit.transpiler import CouplingMap

from ..graphs import tree_graph, torus_coupling_map
from benchpress.config import Configuration

BASIS_GATES = Configuration.options["general"]["basis_gates"]


class FlexibleBackend(GenericBackendV2):
    """A flexible size backend"""

    def __init__(self, min_qubits, layout="square", basis_gates=None):
        """Create an instance of a backend supporting, at minimum,
        a target number of qubits over a given layout (topology).

        Parameters:
            min_qubits (int): Minimum desired number of qubits
            layout (str): Target qubit topology.  Options are
                          'heavy-hex', 'linear', 'square', 'torus',
                          'tree', or 'all-to-all'
            basis_gates (list): Supported basis gates.  If none
                                supplied, defaults to the global
                                default set
        """
        if basis_gates is None:
            basis_gates = BASIS_GATES
        self._basis_gates = basis_gates
        self._coupling_map = None
        if layout == "square":
            dim = math.ceil(math.sqrt(min_qubits))
            graph = rx.generators.grid_graph(rows=dim, cols=dim)
            num_qubits = len(graph)
            cmap = CouplingMap(list(graph.edge_list()))

        elif layout == "heavy-hex":

            def heavy_bound(d):
                out = 5 * d**2 - 2 * d - 1 - 2 * min_qubits
                return out

            dim = math.ceil(opt.root(heavy_bound, 1).x[0])
            if not dim % 2:
                dim += 1
            graph = rx.generators.heavy_hex_graph(dim)
            num_qubits = len(graph)
            cmap = CouplingMap(list(graph.edge_list()))

        elif layout == "linear":
            dim = min_qubits
            graph = rx.generators.grid_graph(1, min_qubits)
            num_qubits = len(graph)
            cmap = CouplingMap(list(graph.edge_list()))

        elif layout == "tree":
            levels = math.ceil(math.log2(min_qubits + 1) - 1)
            cmap = CouplingMap(tree_graph(levels))
            num_qubits = cmap.size()

        elif layout == "torus":
            cmap = CouplingMap(torus_coupling_map(min_qubits))
            num_qubits = cmap.size()

        elif layout == 'all-to-all':
            cmap = None
            num_qubits = min_qubits

        else:
            raise ValueError(f"Invalid layout ({layout})")

        self._layout = layout
        if cmap:
            cmap.make_symmetric()

        self._configuration = QasmBackendConfiguration(
            backend_name=f"FlexibleBackend-{layout}",
            backend_version="1.0.0",
            basis_gates=self._basis_gates,
            conditional=False,
            coupling_map=list(cmap) if cmap else cmap,
            gates=None,
            local=True,
            max_shots=int(1e5),
            memory=False,
            n_qubits=num_qubits,
            open_pulse=False,
            simulator=True,  # needs to be True for Tket compatibility
        )

        super().__init__(num_qubits, basis_gates=self._basis_gates, coupling_map=cmap)

    def __repr__(self):
        out = f"<FlexibleBackend(num_qubits={self.target.num_qubits}, "
        out += f"layout='{self._layout}', "
        out += f"basis_gates={self._basis_gates}>"
        return out

    @property
    def target(self):
        """Return backend target"""
        return self._target

    def configuration(self):
        """Return backend configuration"""
        return self._configuration

    def properties(self):
        return None

    @property
    def max_circuits(self):
        return None

    @classmethod
    def _default_options(cls):
        pass

    def run(self, circuit, **kwargs):
        raise NotImplementedError("This backend does not contain a run method")
