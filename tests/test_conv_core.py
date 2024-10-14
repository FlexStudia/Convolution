# coding: utf-8

# PACKAGES
import numpy as np

# MODULES
# external
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import conv_core
from tools import data_pars
from tools.extrapolations import linear_regression
from tools.data_length_adjust import width_cut_off
from list_compare import list_compare


# TESTS
# list compare
def test_list_compare():
    # different length
    list1 = [0, 1, 2, 3]
    list2 = [0, 1, 2, 3, 4]
    # absolut equality
    assert not list_compare(list1, list2, 0)
    list1 = [0, 1, 2, 3, 4]
    list2 = [0, 1.01, 2.02, 3.03, 4.04]
    assert not list_compare(list1, list2, 0)
    # equality with too big accuracy
    list1 = [0, 1, 2, 3, 4]
    list2 = [0, 1.01, 2.02, 3.03, 4.04]
    assert not list_compare(list1, list2, 10 ** (-4))
    # equality with appropriate accuracy
    list1 = [0, 1, 2, 3, 4]
    list2 = [0, 1.01, 2.02, 3.03, 4.04]
    assert list_compare(list1, list2, 10 ** (-1))


# numpy convolve
def test_numpy_convolve(): # numpy convolve examples
    # example 1
    u = np.array([1, 0, 1])
    v = np.array([2, 7])
    result = np.array([2, 7, 2, 7])
    convolution = np.convolve(u, v, "full")
    assert list_compare(result, convolution, 0)
    # example 2
    u = np.array([1, 1, 1])
    v = np.array([1, 1, 0, 0, 0, 1, 1])
    result = np.array([1, 2, 2, 1, 0, 1, 2, 2, 1])
    convolution = np.convolve(u, v, "full")
    assert list_compare(result, convolution, 0)
    # example 3
    u = np.array([1, 2, 3])
    v = np.array([0, 1, 0.5])
    result = np.array([0, 1, 2.5, 4, 1.5])
    convolution = np.convolve(u, v, "full")
    assert list_compare(result, convolution, 0)
    # example 4
    u = np.array([1, 2, 3])
    v = np.array([0, 1, 0.5])
    result = np.array([1, 2.5, 4])
    convolution = np.convolve(u, v, "same")
    assert list_compare(result, convolution, 0)
    # example 5
    u = np.array([-1, 2, 3, -2, 0, 1, 2])
    v = np.array([2, 4, -1, 1])
    result = np.array([0, 15, 5, -9, 7, 6, 7])
    convolution = np.convolve(u, v, "same")
    assert list_compare(result, convolution, 0)
    # example 6
    u = np.array([1, 2, 3])
    v = np.array([0, 1, 0.5])
    result = np.array([2.5])
    convolution = np.convolve(u, v, "valid")
    assert list_compare(result, convolution, 0)


# Voigt function
def test_voigt_sigma_zero():
    # If sigma_gauss is zero, division by zero is output. However, the Lorentz distribution should actually be obtained. That is why we added a substitution to the code: if sigma_gauss is equal to zero, its value is equated to 10 ** -15.
    assert conv_core.voigt_f(0, 0, 1.8, 0) == 0.17683882565766149


def test_voigt_extreme_cases():
    assert conv_core.voigt_f(0, 0, 1.8, 0) == conv_core.lorentz_f(0,1.8, 0)
    assert conv_core.voigt_f(0, 0, 1.8, 0) == conv_core.gauss_lorentz_f(0,0, 1.8, 0, 0)
    assert conv_core.voigt_f(0, 1.53, 0, 0) == conv_core.gauss_f(0, 1.53, 0)
    assert conv_core.voigt_f(0, 1.53, 0, 0) == conv_core.gauss_lorentz_f(0, 1.53, 0, 0, 1)


# Units
def test_units_conversion_regular():
    data = 5
    # the same units
    result = 5
    assert conv_core.units_conversion(data, "cm-1", "cm-1") == result
    assert conv_core.units_conversion(data, "micron", "micron") == result
    assert conv_core.units_conversion(data, "nm", "nm") == result
    assert conv_core.units_conversion(data, "A", "A") == result
    # cm-1 and micron or micron and cm-1
    result = 2000
    assert conv_core.units_conversion(data, "cm-1", "micron") == result
    assert conv_core.units_conversion(data, "micron", "cm-1") == result
    # cm-1 and nm or nm and cm-1
    result = 2000000
    assert conv_core.units_conversion(data, "cm-1", "nm") == result
    assert conv_core.units_conversion(data, "nm", "cm-1") == result
    # cm-1 and A or A and cm-1
    result = 20000000
    assert conv_core.units_conversion(data, "cm-1", "A") == result
    assert conv_core.units_conversion(data, "A", "cm-1") == result
    # micron and nm
    result = 5000
    assert conv_core.units_conversion(data, "micron", "nm") == result
    # nm and micron
    result = 0.005
    assert conv_core.units_conversion(data, "nm", "micron") == result
    # micron and A
    result = 50000
    assert conv_core.units_conversion(data, "micron", "A") == result
    # A and micron
    result = 0.0005
    assert conv_core.units_conversion(data, "A", "micron") == result
    # nm and A
    result = 50
    assert conv_core.units_conversion(data, "nm", "A") == result
    # A and nm
    result = 0.5
    assert conv_core.units_conversion(data, "A", "nm") == result
    # zero
    data = 0
    result = 0
    assert conv_core.units_conversion(data, "cm-1", "cm-1") == result
    assert conv_core.units_conversion(data, "cm-1", "micron") == result
    assert conv_core.units_conversion(data, "nm", "cm-1") == result
    assert conv_core.units_conversion(data, "cm-1", "A") == result


def test_change_unit_regular():
    # micron and cm-1
    data = np.array([1, 2, 3, 4, 5])
    result = np.array([10000, 5000, 3333.333333, 2500, 2000])
    function_result = conv_core.change_unit(data, "micron", "cm-1")
    assert list_compare(result, function_result, 10**-6)


def test_change_width_unit():
    # variable width
    data = np.array([1, 2, 3, 4, 5])
    wavelength = np.array([10, 20, 30, 40, 50])
    result = np.array([100, 50, 33.333333, 25, 20])
    function_result = conv_core.change_width_unit(data, wavelength, "micron", "cm-1")
    assert list_compare(result, function_result, 10**-6)
    # constant width
    data = np.array([1, 1, 1, 1, 1])
    wavelength = np.array([10, 20, 30, 40, 50])
    result = np.array([100, 25, 11.111111, 6.25, 4])
    function_result = conv_core.change_width_unit(data, wavelength, "micron", "cm-1")
    assert list_compare(result, function_result, 10 ** -6)


