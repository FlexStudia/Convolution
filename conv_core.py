# coding: utf-8

"""
    This code (mainly ConvolutionCore class) represents the core.

    Core completely solves the problem of the convolution, but its interface is limited to the console.

    At the end of this file there is the demo_f function, which demonstrates how to use this class to calculate convolution.
"""

# PACKAGES
import os
import math
import numpy as np
import copy

# MODULES
from tools.data_pars import DataPars as DataPars
from tools.profile_functions import gauss_f, lorentz_f, gauss_lorentz_f, voigt_f, triangle_f, trapeze_f
from tools.units_change_operations import units_conversion, change_width_unit, change_unit
from tools.data_length_adjust import spectrum_to_destination_cut, width_cut_off
from tools.data_extraction import extract_one_column_from_data, extract_two_columns_from_data
from tools.extrapolations import const_extrapolation, linear_extrapolation, y_extrapolation
from tools.array_tools import is_array_empty
from progress_dialog import initialize_progress_dialog, update_progress, finalize_progress

# GLOBALS
version = "2.0"
copyright = "The MIT License"
copyright_URL = "https://opensource.org/license/mit"
author_mail = "flex.studia.dev@gmail.com"
bug_support_mail = "flex.studia.help@gmail.com"
github_url = "https:github.com/FlexStudia/Convolution_core"
__app_name__ = "Spectrum convolution core"
__org_name__ = "Flex Studia Dev"
__org_site__ = github_url

