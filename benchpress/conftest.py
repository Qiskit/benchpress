# conftest.py
import numpy
import scipy


def pytest_benchmark_update_json(config, benchmarks, output_json):
    """Adds custom sections to the pytest-benchmark report
    """
    output_json['env_info'] = {'numpy': str(numpy.__version__),
                               'scipy': str(scipy.__version__)}
