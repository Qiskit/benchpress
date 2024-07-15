"""Test circuit generation"""

from benchpress.workouts.validation import benchpress_test_validation
from benchpress.workouts.build import WorkoutCircuitConstruction

@benchpress_test_validation
class TestWorkoutCircuitConstruction(WorkoutCircuitConstruction):
    pass