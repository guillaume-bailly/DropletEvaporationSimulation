"""
Tests for plots.py module
"""

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

from scipy.integrate import cumulative_trapezoid, solve_ivp
import numpy as np
import matplotlib.pyplot as plt

from utils import interpolate_ode

from plots import (
    plot_velocity,
    plot_diameter_squared,
    plot_droplet_temperature,
    plot_droplet_velocity,
    plot_droplet_position,
)


def test_plot_velocity():
    time = np.linspace(0, 4, 100)
    velocity = 2 * np.exp(-10 * time)
    initial_fig = plt.gcf()
    plot_velocity(time, velocity)
    final_fig = plt.gcf()
    assert initial_fig != final_fig, "A new matplotlib figure should have been created."


def test_plot_diameter_squared():
    time = np.linspace(0, 4, 100)
    diameter = time * 0.5
    initial_fig = plt.gcf()
    plot_diameter_squared(time, diameter, "Test Plot")
    final_fig = plt.gcf()
    assert initial_fig != final_fig, "A new matplotlib figure should have been created."


def test_plot_droplet_temperature():
    time = np.linspace(0, 4, 100)
    f = 2 * time + 4  # test function
    g = 5 * time - 6  # test function
    tspan = [0, 5]  # defining time interval
    Tp0 = [300]  # initial condition
    droplet_temperature = solve_ivp(interpolate_ode, tspan, Tp0, args=(time, f, g))
    initial_fig = plt.gcf()
    plot_droplet_temperature(droplet_temperature)
    final_fig = plt.gcf()
    assert initial_fig != final_fig, "A new matplotlib figure should have been created."


def test_plot_droplet_velocity():
    ta = np.linspace(0, 4, 100)
    f = 2 * ta + 4  # test function
    g = 5 * ta - 6  # test function
    tspan = [0, 5]  # defining time interval
    Up0 = [300]  # initial condition
    Up = solve_ivp(interpolate_ode, tspan, Up0, args=(ta, f, g))
    time = Up.t[:400]
    velocity = Up.y[0][:400]
    initial_fig = plt.gcf()
    plot_droplet_velocity(time, velocity, "Test Plot")
    final_fig = plt.gcf()
    assert initial_fig != final_fig, "A new matplotlib figure should have been created."


def test_plot_droplet_position():
    ta = np.linspace(0, 4, 100)
    f = 2 * ta + 4  # test function
    g = 5 * ta - 6  # test function
    tspan = [0, 5]  # defining time interval
    Up0 = [300]  # initial condition
    Up = solve_ivp(interpolate_ode, tspan, Up0, args=(ta, f, g))
    time = Up.t[:400]
    velocity = Up.y[0][:400]
    position = cumulative_trapezoid(velocity, time, initial=0)
    initial_fig = plt.gcf()
    plot_droplet_position(time, position, "Test Plot")
    final_fig = plt.gcf()
    assert initial_fig != final_fig, "A new matplotlib figure should have been created."