def test_width_cut_off():
    data_width = np.array([-9.369793745222896, -8.751814080633821, -7.673532788648299, -7.344841638886363, -6.494841937086468, -5.441216307568695, -4.4605727873533, -3.4921353881799715, -3.049751401802695, -2.4255113926915723, -1.7907791168122822, -0.907541882846732, -0.4242388260140305, -0.0618013141661749, 0.9332331112191783, 1.6506361063736708, 2.8467941709264526, 3.6537621452319566, 3.8744702417531256, 4.91076611498307, 5.910439446329539, 6.829019746335873, 7.308193390909814, 7.710554020416464, 8.511507364692193, 9.120489141450296, 9.742480469287003, 10.315902139437712, 11.469457712783075, 12.569627710944143])
    spectrum_wavelength = np.array([-14.03728598226862, -13.14345807165166, -12.102397217861615, -10.423642641035231, -9.170864979549144, -8.164167629840842, -7.142700631436471, -5.527117787540342, -4.567382944223645, -2.9399373153984643, -1.4952246190320717, -0.21546437091981707, 1.4649859554424305, 3.0656382419235166, 4.33053633804392, 5.225073733326168, 6.800588027690935, 7.74427253368689, 8.506921887409536, 9.330259956708717, 10.993920511329705, 11.948969252439975, 13.33091745286012, 14.244895369640226, 15.257178903747672, 16.167567551151812, 17.273546628231667, 18.39105301223708, 19.99518039506823, 21.420593022118016])
    destination_wavelength = np.array([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    result = np.array([-7.344841638886363, -5.441216307568695, -3.4921353881799715, -3.049751401802695, -1.7907791168122822, -0.907541882846732, -0.0618013141661749, 0.9332331112191783, 1.6506361063736708, 3.6537621452319566, 4.91076611498307])
    assert list_compare(width_cut_off(data_width, spectrum_wavelength, destination_wavelength), result, 10 ** -6)


# Generators
def test_two_from_file_extractor_regular():
    # columns: 0 & 1
    file_path = "file_read/wlth_1_inty_2.txt"
    data_read = data_pars.DataPars(file_path, None)
    data_read.file_pars_f()
    my_data = data_read.file_body
    result1 = np.array([3500.273926, 3500.756104, 3501.238037, 3501.720947, 3502.202881, 3502.685059])
    result2 = np.array([0.735755, 0.737972, 0.738710, 0.739975, 0.743115, 0.744667])
    function_result1 = conv_core.extract_two_columns_from_data(my_data, 0, 1)[0]
    function_result2 = conv_core.extract_two_columns_from_data(my_data, 0, 1)[1]
    assert list_compare(result1, function_result1, 10 ** -6)
    assert list_compare(result2, function_result2, 10 ** -6)
    # columns: 0 & 2
    file_path = "file_read/wlth_1_inty_3.txt"
    data_read = data_pars.DataPars(file_path, None)
    data_read.file_pars_f()
    my_data = data_read.file_body
    result1 = np.array([0, 0.482, 0.964, 1.446, 1.929, 2.411, 2.893, 3.375, 3.857])
    result2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    function_result1 = conv_core.extract_two_columns_from_data(my_data, 0, 2)[0]
    function_result2 = conv_core.extract_two_columns_from_data(my_data, 0, 2)[1]
    assert list_compare(result1, function_result1, 10 ** -3)
    assert list_compare(result2, function_result2, 10 ** 0)
    # columns: 1 & 2
    file_path = "file_read/wlth_1_inty_3.txt"
    data_read = data_pars.DataPars(file_path, None)
    data_read.file_pars_f()
    my_data = data_read.file_body
    result1 = np.array([1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23])
    result2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    function_result1 = conv_core.extract_two_columns_from_data(my_data, 1, 2)[0]
    function_result2 = conv_core.extract_two_columns_from_data(my_data, 1, 2)[1]
    assert list_compare(result1, function_result1, 10 ** -2)
    assert list_compare(result2, function_result2, 10 ** 0)


def test_one_from_file_extractor_regular():
    # columns: 0
    file_path = "file_read/wlth_1_inty_2.txt"
    data_read = data_pars.DataPars(file_path, None)
    data_read.file_pars_f()
    my_data = data_read.file_body
    result = np.array([3500.273926, 3500.756104, 3501.238037, 3501.720947, 3502.202881, 3502.685059])
    function_result = conv_core.extract_one_column_from_data(my_data, 0)
    assert list_compare(result, function_result, 10 ** -6)
    # columns: 1
    file_path = "file_read/wlth_1_inty_3.txt"
    data_read = data_pars.DataPars(file_path, None)
    data_read.file_pars_f()
    my_data = data_read.file_body
    result = np.array([1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23])
    function_result = conv_core.extract_one_column_from_data(my_data, 1)
    assert list_compare(result, function_result, 10 ** -2)
    # columns: 2
    file_path = "file_read/wlth_1_inty_3.txt"
    data_read = data_pars.DataPars(file_path, None)
    data_read.file_pars_f()
    my_data = data_read.file_body
    result = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    function_result = conv_core.extract_one_column_from_data(my_data, 2)
    assert list_compare(result, function_result, 10 ** 0)


def test_linear_extrapolation_regular():
    # int
    result = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    function_result = conv_core.linear_extrapolation(0, 9, 1)
    assert list_compare(result, function_result, 10 ** 0)
    # float
    result = np.array([1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
    function_result = conv_core.linear_extrapolation(1.5, 5, 0.5)
    assert list_compare(result, function_result, 10 ** -1)
    # borders overflow
    result = np.array([1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
    function_result = conv_core.linear_extrapolation(1.5, 5.2, 0.5)
    assert list_compare(result, function_result, 10 ** -1)
    # reverse order
    result = np.flip(np.array([1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]))
    function_result = conv_core.linear_extrapolation(5, 1.5, 0.5)
    assert list_compare(result, function_result, 10 ** -1)
    # borders overflow: more complex cases
    result = np.array([1., 2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8])
    function_result = conv_core.linear_extrapolation(1, 10, 1.1)
    assert list_compare(result, function_result, 10 ** -1)
    result = np.array([1., 2.2, 3.4, 4.6, 5.8, 7., 8.2, 9.4])
    function_result = conv_core.linear_extrapolation(1, 10, 1.2)
    assert list_compare(result, function_result, 10 ** -1)
    result = np.array([1., 2.3, 3.6, 4.9, 6.2, 7.5, 8.8])
    function_result = conv_core.linear_extrapolation(1, 10, 1.3)
    assert list_compare(result, function_result, 10 ** -1)
    result = np.array([1., 2.4, 3.8, 5.2, 6.6, 8., 9.4])
    function_result = conv_core.linear_extrapolation(1, 10, 1.4)
    assert list_compare(result, function_result, 10 ** -1)
    result = np.array([1., 2.5, 4., 5.5, 7., 8.5, 10.])
    function_result = conv_core.linear_extrapolation(1, 10, 1.5)
    assert list_compare(result, function_result, 10 ** -1)
    result = np.array([1., 2.6, 4.2, 5.8, 7.4, 9.])
    function_result = conv_core.linear_extrapolation(1, 10, 1.6)
    assert list_compare(result, function_result, 10 ** -1)
    result = np.array([1., 2.7, 4.4, 6.1, 7.8, 9.5])
    function_result = conv_core.linear_extrapolation(1, 10, 1.7)
    assert list_compare(result, function_result, 10 ** -1)
    result = np.array([1., 2.8, 4.6, 6.4, 8.2, 10.])
    function_result = conv_core.linear_extrapolation(1, 10, 1.8)
    assert list_compare(result, function_result, 10 ** -1)
    result = np.array([1., 2.9, 4.8, 6.7, 8.6])
    function_result = conv_core.linear_extrapolation(1, 10, 1.9)
    assert list_compare(result, function_result, 10 ** -1)
    result = np.array([1., 3., 5., 7., 9.])
    function_result = conv_core.linear_extrapolation(1, 10, 2.0)
    assert list_compare(result, function_result, 10 ** -1)


def test_const_extrapolation_regular():
    # int
    result = np.array([3, 3, 3, 3, 3, 3, 3, 3, 3])
    function_result = conv_core.const_extrapolation(3, 9)
    assert list_compare(result, function_result, 10 ** 0)
    # float
    result = np.array([0.5, 0.5, 0.5, 0.5, 0.5])
    function_result = conv_core.const_extrapolation(0.5, 5)
    assert list_compare(result, function_result, 10 ** -1)


# Regression and extrapolation
def test_linear_regression_regular():
    x_input = np.array([0, 1, 2, 3])
    y_input = np.array([-1, 0.2, 0.9, 2.1])
    result = np.array([-0.95, 0.05, 1.05, 2.05])
    function_result = linear_regression(x_input, y_input, x_input)
    assert list_compare(result, function_result, 10 ** -2)


def test_y_extrapolation_regular(): # interp_mode = 1: "zeros", 2: "constant", 3: "average constant", 4: "linear regression"
    x_vec = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    y_vec = np.array(               [1, 2, 3, 4, 5, 6, 7, 8, 9]                    )
    qty_before = 4
    qty_after = 5
    # zeros
    interp_mode = 0  # "zeros"
    result = np.array([0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0])
    function_result = conv_core.y_extrapolation(x_vec, y_vec, qty_before, qty_after, interp_mode)
    assert list_compare(result, function_result, 10 ** 0)
    # constant
    interp_mode = 1  # "constant"
    result = np.array([1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9])
    function_result = conv_core.y_extrapolation(x_vec, y_vec, qty_before, qty_after, interp_mode)
    assert list_compare(result, function_result, 10 ** 0)
    # average constant
    interp_mode = 2  # "average constant"
    result = np.array([3, 3, 3, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 7, 7, 7, 7])
    function_result = conv_core.y_extrapolation(x_vec, y_vec, qty_before, qty_after, interp_mode)
    assert list_compare(result, function_result, 10 ** 0)
    # linear regression
    interp_mode = 3  # "linear regression"
    result = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    function_result = conv_core.y_extrapolation(x_vec, y_vec, qty_before, qty_after, interp_mode)
    assert list_compare(result, function_result, 10 ** 0)


# convolution applicability
def test_width_and_step_condition():
    # True
    destination_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    width_array = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    my_conv = conv_core.ConvolutionCore()
    my_conv.destination_wavelength = destination_array
    my_conv.convolution_width_1 = width_array
    assert my_conv.convolution_width_and_destination_step_verification()
    # False
    destination_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    width_array = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4])
    my_conv = conv_core.ConvolutionCore()
    my_conv.destination_wavelength = destination_array
    my_conv.convolution_width_1 = width_array
    assert not my_conv.convolution_width_and_destination_step_verification()


def test_truncation_and_width_condition():
    # True
    ## Gauss
    convolution_type = 1
    convolution_truncation = 10
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert my_conv.truncation_and_width_condition()
    ## triangle
    convolution_type = 2
    convolution_truncation = 10
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert my_conv.truncation_and_width_condition()
    ## trapeze
    convolution_type = 3
    convolution_truncation = 10
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert my_conv.truncation_and_width_condition()
    ## Lorentz
    convolution_type = 4
    convolution_truncation = 2000
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert my_conv.truncation_and_width_condition()
    ## Voigt
    convolution_type = 5
    convolution_truncation = 2000
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv =conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert my_conv.truncation_and_width_condition()
    ## Gauss & Lorentz
    convolution_type = 6
    convolution_truncation = 2000
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert my_conv.truncation_and_width_condition()
    # False
    ## Gauss
    convolution_type = 1
    convolution_truncation = 2
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert not my_conv.truncation_and_width_condition()
    ## triangle
    convolution_type = 2
    convolution_truncation = 0.5
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert not my_conv.truncation_and_width_condition()
    ## trapeze
    convolution_type = 3
    convolution_truncation = 0.5
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert not my_conv.truncation_and_width_condition()
    ## Lorentz
    convolution_type = 4
    convolution_truncation = 2
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert not my_conv.truncation_and_width_condition()
    ## Voigt
    convolution_type = 5
    convolution_truncation = 2
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert not my_conv.truncation_and_width_condition()
    ## Gauss & Lorentz
    convolution_type = 6
    convolution_truncation = 2
    width_array = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.convolution_type = convolution_type - 1
    my_conv.convolution_truncation = convolution_truncation
    my_conv.convolution_width_1 = width_array
    assert not my_conv.truncation_and_width_condition()
    

def test_width_condition():
    # correct
    spectrum_width_original = [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]
    spectrum_wavelength =     [0.5,   1, 1.5,   2, 2.5, 3, 3.5,   4, 4.5,   5, 5.5]
    destination_wavelength =                   [2,      3,        4]
    convolution_width_1 =                      [1,      2,        3]
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_width = spectrum_width_original
    my_conv.spectrum_wavelength = spectrum_wavelength
    my_conv.destination_wavelength = destination_wavelength
    my_conv.convolution_width_1 = convolution_width_1
    assert my_conv.width_condition() == ("", 0)
    # one interval
    spectrum_width_original = [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
    spectrum_wavelength =     [0.5,   1, 1.5,   2, 2.5, 3, 3.5,   4, 4.5,   5, 5.5,   6, 6.5]
    destination_wavelength =          [1,          2.5,           4,           5.5]
    convolution_width_1 =             [0.5,        2,             3,           4]
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_width = spectrum_width_original
    my_conv.spectrum_wavelength = spectrum_wavelength
    my_conv.destination_wavelength = destination_wavelength
    my_conv.convolution_width_1 = convolution_width_1
    assert my_conv.width_condition() == ("1 - 2.5", 2)
    # two intervals
    spectrum_width_original = [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
    spectrum_wavelength =     [0.5,   1, 1.5,   2, 2.5, 3, 3.5,   4, 4.5,   5, 5.5,   6, 6.5]
    destination_wavelength =         [1,           2.5,           4,           5.5]
    convolution_width_1 =            [0.5,         2,             0.5,         4]
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_width = spectrum_width_original
    my_conv.spectrum_wavelength = spectrum_wavelength
    my_conv.destination_wavelength = destination_wavelength
    my_conv.convolution_width_1 = convolution_width_1
    assert my_conv.width_condition() == ("1 - 2.5, 4 - 5.5", 4)


# Math: parabola
def test_convolution_calc_linear_cont_non_t_parabola_1_ascending_ascending():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_extrapolation_type = 0  # "zeros"
    convolution_width_1_const = 1
    result = np.array([0.18033995, 0.43033995, 1.18033995, 2.43033995, 4.18033995, 6.43033995, 9.18033995, 12.43033995, 16.18033995, 20.43033995, 25.18033995, 30.43033995, 36.18033995, 42.43033995, 49.18033995, 56.43033995, 64.18033995, 72.43033995, 81.18033995, 90.43033995, 100.18033995])
    my_conv = conv_core.ConvolutionCore()
    # sdc, dcs
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -2)
    assert list_compare(my_conv.destination_intensity_getter(), function_result, 10 ** 0)
    assert not my_conv.revers_order_spectrum
    assert not my_conv.revers_order_destination
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -2)
    assert list_compare(my_conv.destination_intensity_getter(), function_result, 10 ** 0)
    assert not my_conv.revers_order_spectrum
    assert not my_conv.revers_order_destination
    # dcs, sdc
    my_conv = conv_core.ConvolutionCore()
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -2)
    assert list_compare(my_conv.destination_intensity_getter(), function_result, 10 ** 0)
    assert not my_conv.revers_order_spectrum
    assert not my_conv.revers_order_destination
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -2)
    assert list_compare(my_conv.destination_intensity_getter(), function_result, 10 ** 0)
    assert not my_conv.revers_order_spectrum
    assert not my_conv.revers_order_destination


def test_convolution_calc_linear_cont_non_t_parabola_1_descending_ascending():
    spectrum_file_path = "math_examples/parabol_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_extrapolation_type = 0  # "zeros"
    convolution_width_1_const = 1
    result = np.array([0.18033995, 0.43033995, 1.18033995, 2.43033995, 4.18033995, 6.43033995, 9.18033995, 12.43033995, 16.18033995, 20.43033995, 25.18033995, 30.43033995, 36.18033995, 42.43033995, 49.18033995, 56.43033995, 64.18033995, 72.43033995, 81.18033995, 90.43033995, 100.18033995])
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -2)
    assert list_compare(my_conv.destination_intensity_getter(), function_result, 10 ** 0)
    assert my_conv.revers_order_spectrum
    assert not my_conv.revers_order_destination
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -2)
    assert list_compare(my_conv.destination_intensity_getter(), function_result, 10 ** 0)
    assert my_conv.revers_order_spectrum
    assert not my_conv.revers_order_destination


