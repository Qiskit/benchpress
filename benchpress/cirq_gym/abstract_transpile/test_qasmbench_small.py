"""Test summit benchmarks"""
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.abstract_transpile import WorkoutAbstractQasmBenchSmall


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchSmall(WorkoutAbstractQasmBenchSmall):
    pass
