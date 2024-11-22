"""
Main script for the Droplet Evaporation Simulation project.

This script initializes the simulation parameters, computes the evaporation
models, and generates plots for droplet properties over time.
"""

from constants import TIME_ARRAY, DO, TF, TA
from simulation import DropletEvaporationModel
from plots import plot_velocity, plot_diameter_squared, plot_droplet_temperature
import numpy as np


def main():
    # Initialize the evaporation model
    model = DropletEvaporationModel()

    # Compute gas-phase velocity over time
    ug = model.ug
    plot_velocity(TIME_ARRAY, ug)

    # Calculate vapor pressure for low and high temperature ranges
    Pvap1 = model.vapor_pressure(TF, model_type="low")
    Pvap2 = model.vapor_pressure(TF, model_type="high")

    # Compute Spalding mass transfer numbers
    Bm1 = model.calculate_mass_transfer_number(Pvap1)
    Bm2 = model.calculate_mass_transfer_number(Pvap2)

    # Compute D² evolution using D² law and infinite liquid conductivity models
    diameter_squared_d2_law = model.calculate_diameter_squared(TIME_ARRAY, Bm1, model="d2_law")
    diameter_squared_inf_conductivity = model.calculate_diameter_squared(TIME_ARRAY, Bm2, model="infinite_liquid_conductivity")

    # Normalize results for plotting
    normalized_d2_law = diameter_squared_d2_law / DO**2
    normalized_inf_conductivity = diameter_squared_inf_conductivity / DO**2

    # Plot the D² evolution for both models
    plot_diameter_squared(TIME_ARRAY, normalized_d2_law, "D² Evolution (D² Law)")
    plot_diameter_squared(TIME_ARRAY, normalized_inf_conductivity, "D² Evolution (Infinite Liquid Conductivity)")

    #Compute and plot droplet temperature evolution
    droplet_temperature = model.calculate_droplet_temperature(TIME_ARRAY,Bm2,diameter_squared_inf_conductivity)
    plot_droplet_temperature(droplet_temperature)

    # Additional outputs like droplet temperature or axial velocity can be computed here.
    # Example: Integrating the temperature model.

    # End of simulation
    print("Simulation complete. Plots generated.")


if __name__ == "__main__":
    main()
