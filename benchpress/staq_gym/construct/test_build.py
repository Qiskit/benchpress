"""Test circuit generation"""

from benchpress.workouts.build import WorkoutCircuitConstruction
from benchpress.workouts.validation import benchpress_test_validation


@benchpress_test_validation
class TestWorkoutCircuitConstruction(WorkoutCircuitConstruction):
    pass
