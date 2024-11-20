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
