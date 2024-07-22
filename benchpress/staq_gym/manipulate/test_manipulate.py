"""Test circuit manipulation"""

from benchpress.workouts.manipulate import WorkoutCircuitManipulate
from benchpress.workouts.validation import benchpress_test_validation


@benchpress_test_validation
class TestWorkoutCircuitManipulate(WorkoutCircuitManipulate):
    pass
