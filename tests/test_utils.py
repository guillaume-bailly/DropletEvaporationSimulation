"""
Tests for utils.py module using pytest
"""

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

import pytest
import numpy as np

from utils import interpolate_ode


@pytest.fixture
def sample_data():
    """Fixture providing sample data for tests."""
    t = np.linspace(0, 10, 100)  # time points
    ta = np.linspace(0, 10, 10)  # interpolation points
    y = np.sin(t)  # example ODE solution
    f = np.cos(ta)  # time-dependent function 1
    g = np.ones_like(ta)  # time-dependent function 2
    return t, y, ta, f, g


def test_interpolate_ode_with_valid_data(sample_data):
    """Test interpolate_ode with valid data."""
    t, y, ta, f, g = sample_data

    result = interpolate_ode(t, y, ta, f, g)

    assert result.shape == t.shape, "Output shape should match input time array."
    assert np.allclose(
        result[:5], -np.interp(t[:5], ta, f) * y[:5] + np.interp(t[:5], ta, g)
    ), "Interpolated values should be consistent with expected computation."