def test_convolution_calc_linear_cont_non_t_parabola_1_ascending_descending():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 10
    destination_stop = 0
    destination_step = 0.5
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_extrapolation_type = 0  # "zeros"
    convolution_width_1_const = 1
    result = np.array([0.18033995, 0.43033995, 1.18033995, 2.43033995, 4.18033995, 6.43033995, 9.18033995, 12.43033995, 16.18033995, 20.43033995, 25.18033995, 30.43033995, 36.18033995, 42.43033995, 49.18033995, 56.43033995, 64.18033995, 72.43033995, 81.18033995, 90.43033995, 100.18033995])
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -2)
    assert list_compare(my_conv.destination_intensity_getter(), np.flip(function_result), 10 ** 0)
    assert not my_conv.revers_order_spectrum
    assert my_conv.revers_order_destination
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -2)
    assert list_compare(my_conv.destination_intensity_getter(), np.flip(function_result), 10 ** 0)
    assert not my_conv.revers_order_spectrum
    assert my_conv.revers_order_destination


def test_convolution_calc_linear_cont_non_t_parabola_1_descending_descending():
    spectrum_file_path = "math_examples/parabol_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 10
    destination_stop = 0
    destination_step = 0.5
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_extrapolation_type = 0  # "zeros"
    convolution_width_1_const = 1
    result = np.array([0.18033995, 0.43033995, 1.18033995, 2.43033995, 4.18033995, 6.43033995, 9.18033995, 12.43033995, 16.18033995, 20.43033995, 25.18033995, 30.43033995, 36.18033995, 42.43033995, 49.18033995, 56.43033995, 64.18033995, 72.43033995, 81.18033995, 90.43033995, 100.18033995])
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -2)
    assert list_compare(my_conv.destination_intensity_getter(), np.flip(function_result), 10 ** 0)
    assert my_conv.revers_order_spectrum
    assert my_conv.revers_order_destination
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -2)
    assert list_compare(my_conv.destination_intensity_getter(), np.flip(function_result), 10 ** 0)
    assert my_conv.revers_order_spectrum
    assert my_conv.revers_order_destination


