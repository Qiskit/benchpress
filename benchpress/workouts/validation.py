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

from inspect import isfunction


def benchpress_test_validation(cls):
    """A decorator used to validate that no tests outside of the parent Workout are
    attached to the test class in each bench
    """
    parent_methods = set(k for k, v in cls.__base__.__dict__.items() if isfunction(v))
    class_methods = set(k for k, v in cls.__dict__.items() if isfunction(v))
    diff = class_methods.difference(parent_methods)

    if any(diff):
        raise Exception(
            f"class {cls.__name__} should not implement methods ({', '.join(diff)}) outside parent class "
            f"{cls.__base__.__name__}"
        )
    return cls
