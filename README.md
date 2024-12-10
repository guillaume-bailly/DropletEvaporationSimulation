# Droplet Evaporation Simulation

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Coverage Status](https://coveralls.io/repos/github/guillaume-bailly/DropletEvaporationSimulation/badge.svg?branch=main)](https://coveralls.io/github/guillaume-bailly/DropletEvaporationSimulation?branch=main)

This project simulates the evaporation and dynamics of an n-Decane droplet in a heated airflow, using both the D² Law and Infinite Liquid Conductivity models. It visualizes droplet diameter, temperature, velocity, and axial position over time. It can be used to compute the minimal axial length of a combustion chamber to ensure full envaporation of the droplet.

## Features

- **D² Law Model** and **Infinite Liquid Conductivity Model** simulations
- Plots for droplet diameter, temperature, axial velocity and position
- Adjustable parameters and configurations for droplet properties and environmental conditions

## Installation

```bash
git clone https://github.com/guillaume-bailly/DropletEvaporationSimulation.git
cd DropletEvaporationSimulation
pip install -r requirements.txt