def test_convolution_calc_linear_cont_non_t_parabola_2():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 1
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_const = 2
    result = np.array([1, 2,  5, 10, 17, 26, 37, 50, 65, 82, 101])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


# Math: Gauss
def test_convolution_calc_linear_const_non_t_gauss_1():
    spectrum_file_path = "math_examples/gauss.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_const = 1
    result = np.array([6.99723514e-17, 7.64211630e-14, 3.99572993e-11, 1.00038198e-08, 1.19929560e-06, 6.88457809e-05, 1.89242698e-03, 2.49087333e-02, 1.56991039e-01, 4.73793173e-01, 6.84689145e-01, 4.73793173e-01,
                       1.56991039e-01, 2.49087333e-02, 1.89242698e-03, 6.88457809e-05, 1.19929560e-06, 1.00038198e-08, 3.99572993e-11, 7.64211630e-14, 6.99723514e-17])
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -4)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -4)


def test_convolution_calc_linear_const_non_t_gauss_2():
    spectrum_file_path = "math_examples/gauss.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 1
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_const = 2
    result = np.array([2.90530934e-07, 4.81635127e-05, 2.56457838e-03, 4.38617394e-02, 2.40950468e-01, 4.25149575e-01, 2.40950468e-01, 4.38617394e-02, 2.56457838e-03, 4.81635127e-05, 2.90530934e-07])
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


