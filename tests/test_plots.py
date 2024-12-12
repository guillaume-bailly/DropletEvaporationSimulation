"""
Tests for plots.py module
"""

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

from plots import (
    plot_velocity,
    plot_diameter_squared,
    plot_droplet_temperature,
    plot_droplet_velocity,
    plot_droplet_position,
)
from utils import interpolate_ode
from scipy.integrate import cumtrapz, solve_ivp
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


def test_plot_droplet_temperature():
    time = np.linspace(0, 4, 100)
    f = 2 * time + 4  # test function
    g = 5 * time - 6  # test function
    tspan = [0, 5]  # defining time interval
    Tp0 = [300]  # initial condition
    droplet_temperature = solve_ivp(interpolate_ode, tspan, Tp0, args=(time, f, g))
    fig = plot_droplet_temperature(droplet_temperature)
    assert isinstance(fig, plt.Figure), "Should return a matplotlib figure"


def test_plot_droplet_velocity():
    ta = np.linspace(0, 4, 100)
    f = 2 * time + 4  # test function
    g = 5 * time - 6  # test function
    tspan = [0, 5]  # defining time interval
    Up0 = [300]  # initial condition
    Up = solve_ivp(interpolate_ode, tspan, Up0, args=(ta, f, g))
    time = Up.t[:400]
    velocity = Up.y[0][:400]
    fig = plot_droplet_velocity(time, velocity, "Test Plot")
    assert isinstance(fig, plt.Figure), "Should return a matplotlib figure"


def test_plot_droplet_position():
    ta = np.linspace(0, 4, 100)
    f = 2 * time + 4  # test function
    g = 5 * time - 6  # test function
    tspan = [0, 5]  # defining time interval
    Up0 = [300]  # initial condition
    Up = solve_ivp(interpolate_ode, tspan, Up0, args=(ta, f, g))
    time = Up.t[:400]
    velocity = Up.y[0][:400]
    position = cumtrapz(velocity, time, initial=0)
    fig = plot_droplet_position(time, position, "Test Plot")
    assert isinstance(fig, plt.Figure), "Should return a matplotlib figure"
