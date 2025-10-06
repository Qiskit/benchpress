![Benchpress Image - © 2024 IBM. All Rights Reserved.](https://github.com/user-attachments/assets/67b82edb-52d6-47ac-a513-1b7129c20ea5)

Quantum software benchmarking
___

## What is Benchpress?

Benchpress is an open-source tool for benchmarking quantum software.

The Benchpress open-source benchmarking suite comprises over 1,000 different tests. These are standardized benchmarking tests designed by other members of the quantum community. For example, Benchpress compares SDKs’ abilities to generate [QASMBench circuits](https://github.com/pnnl/QASMBench), [Feynman circuits](https://github.com/meamy/feynman), and [Hamiltonian circuits](https://arxiv.org/pdf/2306.13126) (https://portal.nersc.gov/cfs/m888/dcamps/hamlib/). It also includes tests designed to test a language's ability to transpiler circuits for specific hardware, including the heavy hex architecture of IBM quantum processors and other generic qubit layouts.

If you find an issue with the testing or how we completed it, we encourage you to make a pull request.


## Citing Benchpress

 > [Benchmarking the performance of quantum computing software for quantum circuit creation, manipulation and compilation](https://doi.org/10.1038/s43588-025-00792-y),
Paul D. Nation, Abdullah Ash Saki, Sebastian Brandhofer, Luciano Bello, Shelly Garion, Matthew Treinish & Ali Javadi-Abhari, Nat. Comput. Sci. (2025).


## Previous results

This branch contains a collection of Benchpress results.  For consistency, all results are produced on the same desktop machine running a 12-core AMD 7900 processor with 128Gb of memory and a Linux OS.

### Qiskit results

This branch contains a collection of Benchpress results for [Qiskit](https://github.com/Qiskit/qiskit).


### Tket results

Due to the lengthy run times, results are split over multiple files.  Results for the construction and manipulation of circuits are not included as the primary focus point is on the transpilation results.

Note that, due to memory leaks in Tket, not all versions can be successfully executed via Benchpress.  E.g. see https://github.com/Qiskit/benchpress/issues/108


## License

[Apache License 2.0](LICENSE.txt)
