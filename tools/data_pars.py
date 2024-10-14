# coding: utf-8

"""
    This module contains a class that parses data files.

    It can divide the information into a header and data.

    The data is then split into columns, the precision is determined, and the separator is identified.

    Additionally, this code can detect anomalous behavior, such as data lines with unusual lengths or data lines that contain text.
    Anomalous data is stored in a separate class variable to allow some further analysis and consideration.
"""

import os
import re
import numpy as np
from collections import Counter

from progress_dialog import initialize_progress_dialog, update_progress, finalize_progress

"""
    How to use:
        # INPUTS
        file_path: A string containing the path to the file to be parsed (obligatory).
        parent_window: The parent PyQt window where a QProgressDialog can be added in Qt-based apps (if used).
        line_start_from_0: An integer starting from 0 to set the starting line of the file if needed (normally not necessary).
        # CALL
        from data_reading import DataPars as DataPars
        data_read =  DataPars(file_path, parent_window=None) # data_read =  DataPars(file_path, parent_window=None, line_start_from_0)
        data_read.file_pars_f()
        # OUTPUT
        my_data = data_read.file_body  # A NumPy array of floats (float64), of size line by column, containing the parsed data from the file.
        file_header = data_read.file_header  # A list of strings representing each line in the file header.
        file_accuracy = data_read.file_accuracy  # A list of integers indicating the number of decimal signes for numbers in each column.
        file_garbage = data_read.file_garbage  # A list of strings where each string is a line in the data block that could not be parsed correctly, including lines with NaN values.
        file_separator = data_read.file_separator  # A string indicating the characters used as a separator in the file.

        At the end of this file there are two demo-factions to show some examples of usage.
"""

__version__ = "2.0.3"


