![benchpress](https://media.github.ibm.com/user/152294/files/d93c265c-44c1-4a5d-82bd-494342ede900)


# benchpress
Quantum software benchmarking

## Supported SDKs

Benchpress currently supports the following SDKs:

- **BQSKit** (https://github.com/BQSKit/bqskit)
- **Braket** (https://github.com/amazon-braket/amazon-braket-sdk-python)
- **Cirq** (https://github.com/quantumlib/Cirq)
- **Qiskit** (https://github.com/Qiskit/qiskit)
- **Qiskit-Transpiler-Service** (https://github.com/Qiskit/qiskit-transpiler-service)
- **Staq** (https://github.com/softwareQinc/staq)
- **Tket** (https://github.com/CQCL/tket)

## Testing resource requirements

Running Benchpress is resource intensive.  Although the exact requirements depend on the SDK in question,a full execution of all the SDKs requires a system with 96+Gb of memory and, in some cases, will consume as many CPU resources as are available / assigned.  In addition, each suite of tests takes a non-negligible about of time, typically taking several hours or more to complete depending on the machine and timeout specified.

## Installation

Benchpress itself requires no installation.  However running it requires the tools in `requirements.txt`.  In addition, running each of the frameworks has its own dependencies in the corresponding `*-requirements.txt` file

### [pre-running] Create a skiplist

With the parameter `--timeout-skip-list=<SECs>`, a  *skiplist* (a list of tests to skip, given they take too long) is created.
For example, the following line runs the tests in `benchpress/tket_gym/construct` with a 1 hour timeout:

```bash
python -m pytest  --timeout-skip-list=3600 benchpress/tket_gym/construct
```

This will create a `skipfile.txt` file.
The mere existence of this file skips the tests listed there in the following executions.
No modifier needed.

## Running the benchmark tests

To run the benchmarks in the default configuration from inside the environment in which you want to perform the tests run:

```bash
python -m pytest benchpress/*_gym
```
where `*` is one of the frameworks that you want to test, and which matches the environment you are in.

To run the benchmarks and save to JSON one can do:

```bash
python -m pytest --benchmark-save=SAVED_NAME  benchpress/*_gym
```
which will save the file to the CWD in the `.benchmarks` folder

Further details on using `pytest-benchmark` can be found here: https://pytest-benchmark.readthedocs.io/en/latest/usage.html


## :construction: Running the memory tests :construction:

Benchmarking the amount of memory a  test uses can be very costly in terms of time and memory.  Here we use the `pytest-memray` plugin.  Calling the memory bechmark looks like:

```bash

python -m pytest --memray --trace-python-allocators --native --most-allocations=100 --benchmark-disable benchpress/*_gym
```

Here `--memray` turns on the memory profiler, `--trace-python-allocators` tracks all the memoryu allocations from Python, `--native` track C/C++/Rust memory, `--most-allocations=N` shows only the top `N` tests in terms of memory consuption, and finally `--benchmark-disable` turns off the timing benchmarks.

### Histogram issues

The `pytest-memray` plugin will sometimes raise on building the histrogram included in the report by default.  Currently the only way around this error, which does not affect the tests, is to manually comment out L322 and L323 from the `plugin.py` file:

```python
#histogram_txt = cli_hist(sizes, bins=min(len(sizes), N_HISTOGRAM_BINS))
#writeln(f"\t 📊 Histogram of allocation sizes: |{histogram_txt}|")
```
## Testing details

We have designed Benchpress in a manor to allow all tests to be executed on each SDK, regardless of whether that functionality is supported or not.  This is facilitated by the use of "workouts" that define abstract base classes that define each set of tests.  This design choice has the advantage of explicitly measuring the breadth of SDK functionality

### Test status description

In Benchpress each test status has a well defined meaning:

- **PASSED** - Indicates that the SDK has the functionality required to run the test, and doing so completed without error, and within the desired time-limit.

- **SKIPPED** - The SDK does not have the required functionality to execute the test.  This is the default for all tests defined in the workouts.

- **FAILED** - The SDK has the necessary functionality, but the test failed or the test did not complete within the set time-limit.

- **XFAIL** - The test fails in an irrecoverable manner, and is therefore tagged as failed rather than being executed. E.g. the test tries to use more memory than is available.


## Open-source packages

Benchpress makes use of files from the following open-source packages under terms of their licenses. License files are included in the corresponding directories.

- [Feynman](https://github.com/meamy/feynman)

- [QasmBench](https://github.com/pnnl/QASMBench)

- [HamLib](https://portal.nersc.gov/cfs/m888/dcamps/hamlib/)


## License

[Apache License 2.0](LICENSE.txt)

