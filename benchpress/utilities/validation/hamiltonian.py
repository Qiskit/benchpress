from bqskit.ext import bqskit_to_qiskit
from pytket.extensions.qiskit import tk_to_qiskit
from qiskit.providers.fake_provider import GenericBackendV2
from qiskit.quantum_info import SparsePauliOp, Operator
from qiskit.transpiler import Layout
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager


from bqskit import compile
from bqskit.compiler import Compiler

from benchpress.bqskit_gym.utils.bqskit_backend_utils import BqskitFlexibleBackend
from benchpress.bqskit_gym.utils.io import bqskit_hamiltonian_circuit
from benchpress.qiskit_gym.utils.io import qiskit_hamiltonian_circuit
from benchpress.tket_gym.utils.io import tket_hamiltonian_circuit
from benchpress.tket_gym.utils.tket_backend_utils import TketFlexibleBackend


def check_hamiltonian_equiv(spop):
    bk_backend = BqskitFlexibleBackend(4, "all-to-all")
    qk_backend = GenericBackendV2(4)
    tk_backend = TketFlexibleBackend(4, "all-to-all")

    bk_qc = bqskit_hamiltonian_circuit(spop)
    qk_qc = qiskit_hamiltonian_circuit(spop)
    tk_qc = tket_hamiltonian_circuit(spop)

    bk_qct = compile(
        bk_qc,
        model=bk_backend,
        optimization_level=1,
        compiler=Compiler(),
    )
    qk_qct = generate_preset_pass_manager(
        optimization_level=2, initial_layout=list(range(4)), backend=qk_backend
    ).run(qk_qc)
    # TODO look into equivalency for tket with optimisation_level=2, currently there is a mismatch - aggressive optimization?
    tk_backend.default_compilation_pass(optimisation_level=1).apply(tk_qc)

    bk_qct = bqskit_to_qiskit(bk_qct)
    tk_qc = tk_to_qiskit(tk_qc)

    assert Operator.from_circuit(qk_qct).equiv(
        bk_qct, atol=1e-6
    ), "Qiskit/Bqskit Hamiltonians not equal"
    # Note that tket and qiskit have different qubit endianess
    rlayout = Layout({q: i for i, q in enumerate(qk_qct.qubits[::-1])})
    assert Operator.from_circuit(qk_qct, layout=rlayout).equiv(
        tk_qc
    ), "Qiskit/Tket Hamiltonians not equal"


pstr = [
    "IIII",
    "XXYY",
    "XYYX",
    "YXXY",
    "YYXX",
    "ZIII",
    "ZZII",
    "ZIZI",
    "ZIIZ",
    "IZII",
    "IZZI",
    "IZIZ",
    "IIZI",
    "IIZZ",
    "IIIZ",
]
coeffs = [
    -1.47217837e01 + 0.0j,
    -4.83543568e-03 + 0.0j,
    4.83543568e-03 + 0.0j,
    4.83543568e-03 + 0.0j,
    -4.83543568e-03 + 0.0j,
    8.17478553e-02 + 0.0j,
    5.86844977e-02 + 0.0j,
    3.11424089e-02 + 0.0j,
    3.59778446e-02 + 0.0j,
    8.17478553e-02 + 0.0j,
    3.59778446e-02 + 0.0j,
    3.11424089e-02 + 0.0j,
    2.83688863e-02 + 0.0j,
    3.45987447e-02 + 0.0j,
    2.83688863e-02 + 0.0j,
]

check_hamiltonian_equiv(SparsePauliOp(["XYYX", "YXXY"], coeffs=[1.234] * 2))
check_hamiltonian_equiv(SparsePauliOp(pstr, coeffs))
