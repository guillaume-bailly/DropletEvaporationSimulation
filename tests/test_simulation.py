"""
Tests for simulation.py module using pytest
"""

import pytest
import numpy as np
from src.simulation import DropletEvaporationModel

@pytest.fixture
def setup_model():
    """Fixture to set up the DropletEvaporationModel instance."""
    return DropletEvaporationModel()

def test_vapor_pressure_low(setup_model):
    """Test low-temperature vapor pressure calculation."""
    model = setup_model
    Pvap = model.vapor_pressure(300, model_type="low")
    assert Pvap > 0, "Vapor pressure should be positive for low-temperature model"

def test_vapor_pressure_high(setup_model):
    """Test high-temperature vapor pressure calculation."""
    model = setup_model
    Pvap = model.vapor_pressure(400, model_type="high")
    assert Pvap > 0, "Vapor pressure should be positive for high-temperature model"

def test_mass_transfer_number(setup_model):
    """Test mass transfer number calculation."""
    model = setup_model
    Pvap = model.vapor_pressure(300, model_type="low")
    Bm = model.calculate_mass_transfer_number(Pvap)
    assert Bm > 0, "Mass transfer number should be positive"

def test_calculate_droplet_temperature(setup_model):
    """Test droplet temperature calculation."""
    model = setup_model
    ta = np.linspace(0, 4, 100)
    Bm = 0.5
    Dsquare = np.linspace(1e-10, 1, 100)  # Avoid division by zero
    temperature_results = model.calculate_droplet_temperature(ta, Bm, Dsquare)
    
    assert temperature_results is not None, "Droplet temperature calculation should return results"
    assert all(temperature_results.y[0] >= 0), "Temperature values should be non-negative"

def test_calculate_droplet_velocity(setup_model):
    """Test droplet velocity calculation."""
    model = setup_model
    ta = np.linspace(0, 4, 100)
    Dsquare = np.linspace(1e-10, 1, 100)  # Avoid division by zero
    time, velocity = model.calculate_droplet_velocity(ta, Dsquare)
    
    assert time is not None, "Time values for velocity calculation should not be None"
    assert velocity is not None, "Velocity values should not be None"
    assert len(time) == len(velocity), "Time and velocity arrays should have the same length"

def test_calculate_droplet_position(setup_model):
    """Test droplet position calculation."""
    model = setup_model
    time = np.linspace(0, 4, 100)
    velocity = np.linspace(0, 2, 100)
    position = model.calculate_droplet_position(time, velocity)
    
    assert position is not None, "Droplet position calculation should return results"
    assert len(position) == len(time), "Position array should match the length of the time array"
    assert all(position >= 0), "Position values should be non-negative"

def test_d2_law_diameter_squared(setup_model):
    """Test D² law diameter squared calculation."""
    model = setup_model
    ta = np.linspace(0, 4, 100)
    result = model.calculate_diameter_squared(ta, 0.5, model="d2_law")
    
    assert all(result >= 0), "Squared diameter should not have negative values"
