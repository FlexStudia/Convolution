# coding: utf-8

"""
    This model contains functions for extrapolation.
"""

# PACKAGES
import numpy as np


def linear_extrapolation(start, stop, step, quantity=0):  # stop is included!
    """
        Generates a linear extrapolation between start and stop points with a specified step and quantity.

        This function calculates a series of equally spaced values based on given start, stop, and step parameters.
        The stop value is included in the series.
        If quantity is not provided, it is computed from the given start, stop, and step.
        Order of the start and stop is adjusted based on their values to handle both increasing and decreasing series.

    :param start: float
        The starting value of the series.
    :param stop: float
        The stopping value of the series.
    :param step: float
        The increment value between each pair of consecutive numbers in the series.
    :param quantity: int, optional
        The number of values to generate, including the start and stop. If not provided, it will be
        calculated based on start, stop, and step.

    :return: np.array
        A NumPy array containing the generated values in linear order based on the provided parameters.
    """
    try:
        is_reverse_order = start > stop
        if is_reverse_order:
            start, stop = stop, start
        if not quantity:
            stop = start + int((stop - start) / step) * step
            quantity = int(np.round((stop - start) / step, 0)) + 1
        result = np.linspace(start, stop, quantity, endpoint=True)
        return np.flip(result) if is_reverse_order else result
    except Exception as e:
        print(f"Error in linear_extrapolation: {e}")
        return np.zeros(0)


def const_extrapolation(const_value, quantity):
    """
        Generates an array filled with a constant value.

        This function atpredicted_outputts to create a NumPy array of a given quantity filled with a specified constant value.
        In case of an exception, it returns an empty array and prints an error message.

    :param const_value: any type
    	The constant value to fill the array with.
    :param quantity: int
    	The number of elements in the array.
    :return: np.ndarray
    	A NumPy array filled with the constant value, or an empty array if an exception occurs.
    """
    try:
        return np.full(quantity, const_value)
    except Exception as e:
        print(f"Error in const_extrapolation: {e}")
        return np.zeros(0)


