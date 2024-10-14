# coding: utf-8

"""
    This module contains auxiliary functions used to change the unit.
"""

# PACKAGES
import numpy as np


def units_conversion(value_to_convert, unit_from, unit_to):  # possible units: cm-1, micron, nm, A
    """
    	Converts a value from one unit of wavelength measurement to another.

    	This function takes a numerical value and converts it between units.
    	Supported units are: cm-1, micron, nm, and A.
    :param value_to_convert: float
        The numeric value that needs to be converted.
    :param unit_from: str
        The unit of the value that needs to be converted from, expected to be one of the following: cm-1, micron, nm, or A.
    :param unit_to: str
        The unit of the value that needs to be converted to, expected to be one of the following: cm-1, micron, nm, or A.
    :return: float
        The converted value in the requested unit. If conversion is not possible, returns numpy.NaN.
    """
    try:
        UNITS = ["cm-1", "micron", "nm", "A"]
        CONVERSION_FACTORS = {
            ("cm-1", "micron"): (10000, "divide"),
            ("micron", "cm-1"): (10000, "divide"),
            ("cm-1", "nm"): (10000000, "divide"),
            ("nm", "cm-1"): (10000000, "divide"),
            ("cm-1", "A"): (100000000, "divide"),
            ("A", "cm-1"): (100000000, "divide"),
            ("micron", "nm"): (1000, "multiply"),
            ("nm", "micron"): (1 / 1000, "multiply"),
            ("A", "micron"): (1 / 10000, "multiply"),
            ("micron", "A"): (10000, "multiply"),
            ("nm", "A"): (10, "multiply"),
            ("A", "nm"): (1 / 10, "multiply")
        }
        def do_conversion(value, factor, operation):
            return value * factor if operation == "multiply" else factor / value
        if unit_from == unit_to:
            return value_to_convert
        if value_to_convert == 0:
            return 0
        if unit_from not in UNITS or unit_to not in UNITS:
            print(f"Unit can be only cm-1, micron, nm or A ('{unit_from}' and '{unit_to}'were set)!")
            return np.NAN
        factor, operation = CONVERSION_FACTORS.get((unit_from, unit_to))
        if factor:
            return do_conversion(value_to_convert, factor, operation)
        print("Conversion not supported!")
        return np.NAN
    except Exception as e:
        print(f"Error in units_conversion: {e}")
        return np.NAN


def change_width_unit(widths, original_wavelengths, unit_from, unit_to):
    """
        Converts widths from one unit of measurement to another, assuming a linear relation with wavelength.

        This function takes a list of widths and their associated original wavelengths and converts the widths from a
        specified unit to another unit. The conversion takes into account the change in units for wavelengths and
        adjusts the widths accordingly.
    :param widths: list
        The original widths that need to be converted.
    :param original_wavelengths: list
        The original wavelengths corresponding to each width.
    :param unit_from: str
        The original unit of the widths and wavelengths.
    :param unit_to: str
        The target unit to which the widths and wavelengths should be converted.
    :return: numpy.ndarray
        The converted widths in the target unit, or an array of zeros if an error occurs.
    """
    try:
        if len(widths) != len(original_wavelengths):
            return np.zeros(0)
        converted_wavelengths = change_unit(original_wavelengths, unit_from, unit_to)
        converted_data = np.zeros(len(widths))
        for i in range(len(widths)):
            converted_data[i] = widths[i] * converted_wavelengths[i] / original_wavelengths[i]
        return converted_data
    except Exception as e:
        print(f"Error in change_width_unit: {e}")
        return np.zeros(0)


def change_unit(data, unit_from, unit_to):
    """
        Converts a list of values from one unit to another.
    :param data: list
        List of values to be converted.
    :param unit_from: str
        Unit of the original values.
    :param unit_to: str
        Unit to convert the values to.
    :return: ndarray
        An array of the converted values. If an error occurs, returns an array of zeros.
    """
    try:
        return np.array([units_conversion(d, unit_from, unit_to) for d in data])
    except Exception as e:
        print(f"Error in change_unit: {e}")
        return np.zeros(0)
