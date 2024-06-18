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


def get_args(filename: str) -> dict:
    """Accepts the JSON file's name with test arguments, reads it, and returns
        a dictionary.

    Parameters:
        filename (str): Name of the JSON file with test arguments.

    Returns:
        A Python dictionary with the content of the JSON file.
    """
    with open(filename, "r") as args_file:
        return json.load(args_file)
