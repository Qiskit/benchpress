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


import os


class _Config:
    def __init__(self):
        self.qasm_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + "qasm"

    def get_qasm_dir(self, sub_dir=None):
        if sub_dir is None:
            return self.qasm_dir

        qasm_dir = self.qasm_dir
        return qasm_dir + os.sep + sub_dir + os.sep

    def get_args_file(self):
        return os.path.join(os.path.dirname(__file__), "args.json")


Config = _Config()
