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

import numpy as np


def tree_graph(levels=3, directed=False):
    """Generates a tree graph

    Parameters:
        levels (int): Tree levels, default=3
        directed (bool): Make a directed, non-symmetric graph

    Returns:
        list: List of edges between qubit nodes

    Notes:
        The number of qubits in the graph is equal to $2^{levels+1}-1$
    """
    if levels < 1:
        raise ValueError("Need to have at least one level")
    cmap = []
    prev_nodes = [0]
    for layer in range(1, levels + 1):
        current_nodes = np.arange(2**layer) + (2 ** (layer) - 1)
        node_sections = np.split(current_nodes, 2**layer // 2)
        for idx, nodes in enumerate(node_sections):
            for nn in nodes:
                cmap.append([nn, prev_nodes[idx]])
                if not directed:
                    cmap.append([prev_nodes[idx], nn])
        prev_nodes = current_nodes
    return cmap