def y_extrapolation(x_list, y_list, quantity_before, quantity_after, extrapolation_mode):
    """
        Performs y-axis extrapolation on given data.

        This function takes x and y data points and
        extends the y data by a specified quantity before and after the existing y data
        according to different extrapolation modes.

    :param x_list: numpy.ndarray
    	List of x-axis data points.
    :param y_list: numpy.ndarray
    	List of y-axis data points corresponding to x_list.
    :param quantity_before: int
    	Number of points to extrapolate before the existing y data.
    :param quantity_after: int
    	Number of points to extrapolate after the existing y data.
    :param extrapolation_mode: int
    	Mode of extrapolation. Modes are:
    	0 - Zeros extrapolation
    	1 - Constant extrapolation
    	2 - Average constant extrapolation
    	3 - Linear regression extrapolation
    :return: numpy.ndarray
    	The extended y data points array after extrapolation.
    """
    try:
        if len(y_list) + quantity_before + quantity_after != len(x_list):
            print("Error in y_extrapolation: wrong list sizes")
            return np.zeros(0)
        predicted_output = np.zeros(0)
        if extrapolation_mode == 0:  # zeros
            predicted_output = np.zeros(len(y_list) + quantity_before + quantity_after)
            for i in range(quantity_before, len(y_list) + quantity_before):
                predicted_output[i] = y_list[i - quantity_before]
            return predicted_output
        if extrapolation_mode == 1:  # constant
            predicted_output = np.zeros(len(y_list) + quantity_before + quantity_after)
            for i in range(quantity_before):
                predicted_output[i] = y_list[0]
            for i in range(quantity_before, len(y_list) + quantity_before):
                predicted_output[i] = y_list[i - quantity_before]
            for i in range(quantity_before + len(y_list), len(y_list) + quantity_before + quantity_after):
                predicted_output[i] = y_list[len(y_list) - 1]
            return predicted_output
        if extrapolation_mode == 2:  # average constant
            if len(y_list) > 5:
                predicted_output = np.zeros(len(y_list) + quantity_before + quantity_after)
                for i in range(quantity_before):
                    predicted_output[i] = (y_list[0] + y_list[1] + y_list[2] + y_list[3] + y_list[4])/5
                for i in range(quantity_before, len(y_list) + quantity_before):
                    predicted_output[i] = y_list[i - quantity_before]
                for i in range(quantity_before + len(y_list), len(y_list) + quantity_before + quantity_after):
                    predicted_output[i] = (y_list[len(y_list) - 1] + y_list[len(y_list) - 2] + y_list[len(y_list) - 3] + y_list[len(y_list) - 4] + y_list[len(y_list) - 5])/5
                return predicted_output
            else:
                print("Warning in y_extrapolation: not enough points for 'average constant' regression")
                print("'Constant' regression will be done instead.")
                return y_extrapolation(x_list, y_list, quantity_before, quantity_after, 2)
        if extrapolation_mode == 3:  # linear regression
            predicted_output = np.zeros(len(y_list) + quantity_before + quantity_after)
            x_output = np.zeros(quantity_before + quantity_after)
            x_input = np.zeros(5)
            y_input = np.zeros(5)
            # before
            for i in range(quantity_before):
                x_output[i] = x_list[i]
            for i in range(5):
                x_input[i] = x_list[quantity_before + i]
                y_input[i] = y_list[i]
            y_output = linear_regression(x_input, y_input, x_output)
            for i in range(quantity_before):
                predicted_output[i] = y_output[i]
            #middle
            for i in range(quantity_before, len(y_list) + quantity_before):
                predicted_output[i] = y_list[i - quantity_before]
            # after
            x_output = np.zeros(quantity_after)
            y_output = np.zeros(quantity_after)
            for i in range(len(y_list) + quantity_before, len(y_list) + quantity_before + quantity_after):
                x_output[i - len(y_list) - quantity_before] = x_list[i]
            for i in range(5):
                x_input[i] = x_list[len(x_list) - quantity_after - 5 + i]
                y_input[i] = y_list[len(y_list) - 5 + i]
            y_output = linear_regression(x_input, y_input, x_output)
            del x_output, x_input, y_input
            for i in range(quantity_before + len(y_list), len(y_list) + quantity_before + quantity_after):
                predicted_output[i] = y_output[i - quantity_before - len(y_list)]
            return predicted_output
        return predicted_output
    except Exception as e:
        print(f"Error in y_extrapolation: {e}")
        return np.zeros(0)


def linear_regression(x_input, y_input, x_output):
    """
        Computes a linear regression.

        This function calculates the coefficients of a linear regression model based on input data,
        and then uses this model to predict output values for new data points. It uses the formula
        y = coefficient * x + constant to perform predictions.

    :param x_input: numpy.ndarray
    	Input array for the independent variable in the training data.
    :param y_input: numpy.ndarray
    	Input array for the dependent variable in the training data.
    :param x_output: numpy.ndarray
    	Input array for the independent variable in the data to be predicted.
    :return predicted_output: numpy.ndarray
    	Array containing the predicted output values based on the linear regression model.
    """
    try:
        predicted_output = np.zeros(len(x_output))
        coefficient = (len(x_input) * np.sum(x_input * y_input) - np.sum(x_input) * np.sum(y_input)) / (len(x_input) * np.sum(x_input * x_input) - np.sum(x_input) * np.sum(x_input))
        constant = (np.sum(y_input) * np.sum(x_input * x_input) - np.sum(x_input) * np.sum(x_input * y_input)) / (len(x_input) * np.sum(x_input * x_input) - np.sum(x_input) * np.sum(x_input))
        for i in range(len(x_output)):
            predicted_output[i] = coefficient * x_output[i] + constant
        return predicted_output
    except Exception as e:
        print(f"Error in linear_regression: {e}")
        return np.zeros(0)
