![benchpress](https://media.github.ibm.com/user/152294/files/d93c265c-44c1-4a5d-82bd-494342ede900)


# :construction: benchpress :construction:
Benchmarking for Qiskit

## Installation

Benchpress itself requires no installation.  However running it requires the tools in `requirements.txt`.  In addition, running each of the frameworks has its own dependencies in the corresponding `*-requirements.txt` file



## Running the benchmark tests

To run the benchmarks in the default configuration from inside the environment in which you want to perform the tests run:

```bash
python -m pytest --benchmark-min-rounds=1 benchpress/*_gym
```
where `*` is one of the frameworks that you want to test, and which matches the environment you are in.  Here `--benchmark-min-rounds=1`sets the minimum number of repeated trials to 1, which will save a great deal of time

To run the benchmarks and save to JSON one can do:

```bash
python -m pytest --benchmark-min-rounds=1 --benchmark-save=SAVED_NAME  benchpress/*_gym
```
which will save the file to the CWD in the `.benchmarks` folder

Further details on using `pytest-benchmark` can be found here: https://pytest-benchmark.readthedocs.io/en/latest/usage.html


## Running the memory tests

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

## License

[Apache License 2.0](LICENSE.txt)