# Real case, from file, different units
def test_convolution_calc_a_few_calcs():
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # calc 1: file_nh_a_a_trap
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_A.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/A_a_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # calc 2: file_nh_a_cm_gauss
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/A_cm_gauss.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # calc 3: file_nh_cm_a_trap():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_A.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/cm_a_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # case 4: file_linear_t_A_cm():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 16.749254
    convolution_width_1_stop = 33.940654
    convolution_width_2_start = 8.3746270
    convolution_width_2_stop = 16.970327
    result_path = "NH_case/constructors/File_linear_T.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -4)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -4)


def test_convolution_calc_file_nh_a_a_trap():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_A.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/A_a_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_a_cm_gauss():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/A_cm_gauss.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_a_cm_trap_ascending_ascending():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/A_cm_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    assert list_compare(my_conv.destination_intensity_getter(), function_result, 10 ** 0)
    assert my_conv.revers_order_spectrum
    assert not my_conv.revers_order_destination
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    assert list_compare(my_conv.destination_intensity_getter(), function_result, 10 ** 0)
    assert my_conv.revers_order_spectrum
    assert not my_conv.revers_order_destination


def test_convolution_calc_file_nh_a_cm_trap_descending_ascending():
    spectrum_file_path = "NH_case/spectrum_A_descending.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/A_cm_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    assert list_compare(my_conv.destination_intensity_getter(), function_result, 10 ** 0)
    assert my_conv.revers_order_spectrum
    assert not my_conv.revers_order_destination
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    assert list_compare(my_conv.destination_intensity_getter(), function_result, 10 ** 0)
    assert not my_conv.revers_order_spectrum
    assert not my_conv.revers_order_destination


def test_convolution_calc_file_nh_a_cm_trap_ascending_descending():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm_descending.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm_descending.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/A_cm_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    assert list_compare(my_conv.destination_intensity_getter(), np.flip(function_result), 10 ** 0)
    assert my_conv.revers_order_spectrum
    assert my_conv.revers_order_destination
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    assert list_compare(my_conv.destination_intensity_getter(), np.flip(function_result), 10 ** 0)
    assert my_conv.revers_order_spectrum
    assert my_conv.revers_order_destination


def test_convolution_calc_file_nh_a_cm_trap_descending_descending():
    spectrum_file_path = "NH_case/spectrum_A_descending.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm_descending.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm_descending.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/A_cm_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    assert list_compare(my_conv.destination_intensity_getter(), np.flip(function_result), 10 ** 0)
    assert my_conv.revers_order_spectrum
    assert my_conv.revers_order_destination
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    assert list_compare(my_conv.destination_intensity_getter(), np.flip(function_result), 10 ** 0)
    assert not my_conv.revers_order_spectrum
    assert my_conv.revers_order_destination


def test_convolution_calc_file_nh_a_cm_trig():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1 # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/A_cm_trig.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_a_mc_gauss():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/A_mc_gauss.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_a_mc_trap():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/A_mc_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_a_mc_trig():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1 # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/A_mc_trig.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_a_nm_gauss():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_nm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/A_nm_gauss.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_a_nm_trap():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_nm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/A_nm_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_a_nm_trig():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1 # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_nm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/A_nm_trig.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_cm_a_trap():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_A.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/cm_a_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_cm_cm_gauss():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/cm_cm_gauss.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_cm_cm_trap():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/cm_cm_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_cm_cm_trig():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1 # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/cm_cm_trig.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_cm_mc_gauss():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/cm_mc_gauss.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_cm_mc_trap():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/cm_mc_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_cm_mc_trig():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1 # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/cm_mc_trig.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_cm_nm_gauss():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_nm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/cm_nm_gauss.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_cm_nm_trap():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_nm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/cm_nm_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_cm_nm_trig():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1 # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_nm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/cm_nm_trig.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_mc_a_trap():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_A.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/mc_a_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_nm_cm_gauss():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/nm_cm_gauss.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_nm_cm_trap():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/nm_cm_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_nm_cm_trig():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1 # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/nm_cm_trig.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_nm_mc_gauss():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/nm_mc_gauss.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_nm_mc_trap():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/nm_mc_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_nm_mc_trig():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1 # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/nm_mc_trig.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_nm_nm_gauss():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_nm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/nm_nm_gauss.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_nm_nm_trap():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_nm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/results/nm_nm_trap.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_nh_nm_nm_trig():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_nm.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/results/nm_nm_trig.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


# Other constructors
def test_spectrum_setter_file():
    spectrum_file_path = "spectrum_width_constructors/spectrum.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    spectrum_width_column = 2
    result_wavelength = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result_intensity = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    result_width = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, spectrum_width_column)
    assert list_compare(my_conv.spectrum_wavelength, result_wavelength, 10 ** -6)
    assert list_compare(my_conv.spectrum_intensity, result_intensity, 10 ** -6)
    assert list_compare(my_conv.spectrum_width, result_width, 10 ** -6)


def test_spectrum_setter_const():
    spectrum_file_path = "spectrum_width_constructors/spectrum.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    spectrum_width_constant = 2
    result_wavelength = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result_intensity = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    result_width = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_constant(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_width_constant)
    assert list_compare(my_conv.spectrum_wavelength, result_wavelength, 10 ** -6)
    assert list_compare(my_conv.spectrum_intensity, result_intensity, 10 ** -6)
    assert list_compare(my_conv.spectrum_width, result_width, 10 ** -6)


def test_convolution_calc_file_linear_non_t():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 16.749254
    convolution_width_1_stop = 33.940654
    result_path = "NH_case/constructors/File_linear_NonT.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -4)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -4)


def test_convolution_calc_file_linear_t_A_cm():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 16.749254
    convolution_width_1_stop = 33.940654
    convolution_width_2_start = 8.3746270
    convolution_width_2_stop = 16.970327
    result_path = "NH_case/constructors/File_linear_T.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -4)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -4)


def test_convolution_calc_file_const_non_t():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0 # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_const = 0.007
    result_path = "NH_case/constructors/File_Const_NonT.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_const_t():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 75
    convolution_width_2_const = 37
    result_path = "NH_case/constructors/File_Const_T.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_linear_file_non_t():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_A.txt"
    convolution_width_1_column = 1
    result_path = "NH_case/constructors/linear_file_NonT.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_linear_file_t():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131979695
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_A.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    result_path = "NH_case/constructors/linear_file_T.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_linear_t_mc_nm_ascending_ascending():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.36531
    convolution_width_2_start = 2.557569
    convolution_width_2_stop = 5.18267
    result_path = "NH_case/results/mc_nm_trap_file_linear.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_linear_t_mc_nm_descending_ascending():
    spectrum_file_path = "NH_case/spectrum_micron_descending.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.36531
    convolution_width_2_start = 2.557569
    convolution_width_2_stop = 5.18267
    result_path = "NH_case/results/mc_nm_trap_file_linear.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_linear_t_mc_nm_ascending_descending():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm_descending.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 10.36531
    convolution_width_1_stop = 5.115138
    convolution_width_2_start = 5.18267
    convolution_width_2_stop = 2.557569
    result_path = "NH_case/results/mc_nm_trap_file_linear.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_file_linear_t_mc_nm_descending_descending():
    spectrum_file_path = "NH_case/spectrum_micron_descending.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm_descending.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 10.36531
    convolution_width_1_stop = 5.115138
    convolution_width_2_start = 5.18267
    convolution_width_2_stop = 2.557569
    result_path = "NH_case/results/mc_nm_trap_file_linear.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