# Main modul CLASS
class ConvolutionCore:
    def __init__(self):
        """
            Initializes the object and its state.
        """
        self.parent_window = None
        self.tests_are_running = False
        self.init_spectrum()
        self.init_destination()
        self.init_convolution()
        self.init_globals()
        self.init_output()

    # INITIALISATION
    def init_spectrum(self):
        """
            Initializes spectrum attributes.

            This function sets up initial values for various attributes related to the spectrum:
            file paths, data separators, and default columns for wavelength, intensity, and width.

        :return: None
        """
        self.spectrum_file_path = ""
        self.spectrum_unit_original = ""
        self.spectrum_unit_current = ""
        self.spectrum_separator = ""
        self.spectrum_wavelength_column = -1
        self.spectrum_intensity_column = -1
        self.spectrum_width_path = ""
        self.spectrum_width_column = -1
        self.spectrum_width_const = 0

    def init_destination(self):
        """
            Initializes the destination attributes.

            This function sets the destination unit, file path, wavelength column,
            wavelength start, wavelength stop, and wavelength step to their respective
            default values.

        :return: None
        """
        self.destination_unit = ""
        self.destination_file_path = ""
        self.destination_wavelength_column = -1
        self.destination_wavelength_start = 0
        self.destination_wavelength_stop = 0
        self.destination_wavelength_step = 0

    def init_convolution(self):
        """
            Initializes the convolution parameters.

            This function sets various convolution attributes to default settings
            which include types, ratios, truncations, constants, file paths, and start/stop values.

        :return: None
        """
        self.convolution_type = -1
        self.convolution_gauss_ratio = 0
        self.convolution_truncation = 0
        self.convolution_extrapolation_type = ""
        self.convolution_width_1_const = 0
        self.convolution_width_2_const = 0
        self.convolution_file_path = ""
        self.convolution_width_1_column = -1
        self.convolution_width_2_column = -1
        self.convolution_width_1_start = 0
        self.convolution_width_1_stop = 0
        self.convolution_width_2_start = 0
        self.convolution_width_2_stop = 0

    def init_globals(self):
        """
            Initializes and resets all global variables related to the spectrum, destination, and convolution.

            Sets up the initial values for wavelength, intensity, widths, and other related parameters for
            spectrum and destination components. Also, sets the initial parameters for convolution-related
            variables.

        :return: None
        """
        # spectrum
        self.spectrum_wavelength_original = np.zeros(0)
        self.spectrum_intensity_original = np.zeros(0)
        self.spectrum_wavelength = np.zeros(0)
        self.spectrum_intensity = np.zeros(0)
        self.spectrum_width = np.zeros(0)
        self.spectrum_garbage = False
        self.spectrum_width_garbage = False
        self.spectrum_set_up = False
        self.revers_order_spectrum = False
        # destination
        self.destination_input_type = 0
        self.linear_destination_warning = False
        self.last_destination_value = 0
        self.destination_wavelength = np.zeros(0)
        self.destination_garbage = False
        self.destination_set_up = False
        self.destination_quantity = 0
        self.revers_order_destination = False
        # convolution
        self.convolution_input_type = 0
        self.convolution_width_1 = np.zeros(0)
        self.convolution_width_2 = np.zeros(0)
        self.convolution_width_garbage = False
        self.convolution_set_up = False
        self.n_truncation_values = {
            0: 3,  # Gauss
            1: 1,  # triangle
            2: 1,  # trapeze
            3: 2000,  # Lorentz
            4: 2000,  # Voigt
            5: 2000,  # Gauss+Lorentz
        }

    def init_output(self):
        """
            Initializes output parameters.

        :return: None
        """
        self.destination_intensity = np.zeros(0)
        self.convolution_is_calculated = False
        # test purposes
        self.mean_truncated_convolution_function_area = 0
        self.spectrum_surface_area = 0
        self.destination_surface_area = 0
        self.destination_brut_surface_area = 0

    # SETTERS
    def parent_window_setter(self, parent_window):
        """
            Sets the parent window for the current object.

        :param parent_window: object (QMainWindow or QDialog)
            The window object to set as the parent.
        :return: None
            The function returns nothing, but it sets the parent window.
        """
        self.parent_window = parent_window

    def spectrum_setter_spectrum_from_file_and_its_width_from_file(self, spectrum_unit,
                                                                   spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column,
                                                                   spectrum_width_path, spectrum_width_column):
        """
            Set up spectrum wavelength and width from a file.

            This function initializes various attributes related to spectrum data and attempts to read the spectrum data from a specified file.

        :param spectrum_unit: str
        	The unit used for the spectrum.
        :param spectrum_file_path: str
        	Path to the file that contains spectrum data.
        :param spectrum_wavelength_column: int
        	Column index (starting at 0) for wavelength data in the spectrum file.
        :param spectrum_intensity_column: int
        	Column index (starting at 0) for intensity data in the spectrum file.
        :param spectrum_width_path: str
        	Path to the file that contains spectrum width data.
        :param spectrum_width_column: int
        	Column index (starting at 0) for width data in the spectrum width file.
        :return: None
        """
        try:
            self.spectrum_file_path = spectrum_file_path
            self.spectrum_unit_original = spectrum_unit
            self.spectrum_unit_current = ""
            self.spectrum_separator = ""
            self.spectrum_wavelength_column = spectrum_wavelength_column
            self.spectrum_intensity_column = spectrum_intensity_column
            self.spectrum_width_path = spectrum_width_path
            self.spectrum_width_column = spectrum_width_column
            self.spectrum_wavelength_original = np.zeros(0)
            self.spectrum_intensity_original = np.zeros(0)
            self.spectrum_wavelength = np.zeros(0)
            self.spectrum_intensity = np.zeros(0)
            self.spectrum_width = np.zeros(0)
            self.spectrum_set_up = False
            self.revers_order_spectrum = False
            self.get_spectrum_and_its_width()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:spectrum_setter_spectrum_from_file_and_its_width_from_file: {str(e)}") from e

    def spectrum_setter_spectrum_from_file_and_its_width_constant(self, spectrum_unit,
                                                                  spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column,
                                                                  spectrum_width_const):
        """
            Set up spectrum data from a file with a constant width.

            This method initializes the spectrum properties from given parameters,
            and reads the spectrum data from the specified file path.

        :param spectrum_unit: str
            The unit of the spectrum (e.g., 'nm', 'cm-1').
        :param spectrum_file_path: str
            Path to the file containing the spectrum data.
        :param spectrum_wavelength_column: int
            Index of the column (starting at 0) in the file that contains spectrum data.
        :param spectrum_intensity_column: int
            Index of the column (starting at 0) in the file that contains spectrum data.
        :param spectrum_width_const: float
            Constant value representing the width of the spectrum.
        :return: None
        """
        try:
            self.spectrum_file_path = spectrum_file_path
            self.spectrum_unit_original = spectrum_unit
            self.spectrum_unit_current = ""
            self.spectrum_separator = ""
            self.spectrum_wavelength_column = spectrum_wavelength_column
            self.spectrum_intensity_column = spectrum_intensity_column
            self.spectrum_width_const = spectrum_width_const
            self.spectrum_wavelength_original = np.zeros(0)
            self.spectrum_intensity_original = np.zeros(0)
            self.spectrum_wavelength = np.zeros(0)
            self.spectrum_intensity = np.zeros(0)
            self.spectrum_width = np.zeros(0)
            self.spectrum_set_up = False
            self.revers_order_spectrum = False
            self.get_spectrum_and_its_width()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:spectrum_setter_spectrum_from_file_and_its_width_constant: {str(e)}") from e

    def destination_setter_from_file(self, destination_unit,
                                     destination_file_path, destination_wavelength_column):
        """
            Sets up the destination from a file.

            This function initializes several attributes related to the destination from a file
            and reads the data.

        :param destination_unit: str
        	The unit used for the destination data.
        :param destination_file_path: str
        	File path of the destination file.
        :param destination_wavelength_column: int
        	Column index (starting at 0) for the wavelength in the destination file.
        :return: None
        """
        try:
            self.destination_unit = destination_unit
            self.destination_file_path = destination_file_path
            self.destination_wavelength_column = destination_wavelength_column
            self.destination_wavelength = np.zeros(0)
            self.destination_set_up = False
            self.destination_quantity = 0
            self.revers_order_destination = False
            self.destination_intensity = np.zeros(0)
            self.destination_input_type = 1
            self.get_destination_from_file()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:destination_setter_from_file: {str(e)}") from e

    def destination_setter_linear_function(self, destination_unit,
                                           destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step):
        """
            Sets up the destination as a linear function.

            This function initializes the destination, as a linear function, including unit, wavelength range, and step.
            It performs initial setup and computation required for the destination setting.

        :param destination_unit: str
        	Unit of the destination.
        :param destination_wavelength_start: float
        	Start wavelength for the destination.
        :param destination_wavelength_stop: float
        	Stop wavelength for the destination.
        :param destination_wavelength_step: float
        	Wavelength step for the destination.

        :return: None
        """
        try:
            self.destination_unit = destination_unit
            self.destination_wavelength_start = destination_wavelength_start
            self.destination_wavelength_stop = destination_wavelength_stop
            self.destination_wavelength_step = destination_wavelength_step
            self.destination_wavelength = np.zeros(0)
            self.destination_set_up = False
            self.destination_quantity = 0
            self.revers_order_destination = False
            self.destination_intensity = np.zeros(0)
            self.destination_input_type = 2
            self.get_destination_as_linear_function()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:destination_setter_linear_function: {str(e)}") from e

    def convolution_setter_width_from_file(self, convolution_type,
                                           convolution_gauss_ratio,
                                           convolution_truncation,
                                           convolution_extrapolation_type,
                                           convolution_file_path, convolution_width_1_column, convolution_width_2_column):
        """
            Sets convolution parameters and its width(s) from file.

            Configures various parameters related to convolution, initializes certain properties,
            and attempts to read convolution data from a specified file path.

        :param convolution_type: int
            Type of convolution to be used (0: Gauss function, 1: triangle, 2: trapeze, 3: Lorentz function, 4: Voigt, 5: Gauss & Lorentz sum).
        :param convolution_gauss_ratio: float
            Ratio for the Gaussian component in the convolution (from 0 to 1).
        :param convolution_truncation: float
            Specifies the truncation level for the convolution (positive value).
        :param convolution_extrapolation_type: int
            Method for extrapolation (0: zeros, 1: constant, 2: average constant, 3: linear regression).
        :param convolution_file_path: str
            File path from which to read convolution data.
        :param convolution_width_1_column: int
            Column index (starting at 0) the first width.
        :param convolution_width_2_column: int or np.NaN
            Column index (starting at 0) for the second width,
            np.NaN if no second width (for the Gauss function, the triangle, and the Lorentz function).
        :return: None
        """
        try:
            self.convolution_type = convolution_type
            self.convolution_gauss_ratio = convolution_gauss_ratio
            self.convolution_truncation = convolution_truncation
            self.convolution_extrapolation_type = convolution_extrapolation_type
            self.convolution_file_path = convolution_file_path
            self.convolution_width_1_column = convolution_width_1_column
            self.convolution_width_2_column = convolution_width_2_column
            self.convolution_width_1 = np.zeros(0)
            self.convolution_width_2 = np.zeros(0)
            self.convolution_set_up = False
            self.convolution_input_type = 1
            self.get_convolution_width_from_file()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_setter_width_from_file: {str(e)}") from e

    def convolution_setter_width_linear_function(self, convolution_type,
                                                 convolution_gauss_ratio,
                                                 convolution_truncation,
                                                 convolution_extrapolation_type,
                                                 convolution_width_1_start, convolution_width_1_stop,
                                                 convolution_width_2_start, convolution_width_2_stop):
        """
            Set convolution parameters and its width(s) as a linear function.

            This function sets various convolution parameters including type, ratio, truncation, extrapolation type,
            and start and stop for the width(s).

        :param convolution_type: int
            Type of convolution (0: Gauss function, 1: triangle, 2: trapeze, 3: Lorentz function, 4: Voigt, 5: Gauss & Lorentz sum).
        :param convolution_gauss_ratio: float
            Ratio used for Gaussian convolution (from 0 to 1 including).
        :param convolution_truncation: float
            Truncation parameter for the convolution (positive value).
        :param convolution_extrapolation_type: int
            Type of extrapolation beyond the data range (0: zeros, 1: constant, 2: average constant, 3: linear regression).
        :param convolution_width_1_start: float
            Starting width for the first convolution parameter.
        :param convolution_width_1_stop: float
            Stopping width for the first convolution parameter.
        :param convolution_width_2_start: float or np.NaN
            Starting width for the second convolution parameter,
            np.NaN if no second width (for the Gauss function, the triangle, and the Lorentz function).
        :param convolution_width_2_stop: float or np.NaN
            Stopping width for the second convolution parameter,
            np.NaN if no second width (for the Gauss function, the triangle, and the Lorentz function).
        :return: None
        """
        try:
            self.convolution_type = convolution_type
            self.convolution_gauss_ratio = convolution_gauss_ratio
            self.convolution_truncation = convolution_truncation
            self.convolution_extrapolation_type = convolution_extrapolation_type
            self.convolution_width_1_start = convolution_width_1_start
            self.convolution_width_1_stop = convolution_width_1_stop
            self.convolution_width_2_start = convolution_width_2_start
            self.convolution_width_2_stop = convolution_width_2_stop
            self.convolution_width_1 = np.zeros(0)
            self.convolution_width_2 = np.zeros(0)
            self.convolution_set_up = False
            self.convolution_input_type = 2
            self.get_convolution_width_as_linear_function()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_setter_width_linear_function: {str(e)}") from e

    def convolution_setter_width_constant(self, convolution_type,
                                          convolution_gauss_ratio,
                                          convolution_truncation,
                                          convolution_extrapolation_type,
                                          convolution_width_1_const,
                                          convolution_width_2_const):
        """
            Sets the convolution parameters and its width(s) as a constant.

            This method initializes the convolution parameters using the provided constant values and, subsequently,
            invokes the method to handle convolution with these constants. It sets various properties of the convolution
            such as type, ratio, truncation, and extrapolation type. Default values for convolution widths and set up flag are also initialized.

        :param convolution_type: int
        	Specifies the type of convolution. (0: Gauss function, 1: triangle, 2: trapeze, 3: Lorentz function, 4: Voigt, 5: Gauss & Lorentz sum).
        :param convolution_gauss_ratio: float
        	The ratio of Gaussian convolution (from 0 to 1).
        :param convolution_truncation: float
        	The truncation value for the convolution (positive value).
        :param convolution_extrapolation_type: int
        	Specifies the type of extrapolation at the edges of the data. (0: zeros, 1: constant, 2: average constant, 3: linear regression).
        :param convolution_width_1_const: float
        	The first constant width used in the convolution.
        :param convolution_width_2_const: float or np.NaN
        	The second constant width used in the convolution,
        	np.NaN if no second width (for the Gauss function, the triangle, and the Lorentz function).
        :return: None
        """
        try:
            self.convolution_type = convolution_type
            self.convolution_gauss_ratio = convolution_gauss_ratio
            self.convolution_truncation = convolution_truncation
            self.convolution_extrapolation_type = convolution_extrapolation_type
            self.convolution_width_1_const = convolution_width_1_const
            self.convolution_width_2_const = convolution_width_2_const
            self.convolution_width_1 = np.zeros(0)
            self.convolution_width_2 = np.zeros(0)
            self.convolution_set_up = False
            self.convolution_input_type = 3
            self.get_convolution_width_as_constant()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_setter_width_constant: {str(e)}") from e

    # DATA GETTERS
    # spectrum
    def get_spectrum_and_its_width(self):
        """
            Get the spectrum and its width for further processing.

            This function reads the spectrum data from a file, determines the spectrum width using a file or constant,
            and sets up the final spectrum.

        :return: None
        """
        try:
            self.read_spectrum_from_file()
            if not np.isnan(self.spectrum_width_column) and os.path.isfile(self.spectrum_width_path):
                self.read_spectrum_width_from_file()
            elif not np.isnan(self.spectrum_width_const):
                self.spectrum_width_from_constant()
            self.spectrum_final_set_up()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:get_spectrum_and_its_width: {str(e)}") from e

    def read_spectrum_from_file(self):
        """
            Reads the spectrum data from a specified file and extracts the wavelength and intensity.

            This function initializes a DataPars object with the provided file path and parent window,
            calls the method to parse the file, and then extracts the spectral data into wavelength
            and intensity columns based on specified column indices.
        :return: None
            The function returns nothing, but it sets the spectrum_separator, spectrum_wavelength, and
            spectrum_intensity attributes of the class.
        """
        try:
            spectrum_reader = DataPars(self.spectrum_file_path, self.parent_window)
            spectrum_reader.file_pars_f()
            if not is_array_empty(spectrum_reader.file_garbage):
                self.spectrum_garbage = True
            self.spectrum_separator = spectrum_reader.file_separator
            self.spectrum_wavelength, self.spectrum_intensity = extract_two_columns_from_data(spectrum_reader.file_body, self.spectrum_wavelength_column, self.spectrum_intensity_column)
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:read_spectrum_from_file: {str(e)}") from e

    def read_spectrum_width_from_file(self):
        """
            Reads and processes the spectrum width from a file.

            Attempts to read the spectrum width data from the specified path and column.
            If the data is successfully read, processes and stores it the spectrum_width_original clss attribute.

        :return: None
            The function returns nothing, but it sets the spectrum_width_original class attribute.
        """
        try:
            spectrum_data = DataPars(self.spectrum_width_path, self.parent_window)
            spectrum_data.file_pars_f()
            if not is_array_empty(spectrum_data.file_garbage):
                self.spectrum_width_garbage = True
            self.spectrum_width = extract_one_column_from_data(spectrum_data.file_body, self.spectrum_width_column)
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:read_spectrum_width_from_file: {str(e)}") from e

    def spectrum_width_from_constant(self):
        """
            Sets a constant spectrum width based on input parameters.

            This function sets the original spectrum width using
            the provided constant spectrum width and the length of
            the spectrum wavelength array.

        :return: None
        	The function returns nothing, but updates self.spectrum_width_original with the computed spectrum width.
        """
        try:
            self.spectrum_width = const_extrapolation(self.spectrum_width_const, len(self.spectrum_wavelength))
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:spectrum_width_from_constant: {str(e)}") from e

    def spectrum_final_set_up(self):
        """
            Sets up the final state of the spectrum.

            This function coordinates the final preparatory steps required for spectrum setup.
            It ensures that the spectrum unit matches the destination unit and preserves the original
            wavelength and intensity data (used to keep non-extrapolated raw spectrum).

            :return: None
        	    The function returns nothing, but updates the spectrum configuration and preserves its original state.
            """
        try:
            if self.destination_set_up and self.spectrum_unit_current != self.destination_unit:
                self.spectrum_unit_change()
            self.spectrum_change_order()
            self.spectrum_wavelength_original = copy.deepcopy(self.spectrum_wavelength)
            self.spectrum_intensity_original = copy.deepcopy(self.spectrum_intensity)
            self.spectrum_set_up = True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:spectrum_final_set_up: {str(e)}") from e

    def spectrum_unit_change(self):
        """
            Updates the spectrum unit and its related parameters.

            This function changes the current spectrum unit to a destination unit, updating
            the relevant spectrum width and wavelength parameters.

        :return: None
            The function returns nothing, but modifies the spectrum unit and related parameters.
        """
        try:
            self.spectrum_unit_current = self.spectrum_unit_original
            if not is_array_empty(self.spectrum_width):
                self.spectrum_width = change_width_unit(self.spectrum_width, self.spectrum_wavelength, self.spectrum_unit_current, self.destination_unit)
            self.spectrum_wavelength = change_unit(self.spectrum_wavelength, self.spectrum_unit_current, self.destination_unit)
            self.spectrum_unit_current = self.destination_unit
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:spectrum_unit_change: {str(e)}") from e

    def spectrum_change_order(self):
        """
            Check and reverse the order of the spectrum data if necessary.

            This function verifies whether the spectral data is in ascending order of wavelength.
            If the wavelengths are not in ascending order, it reverses the order of both the wavelengths and intensities.
            It also sets a flag to indicate the reversal.

        :return: None
        	The function return nothing, but alters the order of spectrum data if necessary.
        """
        try:
            if len(self.spectrum_wavelength) > 1 and self.spectrum_wavelength[0] > self.spectrum_wavelength[1]:
                self.spectrum_wavelength = np.flip(self.spectrum_wavelength)
                self.spectrum_intensity = np.flip(self.spectrum_intensity)
                self.revers_order_spectrum = True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:spectrum_change_order: {str(e)}") from e

    # destination
    def get_destination_from_file(self):
        """
            Reads destination data from a file and sets up corresponding parameters.

            The function attempts to read destination data from a specified file using a DataPars object.
            It then parses the file, extracts specific column data, and sets the appropriate
            attributes before performing final setup.

        :return: None
        	The function returns nothing, but sets various attributes related to destination data.
        """
        try:
            self.destination_quantity = 0
            destination_read = DataPars(self.destination_file_path, self.parent_window)
            destination_read.file_pars_f()
            if not is_array_empty(destination_read.file_garbage):
                self.destination_garbage = True
            self.destination_wavelength = extract_one_column_from_data(destination_read.file_body, self.destination_wavelength_column)
            self.destination_final_set_up()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:get_destination_from_file: {str(e)}") from e

    def get_destination_as_linear_function(self):
        """
            Reads and processes destination data using linear extrapolation.

            This function computes the destination wavelength using a linear extrapolation
            based on the start, stop, and step values, and then sets up the final destination parameters.

        :return: None
            The function return nothing, but creates changes in the destination dat.
        """
        try:
            self.destination_quantity = 0
            self.destination_wavelength = linear_extrapolation(self.destination_wavelength_start,
                                                               self.destination_wavelength_stop,
                                                               self.destination_wavelength_step)
            if self.destination_wavelength_start + int((self.destination_wavelength_stop - self.destination_wavelength_start) / self.destination_wavelength_step) * self.destination_wavelength_step != self.destination_wavelength_stop:
                self.linear_destination_warning = True  # indicates that the step is not within the interval start-stop an integer number of times
                self.last_destination_value = self.destination_wavelength_start + int((self.destination_wavelength_stop - self.destination_wavelength_start) / self.destination_wavelength_step) * self.destination_wavelength_step
            self.destination_final_set_up()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:get_destination_as_linear_function: {str(e)}") from e

    def destination_final_set_up(self):
        """
            Final setup for destination parameters adjusting spectrum and convolution settings.

            The function sets the destination quantity based on the length of the destination wavelength.
            If the spectrum setup flag is true and its current unit does not match the destination unit,
            it changes the spectrum unit and order. It then deep copies the original spectrum wavelength and intensity.
            Additionally, it changes the order of the destination and possibly the convolution settings if required.

        :return: None
            The function returns nothing, but it updates setup flags and the destination data and adjusts spectrum and convolution properties.
        """
        try:
            self.destination_change_order()
            self.destination_quantity = len(self.destination_wavelength)  # needed to calculate linear or constant convolution width(s)
            if self.spectrum_set_up and self.spectrum_unit_current != self.destination_unit:
                self.spectrum_unit_change()
                self.spectrum_change_order()
                self.spectrum_wavelength_original = copy.deepcopy(self.spectrum_wavelength)
                self.spectrum_intensity_original = copy.deepcopy(self.spectrum_intensity)
            if self.convolution_set_up:
                self.convolution_change_order()
            self.destination_set_up = True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:destination_final_set_up: {str(e)}") from e

    def destination_change_order(self):
        """
            Ensure the destination wavelength array is in ascending order and set a flag if the order is reversed.

            If the destination wavelength array is not in ascending order, it reverses the array and sets a flag indicating the order was reversed.

        :return: None
            The function returns nothing, but may modify destination_wavelength and revers_order_destination attributes.
        """
        try:
            if len(self.destination_wavelength) > 1 and self.destination_wavelength[1] - self.destination_wavelength[0] < 0:
                self.destination_wavelength = np.flip(self.destination_wavelength)
                self.revers_order_destination = True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:destination_change_order: {str(e)}") from e

    # convolution width
    def get_convolution_width_from_file(self):
        """
            Fetches and processes convolution width data from a file.

            This function reads convolution width data from a specified file path, extracts designated columns,
            and sets up the final convolution parameters.

        :return: None
            The function returns nothing, but modifies self.convolution_width_1, self.convolution_width_2,
            and performs the final convolution setup.
        """
        try:
            convolution_read = DataPars(self.convolution_file_path, self.parent_window)
            convolution_read.file_pars_f()
            if not is_array_empty(convolution_read.file_garbage):
                self.convolution_width_garbage = True
            self.convolution_width_1 = extract_one_column_from_data(convolution_read.file_body, self.convolution_width_1_column)
            if self.convolution_type in [2, 4, 5]:  # trapeze, Voigt, Gauss+Lorentz (+ potentially other functions with the second width)
                self.convolution_width_2 = extract_one_column_from_data(convolution_read.file_body, self.convolution_width_2_column)
            self.convolution_final_set_up()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:get_convolution_width_from_file: {str(e)}") from e

    def get_convolution_width_as_linear_function(self):
        """
            Calculate convolution widths using linear extrapolation and set them up accordingly.

            This function determines the convolution widths based on a linear extrapolation
            from initial to final values over a specified quantity range. It supports different
            convolution types and sets up the computed widths for further processing.

        :return: None
            The function returns nothing, but computes and sets up convolution widths.
        """
        try:
            self.convolution_width_1 = linear_extrapolation(self.convolution_width_1_start, self.convolution_width_1_stop, 0, self.destination_quantity)
            if self.convolution_type in [2, 4, 5]:  # trapeze, Voigt, Gauss+Lorentz (and other functions with the second width if added later)
                self.convolution_width_2 = linear_extrapolation(self.convolution_width_2_start, self.convolution_width_2_stop, 0, self.destination_quantity)
            self.convolution_final_set_up()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:get_convolution_width_as_linear_function: {str(e)}") from e

    def get_convolution_width_as_constant(self):
        """
            Compute the convolution width as a constant and finalize the setup.

            This method computes the convolution width(s) using a constant extrapolation method
            and finalizes the convolution setup. If the convolution type is of specific types,
            an additional width computation is done.

        :return: None
        	The function return nothing, but creates changes in convolution width data.
        """
        try:
            self.convolution_width_1 = const_extrapolation(self.convolution_width_1_const, self.destination_quantity)
            if self.convolution_type in [2, 4, 5]:  # trapeze, Voigt, Gauss+Lorentz (and other functions with the second width if added later)
                self.convolution_width_2 = const_extrapolation(self.convolution_width_2_const, self.destination_quantity)
            self.convolution_final_set_up()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:get_convolution_width_as_constant: {str(e)}") from e

    def convolution_final_set_up(self):
        """
            Finalizes the setup process for convolution by adjusting the order if necessary.

            This method checks if the destination setup is complete, and if so, it
            changes the order of the convolution. It then marks the convolution setup
            as complete.

        :return: None
            The function returns nothing, but sets up and marks the convolution set up as complete.
        """
        try:
            if self.destination_set_up:
                self.convolution_change_order()
            self.convolution_set_up = True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_final_set_up: {str(e)}") from e

    def convolution_change_order(self):
        """
            Change the order of convolution arrays if the reverse order destination flag is set.

            This function checks if the `revers_order_destination` flag is set and, if so, reverses
            the order of the convolution width arrays `convolution_width_1` and `convolution_width_2`.

        :return: None
            The function returns nothing, but modifies convolution_width_1 and convolution_width_2 if the condition is met.
        """
        try:
            if self.revers_order_destination:
                self.convolution_width_1 = np.flip(self.convolution_width_1)
                self.convolution_width_2 = np.flip(self.convolution_width_2)
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_change_order: {str(e)}") from e

    # MAIN CLASS FUNCTION
    def convolution_stack(self):
        """
            Performs a series of checks and calculations to execute a convolution stack.

            This method verifies the presence of all required inputs, ensures their correctness,
            checks the applicability of a convolution operation, and then performs extrapolation
            if needed. Finally, it carries out the convolution calculation.

            Note: This function is specific to the core. When creating an application with an interface,
            it should be used as a basis.

        :return: None
        """
        try:
            # verification: all inputs are here
            if self.verification_all_inputs_are_here():
                # verification: all inputs are correct (= usable)
                if self.verification_all_inputs_correct():
                    # verification: convolution applicability
                    if self.convolution_applicability():
                        # extrapolation (if needed)
                        self.extrapolation()
                        # calc
                        self.convolution_calc()
                        self.convolution_is_calculated = True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_stack: {str(e)}") from e

    # VERIFICATIONS
    @staticmethod
    def conditions_checker(conditions):
        """
            Checks a set of conditions and provides warnings if necessary.

            Iterates through a dictionary of conditions, evaluates each condition,
            and prints a warning message if the condition is met. If any condition
            is met, it returns False; otherwise, it returns True.

        :param conditions: dict
            Dictionary containing condition names as keys and a dictionary
            with 'condition' (a boolean to evaluate) and 'warning' (message
            to print if condition is met) as values.
        :return: bool
            Returns True if no condition is met, otherwise returns False.
        """
        try:
            for name, value in conditions.items():
                if value["condition"]:
                    print("\n" + value["warning"])
                    return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:conditions_checker: {str(e)}") from e

    def verification_all_inputs_are_here(self):
        """
            Verifies that all necessary inputs are present.

            This function performs a series of checks to ensure that all required inputs for the convolution
            process are available. It calls three internal verification methods for spectrum, destination,
            and convolution, and only returns True if all verifications pass successfully. In case of any
            failure during these checks, it will return False.

            This function is peculiar only to core code. If you have an interface, you will need to write your
            own function that checks if the input data is provided and points out possible errors to the user.
            However, this code can be used as a basis, since the interface must contain elements that serve as
            a data source for the core code.

            Note: in main.py, the analogue of this function is all_inputs_here.

        :return: bool
            True if all inputs are verified and present; False otherwise.
        """
        try:
            if not self.verification_all_inputs_are_here_spectrum():
                return False
            if not self.verification_all_inputs_are_here_destination():
                return False
            if not self.verification_all_inputs_are_here_convolution():
                return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:verification_all_inputs_are_here: {str(e)}") from e

    def verification_all_inputs_are_here_spectrum(self):
        """
            Checks the existence of all required spectrum inputs.

            This function verifies that all necessary spectrum inputs are present. It checks paths, units,
            separators, column indices, and arrays for proper types and values. If any condition fails, the function returns False.

        :return: bool
        	True if all conditions are met and inputs are valid; otherwise, False.
        """
        try:
            conditions = {
                "spectrum_file_path": {
                    "condition": type(self.spectrum_file_path) != str or self.spectrum_file_path == "",
                    "warning": "No spectrum file path is provided!",
                },
                "spectrum_unit_original": {
                    "condition": type(self.spectrum_unit_original) != str or self.spectrum_unit_original == "",
                    "warning": "No spectrum unit is given!",
                },
                "spectrum_unit_current": {
                    "condition": type(self.spectrum_unit_current) != str or self.spectrum_unit_current == "",
                    "warning": "No spectrum unit is found!",
                },
                "spectrum_separator": {
                    "condition": type(self.spectrum_separator) != str or self.spectrum_separator == "",
                    "warning": "No spectrum file separator is found!",
                },
                "spectrum_wavelength_column": {
                    "condition": type(self.spectrum_wavelength_column) != int,
                    "warning": "No spectrum wavelength column is given!",
                },
                "spectrum_intensity_column": {
                    "condition": type(self.spectrum_intensity_column) != int,
                    "warning": "No spectrum intensity column is given!",
                },
                "spectrum_wavelength": {
                    "condition": is_array_empty(self.spectrum_wavelength),
                    "warning": "No spectrum wavelength is found!",
                },
                "spectrum_intensity": {
                    "condition": is_array_empty(self.spectrum_intensity),
                    "warning": "No spectrum intensity is found!",
                },
                "spectrum_set_up": {
                    "condition": self.spectrum_set_up == False,
                    "warning": "No initial spectrum is provided!",
                },
            }
            if not self.conditions_checker(conditions):
                return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:verification_all_inputs_are_here_spectrum: {str(e)}") from e

    def verification_all_inputs_are_here_destination(self):
        """
            Verifies that all necessary inputs for the destination are present.

            This function checks a comprehensive list of conditions to ensure that all required
            parameters for the destination are correctly specified. If any condition is not met,
            an appropriate warning message is printed and the function returns False.

        :return: bool
        	True if all required inputs are present and valid, otherwise False.
        """
        try:
            # common verifications
            conditions = {
                "destination_unit": {
                    "condition": type(self.destination_unit) != str or self.destination_unit == "",
                    "warning": "No destination unit is given!",
                },
                "destination_wavelength": {
                    "condition": is_array_empty(self.destination_wavelength),
                    "warning": "No destination wavelength is provided!",
                },
                "destination_set_up": {
                    "condition": self.destination_set_up == False,
                    "warning": "No destination spectrum is provided!",
                },
                "destination_quantity": {
                    "condition": self.destination_quantity == 0,
                    "warning": "No destination wavelength is found!",
                },
            }
            if not self.conditions_checker(conditions):
                return False
            # sources verification
            if self.destination_input_type == 0:  # no source found
                print("\nA source must be specified (file or linear function) for the destination!")
                return False
            if self.destination_input_type == 1:  # file source
                conditions = {
                    "destination_file_path": {
                        "condition": type(self.destination_file_path) != str or self.destination_file_path == "",
                        "warning": "No destination file is found!",
                    },
                    "destination_wavelength_column": {
                        "condition": type(self.destination_wavelength_column) != int,
                        "warning": "No destination wavelength column is given!",
                    },
                }
                if not self.conditions_checker(conditions):
                    return False
            elif self.destination_input_type == 2:  # linear function source
                conditions = {
                    "destination_wavelength_start": {
                        "condition": type(self.destination_wavelength_start) not in [int, float],
                        "warning": "No destination wavelength start value is given!",
                    },
                    "destination_wavelength_stop": {
                        "condition": type(self.destination_wavelength_stop) not in [int, float],
                        "warning": "No correct destination wavelength end value is given!",
                    },
                    "destination_wavelength_step": {
                        "condition": type(self.destination_wavelength_step) not in [int, float] or self.destination_wavelength_step == 0,
                        "warning": "No correct destination wavelength step value is given!",
                    },
                }
                if not self.conditions_checker(conditions):
                    return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:verification_all_inputs_are_here_destination: {str(e)}") from e

    def verification_all_inputs_are_here_convolution(self):
        """
            Verifies that all necessary convolution parameters are provided and correctly formatted.

            The function checks multiple conditions to ensure that all convolution parameters are provided and correctly formatted.
            It performs common checks and source-specific checks based on the convolution input type.

        :return: bool
        	Returns True if all inputs are correctly provided and formatted,
        	otherwise returns False.
        """
        try:
            # common verifications
            conditions = {
                "convolution_type": {
                    "condition": type(self.convolution_type) != int,
                    "warning": "No convolution type is given!",
                },
                "convolution_gauss_ratio": {
                    "condition": type(self.convolution_gauss_ratio) not in [int, float],
                    "warning": "No correct Gauss ratio value is given!",
                },
                "convolution_truncation": {
                    "condition": type(self.convolution_truncation) not in [int, float],
                    "warning": "No correct truncation value is given!",
                },
                "convolution_extrapolation_type": {
                    "condition": type(self.convolution_extrapolation_type) != int,
                    "warning": "No correct extrapolation type is given!",
                },
                "convolution_width_1": {
                    "condition": is_array_empty(self.convolution_width_1),
                    "warning": "No width is found!",
                },
                "convolution_width_2": {
                    "condition": self.convolution_type in [2, 4, 5] and is_array_empty(self.convolution_width_1),
                    "warning": "No top/second width is found!",
                },
                "convolution_set_up": {
                    "condition": self.convolution_set_up == False,
                    "warning": "No width(s) is provided!",
                },
            }
            if not self.conditions_checker(conditions):
                return False
            # sources verification
            if self.convolution_input_type == 0:  # no source found
                print("\nA source must be specified (file, linear, or constant) for the convolution width(s).")
                return False
            if self.convolution_input_type == 1:  # file source verifications
                conditions = {
                    "convolution_file_path": {
                        "condition": type(self.convolution_file_path) != str or self.convolution_file_path == "",
                        "warning": "No convolution width(s) file is found!",
                    },
                    "convolution_width_1_column": {
                        "condition": type(self.convolution_width_1_column) != int,
                        "warning": "No convolution width column is given!",
                    },
                    "convolution_width_2_column": {
                        "condition": self.convolution_type in [2, 4, 5] and type(self.convolution_width_2_column) != int,
                        "warning": "No second convolution width column is given!",
                    },
                }
                if not self.conditions_checker(conditions):
                    return False
            elif self.convolution_input_type == 2:  # linear source verifications
                conditions = {
                    "convolution_width_1_start": {
                        "condition": type(self.convolution_width_1_start) not in [int, float],
                        "warning": "No convolution width start value is given!",
                    },
                    "convolution_width_1_stop": {
                        "condition": type(self.convolution_width_1_stop) not in [int, float],
                        "warning": "No convolution width end value is given!",
                    },
                    "convolution_width_2_start": {
                        "condition": self.convolution_type in [2, 4, 5] and type(self.convolution_width_2_start) not in [int, float],
                        "warning": "No second convolution width start value is given!",
                    },
                    "convolution_width_2_stop": {
                        "condition": self.convolution_type in [2, 4, 5] and type(self.convolution_width_2_stop) not in [int, float],
                        "warning": "No second convolution width end value is given",
                    },
                }
                if not self.conditions_checker(conditions):
                    return False
            elif self.convolution_input_type == 3:  # constante source verifications
                conditions = {
                    "convolution_width_1_const": {
                        "condition": type(self.convolution_width_1_const) not in [int, float],
                        "warning": "No convolution width constant value is given!",
                    },
                    "convolution_width_2_const": {
                        "condition": self.convolution_type in [2, 4, 5] and type(self.convolution_width_1_const) not in [int, float],
                        "warning": "No second convolution width constant value is given!",
                    },
                }
                if not self.conditions_checker(conditions):
                    return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:verification_all_inputs_are_here_convolution: {str(e)}") from e

    def verification_all_inputs_correct(self):
        """
            Checks if all input verifications are correct.

            This method verifies the correctness of all input parameters required
            for the ConvolutionCore process by sequentially calling specific
            verification methods. If any verification fails, it returns False.

            The verification_all_inputs_are_here function is unique to the core code.
            If you are developing an interface, you will need to create a custom function
            to verify that all required input data is correct and to notify the user of
            any errors. However, you can use this code as a reference.

            Note: in main.py, the analogue of this function is all_inputs_correct.

        :return: bool
            True if all input verifications are correct, otherwise False.
        """
        try:
            if not self.verification_all_inputs_correct_spectrum():
                return False
            if not self.verification_all_inputs_correct_destination():
                return False
            if not self.verification_all_inputs_correct_convolution():
                return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:verification_all_inputs_correct: {str(e)}") from e

    def verification_all_inputs_correct_spectrum(self):
        """
            Verify the correctness of all input parameters related to the spectrum.

            This function checks if the provided spectrum file exists, if the spectrum wavelength unit is valid,
            and if the spectrum wavelength and intensity columns are proper integers and greater than or equal to 0.

        :return: bool
        	Returns True if all input conditions are met, otherwise prints a warning and returns False.
        """
        try:
            conditions = {
                "spectrum_file_path": {
                    "condition": not os.path.exists(self.spectrum_file_path),
                    "warning": "Provided spectrum file doesn't exist!",
                },
                "spectrum_unit_original": {
                    "condition": self.spectrum_unit_original not in ["cm-1", "micron", "nm", "A"],
                    "warning": "Spectrum wavelength unit must be cm-1, micron, nm or A!",
                },
                "spectrum_wavelength_column": {
                    "condition": self.spectrum_wavelength_column < 0,
                    "warning": "Spectrum wavelength column must be integer and grater than or equal to 0!",
                },
                "spectrum_intensity_column": {
                    "condition": self.spectrum_intensity_column < 0,
                    "warning": "Spectrum intensity column must be integer and grater than or equal to 0!",
                },
                "spectrum_width": {
                    "condition": os.path.exists(self.spectrum_width_path) and len(self.spectrum_wavelength) != len(self.spectrum_width),
                    "warning": "Spectrum width array length doesn't match the spectrum wavelength array length!",
                },
                "spectrum_garbage": {
                    "condition": self.spectrum_garbage,
                    "warning": "The spectrum data block contains text or NaN or has an invalid format or a format that this algorithm cannot parse. Some data can be lost.",
                },
                "spectrum_width_garbage": {
                    "condition": self.spectrum_width_garbage,
                    "warning": "The spectrum width data block contains text or NaN or has an invalid format or a format that this algorithm cannot parse. Some data can be lost.",
                },
            }
            if not self.conditions_checker(conditions):
                return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:verification_all_inputs_correct_spectrum: {str(e)}") from e

    def verification_all_inputs_correct_destination(self):
        """
            Checks the validity of all input parameters for the destination.

            This function performs several validations to ensure that input parameters related to the destination
            are correctly configured. Depending on the type of input (file or linear), different sets of conditions are checked.

        :return: bool
        	True if all conditions pass, False otherwise.
        """
        try:
            # common conditions
            conditions = {
                "destination_unit": {
                    "condition": self.destination_unit not in ["cm-1", "micron", "nm", "A"],
                    "warning": "Destination wavelength unit must be cm-1, micron, nm or A!"
                },
            }
            if not self.conditions_checker(conditions):
                return False
            # source verifications
            if self.destination_input_type == 1:  # file source
                conditions = {
                    "destination_file_path": {
                        "condition": not os.path.exists(self.destination_file_path),
                        "warning": "Provided destination file doesn't exist!",
                    },
                    "destination_wavelength_column": {
                        "condition": self.destination_wavelength_column < 0,
                        "warning": "Destination wavelength column must be integer and grater or equal to 0!"
                    },
                    "destination_garbage": {
                        "condition": self.destination_garbage,
                        "warning": "The destination data block contains text or NaN or has an invalid format or a format that this algorithm cannot parse. Some data can be lost.",
                    },
                }
                if not self.conditions_checker(conditions):
                    return False
            elif self.destination_input_type == 2:  # linear function source
                conditions = {
                    "destination_wavelength_step": {
                        "condition": self.destination_wavelength_step > np.fabs(self.destination_wavelength_stop - self.destination_wavelength_start),
                        "warning": "Destination wavelength step is too big!",
                    },
                }
                if not self.conditions_checker(conditions):
                    return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:verification_all_inputs_correct_destination: {str(e)}") from e

    def verification_all_inputs_correct_convolution(self):
        """
        	Checks if all convolution input conditions are met.

        	This function verifies various conditions to validate the inputs
        	related to convolution operations. Checks include convolution type,
        	gaussian ratio, truncation, extrapolation type, and conditions specific
        	to file inputs and widths.

        :return: bool
            Returns True if all input conditions are met. Prints warnings and returns False otherwise.
        """
        try:
            # common conditions
            conditions = {
                "convolution_type": {
                    "condition": self.convolution_type not in [0, 1, 2, 3, 4, 5],
                    "warning": "Convolution type must be 0, 1, 2, 3, 4, or 5!",
                },
                "convolution_gauss_ratio": {
                    "condition": self.convolution_gauss_ratio < 0 or self.convolution_gauss_ratio > 1,
                    "warning": "Gauss ration must be between 0 and 1!",
                },
                "convolution_truncation": {
                    "condition": self.convolution_truncation <= 0,
                    "warning": "Convolution truncation must be positive!",
                },
                "convolution_extrapolation_type": {
                    "condition": self.convolution_extrapolation_type not in [0, 1, 2, 3],
                    "warning": "Extrapolation type must be 0, 1, 2, or 3!",
                },
            }
            if not self.conditions_checker(conditions):
                return False
            # file input verification
            if self.convolution_input_type == 1:
                conditions = {
                    "convolution_file_path": {
                        "condition": not os.path.exists(self.convolution_file_path),
                        "warning": "Provided convolution file doesn't exist!",
                    },
                    "convolution_width_1_column": {
                        "condition": self.convolution_width_1_column < 0,
                        "warning": "Convolution width column must be integer and grater or equal to 0!",
                    },
                    "convolution_width_2_column": {
                        "condition": self.convolution_type in [2, 4, 5] and self.convolution_width_2_column < 0,
                        "warning": "Second convolution width column must be integer and grater or equal to 0!",
                    },
                    "convolution_garbage": {
                        "condition": self.convolution_width_garbage,
                        "warning": "The convolution width(s) data block contains text or NaN or has an invalid format or a format that this algorithm cannot parse. Some data can be lost.",
                    },
                }
                if not self.conditions_checker(conditions):
                    return False
            # destination wavelength size must be = convolution width size
            if len(self.destination_wavelength) != len(self.convolution_width_1):
                print("\nDestination wavelength and convolution width have different sizes!")
                return False
            # width must be >= top
            if self.convolution_type == 2:
                for i in range(len(self.convolution_width_1)):
                    if self.convolution_width_1[i] < self.convolution_width_2[i]:
                        print("\nThe width must be greater than or equal to the top!")
                        return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:verification_all_inputs_correct_convolution: {str(e)}") from e

    # CONVOLUTION APPLICABILITY
    def convolution_applicability(self):
        """
        	Determines the applicability of convolution based on various conditions.

        	This method evaluates multiple conditions to ensure the convolution process can be applied correctly.
        	If any condition fails, the user is prompted whether to proceed despite the failure.
        	Main checks include step interval, width and resolution conditions of the destination spectrum,
        	and adherence to the truncation and width conditions.

        	Note: This function is specific to core. When creating an interface, it should be used as a base.
        	Its analogue in main.py is convolution_applicability_and_extrapolation (which also contains extrapolation).

        	:return: bool
        		True if convolution conditions are met or the user decides to proceed despite warnings, False otherwise.
        """
        try:
            if not self.tests_are_running:
                # linear destination warning
                if self.linear_destination_warning:
                    print("\nWith the given start and end values for the destination, the step value is not included in the start-end interval an integer number of times.\n"
                          "Therefore, the interval will be shortened to contain the integer number of steps.\n"
                          f"The last destination wavelength value is {self.last_destination_value}{self.destination_unit}.")
                    reply = input("Calculate it this way? (y/n): ")
                    if reply != "y":
                        return False
                # width > 2 * step
                if not self.convolution_width_and_destination_step_verification():
                    print("\nOne of conditions for the applicability of convolution is not fulfilled.\n"
                          "The sampling step of the destination spectrum did not satisfy the sampling condition (step ~ 0.5 resolution (FWHM)) to garant high photometric accuracy.")
                    reply = input("Calculate it anyway? (y/n): ")
                    if reply != "y":
                        return False
                # T > n * width
                if not self.truncation_and_width_condition():
                    n = self.n_truncation_values[self.convolution_type]
                    print("\nOne of conditions for the applicability of convolution is not fulfilled."
                          "\nThe current truncation of the convolution function did not garant high photometric accuracy.\n"
                          f"It must be greater than {n} times the resolution (FWHM).")
                    reply = input("Calculate it anyway? (y/n): ")
                    if reply != "y":
                        return False
                # width_d > width_s
                if not is_array_empty(self.spectrum_width):
                    str_interval, len_interval_array = self.width_condition()
                    if str_interval:
                        print("\nOne of conditions for the applicability of convolution is not fulfilled.\n"
                              "The resolution of the destination spectrum is higher (lower FWHM) than that of the original data, at least over part of the spectrum:\n"
                              f"{str_interval} {self.spectrum_unit_original}.\n"
                              f"Spurious results may occurs in {'this range' if len_interval_array == 2 else 'these ranges'}.")
                        reply = input("Calculate it anyway? (y/n): ")
                        if reply != "y":
                            return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_applicability: {str(e)}") from e

    def convolution_width_and_destination_step_verification(self):
        """
            Verifies if the convolution width satisfies the specified conditions against destination wavelengths.

            This function iteratively checks if each convolution width value is greater than or equal to the difference between
            the destination wavelengths at adjacent indices. If the condition fails for any width, the function returns False;
            otherwise, it returns True upon successful verification for all widths.

        :return: bool
            True if all convolution width values satisfy the condition; False otherwise.
        """
        try:
            for i in range(1, len(self.convolution_width_1) - 1):
                if self.convolution_width_1[i] < self.destination_wavelength[i + 1] - self.destination_wavelength[i - 1]:
                    return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_width_and_destination_step_verification: {str(e)}") from e

    def truncation_and_width_condition(self):
        """
            Determines if the truncation condition based on width is satisfied.

            This function checks whether the current truncation value is greater than or
            equal to the product of specific width values and a truncation constant for
            the given convolution type. If any of the conditions are not met, it returns False.

        :return: bool
            Returns True if all truncation conditions are met, otherwise False.
        """
        try:
            n = self.n_truncation_values[self.convolution_type]
            for i in range(0, len(self.convolution_width_1)):
                if self.convolution_truncation < n * self.convolution_width_1[i]:
                    return False
            return True
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:truncation_and_width_condition: {str(e)}") from e

    def width_condition(self):
        """
            Checks the width condition between the spectrum and convolution and returns the interval.

            First, the function calculates the width of the spectrum at the specified wavelengths.
            It then searches for intervals where the spectrum width exceeds the convolution width.
            Finally, it formats these intervals into a string and returns it along with the count of intervals.

        :return: tuple(str, int)
            A string representation of the intervals where the spectrum width exceeds the convolution width, and the length of the interval array.
        """
        # width_destination >= width_spectrum
        try:
            # set up
            spectrum_width = width_cut_off(self.spectrum_width, self.spectrum_wavelength, self.destination_wavelength)
            interval_array = []
            interval_started = False
            interval_ended = True
            # interval search
            for i in range(len(self.destination_wavelength)):
                if spectrum_width[i] > self.convolution_width_1[i] and interval_ended and not interval_started:
                    interval_started, interval_ended = True, False
                    interval_array.append(self.destination_wavelength[i])
                if spectrum_width[i] <= self.convolution_width_1[i] and interval_started and not interval_ended:
                    interval_started, interval_ended = False, True
                    interval_array.append(self.destination_wavelength[i])
            # str creation
            intervals = [(f"{units_conversion(interval_array[i], self.destination_unit, self.destination_unit)} - "
                          f"{units_conversion(interval_array[i + 1], self.destination_unit, self.destination_unit)}")
                        for i in range(0, len(interval_array), 2)]
            str_interval = ", ".join(intervals)
            return str_interval, len(interval_array)
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:width_condition: {str(e)}") from e

    # SPECTRUM EXTRAPOLATION
    def extrapolation(self):
        """
            Performs a verification and potential extrapolation of the original spectrum.

            This function checks if the spectrum's wavelength is within bounds and, if not, prompts the user for extrapolation.
            If tests are running, it automatically performs the extrapolation.

        :return: None
        	The function returns nothing, but may modify the spectrum through extrapolation.
        """
        try:
            if not self.tests_are_running:
                check_result = self.spectrum_wavelength_bounds_check()
                if check_result:
                    print("\nIt has been discovered that:")
                    for error_message in check_result:
                        print("\n" + error_message)
                    reply = input("Would you like to extrapolate the original spectrum to the required range? (y/n): ")
                    if reply == "y":
                        self.spectrum_extrapolation()
            else:
                self.spectrum_extrapolation()
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:extrapolation: {str(e)}") from e

    def spectrum_wavelength_bounds_check(self):
        """
            Checks if the spectrum wavelength bounds are within acceptable limits.

            This function computes the minimum and maximum wavelength bounds based on the convolution settings
            and checks if the spectrum wavelength falls within these bounds. If the spectrum wavelength
            is out of bounds, appropriate error messages are generated and returned.

        :return: list of str
        	List of error messages if there are any wavelength bound lack.
        """
        error_message = []
        try:
            # compute wavelength bounds
            wlth_min, wlth_max = self.get_spectrum_bounds()
            # error message
            if self.spectrum_wavelength[0] > wlth_min:
                error_message.append(f"Spectrum wavelength is too short at its {'minimum' if not self.revers_order_spectrum else 'maximum'}. "
                                     f"Recommended value is {'lesser' if not self.revers_order_spectrum else 'grater'} than {units_conversion(wlth_min, self.spectrum_unit_current, self.spectrum_unit_original)} {self.spectrum_unit_original}.")
            if self.spectrum_wavelength[-1] < wlth_max:
                error_message.append(f"Spectrum wavelength is too short at its {'maximum' if not self.revers_order_spectrum else 'minimum'}. "
                                     f"Recommended value is {'grater' if not self.revers_order_spectrum else 'lesser'} than {units_conversion(wlth_max, self.spectrum_unit_current, self.spectrum_unit_original)} {self.spectrum_unit_original}.")
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:spectrum_wavelength_bounds_check: {str(e)}") from e
        return error_message

    def get_spectrum_bounds(self):
        """
            Calculates the minimum and maximum wavelength bounds for the spectrum.

            The function computes the bounds for the spectrum based on the convolution type and
            its associated parameters.

        :return: tuple(float, float)
            Computed minimum and maximum wavelength bounds.
        """
        try:
            wlth_min, wlth_max = 0, 0
            if self.convolution_type not in [2, 4, 5]:
                wlth_min = self.destination_wavelength[0] - self.convolution_truncation * self.convolution_width_1[0]
                wlth_max = self.destination_wavelength[-1] + self.convolution_truncation * self.convolution_width_1[-1]
            elif self.convolution_type == 2:  # "trapeze"
                wlth_min = self.destination_wavelength[0] - self.convolution_truncation * self.convolution_width_1[0] - self.convolution_width_2[0]
                wlth_max = self.destination_wavelength[-1] + self.convolution_truncation * self.convolution_width_1[-1] + self.convolution_width_2[-1]
            elif self.convolution_type in [4, 5]:  # "Voigt", "Gauss+Lorentz"
                wlth_min = self.destination_wavelength[0] - self.convolution_truncation * (self.convolution_width_1[0] + self.convolution_width_2[0])
                wlth_max = self.destination_wavelength[-1] + self.convolution_truncation * (self.convolution_width_1[-1] + self.convolution_width_2[-1])
            return wlth_min, wlth_max
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:get_spectrum_bounds: {str(e)}") from e

    def spectrum_extrapolation(self):
        """
            Adjusts the wavelength boundaries and recalculates the corresponding intensity values to perform spectrum extrapolation.

            This function aims to extrapolate the spectrum data by modifying its boundaries
            to match a specified range. It performs different extrapolation steps for the
            beginning, middle, and end parts of the spectrum. Once the wavelength boundaries
            are identified, it proceeds to extrapolate the intensity.

        :return: None
            This function returns nothing but modifies the spectrum wavelength and
            intensity through the extrapolation process.
        """
        try:
            self.spectrum_wavelength = copy.deepcopy(self.spectrum_wavelength_original)
            wlth_min, wlth_max = self.get_spectrum_bounds()
            if self.spectrum_wavelength[0] > wlth_min or self.spectrum_wavelength[-1] < wlth_max:
                step = self.spectrum_wavelength[1] - self.spectrum_wavelength[0]
                # before
                x_list = self.extrapolation_process_before(wlth_min, step)
                qty_before = len(x_list)
                # middle
                x_list = self.extrapolation_process_middle(x_list, qty_before)
                # after
                temp = self.extrapolation_process_after(wlth_max, step)
                qty_after = len(temp) if temp is not None else 0
                x_list = self.combine_results(x_list, temp)
                # finalization
                self.finalize_extrapolation(x_list, qty_before, qty_after)
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:spectrum_extrapolation: {str(e)}") from e

    def extrapolation_process_before(self, wlth_min, step):
        """
            Performs extrapolation process before the minimum wavelength.

            This function attempts to perform a linear extrapolation process below the
            minimum wavelength value found in the spectrum data.

        :param wlth_min: float
        	Defines the minimum wavelength value for extrapolation.
        :param step: float
        	Defines the step size used to generate the extrapolation range.

        :return: numpy.ndarray
        	Returns an array containing the extrapolated values. If the minimum
        	wavelength in the spectrum is greater than wlth_min, a linear extrapolation
        	array is returned. Otherwise, an empty array of zeros is returned.
        """
        try:
            if np.amin(self.spectrum_wavelength) > wlth_min:
                return linear_extrapolation(wlth_min, np.amin(self.spectrum_wavelength) - step, step)
            return np.zeros(0)
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:extrapolation_process_before: {str(e)}") from e

    def extrapolation_process_middle(self, x_list, qty_before):
        """
            Performs an extrapolation process by resizing and populating x_list with spectrum wavelengths.

            This function adjusts the size of x_list to accommodate additional spectrum wavelengths
            from the spectrum_wavelength, and then populates the resized portion with these wavelengths.

        :param x_list: list of float
            The input list that will be resized and populated with additional spectrum wavelengths.
        :param qty_before: int
            The starting index where the spectrum wavelengths will be inserted in the resized x_list.

        :return: list of float
            The modified `x_list` containing the original values and the appended spectrum wavelengths.
        """
        try:
            x_list = np.resize(x_list, len(x_list) + len(self.spectrum_wavelength))
            for i in range(len(self.spectrum_wavelength)):
                x_list[qty_before + i] = self.spectrum_wavelength[i]
            return x_list
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:extrapolation_process_middle: {str(e)}") from e

    def extrapolation_process_after(self, wlth_max, step):
        """
            Computes linear extrapolation on the spectrum wavelength if
            the maximum wavelength is less than the specified value.

            This function checks if the maximum value in self.spectrum_wavelength
            is less than `wlth_max`. If true, it performs linear
            extrapolation from the maximum value plus the step size up to wlth_max.

        :param wlth_max: float
        	The maximum wavelength limit for the extrapolation process.
        :param step: float
        	The step size for intervals of extrapolation.

        :return: np.ndarray
        	The extrapolated wavelengths if extrapolation is performed.
        """
        try:
            if np.amax(self.spectrum_wavelength) < wlth_max:
                return linear_extrapolation(np.amax(self.spectrum_wavelength) + step, wlth_max, step)
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:extrapolation_process_after: {str(e)}") from e

    @staticmethod
    def combine_results(x_list, additional_list):
        """
            Combines two lists for the before-middle extrapolation and the after extrapolation
            results, and updates a progress dialog during the process.

            This function resizes the x_list to accommodate the elements of the additional_list,
            then iterates through the additional_list to add its elements to the x_list.

        :param x_list: list
        	Main list to which elements of additional_list will be added.
        :param additional_list: list
        	Additional elements to be appended to x_list.

        :return: list
        	Combined list containing the original elements of x_list followed by elements of additional_list.
        """
        try:
            if additional_list is not None:
                mid_size = len(x_list)
                x_list = np.resize(x_list, len(x_list) + len(additional_list))
                for i in range(len(additional_list)):
                    x_list[mid_size + i] = additional_list[i]
            return x_list
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:combine_results: {str(e)}") from e

    def finalize_extrapolation(self, x_list, qty_before, qty_after):
        """
            Finalize the extrapolation process for spectral data.

            This function takes the given lists of wavelengths and quantity parameters to
            finalize the extrapolation of spectral intensity data. It uses a specified
            type of convolution for the extrapolation and updates the internal spectrum
            wavelength and intensity attributes accordingly.

        :param x_list: list
        	List of wavelength values.
        :param qty_before: float
        	Quantity parameter before the extrapolation range.
        :param qty_after: float
        	Quantity parameter after the extrapolation range.
        :return: None
        	The function return nothing, but modifies internal spectrum attributes.
        """
        try:
            self.spectrum_wavelength = x_list
            self.spectrum_intensity = y_extrapolation(self.spectrum_wavelength, self.spectrum_intensity_original, qty_before, qty_after, self.convolution_extrapolation_type)
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:finalize_extrapolation: {str(e)}") from e

    # main calc function
    def convolution_calc(self):
        """
            Compute the convolution for each destination wavelength.

            This function initializes an intensity array for the destination wavelengths and progresses through each
            wavelength to calculate and normalize a convolution function. The results are then updated in the intensity array.
            The function also manages a progress dialog and handles any exceptions that may occur during execution.

        :return: None
            The function returns nothing, but modifies self.destination_intensity with computed convolution values.
        """
        try:
            self.destination_intensity = np.zeros(len(self.destination_wavelength))
            progress = initialize_progress_dialog(self.parent_window, len(self.destination_wavelength))
            for i in range(len(self.destination_wavelength)):
                if not update_progress(self.parent_window, progress, i):
                    break
                # sigma_1 & 2
                sigma_1, sigma_2 = self.get_sigmas(i)
                # j_min & j_max in self.spectrum_wavelength
                j_min, j_max = self.get_wavelength_boundaries(sigma_1, sigma_2, i)
                # convolution function application
                truncated_convolution_function = self.convolution_profil_calc(i, j_min, j_max, sigma_1, sigma_2)
                # normalization
                normalized_convolution_function = self.normalization(truncated_convolution_function, j_min, j_max)
                del truncated_convolution_function
                # convolution
                self.convolution_finalization(i, normalized_convolution_function, j_min, j_max)
            self.calculate_area_under_curve()  # test purposes only
            finalize_progress(self.parent_window, progress, len(self.destination_wavelength))
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_calc: {str(e)}") from e

    def get_sigmas(self, i):
        """
            Retrieves the sigma values based on the specified convolution type and widths.

            This function calculates the sigma values (sigma_1 and sigma_2) using predefined sigma factors
            associated with different convolution types. It checks if a secondary convolution width is available,
            returning 0 if it is not.

        :param i: int
        	Index to access the convolution width arrays.
        :return: tuple
        	Two sigma values (sigma_1, sigma_2) calculated based on the convolution type and widths.
        """
        try:
            sigma_factors = {0: (2.3548, 1), # "Gauss function"
                             1: (2, 1), # "triangle"
                             2: (2, 2), # "trapeze"
                             3: (2, 1), # "Lorentz"
                             4: (2.3548, 2), # "Voigt"
                             5: (2.3548, 2), # "Gauss+Lorentz"
                             }
            sigma_1 = self.convolution_width_1[i]/sigma_factors[self.convolution_type][0]
            sigma_2 = 0 if is_array_empty(self.convolution_width_2) else self.convolution_width_2[i]/sigma_factors[self.convolution_type][1]
            return sigma_1, sigma_2
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:get_sigmas: {str(e)}") from e

    def get_wavelength_boundaries(self, sigma_1, sigma_2, i):
        """
        	Determine the wavelength boundaries for convolution based on the convolution type.

        	This function computes the indices of the minimum and maximum wavelengths to be considered in a convolution process.
        	It accounts for different convolution types including Gaussian, Triangle, Lorentz, Trapezoidal, Voigt, and Gaussian+Lorentz shapes.

        :param sigma_1: float
        	Sigma parameter.
        :param sigma_2: float
        	Additional sigma parameter for convolution; for trapeze, Voigt, or Gaussian+Lorentz cases.
        :param i: int
        	Index indicating which destination wavelength to use for boundary calculations.
        :return: tuple (j_min, j_max)
        	Two integers representing the minimum and maximum index boundaries within the spectrum wavelengths that should be considered for the convolution.
        """
        try:
            j_min = 0
            j_max = len(self.spectrum_wavelength) - 1
            if self.convolution_type not in [2, 4, 5]: # Gauss function, triangle, Lorentz function
                for j in range(len(self.spectrum_wavelength)):
                    if self.spectrum_wavelength[j] > self.destination_wavelength[i] - self.convolution_truncation * sigma_1 and j_min == 0:
                        j_min = j
                    if self.spectrum_wavelength[j] > self.destination_wavelength[i] + self.convolution_truncation * sigma_1 and j_max == len(self.spectrum_wavelength) - 1:
                        j_max = j
                        break
            elif self.convolution_type == 2:  # trapeze
                for j in range(len(self.spectrum_wavelength)):
                    if self.spectrum_wavelength[j] > self.destination_wavelength[i] - sigma_2 - self.convolution_truncation * sigma_1 and j_min == 0:
                        j_min = j
                    if self.spectrum_wavelength[j] > self.destination_wavelength[i] + sigma_2 + self.convolution_truncation * sigma_1 and j_max == len(self.spectrum_wavelength) - 1:
                        j_max = j
                        break
            elif self.convolution_type in [4, 5]:  # Voigt, Gauss+Lorentz
                for j in range(len(self.spectrum_wavelength)):
                    if self.spectrum_wavelength[j] > self.destination_wavelength[i] - self.convolution_truncation * (sigma_1 + sigma_2) and j_min == 0:
                        j_min = j
                    if self.spectrum_wavelength[j] > self.destination_wavelength[i] + self.convolution_truncation * (sigma_1 + sigma_2) and j_max == len(self.spectrum_wavelength) - 1:
                        j_max = j
                        break
            return j_min, j_max
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:get_wavelength_boundaries: {str(e)}") from e

    def convolution_profil_calc(self, i, j_min, j_max, sigma_1, sigma_2):
        """
            Performs convolution profile calculation for a given range and set of parameters.

            This function calculates a truncated convolution function over a specified range
            of indices using various convolution functions. The function used depends on the
            convolution_type attribute of the class.

        :param i: int
                The index in destination_wavelength used for the convolution calculation.
        :param j_min: int
                The starting index in spectrum_wavelength for the convolution.
        :param j_max: int
                The ending index in spectrum_wavelength for the convolution.
        :param sigma_1: float
                A parameter used in the convolution function, typically representing the
                standard deviation for Gaussian profiles or similar.
        :param sigma_2: float
                Additional parameter for convolution functions that require it, e.g.,
                for Voigt profiles, this could represent the Lorentzian component.
        :return: np.ndarray
                The truncated convolution function computed over the specified range.
        """
        try:
            index = 0
            truncated_convolution_function = np.zeros(j_max - j_min)
            methods = {
                0: gauss_f,
                1: triangle_f,
                2: trapeze_f,
                3: lorentz_f,
                4: voigt_f,
                5: gauss_lorentz_f
            }
            for j in range(j_min, j_max):
                if self.convolution_type == 2 or self.convolution_type == 4:
                    truncated_convolution_function[index] = methods[self.convolution_type](self.destination_wavelength[i], sigma_1, sigma_2, self.spectrum_wavelength[j])
                elif self.convolution_type == 5:
                    truncated_convolution_function[index] = methods[self.convolution_type](self.destination_wavelength[i], sigma_1, sigma_2, self.spectrum_wavelength[j], self.convolution_gauss_ratio)
                else:
                    truncated_convolution_function[index] = methods[self.convolution_type](self.destination_wavelength[i], sigma_1, self.spectrum_wavelength[j])
                index += 1
            return truncated_convolution_function
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_profil_calc: {str(e)}") from e

    def normalization(self, truncated_conv_func, j_min, j_max):
        """
            Normalizes a truncated convolution function over a specified wavelength range.

            This method normalizes a given truncated convolution function by calculating the area
            under the curve over a specified wavelength range and dividing the function by this area.
            The area is calculated using numerical integration.

            Note: The variable self.mean_truncated_convolution_function_area is unnecessary
            for the calculation of convolution and is used for testing purposes only.
            We will then use it in calculate_area_under_curve along with other variables to
            validate some hypotheses about how to calculate the convolution
            (see the doc-string for calculate_area_under_curve for details).

        :param truncated_conv_func: array-like
        	A 1D array representing the truncated convolution function that needs to be normalized.
        :param j_min: int
        	The starting index of the wavelength range for which the normalization is performed.
        :param j_max: int
        	The ending index of the wavelength range for which the normalization is performed.
        :return: array-like
        	The normalized truncated convolution function.
        """
        try:
            area_under_curve = np.trapz(truncated_conv_func, self.spectrum_wavelength[j_min:j_max])
            self.mean_truncated_convolution_function_area = self.mean_truncated_convolution_function_area + area_under_curve  # for testing purposes only
            return truncated_conv_func / area_under_curve
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:normalization: {str(e)}") from e

    def convolution_finalization(self, i, normalized_convolution_function, j_min, j_max):
        """
            Finalize the convolution by applying a specified function to an interval within the spectrum.

            This function computes the convolution of a slice of the spectrum intensity with a normalized convolution function.
            If the sum of the normalized convolution function is non-zero, the convolution result is assigned to the
            destination intensity array. If the sum is zero, it finds the closest wavelength and assigns the intensity value
            from the closest wavelength.

        :param i: int
            Index in the destination intensity array where the result will be stored.
        :param normalized_convolution_function: array-like
            The convolution function to be applied, normalized beforehand.
        :param j_min: int
            Minimum index in the spectrum interval to be convolved.
        :param j_max: int
            Maximum index in the spectrum interval to be convolved.
        :return: None
            The function returns nothing, but it modifies the destination intensity array.
        """
        try:
            if sum(normalized_convolution_function):
                self.destination_intensity[i] = np.convolve(self.spectrum_intensity[j_min:j_max], np.flip(normalized_convolution_function), "valid")[0] / sum(normalized_convolution_function)
            else:
                closest_index = 0
                delta_value = math.fabs(self.destination_wavelength[i] - self.spectrum_wavelength[0])
                for j in range(len(self.spectrum_wavelength)):
                    if delta_value < math.fabs(self.destination_wavelength[i] - self.spectrum_wavelength[j]):
                        closest_index = j
                        delta_value = math.fabs(self.destination_wavelength[i] - self.spectrum_wavelength[j])
                self.destination_intensity[i] = self.spectrum_intensity[closest_index]
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:convolution_finalization: {str(e)}") from e

    def calculate_area_under_curve(self):
        """
            Calculate the area under the curve for the destination and spectrum wavelengths and intensities.

            This function computes the surface areas under the curves defined by the destination intensities and wavelengths,
            as well as the cut spectrum and intensities, using numerical integration. It also adjusts the mean truncated convolution
            function area if applicable.

            This function calculates the parameters to test the hypotheses of the calculation.
            So it can be ignored if only an algorithm for calculating convolution is needed.

            In order to validate hypotheses, we use two facts. First, the area under the curve of the normalised convolution
            function self.mean_truncated_convolution_function_area must be equal to 1.
            Second, the area under the curve of the original spectrum self.spectrum_surface_area and the result of convolution
            self.destination_surface_area should differ as little as possible as required by the law of conservation of energy.

        :return: None
        	The function returns nothing, but it updates self.destination_surface_area and self.spectrum_surface_area.
        """
        try:
            if len(self.destination_wavelength):
                self.mean_truncated_convolution_function_area = self.mean_truncated_convolution_function_area / len(self.destination_wavelength)
            self.destination_surface_area = np.trapz(self.destination_intensity_getter(), self.destination_wavelength)
            cut_spectrum, cut_intensity = spectrum_to_destination_cut(self.spectrum_wavelength, self.spectrum_intensity, self.destination_wavelength)
            self.spectrum_surface_area = np.trapz(cut_intensity, cut_spectrum)
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:calculate_area_under_curve: {str(e)}") from e

    def energy_gain_loss(self):
        """
            Evaluates the energy gain or loss by comparing the high-resolution and convoluted spectra surface areas.

            This function calculates the percentage of energy gain or loss by comparing the integral values
            under the high-resolution spectrum curve and the convoluted spectrum. If the high-resolution
            spectrum area is greater, it signifies an energy loss and vice versa. If the input values are
            not valid, it returns a corresponding error message.

        :return: str
            A message describing the energy gain or loss in percentage.
        """
        try:
            if not self.spectrum_surface_area or not self.spectrum_surface_area:
                return f"Cannot conclude for {self.spectrum_surface_area} and {self.spectrum_surface_area}"
            message = (f"The integral under the high-resolution spectrum curve is {self.spectrum_surface_area:.6f}, "
                       f"for the convoluted spectrum it is {self.destination_surface_area:.6f}, ")
            if self.destination_surface_area < self.spectrum_surface_area:
                quantity = 100 * (1 - self.destination_surface_area / self.spectrum_surface_area)
                difference_is = "loss"
            else:
                quantity = 100 * (1 - self.spectrum_surface_area / self.destination_surface_area)
                difference_is = "gain"
            message = message + f"corresponding to {quantity:.6f}% energy {difference_is}."
            return message
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:energy_gain_loss: {str(e)}") from e

    # result export
    def destination_intensity_getter(self):
        """
            Gets the destination intensity array, reversing its order if specified.

            This function returns the destination intensity. If the revers_order_destination
            flag is set to True, it returns the reversed version of the destination intensity.

        :return: numpy.ndarray or list
        	The destination intensity vector, potentially reversed.
        """
        try:
            if self.revers_order_destination:
                return np.flip(self.destination_intensity)
            return self.destination_intensity
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:destination_intensity_getter: {str(e)}") from e

    def export_result_in_a_file(self):
        """
            Exports the spectrum results into a file.

            This function constructs a new file name based on the current spectrum file path,
            gathers intensity data, and writes the wavelength and intensity data into the new file.

        :return: None
            The function returns nothing but writes the spectrum data into a newly created file.
        """
        try:
            point_index = self.spectrum_file_path.rfind(".")
            new_file_name = self.spectrum_file_path[0:point_index] + "_conv" + self.spectrum_file_path[point_index:]
            result_str = ""
            intensity_result = self.destination_intensity_getter()
            for i in range(len(self.destination_wavelength)):
                result_str = result_str + str(self.destination_wavelength[i]) + self.spectrum_separator + str(intensity_result[i]) + "\n"
            with open(new_file_name, "w+", encoding="utf8") as file:
                file.write(result_str)
        except Exception as e:
            raise Exception(f"Critical error in ConvolutionCore:export_result_in_a_file: {str(e)}") from e


