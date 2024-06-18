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


def torus_coupling_map(min_qubits, directed=False):
    """Create a torus coupling map given a minimum desired
    number of qubits

    Parameters:
        min_qubits (int): Minimum number of qubits
        directed (bool): Create a directed graph, default=False
    """
    little_diameter = math.ceil(math.sqrt(min_qubits / 3))
    big_diameter = 3 * little_diameter
    cmap = []
    # Big diameter couplings
    for edge in range(little_diameter):
        start_qubit = edge
        for idx in range(big_diameter):
            if idx == big_diameter - 1:
                cmap.append([start_qubit, edge])
            else:
                cmap.append([start_qubit, start_qubit + little_diameter])
                start_qubit += little_diameter

    # little diameter couplings
    for edge in range(big_diameter):
        start_idx = edge * little_diameter
        # couple ends first
        cmap.append([start_idx, start_idx + little_diameter - 1])
        if little_diameter > 2:
            for qubit in range(little_diameter - 1):
                cmap.append([start_idx + qubit, start_idx + qubit + 1])
    if directed:
        temp_cmap = []
        for edge in cmap:
            temp_cmap.append(edge)
            if edge[::-1] not in temp_cmap:
                temp_cmap.append(edge[::-1])
        cmap = temp_cmap
    return cmap
