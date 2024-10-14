# coding: utf-8

"""
    This module contains auxiliary functions for adjusting the size of data arrays.
"""

# PACKAGES
import numpy as np


def width_cut_off(spectrum_width, spectrum_wavelength, destination_wavelength):
    """
        Adjusts the spectrum width array to a given destination wavelength array.

        The function takes a spectrum width array and a spectrum wavelength array,
        then trims or interpolates it to match a specified destination wavelength array.
        It ensures that the lengths of the input spectrum width and wavelength arrays are identical
        and that the spectrum wavelength array starts no later than the destination wavelength array.
    :param spectrum_width: list or numpy.ndarray
        A list or array of spectrum widths that needs to be adjusted.
    :param spectrum_wavelength: list or numpy.ndarray
        A list or array of wavelengths corresponding to the spectrum_width.
    :param destination_wavelength: list or numpy.ndarray
        A list or array of desired wavelengths to which the spectrum_width should be adjusted.
    :return return_var: numpy.ndarray
        An array of spectrum widths adjusted to the destination wavelength.
    """
    try:
        if len(spectrum_width) != len(spectrum_wavelength):
            print(f"Error in width_cut_off: spectrum_wavelength must be the same length as spectrum_width")
            return np.zeros(0)
        if spectrum_wavelength[0] > destination_wavelength[0]:
            print(f"Error in width_cut_off: spectrum_wavelength must start at least at the same place as destination_wavelength")
            return np.zeros(0)
        converted_data = np.zeros(len(destination_wavelength))
        dw_before = spectrum_wavelength[0] - destination_wavelength[0]
        index = 0
        destination_now = destination_wavelength[index]
        for i in range(1, len(spectrum_wavelength)):
            dw_now = spectrum_wavelength[i] - destination_now
            if dw_now >= 0:
                if np.fabs(dw_before) < np.fabs(dw_now):
                    converted_data[index] = spectrum_width[i - 1]
                else:
                    converted_data[index] = spectrum_width[i]
                index = index + 1
                if index >= len(converted_data):
                    break
                destination_now = destination_wavelength[index]
            dw_before = dw_now
        return converted_data
    except Exception as e:
        print(f"Error in width_cut_off: {e}")
        return np.zeros(0)


def spectrum_to_destination_cut(spectrum_wavelength, spectrum_intensity, destination_wavelength):
    """
    	Converts and crops the spectrum wavelength and intensity to the specified destination wavelength range.

    	This function filters the provided spectrum wavelength and intensity such that only the values
    	that fall within the given destination wavelength range are preserved. If no values are within the range,
    	it returns arrays of zeros.
    :param spectrum_wavelength: list of float
        List of wavelength values in the spectrum to be filtered.
    :param spectrum_intensity: list of float
        List of intensity values corresponding to the spectrum wavelengths.
    :param destination_wavelength: list of float
        List containing the start and end wavelength defining the destination range.
    :return: tuple of (numpy.ndarray, numpy.ndarray)
        The filtered wavelength and intensity values as numpy arrays. Returns arrays of zeros if no values match the range.
    """
    try:
        def is_within_destination_range(wavelength, destination_range):
            return destination_range[0] <= wavelength <= destination_range[-1]
        filtered_wavelength = []
        filtered_intensity = []
        inside_destination_range = False
        for wavelength, intensity in zip(spectrum_wavelength, spectrum_intensity):
            if is_within_destination_range(wavelength, destination_wavelength):
                inside_destination_range = True
                filtered_wavelength.append(wavelength)
                filtered_intensity.append(intensity)
            elif inside_destination_range:
                break
        if inside_destination_range:
            return np.array(filtered_wavelength), np.array(filtered_intensity)
        return np.zeros(0), np.zeros(0)
    except Exception as e:
        print(f"Error in spectrum_to_destination_cut: {e}")
        return np.zeros(0), np.zeros(0)
