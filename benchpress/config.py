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


"""Utils for reading a config file"""

import configparser
import os
from ast import literal_eval

DEFAULT_FILENAME = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "default.conf")
)


class BenchpressConfig:
    """Class representing a user config file

    The config file format should be in a form that looks like

    [general]
    backend = ibm_torino

    """

    def __init__(self, filename=None):
        """Create a BenchpressConfig

        Args:
            filename (str): The path to the user config file. If one isn't
                specified the `default.config` file in the parent dir is used
        """
        if filename is None:
            self.filename = DEFAULT_FILENAME
        else:
            self.filename = filename
        self.options = {}
        self._gym_name = None
        self.config_parser = configparser.ConfigParser()
        self.qasm_dir = os.path.dirname(os.path.abspath(__file__)) + os.sep + "qasm"
        # read file
        self.config_parser.read(self.filename)
        for sec in self.config_parser.sections():
            self.options[sec] = {}
            for item in list(self.config_parser.items(sec)):
                self.options[sec][item[0]] = literal_eval(item[1])

    @property
    def gym_name(self):
        return self._gym_name

    @gym_name.setter
    def gym_name(self, name):
        # This is here to prevent overwriting the gym name when
        # calling across differnet gyms for getting backend info
        if self._gym_name is None:
            self._gym_name = name

    def get_qasm_dir(self, sub_dir=None):
        if sub_dir is None:
            return self.qasm_dir

        qasm_dir = self.qasm_dir
        return qasm_dir + os.sep + sub_dir + os.sep

    def backend(self):
        from benchpress.utilities.backends import get_backend

        if self.gym_name is None:
            raise ValueError("gym_name not set")

        if self.gym_name in ["qiskit", "tket", "bqskit", "staq"]:
            backend = get_backend(
                backend_name=self.options["general"]["backend_name"],
                gym_name=self.gym_name,
            )
            return backend
        else:
            raise ValueError(f"{self.gym_name} does not support backends")


Configuration = BenchpressConfig()
