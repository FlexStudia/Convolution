# coding: utf-8

"""
    This module contains functions for conversions between numbers and strings.
"""

import numpy as np

def float_to_str(value_format, qty_digits, float_type):
    """
    	Converts a floating point number to a formatted string.

    	This function takes a floating point number along with the desired number
    	of decimal places and the type of float formatting to output a formatted
    	string representation of the float.

    	:param value_format: float
    		The float value that needs to be formatted.
    	:param qty_digits: int
    		The number of decimal places to format the float to.
    	:param float_type: str
    		The type of float formatting ('f' for fixed-point, 'e' for scientific notation, etc.).

    	:return: str
    		A formatted string representation of the float value.
    """
    try:
        return f"{value_format:.{qty_digits}{float_type}}"
    except Exception as e:
        raise Exception(f"Critical error in float_to_str: {str(e)}") from e


def is_int(anything):
    """
        Determines if the given string represents an integer.

        This function tries to convert the input string to an integer.
        If the conversion is successful, it returns True, indicating that the string represents an integer.
        If the conversion fails, it raises a ValueError and returns False, indicating that the string does not represent an integer.

    :param anything: str
    	The input string to check if it represents an integer.
    :return: bool
    	True if the input string represents an integer, False otherwise.
    """
    try:
        int(anything)
        return True
    except ValueError:
        return False
    

def is_float(anything):
    """
        Determine if the provided string can be converted to a float.

        The function attempts to convert the given input string into a float.
        If the conversion is successful, it returns True. Otherwise, it catches a ValueError and returns False.

        :param anything: str
            The string to be checked if it can be converted to a float.

        :return: bool
            True if the string can be converted to a float, otherwise False.
    """
    try:
        float(anything)
        return True
    except ValueError:
        return False


def str_to_float(some_string):
    """
    	Converts a string to a float if it represents a valid float, otherwise returns NaN.

    	This function takes a string input, checks if it can be converted to a float. If the string
    	is a valid representation of a floating-point number, it converts and returns the float.
    	If not, the function returns NaN to indicate that the conversion was not possible.

    	:param some_string: str
    		A string to be evaluated for conversion into a float.
    	:return: float
    		The floating-point number if conversion is possible, otherwise NaN.
    """
    if is_float(some_string):
        return float(some_string)
    else:
        return np.NAN
