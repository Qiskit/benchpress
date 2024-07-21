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


def get_backend(backend_name: str, gym_name: str):
    if gym_name in ["qiskit", "qiskit-transpiler-service"]:
        from benchpress.qiskit_gym.utils.qiskit_backend_utils import (
            get_qiskit_bench_backend,
        )

        return get_qiskit_bench_backend(backend_name)
    elif gym_name == "tket":
        from benchpress.tket_gym.utils.tket_backend_utils import get_tket_bench_backend

        return get_tket_bench_backend(backend_name)
    elif gym_name == "bqskit":
        from benchpress.bqskit_gym.utils.bqskit_backend_utils import (
            get_bqskit_bench_backend,
        )

        return get_bqskit_bench_backend(backend_name)
    elif gym_name == "staq":
        from benchpress.staq_gym.utils.staq_backend_utils import (
            get_staq_bench_backend,
        )

        return get_staq_bench_backend(backend_name)
    else:
        raise NotImplementedError(
            f"Backend support not implemented for {gym_name} bench."
        )
