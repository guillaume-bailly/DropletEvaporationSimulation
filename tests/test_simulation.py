"""
Tests for simulation.py module
"""

import unittest
import numpy as np
from src.simulation import DropletEvaporationModel

class TestDropletEvaporationModel(unittest.TestCase):
    def setUp(self):
        self.model = DropletEvaporationModel()

    def test_vapor_pressure_low(self):
        # Test low-temperature vapor pressure calculation
        Pvap = self.model.vapor_pressure(300, model_type="low")
        self.assertGreater(Pvap, 0)

    def test_vapor_pressure_high(self):
        # Test high-temperature vapor pressure calculation
        Pvap = self.model.vapor_pressure(400, model_type="high")
        self.assertGreater(Pvap, 0)

    def test_mass_transfer_number(self):
        # Test mass transfer number calculation
        Pvap = self.model.vapor_pressure(300, model_type="low")
        Bm = self.model.calculate_mass_transfer_number(Pvap)
        self.assertGreater(Bm, 0)

    def test_d2_law_diameter_squared():
        model = DropletEvaporationModel()
        time_array = np.linspace(0, 4, 100)
        result = model.calculate_diameter_squared(time_array, 0.5, model="d2_law")
        assert all(result >= 0), "Squared diameter should not have negative values"

if __name__ == "__main__":
    unittest.main()
