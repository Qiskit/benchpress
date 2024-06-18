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
import qiskit
import qiskit_ibm_runtime


def pytest_report_header(config):
    """Add some info about packages and backend to the pytest CLI header
    """
    return [
            f"qiskit: {qiskit.__version__}",
            f"qiskit_ibm_runtime: {qiskit_ibm_runtime.__version__}"
           ]


def pytest_benchmark_update_json(config, benchmarks, output_json):
    """Adds custom sections to the pytest-benchmark report
    """
    output_json['qiskit_info'] = {'qiskit': str(qiskit.__version__),
                                  'qiskit_ibm_runtime': str(qiskit_ibm_runtime.__version__)}
