"""
Tests for constants.py module
"""

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

from src.constants import TIME_ARRAY, DO, TF, TA


def test_time_array_length():
    assert len(TIME_ARRAY) > 0, "Time array should not be empty"


def test_initial_conditions():
    assert DO > 0, "Initial droplet diameter must be positive"
    assert TF > 0, "Initial temperature must be positive"
    assert TA > 0, "Ambient temperature must be positive"
