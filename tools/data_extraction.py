# coding: utf-8

"""
    This model contains helper functions to extract one or two columns from a data set.
"""

# PACKAGES
import numpy as np


def extract_two_columns_from_data(data, first_col_index, second_col_index):
    """
        Extracts two specified columns from a given dataset.

        This function takes a dataset and two column indices to extract the corresponding columns from each row.
        It returns two separate numpy arrays for the extracted columns.
        If the dataset is empty or if the specified indices are out of range, it returns two empty numpy arrays and prints an error message.
    :param data: list of lists
        The dataset from which columns are to be extracted.
    :param first_col_index: int
        The index of the first column to extract.
    :param second_col_index: int
        The index of the second column to extract.
    :return: tuple of numpy.ndarray
        Two numpy arrays containing the extracted columns. If an error occurs, both arrays will be empty.
    """
    try:
        if len(data) == 0 or len(data[0]) <= first_col_index or len(data[0]) <= second_col_index:
            print(f"Error in extract_two_columns_from_data: problem with the number of columns:\n"
                  f"data length is {len(data)}, but indexes {first_col_index} and {second_col_index} have been requested")
            return np.zeros(0), np.zeros(0)
        return extract_one_column_from_data(data, first_col_index), extract_one_column_from_data(data, second_col_index)
    except Exception as e:
        print(f"Error in two_from_file_extractor: {e}")
        return np.zeros(0), np.zeros(0)


def extract_one_column_from_data(data, column):
    """
        Extracts a single column from a 2D list of data.

        Given a 2D list of data, this function extracts the specified column and returns it as a numpy array.
        If the requested column index is out of bounds, it returns an empty numpy array and prints an error message.
    :param data: list of lists of float
        2D list from which a specific column is to be extracted.
    :param column: int
        Index of the column that needs to be extracted.
    :return: np.ndarray
        A numpy array containing the extracted column, or an empty numpy array if an error occurs.
    """
    try:
        if len(data) == 0 or len(data[0]) <= column:
            print(f"Error in extract_one_column_from_data: problem with the number of columns:\n"
                  f"data length is {len(data)}, index {column} has been requested")
            return np.zeros(0)
        return np.array([row[column] for row in data])
    except Exception as e:
        print(f"Error in one_from_file_extractor: {e}")
        return np.zeros(0)
