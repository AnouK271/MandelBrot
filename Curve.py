import numpy as np
from scipy.optimize import curve_fit

# Define the function to fit
def func(x, a, b, c, d):
    return a * np.cos(b * (x - c)) + d

# Your data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = np.array([22.8, 21.4, 19.2, 14.9, 10.7, 6.9, 7.2, 10.1, 14.6, 17.5, 19.9, 21.9])

# Initial guess for the parameters
guess = [7.95, 2*np.pi/11, 1, 14.85]

# Perform the curve fit
params, params_covariance = curve_fit(func, x, y, p0=guess)

print("Fitted function: f(x) = {:.2f} * cos({:.2f} * (x - {:.2f})) + {:.2f}".format(*params))