class DataPars:
    """
        The DataPars class provides methods for processing and parsing data from files.

        DataPars assumes that the file begins with a header, followed by data organised into rows and columns.
        Each row of data is assumed to be a line of floats, with individual elements separated by a separator (the same within a row).
        All this information - data, header and separator - is stored in the corresponding variables (file_body, file_header, file_separator).

        If there are NaNs, strings and some other anomalies in the data, they are processed and stored separately (in the file_garbage variable).

        DataPars also determines the accuracy of the original data. So it can be reused from file_accuracy to keep the initial accuracy, for example.
    """

    def __init__(self, file_path, parent_window, file_start=0):
        """
            Initialize the DataPars object with file_path, parent_window, and file_start.
        :param file_path: str
            The path to the file to be processed.
        :param parent_window: object
            Reference to the parent window object in the UI.
        :param file_start: int
            The starting point in the file, default is 0.
        """
        # INPUTS
        self.file_path = file_path
        self.parent_window = parent_window
        self.file_start = file_start
        # Initialize all other attributes with default values.
        self.reset_values()

    def reset_values(self):
        """
            Resets the values of the DataPars object to their initial states.

            This function initializes the key attributes of a DataPars object,
            resetting them to ensure it starts from a clean state. This includes
            clearing file-related properties, setting patterns, and handling
            potential exceptions during the process.
        :return: None
        	The function returns nothing, but it resets various attributes of
        	the DataPars object.
        """
        try:
            # OUTPUTS
            self.file_header = []
            self.file_body = np.array([[]])
            self.file_accuracy = []
            self.file_garbage = []
            self.file_separator = ""
            # ACCESSORIES
            self.lines_length_collection = Counter()
            self.parsed_content = np.array([[]])
            self.separator_pattern = r"[ \,\t]+"
        except Exception as e:
            raise Exception(f"Critical error in DataPars:reset_values: {str(e)}") from e

    def read_file(self):
        """
            Reads the content of a file and returns it as a list of lines.

            This function attempts to open a file in read mode and return its content.
        :return: list
        	A list containing lines of the file.
        """
        try:
            with open(self.file_path, "r", encoding="utf8") as file:
                return file.readlines()
        except Exception as e:
            raise Exception(f"Critical error in DataPars:read_file: {str(e)}") from e

    def parse_file_content(self, file_content):
        """
            Parses the given file content line-by-line and stores the parsed data.

            Initializes necessary data structures for parsing the file content.
            Utilizes a progress bar if a parent window is present.
            Each line is split according to a specified pattern and converted into a numpy array.
            Lengths of these arrays are tracked to determine the main data block pattern.
        :param file_content: list of str
        	Each element represents a line from the file to be parsed.
        :return: None
        	The function returns nothing, but creates changes in parsed_content and lines_length_collection.
        """
        try:
            # initialization for self.parsed_content and self.lines_length_collection
            self.parsed_content = np.zeros(len(file_content), dtype=object)
            self.lines_length_collection = Counter()
            # progress bar is created
            progress = initialize_progress_dialog(self.parent_window, len(file_content), title='Parsing...', text='Parsing the file data')
            # parsing line by line
            for i, line in enumerate(file_content[self.file_start:], start=self.file_start):
                # progress bar continues or is canceled
                if not update_progress(self.parent_window, progress, i):
                    break
                # line is split according to self.separator_pattern using regular expression
                split_result = re.split(self.separator_pattern, line.strip())
                # now we try to create a np.array from the split_result
                try:
                    # the plit result is converted into a numpy array, where each item in the array is interpreted as a double type
                    line_to_vector = np.array(split_result, dtype=np.double)
                    # the length of the line_to_vector is counted and added to self.lines_length_collection
                    # we will use it later to determine the main data block pattern
                    self.lines_length_collection[len(line_to_vector)] += 1
                    # the line_to_vector is stored in the corresponding index of self.parsed_content
                    self.parsed_content[i] = line_to_vector
                except ValueError:
                    # if we cannot create a np.array from the split_result, we continue
                    continue
            # progress bar finishes
            finalize_progress(self.parent_window, progress, len(file_content))
        except Exception as e:
            raise Exception(f"Critical error in DataPars:parse_file_content: {str(e)}") from e

    def most_frequent_line_length(self):
        """
            Determine the most frequent line length in a collection of line lengths.

            This function retrieves the most common line length from a collection of line lengths
            and returns both the frequency of this length and the length value itself.
        :return: tuple
        	A tuple containing the count of the most common line length and the actual most common line length.
        """
        try:
            most_common_length, count = self.lines_length_collection.most_common(1)[0]
            return count, most_common_length
        except Exception as e:
            raise Exception(f"Critical error in DataPars:most_frequent_line_length: {str(e)}") from e

    def indexes_to_clear_f(self, max_length):
        """
            Indexes the elements that need to be cleared based on their type and content.

            This function scans the `parsed_content` list,
            identifying elements that are either not numpy arrays of the given `max_length` or contain NaN values.
            It returns the indexes of such elements along with markers for the headers' end and data's start.
        :param max_length: int
        	The expected length of the array elements in `parsed_content`.
        :return: tuple
        	A tuple containing:
        	- A list of indexes that should be cleared.
        	- The index where headers end.
        	- The index where data starts.
        """
        try:
            indexes_to_clean = []
            index_header_ends, index_data_starts = -1, -1
            progress = initialize_progress_dialog(self.parent_window, len(self.parsed_content), title='Processing...', text='Cleaning the data...')
            for i, element in enumerate(self.parsed_content):
                if not update_progress(self.parent_window, progress, i):
                    break
                if not isinstance(element, np.ndarray) or len(element) != max_length:
                    indexes_to_clean.append(i)
                elif np.isnan(element).any():  # NaN action is possible here
                    indexes_to_clean.append(i)
                    if index_header_ends == -1:
                        index_header_ends = i
                else:
                    if index_header_ends == -1:
                        index_header_ends = i
                    if index_data_starts == -1:
                        index_data_starts = i
            finalize_progress(self.parent_window, progress, len(self.parsed_content))
            return indexes_to_clean, index_header_ends, index_data_starts
        except Exception as e:
            raise Exception(f"Critical error in DataPars:indexes_to_clear_f: {str(e)}") from e

    def header_and_garbage_f(self, indexes_to_clean, index_header_ends, file_content):
        """
            Processes header and garbage data from the provided file content based on indexes.

            This function separates the header and garbage data from the file content using the provided indexes.
            It updates the `file_header` and `file_garbage` attributes accordingly.
            If a parent window is provided, it will display a progress dialog during the processing.

        :param indexes_to_clean: list[int]
        	List of indexes to be processed.
        :param index_header_ends: int
        	Index indicating the end of the header section.
        :param file_content: list[str]
        	Content of the file being processed.
        :return: None
        	The function returns nothing, but updates `file_header` and `file_garbage` attributes.
        """
        try:
            # header & garbage
            progress = initialize_progress_dialog(self.parent_window, len(indexes_to_clean), title='Processing...', text='Set up the header and the garbage...')
            for index in indexes_to_clean:
                if not update_progress(self.parent_window, progress, index):
                    break
                if index < index_header_ends:
                    self.file_header.append(file_content[index])
                else:
                    if np.isnan(self.parsed_content[index]).any():
                        self.file_garbage.append((index, self.parsed_content[index]))
                    else:
                        self.file_garbage.append((index, file_content[index]))
            finalize_progress(self.parent_window, progress, len(indexes_to_clean))
        except Exception as e:
            raise Exception(f"Critical error in DataPars:header_and_garbage_f: {str(e)}") from e

    def accuracy_and_separator_f(self, index_data_starts, file_content):
        """
            Processes accuracy and separator information from file content.

            This function iterates over the parsed content starting at a specified index
            to determine the numerical accuracy and separator patterns used in the file content.
            It also displays a progress dialog if a parent window is provided.
        :param index_data_starts: int
        	Index from which to start processing the data.
        :param file_content: list
        	List of strings representing the file content to process.
        :return: None
        	The function returns nothing, but updates file_accuracy and file_separator attributes.
        """
        try:
            # accuracy & separator
            progress = initialize_progress_dialog(self.parent_window, len(self.parsed_content), title='Processing...', text='Set up the accuracy and the separator...')
            for i in range(len(self.parsed_content)):
                if self.parent_window:
                    if not update_progress(self.parent_window, progress, i):
                        break
                if i >= index_data_starts and not np.isnan(self.parsed_content[i]).any():
                    for s in re.split(self.separator_pattern, file_content[i].strip()):
                        if "." in s:
                            if "E" in s or "e" in s:
                                self.file_accuracy.append(s.strip().lower().find("e") - s.strip().find(".") - 1)
                            else:
                                self.file_accuracy.append(len(s.strip()) - s.strip().find(".") - 1)
                        else:
                            self.file_accuracy.append(0)
                    match_separator = re.search(self.separator_pattern, file_content[i].strip())
                    if match_separator:
                        self.file_separator = match_separator[0]
                    break
            finalize_progress(self.parent_window, progress, len(self.parsed_content))
        except Exception as e:
            raise Exception(f"Critical error in DataPars:accuracy_and_separator_f: {str(e)}") from e

    def assign_no_data_content(self, file_content):
        """
            Assign initial no-data content to the file-related variables.

            This function initializes class attributes to empty states by setting file header to the given content
            and other metadata attributes to empty or default values.
        :param file_content: str
        	File header content to be assigned.
        :return: None
        	The function returns nothing but initializes the file-related attributes to default empty states.
        """
        try:
            self.file_header = file_content
            self.file_body = np.array([[]])
            self.file_accuracy = []
            self.file_garbage = []
            self.file_separator = ""
        except Exception as e:
            raise Exception(f"Critical error in DataPars:assign_no_data_content: {str(e)}") from e

    def assign_file_body(self, indexes_to_clean, max_length):
        """
            Assigns and cleans the file body based on specified indexes and maximum length.

            This method initializes the file_body attribute by creating a NumPy array,
            then iterates through the parsed content to populate the array, excluding specified indexes.
            The NumPy array is set up with predefined dimensions and data type.
        :param indexes_to_clean: list
                A list of integers representing indexes that need to be excluded from the file_body.
        :param max_length: int
                An integer specifying the maximum length of each line in the file_body.
        :return: None
                The function returns nothing, but modifies the `file_body` attribute of the instance.
        """
        try:
            self.file_body = np.empty([len(self.parsed_content) - len(indexes_to_clean), max_length], dtype=np.double)
            index = 0
            for i, line in enumerate(self.parsed_content):
                if i not in indexes_to_clean:
                    for j, data in enumerate(line):
                        self.file_body[index][j] = data
                    index += 1
        except Exception as e:
            raise Exception(f"Critical error in DataPars:assign_file_body: {str(e)}") from e

    def file_pars_f(self):
        """
        	Parses the content of a file based on various heuristics to separate data blocks from headers and garbage.

        	This function first checks if the file exists, resets any previous values, and reads the file's content.
        	It then applies the first approach to parsing the file to collect line lengths.
        	Depending on the result, it either processes the entire content as a single header
        	or proceeds with a second approach to identify and isolate data blocks.
        	:param file_path: str
        		The path to the file that needs to be parsed.
        	:return: None
        		 The function returns nothing, but modifies class attributes to store header, data, and related parsing information.
        """
        try:
            if os.path.isfile(self.file_path):
                # reset class variables
                self.reset_values()
                # read the file
                file_content = self.read_file()
                # apply "first-approach" file parsing and collect line lengths in self.lines_length_collection
                self.parse_file_content(file_content)
                # If self.lines_length_collection is empty, then the file has no blocks of data
                # So, we put all its content into the self.file_header
                if len(self.lines_length_collection.keys()) == 0:  # No numbers found
                    self.assign_no_data_content(file_content)
                # Otherwise we proceed to the "second-approach" file parsing
                else:
                    # we assume that lines with the data must have the most frequent length
                    # so, we search for it
                    max_qty, max_length = self.most_frequent_line_length()
                    # all lines with length different to max_length is not the data block
                    # so, we put their indexes apart in indexes_to_clean to avoid them later
                    # also we determine where the header is ended and the data is started
                    indexes_to_clean, index_header_ends, index_data_starts = self.indexes_to_clear_f(max_length)
                    # now we can determine header & garbage
                    self.header_and_garbage_f(indexes_to_clean, index_header_ends, file_content)
                    # as well as accuracy & separator
                    self.accuracy_and_separator_f(index_data_starts, file_content)
                    # finally, the data block is self.parsed_content without data on indexes_to_clean indexes
                    self.assign_file_body(indexes_to_clean, max_length)
            else:
                raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        except Exception as e:
            raise Exception(f"Critical error in DataPars:file_pars_f: {str(e)}") from e
