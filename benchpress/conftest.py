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
# conftest.py
import time
import numpy
import scipy
import pytest
import packaging


def pytest_benchmark_update_json(config, benchmarks, output_json):
    """Adds custom sections to the pytest-benchmark report"""
    reporter = config.pluginmanager.get_plugin("terminalreporter")

    # 8.4.0 changed the internal attribute and type that session start
    # is recorded at. There does not seem to be a public api for it on
    # the terminal reporter so this lets us support both 8.4.0 or older
    # versions
    pytest_version = packaging.version.parse(pytest.__version__)
    if pytest_version.release >= (8, 4, 0):
        output_json["total_duration"] = time.time() - reporter._session_start.time
    else:
        output_json["total_duration"] = time.time() - reporter._sessionstarttime

    output_json["env_info"] = {
        "numpy": str(numpy.__version__),
        "scipy": str(scipy.__version__),
    }

    output_json["test_status_counts"] = {
        "passed": len(reporter.stats.get("passed", [])),
        "failed": len(reporter.stats.get("failed", [])),
        "xfailed": len(reporter.stats.get("xfailed", [])),
        "skipped": len(reporter.stats.get("skipped", [])),
    }

    test_dumps = {"passed": {}, "failed": {}, "xfailed": {}, "skipped": {}}
    for status in test_dumps:
        for test in reporter.stats.get(status, []):
            test_dumps[status][test.nodeid] = {
                "duration": test.duration,
                "exception": str(test.longrepr),
                "keywords": test.keywords,
            }
    output_json["test_dumps"] = test_dumps