def demo_f():
    """
        This is an examples how to use this class to calculate the convolution.

        This function reads spectrum data from a file, sets up destination parameters
        and convolution parameters, performs convolution, and then prints and optionally
        exports the results.
    """
    # INPUT
    ## spectrum: micron
    spectrum_file_path = "tests/NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    ## destination: linear function, A
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131979695
    ## convolution: trapeze function, constant width & top
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0  # not used in this case
    convolution_truncation = 3
    convolution_width_1_const = 77
    convolution_width_2_const = 38.5
    # CLASS instance evocation
    """
            Note: the order of the setters is crucial. Ideally, the spectrum setter should be 
            called first, followed by the destination setter, and finally, the convolution 
            setter. The destination setter can be called before the spectrum setter. 
            However, the convolution setter should never be called before the destination setter.
    """
    my_conv = ConvolutionCore()
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    # CALC
    my_conv.tests_are_running = False  # flag for tests; can be used to prevent the interface from "asking questions" if True.
    my_conv.convolution_stack()
    # OUTPUT
    ## convoluted spectrum
    if my_conv.convolution_is_calculated:  # if the calculation process has been completed without errors (or was not canceled)
        print("\n\nConvoluted intensity:")
        print(my_conv.destination_intensity_getter())
        ## export (optional); The values are separated by the separator found in the spectrum file and the file is stored in the same directory as the spectrum file.
        # my_conv.result_export_in_a_file()  # saves the destination wavelength and the convolved intensity into a file
        ## truncated convolution function is normalized (optional)
        print(f"\nTruncated convolution function is normalized as this value is (technically) equal to 1: {my_conv.mean_truncated_convolution_function_area:.6f}")
        ## energy conservation (optional)
        print("\nEnergy conservation")
        print(my_conv.energy_gain_loss())


# demo_f()  # uncomment to run demo_f()