def test_convolution_calc_linear_linear_non_t():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131979695
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1 # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 51.15138
    convolution_width_1_stop = 103.65304
    result_path = "NH_case/constructors/linear_linear_NonT.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -5)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -5)


def test_convolution_calc_linear_linear_t():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131979695
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2 # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 51.15138
    convolution_width_1_stop = 103.65304
    convolution_width_2_start = 25.57569
    convolution_width_2_stop = 51.82652
    result_path = "NH_case/constructors/linear_linear_T.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -5)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_linear_function(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -5)


def test_convolution_calc_linear_const_t():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131979695
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 77
    convolution_width_2_const = 38.5
    result_path = "NH_case/constructors/linear_Const_T.txt"
    result_read = data_pars.DataPars(result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** -6)


# Lorentz
def test_convolution_calc_lorentz_parabola_1():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "Lorentz function"
    convolution_gauss_ratio = 0
    convolution_truncation = 15
    convolution_width_1_const = 1
    result = np.array([2.2429729, 2.49319352, 3.24341414, 4.49363475, 6.24385537, 8.49407599, 11.2442966, 14.49451722, 18.24473784, 22.49495846, 27.24517907, 32.49539969, 38.24562031, 44.49584092, 51.24606154, 58.49628216, 66.24650278, 74.49672339, 83.24694401, 92.49716463, 102.24738524])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


def test_convolution_calc_lorentz_parabola_2():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 1
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "Lorentz function"
    convolution_gauss_ratio = 0
    convolution_truncation = 15
    convolution_width_1_const = 2
    result = np.array([8.11889056,  9.5207998, 12.82952787, 17.97321521, 24.97365645, 33.97409768, 44.97453892, 57.97498015, 72.97542138, 89.97586262, 108.97630385])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


def test_convolution_calc_lorentz_gauss_1():
    spectrum_file_path = "math_examples/gauss.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = -1
    destination_stop = 11
    destination_step = 0.5
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "Lorentz function"
    convolution_gauss_ratio = 0
    convolution_truncation = 15
    convolution_width_1_const = 1
    result = np.array([0.00449621, 0.00535725, 0.00649252, 0.00803267, 0.01019697, 0.01337713, 0.0183313, 0.02669253, 0.04253249, 0.07790402, 0.16758519, 0.34531762, 0.46578183, 0.34535621, 0.16762271, 0.07793026, 0.04255168, 0.02670766, 0.01834384, 0.01338789, 0.01020644, 0.00804114, 0.00650022, 0.00536432, 0.00450278])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


def test_convolution_calc_lorentz_gauss_2():
    spectrum_file_path = "math_examples/gauss.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = -10
    destination_stop = 20
    destination_step = 1
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "Lorentz function"
    convolution_gauss_ratio = 0
    convolution_truncation = 15
    convolution_width_1_const = 2
    result = np.array([0.00143423, 0.00164545, 0.00190707, 0.00223649, 0.00265925, 0.00321421, 0.00396264, 0.00500582, 0.00652077, 0.00883943, 0.01264306, 0.01950686, 0.03370817, 0.06939651, 0.17074617, 0.28610405, 0.17074597, 0.06939635, 0.03370804, 0.01950676, 0.01264298, 0.00883936, 0.0065207, 0.00500576, 0.00396258, 0.00321414, 0.00265919, 0.00223642, 0.001907, 0.00164536, 0.00143413])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


# Voigt
def test_convolution_calc_voigt_parabola_1():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 4  # "Voigt"
    convolution_gauss_ratio = 0.7
    convolution_truncation = 15
    convolution_width_1_const = 1
    convolution_width_2_const = 0.5
    result = np.array([1.92542491, 2.17542491, 2.92542491, 4.17542491, 5.92542491, 8.17542491, 10.92542491, 14.17542491, 17.92542491, 22.17542491, 26.92542491, 32.17542491, 37.92542491, 44.17542491, 50.92542491, 58.17542491, 65.92542491, 74.17542491, 82.92542491, 92.17542491, 101.92542491])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


def test_convolution_calc_voigt_parabola_2():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 1
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 4  # "Voigt"
    convolution_gauss_ratio = 0.5
    convolution_truncation = 15
    convolution_width_1_const = 2
    convolution_width_2_const = 1.25
    result = np.array([7.28693876, 8.68956912, 12.02535429, 17.30547396, 24.29343471, 33.15440454, 43.92344788, 56.59654566,  71.16711777, 87.62567181, 105.9407116])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


def test_convolution_calc_voigt_gauss_1():
    spectrum_file_path = "math_examples/gauss.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = -1
    destination_stop = 11
    destination_step = 0.5
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 4  # "Voigt"
    convolution_gauss_ratio = 0.9
    convolution_truncation = 15
    convolution_width_1_const = 1
    convolution_width_2_const = 1
    result = np.array([4.45372243e-04, 5.30668796e-04, 6.43128548e-04, 7.95691753e-04, 1.01007823e-03, 1.32525601e-03, 1.82519164e-03, 2.91475895e-03, 8.44713223e-03, 4.36534423e-02, 1.82155667e-01, 4.48191804e-01, 6.08048292e-01, 4.48196764e-01, 1.82159705e-01, 4.36548982e-02, 8.44750941e-03, 2.91492250e-03, 1.82531532e-03, 1.32536158e-03, 1.01017101e-03, 7.95774809e-04, 6.43203988e-04, 5.30738138e-04, 4.45436618e-04])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


def test_convolution_calc_voigt_gauss_2():
    spectrum_file_path = "math_examples/gauss.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = -6
    destination_stop = 16
    destination_step = 1
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 4  # "Voigt"
    convolution_gauss_ratio = 0.3
    convolution_truncation = 15
    convolution_width_1_const = 2
    convolution_width_2_const = 2
    result = np.array([0.00185521, 0.00224239, 0.00276455, 0.00349236, 0.00454931, 0.00616702, 0.00882306, 0.01372258, 0.02583351, 0.0684331, 0.19213544, 0.31199397, 0.19213524, 0.06843296, 0.02583342, 0.01372252, 0.00882301, 0.00616698, 0.00454927, 0.00349232, 0.00276452, 0.00224235, 0.00185517])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


