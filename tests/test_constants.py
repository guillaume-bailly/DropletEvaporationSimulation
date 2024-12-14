"""
Tests for constants.py module
"""

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

import constants


def test_time_array_properties():
    """Test the properties of the time array."""
    assert len(constants.TIME_ARRAY) == 1000, "Time array length should be 1000"
    assert constants.TIME_ARRAY[0] == 0, "Time array should start at 0"
    assert constants.TIME_ARRAY[-1] == 4, "Time array should end at 4"


def test_droplet_properties():
    """Test the droplet properties constants."""
    assert constants.DO > 0, "Initial droplet diameter must be positive"
    assert constants.RHO_F > 0, "Droplet density must be positive"
    assert constants.CP_F > 0, "Droplet specific heat must be positive"
    assert constants.H_FG > 0, "Latent heat of evaporation must be positive"
    assert constants.DV > 0, "Mass diffusivity must be positive"
    assert constants.MF > 0, "Molecular weight must be positive"
    assert constants.TF > 0, "Initial droplet temperature must be positive"


def test_vapor_pressure_constants():
    """Test the vapor pressure constants."""
    assert all(
        isinstance(const, (int, float))
        for const in [
            constants.A1,
            constants.B1,
            constants.C1,
            constants.A2,
            constants.B2,
            constants.C2,
        ]
    ), "Vapor pressure constants must be numeric"


def test_gas_phase_properties():
    """Test the gas-phase properties constants."""
    assert constants.LAMBDA > 0, "Thermal conductivity must be positive"
    assert constants.RHO_A > 0, "Ambient density must be positive"
    assert constants.MU_A > 0, "Dynamic viscosity must be positive"
    assert constants.MA > 0, "Molecular weight of air must be positive"
    assert constants.TA > 0, "Far-field temperature must be positive"
    assert constants.CP_A > 0, "Specific heat of air must be positive"


def test_sherwood_number():
    """Test the Sherwood number."""
    assert constants.SH > 0, "Sherwood number must be positive"


def test_update_constants_function():
    """Test the update_constants function for its existence and type."""
    assert hasattr(
        constants, "update_constants"
    ), "The update_constants function should exist"
    assert callable(constants.update_constants), "update_constants should be callable"


def test_constants_are_floats():
    """Test if all numeric constants are of float type where applicable."""
    numeric_constants = [
        constants.DO,
        constants.RHO_F,
        constants.CP_F,
        constants.H_FG,
        constants.DV,
        constants.MF,
        constants.TF,
        constants.LAMBDA,
        constants.RHO_A,
        constants.MU_A,
        constants.MA,
        constants.TA,
        constants.CP_A,
        constants.SH,
    ]
    assert all(
        isinstance(value, (float, int)) for value in numeric_constants
    ), "All constants should be numeric"


def test_constants_have_reasonable_values():
    """Test that constants fall within expected physical ranges."""
    assert 1e-6 <= constants.DO <= 1e-3, "Initial diameter DO out of expected range"
    assert 500 <= constants.RHO_F <= 1000, "Density RHO_F out of expected range"
    assert 1000 <= constants.CP_F <= 3000, "Specific heat CP_F out of expected range"
    assert (
        1e5 <= constants.H_FG <= 1e6
    ), "Latent heat of evaporation H_FG out of expected range"
    assert 1e-8 <= constants.DV <= 1e-5, "Mass diffusivity DV out of expected range"
    assert 0.01 <= constants.MF <= 0.2, "Molecular weight MF out of expected range"
    assert 200 <= constants.TF <= 400, "Initial temperature TF out of expected range"
    assert (
        0.01 <= constants.LAMBDA <= 1
    ), "Thermal conductivity LAMBDA out of expected range"
    assert 0.5 <= constants.RHO_A <= 2, "Density RHO_A out of expected range"
    assert (
        1e-6 <= constants.MU_A <= 1e-4
    ), "Dynamic viscosity MU_A out of expected range"
    assert 0.01 <= constants.MA <= 0.1, "Molecular weight MA out of expected range"
    assert 200 <= constants.TA <= 500, "Far-field temperature TA out of expected range"
    assert 500 <= constants.CP_A <= 2000, "Specific heat CP_A out of expected range"
    assert 1 <= constants.SH <= 10, "Sherwood number SH out of expected range"
