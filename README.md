# Droplet Evaporation Simulation

![PyPI](https://img.shields.io/pypi/v/dropletevaporationsimulation)
[![Documentation Status](https://readthedocs.org/projects/dropletevaporationsimulation/badge/?version=latest)](https://dropletevaporationsimulation.readthedocs.io/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Coverage Status](https://coveralls.io/repos/github/guillaume-bailly/DropletEvaporationSimulation/badge.svg?branch=main)](https://coveralls.io/github/guillaume-bailly/DropletEvaporationSimulation?branch=main)
![Test Status](https://github.com/guillaume-bailly/DropletEvaporationSimulation/actions/workflows/tests.yml/badge.svg)
![pylint](https://img.shields.io/badge/pylint-7.33%2F10-ccff66)





This project simulates the evaporation and dynamics of an n-Decane droplet in a heated airflow, using both the D² Law and Infinite Liquid Conductivity models. It visualizes droplet diameter, temperature, velocity, and axial position over time. 

It can be used to compute the minimal axial length of a combustion chamber to ensure full envaporation of the droplet.

Droplet properties can be modified in src/constants.py to simulate the vaporization of desired fuel.

## Features

- **D² Law Model** and **Infinite Liquid Conductivity Model** simulations
- Plots for droplet diameter, temperature, axial velocity and position
- Adjustable parameters and configurations for droplet properties and environmental conditions

## Documentation

https://dropletevaporationsimulation.readthedocs.io/en/latest/

## Installation

```bash
git clone https://github.com/guillaume-bailly/DropletEvaporationSimulation.git
cd DropletEvaporationSimulation
pip install -r requirements.txt
```
Or:

```bash
pip install dropletevaporationsimulation
```

And update with:

```bash
pip install --upgrade dropletevaporationsimulation
```

## Run the simulation
```bash
des_run_simulation
```