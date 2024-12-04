# src/plots.py

import matplotlib.pyplot as plt

def plot_velocity(time, ug):
    plt.figure()
    plt.plot(time, ug)
    plt.title('Axial velocity of gas phase')
    plt.xlabel('time (s)')
    plt.ylabel('Ug(t) (m/s)')
    plt.show()

def plot_diameter_squared(time, diameter_squared, title):
    plt.figure()
    plt.plot(time, diameter_squared)
    plt.axis([0, 4, 0, 1])
    plt.xlabel('time (s)')
    plt.ylabel('(D/Do)^2')
    plt.title(title)
    plt.show()

def plot_droplet_temperature(droplet_temperature):
    plt.figure()
    plt.plot(droplet_temperature.t, droplet_temperature.y[0])
    plt.xlabel('time (s)')
    plt.ylabel('Tp (K)')
    plt.title('Evolution of droplet temperature over time (Infinite liquid conductivity model)')
    plt.axis([0, 0.5, 300, 450])
    plt.show()

def plot_droplet_velocity(time, velocity, title):
    plt.figure()
    plt.plot(time, velocity)
    plt.xlabel('time (s)')
    plt.ylabel('Up (m/s)')
    plt.title('Evolution of droplet axial velocity over time - ' + title)
    plt.show()

def plot_droplet_position(time, position, title):
    plt.figure()
    plt.plot(time, position)
    plt.xlabel('time (s)')
    plt.ylabel('Xp (m)')
    plt.title('Evolution of droplet axial position over time - ' + title)
    plt.show()