# GaussLorentz
def test_convolution_calc_gauss_lorentz_sum_parabola_1():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 5  # "Gauss & Lorentz sum"
    convolution_gauss_ratio = 0.7
    convolution_truncation = 15
    convolution_width_1_const = 1
    convolution_width_2_const = 1
    result = np.array([0.82992699, 1.07999119, 1.83005538, 3.08011958, 4.83018377, 7.08024797, 9.83031217, 13.08037636, 16.83044056, 21.08050476, 25.83056895, 31.08063315, 36.83069735, 43.08076154, 49.83082574, 57.08088994, 64.83095413, 73.08101833, 81.83108253, 91.08114672, 100.83121092])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


def test_convolution_calc_gauss_lorentz_sum_parabola_2():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 1
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 5  # "Gauss & Lorentz sum"
    convolution_gauss_ratio = 0.5
    convolution_truncation = 15
    convolution_width_1_const = 2
    convolution_width_2_const = 2
    result = np.array([5.9433181, 7.1256988, 10.22326137, 15.24086546, 22.18106329, 31.04441364, 41.82962551, 54.53356324, 69.15112202, 85.67496359, 104.09508118])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


def test_convolution_calc_gauss_lorentz_sum_gauss_1():
    spectrum_file_path = "math_examples/gauss.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = -1
    destination_stop = 11
    destination_step = 0.5
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 5  # "Gauss & Lorentz sum"
    convolution_gauss_ratio = 0.9
    convolution_truncation = 15
    convolution_width_1_const = 1
    convolution_width_2_const = 1
    result = np.array([4.45372243e-04, 5.30668796e-04, 6.43128548e-04, 7.95691753e-04, 1.01007823e-03, 1.32525601e-03, 1.82519164e-03, 2.91475895e-03, 8.44713223e-03, 4.36534423e-02, 1.82155667e-01, 4.48191804e-01, 6.08048292e-01, 4.48196764e-01, 1.82159705e-01, 4.36548982e-02, 8.44750941e-03, 2.91492250e-03, 1.82531532e-03, 1.32536158e-03, 1.01017101e-03, 7.95774809e-04, 6.43203988e-04, 5.30738138e-04, 4.45436618e-04])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


def test_convolution_calc_gauss_lorentz_sum_gauss_2():
    spectrum_file_path = "math_examples/gauss.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = -6
    destination_stop = 16
    destination_step = 1
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 5  # "Gauss & Lorentz sum"
    convolution_gauss_ratio = 0.3
    convolution_truncation = 15
    convolution_width_1_const = 2
    convolution_width_2_const = 2
    result = np.array([0.00185521, 0.00224239, 0.00276455, 0.00349236, 0.00454931, 0.00616702, 0.00882306, 0.01372258, 0.02583351, 0.0684331, 0.19213544, 0.31199397, 0.19213524, 0.06843296, 0.02583342, 0.01372252, 0.00882301, 0.00616698, 0.00454927, 0.00349232, 0.00276452, 0.00224235, 0.00185517])
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)
    # dcs
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.convolution_stack()
    function_result = my_conv.destination_intensity
    assert list_compare(result, function_result, 10 ** 0)


# extrapolation modes
def test_parabol_1_extrapolation_modes():
    spectrum_file_path = "math_examples/parabol_short.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_const = 1
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    # zeros
    convolution_extrapolation_type = 0  # ["zeros", "constant", "average constant", "linear regression"]
    result = np.array([0.09016998, 0.42126126, 1.17999156, 2.43033555, 4.18033993, 6.43033995, 9.18033995, 12.43033995, 16.18033995, 20.43033995, 25.18033995, 30.43033995, 36.18033995, 42.43033995, 49.18033995, 56.43033976, 64.1802208, 72.41019799, 80.2560007, 78.20431302, 47.17170859])
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    assert list_compare(my_conv.destination_intensity_getter(), result, 10 ** 0)
    # constant
    convolution_extrapolation_type = 1  # ["zeros", "constant", "average constant", "linear regression"]
    result = np.array([0.125, 0.48116505, 1.24855782, 2.49994914, 4.24999923, 6.5, 9.25, 12.5, 16.25, 20.5, 25.25, 30.5, 36.25, 42.5, 49.25, 56.49999946, 64.24992782, 72.49612908, 81.16366879, 89.64809101, 96.13571018])
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    assert list_compare(my_conv.destination_intensity_getter(), result, 10 ** 0)
    # average constant
    convolution_extrapolation_type = 2  # ["zeros", "constant", "average constant", "linear regression"]
    result = np.array([0.125, 0.48116505, 1.24855782, 2.49994914, 4.24999923, 6.5, 9.25, 12.5, 16.25, 20.5, 25.25, 30.5, 36.25, 42.5, 49.25, 56.49999946, 64.24992782, 72.49612908, 81.16366879, 89.64809101, 96.13571018])
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    assert list_compare(my_conv.destination_intensity_getter(), result, 10 ** 0)
    # linear regression
    convolution_extrapolation_type = 3  # ["zeros", "constant", "average constant", "linear regression"]
    result = np.array([0.11692222, 0.47946766, 1.2483836, 2.49994124, 4.24999908, 6.49999999, 9.25, 12.5, 16.25, 20.5, 25.25, 30.5, 36.25, 42.5, 49.25, 56.49999999, 64.24999908, 72.49994124, 81.2483836, 90.47946766, 100.11692222])
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    assert list_compare(my_conv.destination_intensity_getter(), result, 10 ** 0)


# data test
def test_data_test_correct_ascending_ascending():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    assert my_conv.spectrum_wavelength_bounds_check() == []


def test_data_test_correct_descending_ascending():
    spectrum_file_path = "NH_case/spectrum_A_descending.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    assert my_conv.spectrum_wavelength_bounds_check() == []


def test_data_test_correct_ascending_descending():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm_descending.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm_descending.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    assert my_conv.spectrum_wavelength_bounds_check() == []


def test_data_test_correct_descending_descending():
    spectrum_file_path = "NH_case/spectrum_A_descending.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm_descending.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "NH_case/ref_cm_descending.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    my_conv = conv_core.ConvolutionCore()
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    assert my_conv.spectrum_wavelength_bounds_check() == []


