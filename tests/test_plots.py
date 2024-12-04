"""
Tests for plots.py module
"""

from src.plots import plot_velocity, plot_diameter_squared
import numpy as np
import matplotlib.pyplot as plt

def test_plot_velocity():
    time = np.linspace(0, 4, 100)
    velocity = 2 * np.exp(-10 * time)
    fig = plot_velocity(time, velocity)
    assert isinstance(fig, plt.Figure), "Should return a matplotlib figure"

def test_plot_diameter_squared():
    time = np.linspace(0, 4, 100)
    diameter = time * 0.5
    fig = plot_diameter_squared(time, diameter, "Test Plot")
    assert isinstance(fig, plt.Figure), "Should return a matplotlib figure"
