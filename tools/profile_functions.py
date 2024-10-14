# coding: utf-8

"""
    This module contains definitions of convolution functions.
"""

# PACKAGES
import math
import numpy as np
from scipy import special

def gauss_f(mean, sigma, x):
    """
        Computes the Gaussian function for given mean, standard deviation, and x value.

    This function calculates the value of the Gaussian (normal) distribution for a given mean,
    standard deviation (sigma), and x value using the formula:
        f(x) = exp(- (x - mean)^2 / (2 * sigma^2)) / (sqrt(2 * pi) * sigma).
    If sigma is zero, it will be replaced by a very small number to avoid division by zero.
    :param mean: float
    	The mean (average) of the Gaussian distribution.
    :param sigma: float
    	The standard deviation of the Gaussian distribution. It determines the width of the bell curve.
    :param x: float
    	The input value for which the Gaussian function needs to be computed.
    :return: float
    	The value of the Gaussian function for the given parameters.
    """
    try:
        if sigma == 0:
            sigma = 10 ** -15
        return math.exp(- ((x - mean) ** 2) / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
        # in Maple f_{Gauss}(x, mean, sigma) = \frac{e^{-\frac{(x-mean)^{2}}{2sigma^{2}}}}{\sqrt{2\pi}sigma}
    except Exception as e:
        print(f"Error in gauss_f: {e}")
        return np.NAN


def lorentz_f(mean, sigma, x):
    """
        Computes the Lorentzian function value for a given mean, sigma, and x.

        This function calculates the Lorentzian (or Cauchy) distribution, which is frequently utilized in spectroscopy and physics.
        The distribution is normalized to be 1 at its peak.

    :param mean: float
    	The central value (mean) of the distribution.
    :param sigma: float
    	The scale parameter of the distribution which determines its width. If sigma is 0, it is set to a very small value.
    :param x: float
    	The point at which the function is evaluated.
    :return: float
    	The value of the Lorentzian function at point x.
    """
    try:
        if sigma == 0:
            sigma = 10 ** -15
        return 1 / (math.pi * sigma * (1 + ((x - mean) ** 2 / (sigma ** 2))))
        # in Maple f_{Lorentz}(x, mean, gamma) = \frac{1}{\pi }\left (\frac{gamma}{(x-mean)^{2}+gamma^{2}}  \right )
    except Exception as e:
        print(f"Error in lorentz_f: {e}")
        return np.NAN


def gauss_lorentz_f(mean, sigma_gauss, sigma_lorentz, x, gauss_ratio):
    """
        Computes a linear combination of Gaussian and Lorentzian functions.

        The function calculates a weighted sum of a Gaussian and Lorentz function
        evaluated at a given point x, with respective means and standard deviations.
    :param mean: float
    	The mean value for both the Gaussian and Lorentzian functions.
    :param sigma_gauss: float
    	Standard deviation of the Gaussian function.
    :param sigma_lorentz: float
    	Half-width at half-maximum of the Lorentzian function.
    :param x: float
    	The point at which the function is evaluated.
    :param gauss_ratio: float
    	The weight of the Gaussian function in the linear combination.
    :return: float
    	The weighted sum of the Gaussian and Lorentzian function values at x.
    """
    try:
        return gauss_ratio * gauss_f(mean, sigma_gauss, x) + (1 - gauss_ratio) * lorentz_f(mean, sigma_lorentz, x)
        # in Maple f_{G+L}(x, mean, sigma, gamma) = g\cdot f_{G}(x, mean, sigma) + (1-g) f_{L}(x, mean, gamma)
    except Exception as e:
        print(f"Error in gauss_lorentz_f: {e}")
        return np.NAN


def voigt_f(mean, sigma_gauss, sigma_lorentz, x):
    """
        Computes the Voigt profile function.

        The Voigt profile is a convolution of a Gaussian and a Lorentzian profile.
    :param mean: float
        The center or mean of the distribution.
    :param sigma_gauss: float
        The standard deviation of the Gaussian component.
    :param sigma_lorentz: float
        The scale parameter of the Lorentzian component.
    :param x: float
        The point at which the function is evaluated.
    :return: float
        The computed value of the Voigt function at point x.
    """
    # in Maple f_{Voigt}(x, mean, sigma, gamma) = \int_{-\infty }^{+\infty}f_{Gauss}(y, mean, sigma)f_{Lorentz}(x-y, mean, gamma)dy
    try:
        if sigma_gauss == 0:
            sigma_gauss = 10 ** -15
        z = (x - mean + sigma_lorentz * 1j) / (sigma_gauss * math.sqrt(2))  # in Maple z = \frac{x-mean+i\cdot gamma}{\sqrt{2}\cdot sigma}
        return special.wofz(z).real / (sigma_gauss * math.sqrt(2 * math.pi))  # in Maple f_{Voigt}(x, mean, sigma, gamma) = \frac{Re(w(z))}{\sqrt{2\pi }sigma}
    except Exception as e:
        print(f"Error in voigt_f: {e}")
        return np.NAN


def triangle_f(mean, sigma, x):
    """
        Computes the value of a triangular function.

        This function calculates the value of a triangular function with a given mean,
        standard deviation, and input x. If the input x deviates from the mean by more
        than twice the standard deviation, it returns a very small value (10^-15).
    :param mean: float
        Mean value of the triangular function.
    :param sigma: float
        Standard deviation of the triangular function. If sigma is zero, it is
        adjusted to a very small value (10^-15) to prevent division by zero.
    :param x: float
        The input value for which the function value is being computed.
    :return: float
        The calculated value of the triangular function.
    """
    try:
        if sigma == 0:
            sigma = 10 ** -15
        if np.fabs(x - mean) > 2 * sigma:
            return 10 ** -15
        return (- np.fabs(mean - x) + 2 * sigma) / (4 * sigma ** 2)
        # in Maple f_{triangle}(x, mean, sigma) = \frac{-|mean-x|+2sigma}{4sigma^{2}}
    except Exception as e:
        print(f"Error in triangle_f: {e}")
        return np.NAN


def trapeze_f(mean, sigma, top, x):
    """
        Calculates the trapezoidal function for given parameters.

        This function computes a trapezoidal-shaped function.
    :param mean: float
    	The central value around which the trapezoidal function is shaped.
    :param sigma: float
    	The spread or width of the trapezoidal function. Should not be zero.
    :param top: float
    	The width of the top flat part of the trapezoid.
    :param x: float
    	The input value for which the function is evaluated.
    :return: float
    	The computed value of the trapezoidal function evaluated at x.
    """
    try:
        if sigma == 0:
            sigma = 10 ** -15
        if math.fabs(x - mean) > 2 * sigma - top:
            return 10 ** -15
        if math.fabs(x - mean) <= top:
            return 1 / (2 * sigma)
        return (- np.fabs(mean - x) + 2 * sigma - top) / (4 * sigma * (sigma - top))
        # in Maple f_{trapeze}(x, mean, sigma) = \frac{-|mean-x|+2sigma-top}{4sigma(sigma-top)}
    except Exception as e:
        print(f"Error in trapeze_f: {e}")
        return np.NAN