def test_data_test_gauss_spectrum_wavelength_too_short_ascending_ascending():
    spectrum_file_path = "data_verif/spectrum_short.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "data_verif/ref_wth_top.txt"
    convolution_width_1_column = 1
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3852.3284599999997 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8485.16354 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3852.3284599999997 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8485.16354 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_gauss_spectrum_wavelength_too_short_descending_ascending():
    spectrum_file_path = "data_verif/spectrum_short_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "data_verif/ref_wth_top.txt"
    convolution_width_1_column = 1
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3852.3284599999997 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8485.16354 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3852.3284599999997 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8485.16354 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_gauss_spectrum_wavelength_too_short_ascending_descending():
    spectrum_file_path = "data_verif/spectrum_short.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top_descending.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "data_verif/ref_wth_top_descending.txt"
    convolution_width_1_column = 1
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3852.3284599999997 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8485.16354 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3852.3284599999997 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8485.16354 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_gauss_spectrum_wavelength_too_short_descending_descending():
    spectrum_file_path = "data_verif/spectrum_short_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top_descending.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 0  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "data_verif/ref_wth_top_descending.txt"
    convolution_width_1_column = 1
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3852.3284599999997 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8485.16354 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3852.3284599999997 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8485.16354 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_triangle_spectrum_wavelength_too_short_ascending_ascending():
    spectrum_file_path = "data_verif/spectrum_short.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # triangle
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "data_verif/ref_wth_top.txt"
    convolution_width_1_column = 1
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3969.573238 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8247.578962 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3969.573238 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8247.578962 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_triangle_spectrum_wavelength_too_short_descending_ascending():
    spectrum_file_path = "data_verif/spectrum_short_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # triangle
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "data_verif/ref_wth_top.txt"
    convolution_width_1_column = 1
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3969.573238 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8247.578962 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3969.573238 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8247.578962 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_triangle_spectrum_wavelength_too_short_ascending_descending():
    spectrum_file_path = "data_verif/spectrum_short.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top_descending.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # triangle
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "data_verif/ref_wth_top_descending.txt"
    convolution_width_1_column = 1
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3969.573238 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8247.578962 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3969.573238 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8247.578962 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_triangle_spectrum_wavelength_too_short_descending_descending():
    spectrum_file_path = "data_verif/spectrum_short_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top_descending.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # triangle
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "data_verif/ref_wth_top_descending.txt"
    convolution_width_1_column = 1
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3969.573238 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8247.578962 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3969.573238 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8247.578962 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_trapeze_spectrum_wavelength_too_short_ascending_ascending():
    spectrum_file_path = "data_verif/spectrum_short.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # trapeze
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "data_verif/ref_wth_top.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3961.198611 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8264.549289 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3961.198611 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8264.549289 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_trapeze_spectrum_wavelength_too_short_descending_ascending():
    spectrum_file_path = "data_verif/spectrum_short_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # trapeze
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "data_verif/ref_wth_top.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3961.198611 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8264.549289 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3961.198611 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8264.549289 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_trapeze_spectrum_wavelength_too_short_ascending_descending():
    spectrum_file_path = "data_verif/spectrum_short.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top_descending.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # trapeze
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "data_verif/ref_wth_top_descending.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3961.198611 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8264.549289 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its minimum. Recommended value is lesser than 3961.198611 cm-1.", "Spectrum wavelength is too short at its maximum. Recommended value is grater than 8264.549289 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_data_test_trapeze_spectrum_wavelength_too_short_descending_descending():
    spectrum_file_path = "data_verif/spectrum_short_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_file_path = "data_verif/ref_wth_top_descending.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # trapeze
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_file_path = "data_verif/ref_wth_top_descending.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    my_conv = conv_core.ConvolutionCore()
    # sdc
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3961.198611 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8264.549289 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result
    # dcs
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, convolution_width_2_column)
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    result = ["Spectrum wavelength is too short at its maximum. Recommended value is grater than 3961.198611 cm-1.", "Spectrum wavelength is too short at its minimum. Recommended value is lesser than 8264.549289 cm-1."]
    data_test_result = my_conv.spectrum_wavelength_bounds_check()
    assert len(data_test_result) == 2
    assert data_test_result == result


def test_scientific_dirac_test():
    spectrum_file_path = "math_examples/dirac.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.1
    convolution_extrapolation_type = 0  # "zeros"
    convolution_gauss_ratio = 0.5
    convolution_width_1_const = 0.5
    convolution_width_2_const = 0.25
    # gauss
    convolution_type = 0
    convolution_truncation = 10
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    spectrum_area = np.trapz(my_conv.spectrum_intensity, dx=(my_conv.spectrum_wavelength[1] - my_conv.spectrum_wavelength[0]))
    convolution_area = np.trapz(my_conv.destination_intensity_getter(), dx=(my_conv.destination_wavelength[1] - my_conv.destination_wavelength[0]))
    assert np.fabs(spectrum_area - convolution_area) < 10 ** -10
    # triangle
    convolution_type = 1
    convolution_truncation = 3
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    spectrum_area = np.trapz(my_conv.spectrum_intensity, dx=(my_conv.spectrum_wavelength[1] - my_conv.spectrum_wavelength[0]))
    convolution_area = np.trapz(my_conv.destination_intensity_getter(), dx=(my_conv.destination_wavelength[1] - my_conv.destination_wavelength[0]))
    assert np.fabs(spectrum_area - convolution_area) < 10 ** -10
    # trapeze
    convolution_type = 2
    convolution_truncation = 3
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    spectrum_area = np.trapz(my_conv.spectrum_intensity, dx=(my_conv.spectrum_wavelength[1] - my_conv.spectrum_wavelength[0]))
    convolution_area = np.trapz(my_conv.destination_intensity_getter(), dx=(my_conv.destination_wavelength[1] - my_conv.destination_wavelength[0]))
    assert np.fabs(spectrum_area - convolution_area) < 10 ** -10
    # Lorentz
    convolution_type = 3
    convolution_truncation = 15
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    spectrum_area = np.trapz(my_conv.spectrum_intensity, dx=(my_conv.spectrum_wavelength[1] - my_conv.spectrum_wavelength[0]))
    convolution_area = np.trapz(my_conv.destination_intensity_getter(), dx=(my_conv.destination_wavelength[1] - my_conv.destination_wavelength[0]))
    assert np.fabs(spectrum_area - convolution_area) < 10 ** -6
    # Voigt
    convolution_type = 4
    convolution_truncation = 15
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    spectrum_area = np.trapz(my_conv.spectrum_intensity, dx=(my_conv.spectrum_wavelength[1] - my_conv.spectrum_wavelength[0]))
    convolution_area = np.trapz(my_conv.destination_intensity_getter(), dx=(my_conv.destination_wavelength[1] - my_conv.destination_wavelength[0]))
    assert np.fabs(spectrum_area - convolution_area) < 10 ** -5
    # Gauss & Lorentz
    convolution_type = 5
    convolution_truncation = 15
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, spectrum_file_path, np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_start, destination_stop, destination_step)
    my_conv.convolution_setter_width_constant(convolution_type, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    spectrum_area = np.trapz(my_conv.spectrum_intensity, dx=(my_conv.spectrum_wavelength[1] - my_conv.spectrum_wavelength[0]))
    convolution_area = np.trapz(my_conv.destination_intensity_getter(), dx=(my_conv.destination_wavelength[1] - my_conv.destination_wavelength[0]))
    assert np.fabs(spectrum_area - convolution_area) < 10 ** -5
