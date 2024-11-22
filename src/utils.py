# src/utils.py

import numpy as np
from scipy.integrate import solve_ivp

def interpolate_ode(t, y, ta, f, g):
    #ODE function with interpolated f and g values for differential equation.
    f_interp = np.interp(t, ta, f)
    g_interp = np.interp(t, ta, g)
    return -f_interp * y + g_interp
"""
def interpolate_ode(f, g, y):
    dydt = -f * y + g 
    return dydt

    """