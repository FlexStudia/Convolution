# coding: utf-8

"""
    This model contains a tool for working with arrays.
"""

# PACKAGES
import numpy as np


def is_array_empty(arr):
    """
    Checks if a given array is empty and prints a warning if it is.

    :param arr: np.array:
        The array to check
    :return: bool:
        True if the array is empty, False otherwise.
    """
    if not isinstance(arr, np.ndarray) and not isinstance(arr, list):
        return True
    if type(arr) == list:
        if arr == [] or arr == [0] * len(arr):
            return True
    if isinstance(arr, np.ndarray):
        if np.array_equal(arr, np.array([])) or np.array_equal(arr, np.zeros(len(arr))):
            return True
    return False
