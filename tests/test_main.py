# coding: utf-8

# PACKAGES
import os
import sys
import filecmp

# MODULES
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from list_compare import list_compare
import main
from main import *
from tools import data_pars

# test QApp
test_app = QApplication(sys.argv)


# app tests: different units, different input types, Gauss, triangle & trapeze functions
# unit unit file gauss file
def test_unit_unit_file_gauss_file():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1 # "Gauss function"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit file gauss linear
def test_unit_unit_file_gauss_linear():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit file gauss constant
def test_unit_unit_file_gauss_constant():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit file triangle file
def test_unit_unit_file_triangle_file():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit file triangle linear
def test_unit_unit_file_triangle_linear():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit file triangle constant
def test_unit_unit_file_triangle_constant():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.5
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit file trapeze file
def test_unit_unit_file_trapeze_file():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit file trapeze linear
def test_unit_unit_file_trapeze_linear():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    convolution_width_2_start = 2.557569
    convolution_width_2_stop = 5.182652
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit file trapeze constant
def test_unit_unit_file_trapeze_constant():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.740221
    convolution_width_2_const = 3.8701105
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit linear gauss file: hard to make as the file length must correspond to the linear destination
# unit unit linear gauss linear
def test_unit_unit_linear_gauss_linear():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit linear gauss constant
def test_unit_unit_linear_gauss_constant_ascending_ascending():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_extrapolation_type = 0  # "zeros"
    convolution_width_1_const = 1
    result = np.array([0.25, 0.5, 1.25, 2.5, 4.25, 6.5, 9.25, 12.5, 16.25, 20.5, 25.25, 30.5, 36.25, 42.5, 49.25, 56.5, 64.25, 72.5, 81.25, 90.5, 100.25])
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


def test_unit_unit_linear_gauss_constant_descending_ascending():
    spectrum_file_path = "math_examples/parabol_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_extrapolation_type = 0  # "zeros"
    convolution_width_1_const = 1
    result = np.array([0.25, 0.5, 1.25, 2.5, 4.25, 6.5, 9.25, 12.5, 16.25, 20.5, 25.25, 30.5, 36.25, 42.5, 49.25, 56.5, 64.25, 72.5, 81.25, 90.5, 100.25])
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


def test_unit_unit_linear_gauss_constant_ascending_descending():
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 10
    destination_stop = 0
    destination_step = 0.5
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_extrapolation_type = 0  # "zeros"
    convolution_width_1_const = 1
    result = np.flip(np.array([0.25, 0.5, 1.25, 2.5, 4.25, 6.5, 9.25, 12.5, 16.25, 20.5, 25.25, 30.5, 36.25, 42.5, 49.25, 56.5, 64.25, 72.5, 81.25, 90.5, 100.25]))
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


def test_unit_unit_linear_gauss_constant_descending_descending():
    spectrum_file_path = "math_examples/parabol_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 10
    destination_stop = 0
    destination_step = 0.5
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_extrapolation_type = 0  # "zeros"
    convolution_width_1_const = 1
    result = np.flip(np.array([0.25, 0.5, 1.25, 2.5, 4.25, 6.5, 9.25, 12.5, 16.25, 20.5, 25.25, 30.5, 36.25, 42.5, 49.25, 56.5, 64.25, 72.5, 81.25, 90.5, 100.25]))
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit linear triangle file: hard to make as the file length must correspond to the linear destination
# unit unit linear triangle linear
def test_unit_unit_linear_triangle_linear():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit linear triangle constant
def test_unit_unit_linear_triangle_constant():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit linear trapeze file: hard to make as the file length must correspond to the linear destination
# unit unit linear trapeze linear
def test_unit_unit_linear_trapeze_linear():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    convolution_width_2_start = 2.557569
    convolution_width_2_stop = 5.182652
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit unit linear trapeze constant
def test_unit_unit_linear_trapeze_constant():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.740221
    convolution_width_2_const = 3.8701105
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 file gauss file
def test_unit1_unit2_file_gauss_file():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 file gauss linear
def test_unit1_unit2_file_gauss_linear():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron" # 2
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"  # 3
    destination_file_path = "NH_case/ref_nm.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 file gauss constant
def test_unit1_unit2_file_gauss_constant():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron" # 2
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"  # 3
    destination_file_path = "NH_case/ref_nm.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 file triangle file
def test_unit1_unit2_file_triangle_file():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 file triangle linear
def test_unit1_unit2_file_triangle_linear():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron" # 2
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"  # 3
    destination_file_path = "NH_case/ref_nm.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 file triangle constant
def test_unit1_unit2_file_triangle_constant():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron" # 2
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"  # 3
    destination_file_path = "NH_case/ref_nm.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 file trapeze file
def test_unit1_unit2_file_trapeze_file():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 file trapeze linear
def test_unit1_unit2_file_trapeze_linear():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 file trapeze constant
def test_unit1_unit2_file_trapeze_constant():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron" # 2
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"  # 3
    destination_file_path = "NH_case/ref_nm.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.740221
    convolution_width_2_const = 3.8701105
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 linear gauss file
def test_unit1_unit2_linear_gauss_file():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 linear gauss linear
def test1_unit2_unit_linear_gauss_linear():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 linear gauss constant
def test1_unit2_unit_linear_gauss_constant():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "gauss"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 linear triangle file: hard to make as the file length must correspond to the linear destination
# unit1 unit2 linear triangle linear
def test_unit1_unit2_linear_triangle_linear():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 linear triangle constant
def test1_unit2_unit_linear_triangle_constant():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 linear trapeze file
def test_unit1_unit2_linear_trapeze_file():
    spectrum_file_path = "NH_case/spectrum_nm.txt"
    spectrum_unit = "nm"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 linear trapeze linear
def test_unit1_unit2_linear_trapeze_linear():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 unit2 linear trapeze constant
def test_unit1_unit2_linear_trapeze_constant():
    spectrum_file_path = "NH_case/spectrum_micron.txt"
    spectrum_unit = "micron"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "A"
    destination_start = 12276.33
    destination_stop = 24876.73
    destination_step = 63.96142131
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(2)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 file gauss file
def test_unit1_1_unit2_file_gauss_file():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 file gauss linear
def test_unit1_1_unit2_file_gauss_linear():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"  # 1
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"  # 3
    destination_file_path = "NH_case/ref_nm.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 file gauss constant
def test_unit1_1_unit2_file_gauss_constant():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1" # 1
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"  # 3
    destination_file_path = "NH_case/ref_nm.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 file triangle file
def test_unit1_1_unit2_file_triangle_file():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 file triangle linear
def test_unit1_1_unit2_file_triangle_linear():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"  # 1
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"  # 3
    destination_file_path = "NH_case/ref_nm.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 file triangle constant
def test_unit1_1_unit2_file_triangle_constant():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1" # 1
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"  # 3
    destination_file_path = "NH_case/ref_nm.txt"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 file trapeze file
def test_unit1_1_unit2_file_trapeze_file():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 file trapeze linear
def test_unit1_1_unit2_file_trapeze_linear():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 file trapeze constant
def test_unit1_1_unit2_file_trapeze_constant():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 linear gauss file: hard to make as the file length must correspond to the linear destination
# unit1 1/unit2 linear gauss linear
def test1_1_unit2_unit_linear_gauss_linear():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 linear gauss constant
def test1_1_unit2_unit_linear_gauss_constant():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "gauss"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 linear triangle file: hard to make as the file length must correspond to the linear destination
# unit1 1/unit2 linear triangle linear
def test1_1_unit2_unit_linear_triangle_linear():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, np.NAN, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 linear triangle constant
def test1_1_unit2_unit_linear_triangle_constant():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 2  # "triangle"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 linear trapeze file: hard to make as the file length must correspond to the linear destination
# unit1 1/unit2 linear trapeze linear
def test1_1_unit2_unit_linear_trapeze_linear():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    convolution_width_2_start = 2.557569
    convolution_width_2_stop = 5.182652
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_linear_function(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_start, convolution_width_1_stop, convolution_width_2_start, convolution_width_2_stop)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# unit1 1/unit2 linear trapeze constant
def test1_1_unit2_unit_linear_trapeze_constant():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.740221
    convolution_width_2_const = 3.8701105
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, convolution_width_2_const)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# Real case, from file, different units
def test_convolution_calc_a_few_calcs_sdc():
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    # calc 1: file_nh_a_a_trap
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    # calc 2: file_nh_a_cm_gauss
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
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
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    # calc 3: file_nh_cm_a_trap():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    # case 4: file_linear_t_A_cm():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.conv_wdth_1_start.setValue(convolution_width_1_stop)
    win.conv_wdth_1_stop.setValue(convolution_width_1_start)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_1_stop.setValue(convolution_width_2_stop)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


def test_convolution_calc_a_few_calcs_dcs():
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    # calc 1: file_nh_a_a_trap
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    # calc 2: file_nh_a_cm_gauss
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
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
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    # calc 3: file_nh_cm_a_trap():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_A.txt"
    destination_unit = "A"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(4)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    # case 4: file_linear_t_A_cm():
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # "trapeze"
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
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.conv_wdth_1_start.setValue(convolution_width_1_stop)
    win.conv_wdth_1_stop.setValue(convolution_width_1_start)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_1_stop.setValue(convolution_width_2_stop)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# app tests: different units, different input types, Lorentz and Lorentz+Gauss functions
def test_Lorentz():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 4  # "Lorentz"
    convolution_gauss_ratio = 0
    convolution_truncation = 15
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


def test_Voigt():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 5  # "Voigt"
    convolution_gauss_ratio = 0.5
    convolution_truncation = 15
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


def test_Lorentz_and_Gauss():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 6 # "Lorentz&Gauss"
    convolution_gauss_ratio = 0.5
    convolution_truncation = 15
    convolution_width_1_const = 7.740221
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_linear_function(destination_unit, destination_wavelength_start, destination_wavelength_stop, destination_wavelength_step)
    my_conv.convolution_setter_width_constant(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_width_1_const, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# app tests: extrapolation types
def test_extrapolation_modes():
    spectrum_file_path = "math_examples/parabol_short.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_width_1_const = 1
    my_conv = conv_core.ConvolutionCore()
    # zeros
    convolution_extrapolation_type = 0  # ["zeros", "constant", "average constant", "linear regression"]
    result = np.array([0.09016998, 0.42126126, 1.17999156, 2.43033555, 4.18033993, 6.43033995, 9.18033995, 12.43033995, 16.18033995, 20.43033995, 25.18033995, 30.43033995, 36.18033995, 42.43033995, 49.18033995, 56.43033976, 64.1802208, 72.41019799, 80.2560007, 78.20431302, 47.17170859])
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # constant
    convolution_extrapolation_type = 1  # ["zeros", "constant", "average constant", "linear regression"]
    result = np.array([0.125, 0.48116505, 1.24855782, 2.49994914, 4.24999923, 6.5, 9.25, 12.5, 16.25, 20.5, 25.25, 30.5, 36.25, 42.5, 49.25, 56.49999946, 64.24992782, 72.49612908, 81.16366879, 89.64809101, 96.13571018])
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # average constant
    convolution_extrapolation_type = 2  # ["zeros", "constant", "average constant", "linear regression"]
    result = np.array([0.125, 0.48116505, 1.24855782, 2.49994914, 4.24999923, 6.5, 9.25, 12.5, 16.25, 20.5, 25.25, 30.5, 36.25, 42.5, 49.25, 56.49999946, 64.24992782, 72.49612908, 81.16366879, 89.64809101, 96.13571018])
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # linear regression
    convolution_extrapolation_type = 3  # ["zeros", "constant", "average constant", "linear regression"]
    result = np.array([0.11692222, 0.47946766, 1.2483836, 2.49994124, 4.24999908, 6.49999999, 9.25, 12.5, 16.25, 20.5, 25.25, 30.5, 36.25, 42.5, 49.25, 56.49999999, 64.24999908, 72.49994124, 81.2483836, 90.47946766, 100.11692222])
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()
    # dcs, sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True  # Extrapolation demand is expected
    ## dcs
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


# app test: warnings convolution applicability
def test_applicability_conditions():
    # No asserts here, only warnings
    spectrum_file_path = "math_examples/parabol_short.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_unit = "cm-1"
    destination_start = 0
    destination_stop = 10
    convolution_type = 1  # "Gauss function"
    convolution_extrapolation_type = 0
    convolution_gauss_ratio = 0
    # extrapolation only
    destination_step = 0.1
    convolution_truncation = 10
    convolution_width_1_const = 1
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()  # Warning "extrapolation" is expected
    # width < 2 * step
    destination_step = 2
    convolution_truncation = 10
    convolution_width_1_const = 1
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()  # Warnings "width < 2 * step" & "extrapolation" are expected
    # truncation < n * width
    destination_step = 2
    convolution_truncation = 1
    convolution_width_1_const = 1
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(3)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()  # Warnings "width < 2 * step", "truncation < n * width" & "extrapolation" are expected



# interface test
# spctrm_file_select_action
def test_spctrm_file_select_action_normal():
    # 2 columns
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/spectrum_A.txt"
    win.file_select_action(file_path, "spectrum")
    assert win.my_conv.spectrum_file_path == file_path  # sets up spectrum_file_path
    assert win.ui.spctrm_path_lbl.text() == "spectrum_A.txt"  # changes spctrm_path_lbl
    assert win.ui.spctrm_wlth_clm.count() == 3  # reads the spectrum file and sets up wavelength and intensity columns
    assert win.ui.spctrm_wlth_clm.itemText(0) == "Select column"
    assert win.ui.spctrm_wlth_clm.itemText(1) == "1"
    assert win.ui.spctrm_wlth_clm.itemText(2) == "2"
    assert win.ui.spctrm_inty_clm.count() == 3
    assert win.ui.spctrm_inty_clm.itemText(0) == "Select column"
    assert win.ui.spctrm_inty_clm.itemText(1) == "1"
    assert win.ui.spctrm_inty_clm.itemText(2) == "2"
    win.close()
    # 3 columns
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/ref_A.txt"
    win.file_select_action(file_path, "spectrum")
    assert win.my_conv.spectrum_file_path == file_path
    assert win.ui.spctrm_path_lbl.text() == "ref_A.txt"
    assert win.ui.spctrm_wlth_clm.count() == 4
    assert win.ui.spctrm_wlth_clm.itemText(0) == "Select column"
    assert win.ui.spctrm_wlth_clm.itemText(1) == "1"
    assert win.ui.spctrm_wlth_clm.itemText(2) == "2"
    assert win.ui.spctrm_wlth_clm.itemText(3) == "3"
    assert win.ui.spctrm_inty_clm.count() == 4
    assert win.ui.spctrm_inty_clm.itemText(0) == "Select column"
    assert win.ui.spctrm_inty_clm.itemText(1) == "1"
    assert win.ui.spctrm_inty_clm.itemText(2) == "2"
    assert win.ui.spctrm_inty_clm.itemText(3) == "3"
    win.close()


def test_spctrm_file_select_action_error():  # changes spctrm_path_lbl & spctrm_file styles
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    win.convolution_calc()  # Warning "No spectrum file found" is expected
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_ERROR
    assert win.ui.spctrm_file.styleSheet() == main.BTN_ERROR
    win.spectrum_plot()
    file_path = "NH_case/spectrum_A.txt"
    win.file_select_action(file_path, "spectrum")
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    win.close()


# spctrm_file_del
def test_spctrm_file_del():
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/spectrum_A.txt"
    win.file_select_action(file_path, "spectrum")
    win.file_del("spectrum")
    assert win.my_conv.spectrum_file_path == ""
    assert win.ui.spctrm_path_lbl.text() == "no file selected"
    assert win.ui.spctrm_wlth_clm.count() == 1
    assert win.ui.spctrm_wlth_clm.itemText(0) == "Select column"
    assert win.ui.spctrm_inty_clm.count() == 1
    assert win.ui.spctrm_inty_clm.itemText(0) == "Select column"
    win.close()


# spctrm_wdth_file_select_action
def test_spctrm_wdth_file_select_action_normal():
    # call from spctrm_file_select_action: 2 columns
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/spectrum_A.txt"
    win.file_select_action(file_path, "spectrum")
    assert win.my_conv.spectrum_width_path == ""
    assert win.ui.spctrm_wdth_path_lbl.text() == "no file selected"
    assert win.ui.spctrm_wdth_clm.count() == 1
    assert win.ui.spctrm_inty_clm.itemText(0) == "Select column"
    win.close()
    # call from spctrm_file_select_action: 3 columns
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/ref_A.txt"
    win.file_select_action(file_path, "spectrum")
    assert win.my_conv.spectrum_width_path == file_path
    assert win.ui.spctrm_wdth_path_lbl.text() == "ref_A.txt"
    assert win.ui.spctrm_wdth_clm.count() == 4
    assert win.ui.spctrm_wdth_clm.itemText(0) == "Select column"
    assert win.ui.spctrm_wdth_clm.itemText(1) == "1"
    assert win.ui.spctrm_wdth_clm.itemText(2) == "2"
    assert win.ui.spctrm_wdth_clm.itemText(2) == "2"
    win.close()
    # 2 columns
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/spectrum_A.txt"
    win.file_select_action(file_path, "spectrum_width")
    assert win.my_conv.spectrum_width_path == file_path
    assert win.ui.spctrm_wdth_path_lbl.text() == "spectrum_A.txt"
    assert win.ui.spctrm_wdth_clm.count() == 3
    assert win.ui.spctrm_wdth_clm.itemText(0) == "Select column"
    assert win.ui.spctrm_wdth_clm.itemText(1) == "1"
    assert win.ui.spctrm_wdth_clm.itemText(2) == "2"
    win.close()
    # 3 columns
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/ref_A.txt"
    win.file_select_action(file_path, "spectrum_width")
    assert win.my_conv.spectrum_width_path == file_path
    assert win.ui.spctrm_wdth_path_lbl.text() == "ref_A.txt"
    assert win.ui.spctrm_wdth_clm.count() == 4
    assert win.ui.spctrm_wdth_clm.itemText(0) == "Select column"
    assert win.ui.spctrm_wdth_clm.itemText(1) == "1"
    assert win.ui.spctrm_wdth_clm.itemText(2) == "2"
    assert win.ui.spctrm_wdth_clm.itemText(3) == "3"
    win.close()


# spctrm_wdth_file_del
def test_spctrm_wdth_file_del():
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/spectrum_A.txt"
    win.file_select_action(file_path, "spectrum_width")
    win.file_del("spectrum_width")
    assert win.my_conv.spectrum_width_path == ""
    assert win.ui.spctrm_wdth_path_lbl.text() == "no file selected"
    assert win.ui.spctrm_wdth_clm.count() == 1
    assert win.ui.spctrm_wdth_clm.itemText(0) == "Select column"
    win.close()


# spctrm_plot
def test_spctrm_plot_error():  # changes spctrm_unit, spctrm_wlth_clm & spctrm_inty_clm styles
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/spectrum_A.txt"
    win.file_select_action(file_path, "spectrum")
    win.convolution_calc()  # Warning "No spectrum unit given" is expected
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_ERROR
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.spectrum_plot()
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    win.convolution_calc()  # Warning "No spectrum wavelength column given" is expected
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_ERROR
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    win.ui.spctrm_wlth_clm.setCurrentIndex(1)
    win.spectrum_plot()
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    win.convolution_calc()  # Warning "No spectrum intensity column given" is expected
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_ERROR
    win.ui.spctrm_inty_clm.setCurrentIndex(1)
    win.spectrum_plot()
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    win.close()
    """
        If not all spectrum data has been set up, spctrm_plot should not change the graph.
    """
    win.close()


def test_spctrm_plot_regular():
    # input data correct
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "math_examples/gauss_descending.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)  # spctrm_plot runs when all the date is set up
    assert win.my_conv.spectrum_unit_original == spectrum_unit
    assert win.my_conv.spectrum_set_up
    """
        The function spctrm_plot changes the graph as follows: 
        1. it changes the units of x-axe (it sets the destination unit if known and otherwise the spectrum one); 
        2. it plots the spectrum; 
        3. it removes the convolution result graph; 
        4. it changes the direction of the axes if the unit is cm-1.
        I haven't found how to check these changes automatically through unit-tests. 
    """
    win.close()


# export_a_preset
def test_export_a_preset():
    # empty
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    result = ("preset: \ndestination\n\tunit: 0\n\ttab: 0\n\tpath: \n\tcolumn: 0\n\tstart: 0.0\n\tend: 10.0\n\tstep: 0.1\nconvolution\n\ttab: 0\n\tfunction: 0\n\tratio: 0.5\n\ttruncation: 10.0\n\textrapolation: 0\n\tpath: \n\twidth_1 column: 0\n\twidth_2 column: 0\n\twidth_1 start: 0.0\n\twidth_1 end: 5.0\n\twidth_2 start: 0.0\n\twidth_2 end: 2.5\n\twidth_1 const: 2.5\n\twidth_2 const: 1.5\n")
    str_result = win.export_a_preset_action()
    assert str_result == result
    # filled
    destination_tab = 1
    destination_unit = 2  # "micron"
    destination_file_path = "NH_case/ref_micron.txt"
    destination_wavelength_column = 1
    destination_start = 20.369
    destination_stop = -10.18694
    destination_step = 1.147
    convolution_tab = 2
    convolution_function = 3
    convolution_gauss_ration = 0.75
    convolution_truncation = 7.5
    convolution_extrapolation_type = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 2
    convolution_width_2_column = 3
    convolution_width_1_start = 14.569
    convolution_width_1_stop = 28.564
    convolution_width_2_start = 7.159
    convolution_width_2_stop = 13.987
    convolution_width_1_const = 20.123
    convolution_width_2_const = 10.321
    result = ("preset: \ndestination\n\tunit: 2\n\ttab: 1\n\tpath: NH_case/ref_micron.txt\n\tcolumn: 1\n\tstart: 20.369\n\tend: -10.18694\n\tstep: 1.147\nconvolution\n\ttab: 2\n\tfunction: 3\n\tratio: 0.75\n\ttruncation: 7.5\n\textrapolation: 3\n\tpath: NH_case/ref_micron.txt\n\twidth_1 column: 2\n\twidth_2 column: 3\n\twidth_1 start: 14.569\n\twidth_1 end: 28.564\n\twidth_2 start: 7.159\n\twidth_2 end: 13.987\n\twidth_1 const: 20.123\n\twidth_2 const: 10.321\n")
    win.ui.dstntn_tab.setCurrentIndex(destination_tab)
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    win.conv_type.setCurrentIndex(convolution_function)
    win.conv_gauss_part.setValue(convolution_gauss_ration)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(convolution_tab)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    str_result = win.export_a_preset_action()
    assert str_result == result
    win.close()


def test_import_a_preset():
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    # full correct
    preset_name = ""
    destination_tab = 1
    destination_unit = 3
    destination_file_path = "C:/Users/flex_virt/Dev/Convolution_dev/tests/NH_case/ref_nm.txt"
    destination_wavelength_column = 1
    destination_start = 1200.0
    destination_stop = 2800.0
    destination_step = 10
    convolution_tab = 1
    convolution_function = 4
    convolution_gauss_ration = 0.54
    convolution_truncation = 15
    convolution_extrapolation_type = 2
    convolution_file_path = "C:/Users/flex_virt/Dev/Convolution_dev/tests/NH_case/spectrum_micron.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    convolution_width_1_start = 12.56
    convolution_width_1_stop = 17.85
    convolution_width_2_start = 7.123
    convolution_width_2_stop = 10.987
    convolution_width_1_const = 4.639
    convolution_width_2_const = 2.123456789123457
    preset_file_path = "C:/Users/flex_virt/Dev/Convolution_dev/tests/presets/convolution_preset_full.txt"
    win.import_a_preset_action(preset_file_path)
    assert win.preset_name == preset_name
    assert win.ui.dstntn_tab.currentIndex() == destination_tab
    assert win.ui.dstntn_unit.currentIndex() == destination_unit
    assert win.my_conv.destination_file_path == destination_file_path
    assert win.ui.dstntn_path_lbl.text() == "ref_nm.txt"
    assert win.ui.dstntn_wlth_clm.currentIndex() == destination_wavelength_column
    assert win.dstntn_linear_start.value() == destination_start
    assert win.dstntn_linear_stop.value() == destination_stop
    assert win.dstntn_linear_step.value() == destination_step
    assert win.conv_type.currentIndex() == convolution_function
    assert win.conv_gauss_part.value() == convolution_gauss_ration
    assert win.conv_truncation.value() == convolution_truncation
    assert win.conv_extrap.currentIndex() == convolution_extrapolation_type
    assert win.ui.conv_tab.currentIndex() == convolution_tab
    assert win.my_conv.convolution_file_path == convolution_file_path
    assert win.ui.conv_path_lbl.text() == "spectrum_micron.txt"
    assert win.ui.conv_wdth_1_clm.currentIndex() == convolution_width_1_column
    assert win.ui.conv_wdth_2_clm.currentIndex() == convolution_width_2_column
    assert win.conv_wdth_1_start.value() == convolution_width_1_start
    assert win.conv_wdth_1_stop.value() == convolution_width_1_stop
    assert win.conv_wdth_2_start.value() == convolution_width_2_start
    assert win.conv_wdth_2_stop.value() == convolution_width_2_stop
    assert win.conv_wdth_1_const.value() == convolution_width_1_const
    assert win.conv_wdth_2_const.value() == convolution_width_2_const
    # empty
    preset_name = ""
    destination_tab = 0
    destination_unit = 0
    destination_file_path = ""
    destination_wavelength_column = 0
    destination_start = 0
    destination_stop = 10
    destination_step = 1
    convolution_tab = 0
    convolution_function = 0
    convolution_gauss_ration = 0.5
    convolution_truncation = 0
    convolution_extrapolation_type = 0
    convolution_file_path = ""
    convolution_width_1_column = 0
    convolution_width_2_column = 0
    convolution_width_1_start = 1e-06
    convolution_width_1_stop = 10.0
    convolution_width_2_start = 1e-06
    convolution_width_2_stop = 10.0
    convolution_width_1_const = 1e-06
    convolution_width_2_const = 1e-06
    preset_file_path = "presets/convolution_preset_empty.txt"
    win.import_a_preset_action(preset_file_path)
    assert win.preset_name == preset_name
    assert win.ui.dstntn_tab.currentIndex() == destination_tab
    assert win.ui.dstntn_unit.currentIndex() == destination_unit
    assert win.my_conv.destination_file_path == destination_file_path
    assert win.ui.dstntn_path_lbl.text() == "no file selected"
    assert win.ui.dstntn_wlth_clm.currentIndex() == destination_wavelength_column
    assert win.dstntn_linear_start.value() == destination_start
    assert win.dstntn_linear_stop.value() == destination_stop
    assert win.dstntn_linear_step.value() == destination_step
    assert win.conv_type.currentIndex() == convolution_function
    assert win.conv_gauss_part.value() == convolution_gauss_ration
    assert win.conv_truncation.value() == convolution_truncation
    assert win.conv_extrap.currentIndex() == convolution_extrapolation_type
    assert win.ui.conv_tab.currentIndex() == convolution_tab
    assert win.my_conv.convolution_file_path == convolution_file_path
    assert win.ui.conv_path_lbl.text() == "no file selected"
    assert win.ui.conv_wdth_1_clm.currentIndex() == convolution_width_1_column
    assert win.ui.conv_wdth_2_clm.currentIndex() == convolution_width_2_column
    assert win.conv_wdth_1_start.value() == convolution_width_1_start
    assert win.conv_wdth_1_stop.value() == convolution_width_1_stop
    assert win.conv_wdth_2_start.value() == convolution_width_2_start
    assert win.conv_wdth_2_stop.value() == convolution_width_2_stop
    assert win.conv_wdth_1_const.value() == convolution_width_1_const
    assert win.conv_wdth_2_const.value() == convolution_width_2_const
    # incorrect
    preset_name = ""
    destination_tab = 0
    destination_unit = 0
    destination_file_path = ""
    destination_wavelength_column = 0
    destination_start = 0
    destination_stop = 10
    destination_step = 0.1
    convolution_tab = 0
    convolution_function = 0
    convolution_gauss_ration = 0.5454545454545454
    convolution_truncation = 3
    convolution_extrapolation_type = 0
    convolution_file_path = ""
    convolution_width_1_column = 0
    convolution_width_2_column = 0
    convolution_width_1_start = 0
    convolution_width_1_stop = 0
    convolution_width_2_start = 0
    convolution_width_2_stop = 0
    convolution_width_1_const = 0
    convolution_width_2_const = 0
    preset_file_path = "presets/convolution_preset_incorrect.txt"
    win.import_a_preset_action(preset_file_path)
    assert win.preset_name == preset_name
    assert win.ui.dstntn_tab.currentIndex() == destination_tab
    assert win.ui.dstntn_unit.currentIndex() == destination_unit
    assert win.my_conv.destination_file_path == destination_file_path
    assert win.ui.dstntn_path_lbl.text() == "no file selected"
    assert win.ui.dstntn_wlth_clm.currentIndex() == destination_wavelength_column
    assert win.dstntn_linear_start.value() == destination_start
    assert win.dstntn_linear_stop.value() == destination_stop
    assert win.dstntn_linear_step.value() == destination_step
    assert win.conv_type.currentIndex() == convolution_function
    assert win.conv_gauss_part.value() == convolution_gauss_ration
    assert win.conv_truncation.value() == convolution_truncation
    assert win.conv_extrap.currentIndex() == convolution_extrapolation_type
    assert win.ui.conv_tab.currentIndex() == convolution_tab
    assert win.my_conv.convolution_file_path == convolution_file_path
    assert win.ui.conv_path_lbl.text() == "no file selected"
    assert win.ui.conv_wdth_1_clm.currentIndex() == convolution_width_1_column
    assert win.ui.conv_wdth_2_clm.currentIndex() == convolution_width_2_column
    assert win.conv_wdth_1_start.value() == convolution_width_1_start
    assert win.conv_wdth_1_stop.value() == convolution_width_1_stop
    assert win.conv_wdth_2_start.value() == convolution_width_2_start
    assert win.conv_wdth_2_stop.value() == convolution_width_2_stop
    assert win.conv_wdth_1_const.value() == convolution_width_1_const
    assert win.conv_wdth_2_const.value() == convolution_width_2_const
    # wrong file
    preset_name = ""
    destination_tab = 0
    destination_unit = 0
    destination_file_path = ""
    destination_wavelength_column = 0
    destination_start = 0
    destination_stop = 10
    destination_step = 0.1
    convolution_tab = 0
    convolution_function = 0
    convolution_gauss_ration = 0.5454545454545454
    convolution_truncation = 3
    convolution_extrapolation_type = 0
    convolution_file_path = ""
    convolution_width_1_column = 0
    convolution_width_2_column = 0
    convolution_width_1_start = 0
    convolution_width_1_stop = 0
    convolution_width_2_start = 0
    convolution_width_2_stop = 0
    convolution_width_1_const = 0
    convolution_width_2_const = 0
    preset_file_path = "presets/convolution_preset_no data.txt"
    win.import_a_preset_action(preset_file_path)
    assert win.preset_name == preset_name
    assert win.ui.dstntn_tab.currentIndex() == destination_tab
    assert win.ui.dstntn_unit.currentIndex() == destination_unit
    assert win.my_conv.destination_file_path == destination_file_path
    assert win.ui.dstntn_path_lbl.text() == "no file selected"
    assert win.ui.dstntn_wlth_clm.currentIndex() == destination_wavelength_column
    assert win.dstntn_linear_start.value() == destination_start
    assert win.dstntn_linear_stop.value() == destination_stop
    assert win.dstntn_linear_step.value() == destination_step
    assert win.conv_type.currentIndex() == convolution_function
    assert win.conv_gauss_part.value() == convolution_gauss_ration
    assert win.conv_truncation.value() == convolution_truncation
    assert win.conv_extrap.currentIndex() == convolution_extrapolation_type
    assert win.ui.conv_tab.currentIndex() == convolution_tab
    assert win.my_conv.convolution_file_path == convolution_file_path
    assert win.ui.conv_path_lbl.text() == "no file selected"
    assert win.ui.conv_wdth_1_clm.currentIndex() == convolution_width_1_column
    assert win.ui.conv_wdth_2_clm.currentIndex() == convolution_width_2_column
    assert win.conv_wdth_1_start.value() == convolution_width_1_start
    assert win.conv_wdth_1_stop.value() == convolution_width_1_stop
    assert win.conv_wdth_2_start.value() == convolution_width_2_start
    assert win.conv_wdth_2_stop.value() == convolution_width_2_stop
    assert win.conv_wdth_1_const.value() == convolution_width_1_const
    assert win.conv_wdth_2_const.value() == convolution_width_2_const
    # preset LEISA New Horizons
    preset_name = "LEISA New Horizons"
    destination_tab = 0
    destination_unit = 3
    destination_file_path = ""
    destination_wavelength_column = 0
    destination_start = 0
    destination_stop = 10
    destination_step = 0.1
    convolution_tab = 0
    convolution_function = 1
    convolution_gauss_ration = 0.5454545454545454
    convolution_truncation = 10
    convolution_extrapolation_type = 0
    convolution_file_path = ""
    convolution_width_1_column = 0
    convolution_width_2_column = 0
    convolution_width_1_start = 0
    convolution_width_1_stop = 0
    convolution_width_2_start = 0
    convolution_width_2_stop = 0
    convolution_width_1_const = 0
    convolution_width_2_const = 0
    preset_file_path = "presets/convolution_preset_NH.txt"
    win.import_a_preset_action(preset_file_path)
    assert win.preset_name == preset_name
    assert win.ui.dstntn_tab.currentIndex() == destination_tab
    assert win.ui.dstntn_unit.currentIndex() == destination_unit
    assert win.my_conv.destination_file_path == destination_file_path
    assert win.ui.dstntn_path_lbl.text() == "LEISA New Horizons data"
    assert win.ui.dstntn_wlth_clm.currentIndex() == destination_wavelength_column
    assert win.dstntn_linear_start.value() == destination_start
    assert win.dstntn_linear_stop.value() == destination_stop
    assert win.dstntn_linear_step.value() == destination_step
    assert win.conv_type.currentIndex() == convolution_function
    assert win.conv_gauss_part.value() == convolution_gauss_ration
    assert win.conv_truncation.value() == convolution_truncation
    assert win.conv_extrap.currentIndex() == convolution_extrapolation_type
    assert win.ui.conv_tab.currentIndex() == convolution_tab
    assert win.my_conv.convolution_file_path == convolution_file_path
    assert win.ui.conv_path_lbl.text() == "LEISA New Horizons data"
    assert win.ui.conv_wdth_1_clm.currentIndex() == convolution_width_1_column
    assert win.ui.conv_wdth_2_clm.currentIndex() == convolution_width_2_column
    assert win.conv_wdth_1_start.value() == convolution_width_1_start
    assert win.conv_wdth_1_stop.value() == convolution_width_1_stop
    assert win.conv_wdth_2_start.value() == convolution_width_2_start
    assert win.conv_wdth_2_stop.value() == convolution_width_2_stop
    assert win.conv_wdth_1_const.value() == convolution_width_1_const
    assert win.conv_wdth_2_const.value() == convolution_width_2_const
    # preset SuperCam/VIS
    preset_name = "SuperCam/VIS"
    destination_tab = 0
    destination_unit = 3
    destination_file_path = ""
    destination_wavelength_column = 0
    destination_start = 0
    destination_stop = 10
    destination_step = 0.1
    convolution_tab = 0
    convolution_function = 3
    convolution_gauss_ration = 0.5454545454545454
    convolution_truncation = 3
    convolution_extrapolation_type = 0
    convolution_file_path = ""
    convolution_width_1_column = 0
    convolution_width_2_column = 0
    convolution_width_1_start = 0
    convolution_width_1_stop = 0
    convolution_width_2_start = 0
    convolution_width_2_stop = 0
    convolution_width_1_const = 0
    convolution_width_2_const = 0
    preset_file_path = "presets/convolution_preset_SuperCam_VIS.txt"
    win.import_a_preset_action(preset_file_path)
    assert win.preset_name == preset_name
    assert win.ui.dstntn_tab.currentIndex() == destination_tab
    assert win.ui.dstntn_unit.currentIndex() == destination_unit
    assert win.my_conv.destination_file_path == destination_file_path
    assert win.ui.dstntn_path_lbl.text() == "SuperCam/VIS data"
    assert win.ui.dstntn_wlth_clm.currentIndex() == destination_wavelength_column
    assert win.dstntn_linear_start.value() == destination_start
    assert win.dstntn_linear_stop.value() == destination_stop
    assert win.dstntn_linear_step.value() == destination_step
    assert win.conv_type.currentIndex() == convolution_function
    assert win.conv_gauss_part.value() == convolution_gauss_ration
    assert win.conv_truncation.value() == convolution_truncation
    assert win.conv_extrap.currentIndex() == convolution_extrapolation_type
    assert win.ui.conv_tab.currentIndex() == convolution_tab
    assert win.my_conv.convolution_file_path == convolution_file_path
    assert win.ui.conv_path_lbl.text() == "SuperCam/VIS data"
    assert win.ui.conv_wdth_1_clm.currentIndex() == convolution_width_1_column
    assert win.ui.conv_wdth_2_clm.currentIndex() == convolution_width_2_column
    assert win.conv_wdth_1_start.value() == convolution_width_1_start
    assert win.conv_wdth_1_stop.value() == convolution_width_1_stop
    assert win.conv_wdth_2_start.value() == convolution_width_2_start
    assert win.conv_wdth_2_stop.value() == convolution_width_2_stop
    assert win.conv_wdth_1_const.value() == convolution_width_1_const
    assert win.conv_wdth_2_const.value() == convolution_width_2_const
    win.close()


def test_selected_preset_functionality():
    # set up the usual conv_calc
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = "A"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "instrument_presets/lbd_res-true_LEISA_nm.txt"
    destination_unit = "nm"
    destination_wavelength_column = 0
    convolution_type = 1  # "Gauss function"
    convolution_truncation = 10
    convolution_gauss_ratio = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_file_path = "instrument_presets/lbd_res-true_LEISA_nm.txt"
    convolution_width_1_column = 1
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # preset data
    destination_wavelength = np.array(
        [1228.2, 1232.2, 1236.3, 1240.4, 1244.6, 1248.7, 1253.0, 1257.3, 1261.6, 1266.0, 1270.4, 1274.8, 1279.3, 1283.8, 1288.3, 1292.9, 1297.5, 1302.2, 1306.9, 1311.6, 1316.3, 1321.0, 1325.8, 1330.6, 1335.5, 1340.3, 1345.2, 1350.1, 1355.0, 1360.0, 1364.9, 1369.9, 1374.9, 1380.0, 1385.0, 1390.1, 1395.2, 1400.3, 1405.4, 1410.5, 1415.7, 1420.8, 1426.0, 1431.2, 1436.5, 1441.7, 1446.9, 1452.2, 1457.5, 1462.8, 1468.1, 1473.4, 1478.8, 1484.1, 1489.5, 1494.9, 1500.3, 1505.7, 1511.2, 1516.6, 1522.1, 1527.6, 1533.1, 1538.6, 1544.1, 1549.7, 1555.2, 1560.8, 1566.4, 1572.0, 1577.7, 1583.3, 1589.0, 1594.7, 1600.4, 1606.1, 1611.9, 1617.6, 1623.4, 1629.2, 1635.0, 1640.9, 1646.7, 1652.6, 1658.5, 1664.4, 1670.4, 1676.3, 1682.3, 1688.4, 1694.4, 1700.4, 1706.5, 1712.6, 1718.8, 1724.9, 1731.1, 1737.3, 1743.5, 1749.8, 1756.0, 1762.3, 1768.7, 1775.0, 1781.4, 1787.8, 1794.2, 1800.7, 1807.2, 1813.7, 1820.2, 1826.8, 1833.4, 1840.0, 1846.6, 1853.3, 1860.0, 1866.8, 1873.5, 1880.3, 1887.1, 1894.0, 1900.9,
         1907.8, 1914.7, 1921.7, 1928.7, 1935.7, 1942.7, 1949.8, 1956.9, 1964.1, 1971.2, 1978.4, 1985.7, 1992.9, 2000.2, 2007.5, 2014.9, 2022.3, 2029.7, 2037.1, 2044.6, 2052.0, 2059.6, 2067.1, 2074.7, 2082.3, 2089.9, 2097.6, 2105.3, 2113.0, 2120.7, 2128.5, 2136.2, 2144.1, 2151.9, 2159.8, 2167.6, 2175.6, 2183.5, 2191.5, 2199.4, 2207.4, 2215.5, 2223.5, 2231.6, 2239.7, 2247.8, 2255.9, 2264.1, 2272.2, 2280.4, 2288.6, 2296.9, 2305.1, 2313.4, 2321.6, 2329.9, 2338.2, 2346.5, 2354.8, 2363.2, 2371.5, 2379.9, 2388.3, 2396.6, 2405.0, 2413.4, 2421.8, 2430.2, 2438.6, 2447.1, 2455.5, 2463.9, 2472.3, 2480.8, 2489.2])
    convolution_width = np.array(
        [5.08571, 5.10862, 5.13200, 5.15544, 5.17936, 5.20292, 5.22809, 5.25334, 5.27866, 5.30447, 5.33035, 5.35630, 5.38275, 5.40927, 5.43586, 5.46296, 5.49013, 5.51780, 5.54554, 5.57337, 5.60128, 5.62926, 5.65775, 5.68632, 5.71541, 5.74414, 5.77339, 5.80272, 5.83214, 5.86207, 5.89165, 5.92176, 5.95195, 5.98266, 6.01302, 6.04391, 6.07489, 6.10596, 6.13712, 6.16837, 6.20015, 6.23158, 6.26354, 6.29560, 6.32819, 6.36044, 6.39278, 6.42566, 6.45626, 6.48692, 6.51765, 6.54844, 6.57976, 6.61069, 6.64214, 6.67366, 6.70525, 6.73691, 6.76909, 6.80090, 6.83322, 6.86562, 6.89809, 6.93063, 6.96325, 6.99639, 7.02915, 7.06244, 7.09581, 7.12925, 7.16322, 7.19682, 7.22273, 7.24864, 7.27455, 7.30045, 7.32682, 7.35273, 7.37909, 7.40545, 7.43182, 7.45864, 7.48500, 7.49478, 7.49393, 7.48718, 7.45922, 7.44195, 7.42532, 7.40933, 7.39307, 7.37701, 7.36155, 7.34627, 7.33159, 7.31665, 7.30229, 7.28810, 7.27405, 7.27568, 7.26370, 7.26722, 7.27112, 7.27459, 7.27845, 7.28228, 7.28609, 7.29028, 7.29445, 7.29859,
         7.30271, 7.30720, 7.31167, 7.31610, 7.32052, 7.32530, 7.34748, 7.37002, 7.39215, 7.41465, 7.43712, 7.45996, 7.48277, 7.50555, 7.52831, 7.55143, 7.57453, 7.59760, 7.62065, 7.64405, 7.66744, 7.69118, 7.71451, 7.73820, 7.76226, 7.78589, 7.80989, 7.83386, 7.85820, 7.88250, 7.90678, 7.93103, 7.95564, 7.98444, 8.00708, 8.02931, 8.05188, 8.07441, 8.09690, 8.11974, 8.14254, 8.16531, 8.18803, 8.21110, 8.23375, 8.25712, 8.28008, 8.30337, 8.32625, 8.34985, 8.37303, 8.40299, 8.43652, 8.47696, 8.52115, 8.56840, 8.61622, 8.66422, 8.71240, 8.76448, 8.81719, 8.86976, 8.92297, 8.97643, 9.03055, 9.08453, 9.13916, 9.19366, 9.24883, 9.30426, 9.35995, 9.41592, 9.47257, 9.52909, 9.58629, 9.64377, 9.70113, 9.75917, 9.81751, 9.87613, 9.93505, 9.99426, 10.05418, 10.11399, 10.17409, 10.23450, 10.29563, 10.35666])
    # preset interface calc
    ## sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## preset
    win.ui.instrument_preset.setCurrentIndex(1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_wavelength, destination_wavelength, 10 ** -10)
    assert list_compare(win.my_conv.convolution_width_1, convolution_width, 10 ** -10)
    assert list_compare(win.my_conv.destination_intensity, result, 10 ** -10)
    win.close()
    ## dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## preset
    win.ui.instrument_preset.setCurrentIndex(1)
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(4)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_wavelength, destination_wavelength, 10 ** -10)
    assert list_compare(win.my_conv.convolution_width_1, convolution_width, 10 ** -10)
    assert list_compare(win.my_conv.destination_intensity, result, 10 ** -10)
    win.close()


def test_selected_preset_interface():
    win = main.ConvolutionMainW()
    # interface
    win.ui.instrument_preset.setCurrentIndex(1)
    assert win.ui.dstntn_unit.currentIndex() == 3
    assert win.ui.dstntn_tab.currentIndex() == 0
    assert win.ui.dstntn_path_lbl.text() == "LEISA New Horizons data"
    assert win.ui.dstntn_wlth_clm.count() == 1
    assert win.ui.dstntn_wlth_clm.currentIndex() == 0
    assert win.ui.dstntn_wlth_clm.currentText() == "--"
    assert win.conv_type.currentIndex() == 1
    assert win.ui.conv_path_lbl.text() == "LEISA New Horizons data"
    assert win.ui.conv_wdth_1_clm.count() == 1
    assert win.ui.conv_wdth_1_clm.currentIndex() == 0
    assert win.ui.conv_wdth_1_clm.currentText() == "--"
    # setter
    destination_wavelength = np.array(
        [1228.2, 1232.2, 1236.3, 1240.4, 1244.6, 1248.7, 1253.0, 1257.3, 1261.6, 1266.0, 1270.4, 1274.8, 1279.3, 1283.8, 1288.3, 1292.9, 1297.5, 1302.2, 1306.9, 1311.6, 1316.3, 1321.0, 1325.8, 1330.6, 1335.5, 1340.3, 1345.2, 1350.1, 1355.0, 1360.0, 1364.9, 1369.9, 1374.9, 1380.0, 1385.0, 1390.1, 1395.2, 1400.3, 1405.4, 1410.5, 1415.7, 1420.8, 1426.0, 1431.2, 1436.5, 1441.7, 1446.9, 1452.2, 1457.5, 1462.8, 1468.1, 1473.4, 1478.8, 1484.1, 1489.5, 1494.9, 1500.3, 1505.7, 1511.2, 1516.6, 1522.1, 1527.6, 1533.1, 1538.6, 1544.1, 1549.7, 1555.2, 1560.8, 1566.4, 1572.0, 1577.7, 1583.3, 1589.0, 1594.7, 1600.4, 1606.1, 1611.9, 1617.6, 1623.4, 1629.2, 1635.0, 1640.9, 1646.7, 1652.6, 1658.5, 1664.4, 1670.4, 1676.3, 1682.3, 1688.4, 1694.4, 1700.4, 1706.5, 1712.6, 1718.8, 1724.9, 1731.1, 1737.3, 1743.5, 1749.8, 1756.0, 1762.3, 1768.7, 1775.0, 1781.4, 1787.8, 1794.2, 1800.7, 1807.2, 1813.7, 1820.2, 1826.8, 1833.4, 1840.0, 1846.6, 1853.3, 1860.0, 1866.8, 1873.5, 1880.3, 1887.1, 1894.0, 1900.9,
         1907.8, 1914.7, 1921.7, 1928.7, 1935.7, 1942.7, 1949.8, 1956.9, 1964.1, 1971.2, 1978.4, 1985.7, 1992.9, 2000.2, 2007.5, 2014.9, 2022.3, 2029.7, 2037.1, 2044.6, 2052.0, 2059.6, 2067.1, 2074.7, 2082.3, 2089.9, 2097.6, 2105.3, 2113.0, 2120.7, 2128.5, 2136.2, 2144.1, 2151.9, 2159.8, 2167.6, 2175.6, 2183.5, 2191.5, 2199.4, 2207.4, 2215.5, 2223.5, 2231.6, 2239.7, 2247.8, 2255.9, 2264.1, 2272.2, 2280.4, 2288.6, 2296.9, 2305.1, 2313.4, 2321.6, 2329.9, 2338.2, 2346.5, 2354.8, 2363.2, 2371.5, 2379.9, 2388.3, 2396.6, 2405.0, 2413.4, 2421.8, 2430.2, 2438.6, 2447.1, 2455.5, 2463.9, 2472.3, 2480.8, 2489.2])
    assert list_compare(win.my_conv.destination_wavelength, destination_wavelength, 10 ** -10)
    win.close()


# dstntn_file_select_action
def test_dstntn_file_select_action():
    # 1 column
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/dstntn_micron.txt"
    win.file_select_action(file_path, "destination")
    assert win.my_conv.destination_file_path == file_path
    assert win.ui.dstntn_path_lbl.text() == "dstntn_micron.txt"
    assert win.ui.dstntn_wlth_clm.count() == 2
    assert win.ui.dstntn_wlth_clm.itemText(0) == "Select column"
    assert win.ui.dstntn_wlth_clm.itemText(1) == "1"
    assert win.my_conv.convolution_file_path == ""
    assert win.ui.conv_path_lbl.text() == "no file selected"
    assert win.ui.conv_wdth_1_clm.count() == 1
    assert win.ui.conv_wdth_1_clm.itemText(0) == "Select column"
    assert win.ui.conv_wdth_2_clm.count() == 1
    assert win.ui.conv_wdth_2_clm.itemText(0) == "Select column"
    win.close()
    # 2 columns
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/spectrum_A.txt"
    win.file_select_action(file_path, "destination")
    assert win.my_conv.destination_file_path == file_path
    assert win.ui.dstntn_path_lbl.text() == "spectrum_A.txt"
    assert win.ui.dstntn_wlth_clm.count() == 3
    assert win.ui.dstntn_wlth_clm.itemText(0) == "Select column"
    assert win.ui.dstntn_wlth_clm.itemText(1) == "1"
    assert win.ui.dstntn_wlth_clm.itemText(2) == "2"
    assert win.my_conv.convolution_file_path == file_path
    assert win.ui.conv_path_lbl.text() == "spectrum_A.txt"
    assert win.ui.conv_wdth_1_clm.count() == 3
    assert win.ui.conv_wdth_1_clm.itemText(0) == "Select column"
    assert win.ui.conv_wdth_1_clm.itemText(1) == "1"
    assert win.ui.conv_wdth_1_clm.itemText(2) == "2"
    assert win.ui.conv_wdth_2_clm.count() == 3
    assert win.ui.conv_wdth_2_clm.itemText(0) == "Select column"
    win.close()
    # 3 columns & trapeze
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/ref_A.txt"
    win.conv_type.setCurrentIndex(3)
    win.file_select_action(file_path, "destination")
    assert win.my_conv.destination_file_path == file_path
    assert win.ui.dstntn_path_lbl.text() == "ref_A.txt"
    assert win.ui.dstntn_wlth_clm.count() == 4
    assert win.ui.dstntn_wlth_clm.itemText(0) == "Select column"
    assert win.ui.dstntn_wlth_clm.itemText(1) == "1"
    assert win.ui.dstntn_wlth_clm.itemText(2) == "2"
    assert win.ui.dstntn_wlth_clm.itemText(3) == "3"
    assert win.my_conv.convolution_file_path == file_path
    assert win.ui.conv_path_lbl.text() == "ref_A.txt"
    assert win.ui.conv_wdth_1_clm.count() == 4
    assert win.ui.conv_wdth_1_clm.itemText(0) == "Select column"
    assert win.ui.conv_wdth_1_clm.itemText(1) == "1"
    assert win.ui.conv_wdth_1_clm.itemText(2) == "2"
    assert win.ui.conv_wdth_1_clm.itemText(3) == "3"
    assert win.ui.conv_wdth_2_clm.count() == 4
    assert win.ui.conv_wdth_2_clm.itemText(0) == "Select column"
    assert win.ui.conv_wdth_2_clm.itemText(1) == "1"
    assert win.ui.conv_wdth_2_clm.itemText(2) == "2"
    assert win.ui.conv_wdth_2_clm.itemText(3) == "3"
    win.close()


# dstntn_file_del
def test_dstntn_file_del():
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/spectrum_A.txt"
    win.file_select_action(file_path, "destination")
    win.file_del("destination")
    assert win.my_conv.destination_file_path == ""
    assert win.ui.dstntn_path_lbl.text() == "no file selected"
    assert win.ui.dstntn_wlth_clm.count() == 1
    assert win.ui.dstntn_wlth_clm.itemText(0) == "Select column"
    win.close()


# dstnt_plot
def test_dstnt_plot_error():  ## normalizes styles for dstntn_unit, dstntn_wlth_clm, dstntn_linear_step
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = 1
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.convolution_calc()  # Warning "No destination unit given" is expected
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_ERROR
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.file_select_action(spectrum_file_path, "destination")
    win.convolution_calc()  # Warning "No destination wavelength column given" is expected
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_ERROR
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    win.ui.dstntn_wlth_clm.setCurrentIndex(1)
    win.convolution_calc()  # Warning "No convolution type given" is expected
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_step.setValue(11)
    win.conv_type.setCurrentIndex(1)
    win.conv_extrap.setCurrentIndex(2)
    win.file_select_action(spectrum_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(2)
    win.convolution_calc()  # Warning "Step is too big" is expected
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_ERROR
    win.dstntn_linear_step.setValue(8)
    win.convolution_calc()  # Warning "Destination wavelength and convolution width have different sizes" is expected
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_ERROR
    win.close()


def test_dstnt_plot_regular():
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = 2
    destination_wavelength_column = 1
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    # Under these conditions - when all data has been entered - the dstnt_plot function is triggered automatically.
    assert win.my_conv.destination_set_up
    win.my_conv.destination_set_up = False
    win.ui.dstntn_tab.setCurrentIndex(1)
    # Under these conditions - when all data has been entered - the dstnt_plot function is triggered automatically.
    assert win.my_conv.destination_set_up
    """
        This function changes the graph. It 
        1. removes the graphical representation for destination and the convolution curve; 
        2. removes the infinite lines that limit the range of destination; 
        3. calls the dstnt_graph_plot function that plots the graphical representation for destination.
        These actions should be tested visually.
    """
    win.close()


# dstnt_graph_plot
def test_dstnt_graph_plot():
    pass
    """
    This function 
        1. plots spectrum again (this is necessary to take into account its possible change to the destination unit);
        2. plots the graphical representation for destination; 
        3. plots infinite lines bounding the destination range; 
        4. changes the label for the wavelength axis (x-axis) with destination unit;
        5. changes the direction of the x-axis if destination unit is cm-1.
    All of these changes are only visible on the graph, so they should be tested visually.
    """


# conv_state_toggle
def test_conv_state_toggle():
    # trapeze
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = 1
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = 2
    destination_wavelength_column = 1
    convolution_type = 3
    convolution_extrapolation = 2
    convolution_width_1_column = 2
    convolution_width_2_column = 3
    convolution_width_1_start = 10
    convolution_width_1_stop = 1
    convolution_width_2_start = 5
    convolution_width_2_stop = 0.5
    convolution_width_1_const = 5
    convolution_width_2_const = 2
    # spectrum & destination set up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    win.conv_type.setCurrentIndex(convolution_type)
    # convolution width column
    win.conv_extrap.setCurrentIndex(convolution_extrapolation)
    win.convolution_calc()  # Warning "No width column given" is expected
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_ERROR
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution top column
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column)
    win.convolution_calc()  # Warning "No top column given" is expected
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_ERROR
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column)
    win.convolution_calc()  # "Ok" message is expected
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution linear
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_1_start + 1)
    win.conv_wdth_2_stop.setValue(convolution_width_1_stop + 1)
    win.convolution_calc()  # Warning "The width must be greater than the top" is expected
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_2_start.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    win.convolution_calc()  # "Not enough spectrum" message is expected
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution const
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_1_const + 1)
    win.convolution_calc()  # Warning "The width must be greater than the top" is expected
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_2_const.styleSheet() == main.LE_ERROR
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    win.convolution_calc()  # "Not enough spectrum" message is expected
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.close()
    # non-trapeze
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = 1
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = 2
    destination_wavelength_column = 1
    convolution_type = 2
    convolution_extrapolation = 2
    convolution_width_1_start = 10
    convolution_width_1_stop = 1
    convolution_width_1_const = 5
    # set up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation)
    # convolution linear
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.convolution_calc()  # "Not enough spectrum" message is expected
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution const
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.convolution_calc()  # "Not enough spectrum" message is expected
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.close()


# conv_type_toggle
def test_conv_type_toggle():
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = 1
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_file_path = "NH_case/ref_micron.txt"
    destination_unit = 2
    destination_wavelength_column = 1
    convolution_type = 1  # Gauss
    # set up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    # convolution type state toggle
    win.convolution_calc()  # Warning "No convolution type given" is expected
    assert win.conv_type.styleSheet() == main.QCB_ERROR
    assert win.ui.conv_wdth_2_lbl.isHidden()
    assert win.ui.conv_wdth_2_clm.isHidden()
    assert win.conv_wdth_2_start_lbl.isHidden()
    assert win.conv_wdth_2_start.isHidden()
    assert win.conv_wdth_2_stop_lbl.isHidden()
    assert win.conv_wdth_2_stop.isHidden()
    assert win.conv_wdth_2_const.isHidden()
    assert win.conv_wdth_2_const.isHidden()
    assert win.gauss_part_lbl.isHidden()
    assert win.conv_gauss_part.isHidden()
    assert win.ui.conv_wdth_1_lbl.text() == "width\ncolumn"
    assert win.ui.conv_wdth_2_lbl.text() == "top\ncolumn"
    assert win.conv_wdth_1_start_lbl.text() == "width start"
    assert win.conv_wdth_2_start_lbl.text() == "top start"
    assert win.conv_wdth_1_stop_lbl.text() == "width end"
    assert win.conv_wdth_2_stop_lbl.text() == "top end"
    assert win.conv_wdth_1_const_lbl.text() == "width value"
    assert win.conv_wdth_2_const_lbl.text() == "top value"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.conv_truncation.value() == 10
    win.convolution_calc()  # Warning "No width column" is expected
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_2_lbl.isHidden()
    assert win.ui.conv_wdth_2_clm.isHidden()
    assert win.conv_wdth_2_start_lbl.isHidden()
    assert win.conv_wdth_2_start.isHidden()
    assert win.conv_wdth_2_stop_lbl.isHidden()
    assert win.conv_wdth_2_stop.isHidden()
    assert win.conv_wdth_2_const.isHidden()
    assert win.conv_wdth_2_const.isHidden()
    assert win.gauss_part_lbl.isHidden()
    assert win.conv_gauss_part.isHidden()
    assert win.ui.conv_wdth_1_lbl.text() == "width\ncolumn"
    assert win.ui.conv_wdth_2_lbl.text() == "top\ncolumn"
    assert win.conv_wdth_1_start_lbl.text() == "width start"
    assert win.conv_wdth_2_start_lbl.text() == "top start"
    assert win.conv_wdth_1_stop_lbl.text() == "width end"
    assert win.conv_wdth_2_stop_lbl.text() == "top end"
    assert win.conv_wdth_1_const_lbl.text() == "width value"
    assert win.conv_wdth_2_const_lbl.text() == "top value"
    # trapeze
    win.conv_type.setCurrentIndex(3)
    assert win.conv_truncation.value() == 3
    win.convolution_calc() # Warning "No width column" is expected
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert not win.ui.conv_wdth_2_lbl.isHidden()
    assert not win.ui.conv_wdth_2_clm.isHidden()
    assert not win.conv_wdth_2_start_lbl.isHidden()
    assert not win.conv_wdth_2_start.isHidden()
    assert not win.conv_wdth_2_stop_lbl.isHidden()
    assert not win.conv_wdth_2_stop.isHidden()
    assert not win.conv_wdth_2_const.isHidden()
    assert not win.conv_wdth_2_const.isHidden()
    assert win.gauss_part_lbl.isHidden()
    assert win.conv_gauss_part.isHidden()
    assert win.ui.conv_wdth_1_lbl.text() == "width\ncolumn"
    assert win.ui.conv_wdth_2_lbl.text() == "top\ncolumn"
    assert win.conv_wdth_1_start_lbl.text() == "width start"
    assert win.conv_wdth_2_start_lbl.text() == "top start"
    assert win.conv_wdth_1_stop_lbl.text() == "width end"
    assert win.conv_wdth_2_stop_lbl.text() == "top end"
    assert win.conv_wdth_1_const_lbl.text() == "width value"
    assert win.conv_wdth_2_const_lbl.text() == "top value"
    # Voigt
    win.conv_type.setCurrentIndex(5)
    assert win.conv_truncation.value() == 15
    win.convolution_calc()  # Warning "No width column" is expected
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert not win.ui.conv_wdth_2_lbl.isHidden()
    assert not win.ui.conv_wdth_2_clm.isHidden()
    assert not win.conv_wdth_2_start_lbl.isHidden()
    assert not win.conv_wdth_2_start.isHidden()
    assert not win.conv_wdth_2_stop_lbl.isHidden()
    assert not win.conv_wdth_2_stop.isHidden()
    assert not win.conv_wdth_2_const.isHidden()
    assert not win.conv_wdth_2_const.isHidden()
    assert win.gauss_part_lbl.isHidden()
    assert win.conv_gauss_part.isHidden()
    assert win.ui.conv_wdth_1_lbl.text() == "Gauss width\ncolumn"
    assert win.ui.conv_wdth_2_lbl.text() == "Lorentz width\ncolumn"
    assert win.conv_wdth_1_start_lbl.text() == "Gauss width\nstart"
    assert win.conv_wdth_2_start_lbl.text() == "Lorentz width\nstart"
    assert win.conv_wdth_1_stop_lbl.text() == "Gauss width\nend"
    assert win.conv_wdth_2_stop_lbl.text() == "Lorentz width\nend"
    assert win.conv_wdth_1_const_lbl.text() == "Gauss width\nvalue"
    assert win.conv_wdth_2_const_lbl.text() == "Lorentz width\nvalue"
    # Gauss & Lorenz sum
    win.conv_type.setCurrentIndex(6)
    assert win.conv_truncation.value() == 12.5
    win.convolution_calc() # Warning "No width column" is expected
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert not win.ui.conv_wdth_2_lbl.isHidden()
    assert not win.ui.conv_wdth_2_clm.isHidden()
    assert not win.conv_wdth_2_start_lbl.isHidden()
    assert not win.conv_wdth_2_start.isHidden()
    assert not win.conv_wdth_2_stop_lbl.isHidden()
    assert not win.conv_wdth_2_stop.isHidden()
    assert not win.conv_wdth_2_const.isHidden()
    assert not win.conv_wdth_2_const.isHidden()
    assert not win.gauss_part_lbl.isHidden()
    assert not win.conv_gauss_part.isHidden()
    assert win.ui.conv_wdth_1_lbl.text() == "Gauss width\ncolumn"
    assert win.ui.conv_wdth_2_lbl.text() == "Lorentz width\ncolumn"
    assert win.conv_wdth_1_start_lbl.text() == "Gauss width\nstart"
    assert win.conv_wdth_2_start_lbl.text() == "Lorentz width\nstart"
    assert win.conv_wdth_1_stop_lbl.text() == "Gauss width\nend"
    assert win.conv_wdth_2_stop_lbl.text() == "Lorentz width\nend"
    assert win.conv_wdth_1_const_lbl.text() == "Gauss width\nvalue"
    assert win.conv_wdth_2_const_lbl.text() == "Lorentz width\nvalue"
    win.close()


# conv_file_select_action
def test_conv_file_select_action():
    # 1 column
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/dstntn_micron.txt"
    win.file_select_action(file_path, "convolution")
    assert win.my_conv.convolution_file_path == file_path
    assert win.ui.conv_path_lbl.text() == "dstntn_micron.txt"
    assert win.ui.conv_wdth_1_clm.count() == 2
    assert win.ui.conv_wdth_1_clm.itemText(0) == "Select column"
    assert win.ui.conv_wdth_1_clm.itemText(1) == "1"
    assert win.ui.conv_wdth_2_clm.count() == 2
    assert win.ui.conv_wdth_2_clm.itemText(0) == "Select column"
    assert win.ui.conv_wdth_2_clm.itemText(1) == "1"
    win.close()
    # 3 columns
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/ref_A.txt"
    win.file_select_action(file_path, "convolution")
    assert win.my_conv.convolution_file_path == file_path
    assert win.ui.conv_path_lbl.text() == "ref_A.txt"
    assert win.ui.conv_wdth_1_clm.count() == 4
    assert win.ui.conv_wdth_1_clm.itemText(0) == "Select column"
    assert win.ui.conv_wdth_1_clm.itemText(1) == "1"
    assert win.ui.conv_wdth_1_clm.itemText(2) == "2"
    assert win.ui.conv_wdth_1_clm.itemText(3) == "3"
    assert win.ui.conv_wdth_2_clm.count() == 4
    assert win.ui.conv_wdth_2_clm.itemText(0) == "Select column"
    assert win.ui.conv_wdth_2_clm.itemText(1) == "1"
    assert win.ui.conv_wdth_2_clm.itemText(2) == "2"
    assert win.ui.conv_wdth_2_clm.itemText(3) == "3"
    win.close()


# conv_file_del
def test_conv_file_del():
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    file_path = "NH_case/spectrum_A.txt"
    win.file_select_action(file_path, "convolution")
    win.file_del("convolution")
    assert win.my_conv.convolution_file_path == ""
    assert win.ui.conv_path_lbl.text() == "no file selected"
    assert win.ui.conv_wdth_1_clm.count() == 1
    assert win.ui.conv_wdth_1_clm.itemText(0) == "Select column"
    assert win.ui.conv_wdth_2_clm.count() == 1
    assert win.ui.conv_wdth_2_clm.itemText(0) == "Select column"
    win.close()


# all_inputs_there
def test_all_inputs_there():
    # trapeze
    print("Many warnings QLineEditNumber: Cannot convert '' to float are expected here:")
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = 4
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_unit = 2
    destination_file_path = "NH_case/ref_micron.txt"
    destination_wavelength_column = 1
    destination_linear_start = 1.227633
    destination_linear_stop = 2.487673
    destination_linear_step = 1.231658 - 1.227633
    convolution_type = 3  # trapeze
    convolution_truncation = 2.5
    convolution_width_1_column = 2
    convolution_width_2_column = 3
    convolution_width_1_start = 0.0051151375
    convolution_width_1_stop = 0.01036530416666667
    convolution_width_2_start = 0.00255756875
    convolution_width_2_stop = 0.005182652083333335
    convolution_width_1_const = 0.01036530416666667 - 0.01036530416666667
    convolution_width_2_const = 0.005182652083333335 - 0.00255756875
    # asserts
    # spectrum file
    assert not win.all_inputs_here()  # Warning "No spectrum file found" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_ERROR
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_ERROR
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.file_select_action(spectrum_file_path, "spectrum")
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # spectrum unit
    assert not win.all_inputs_here()  # Warning "No spectrum unit given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_ERROR
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # spectrum wavelength column
    assert not win.all_inputs_here()  # Warning "No spectrum wavelength column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_ERROR
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # spectrum intensity column
    assert not win.all_inputs_here()  # Warning "No spectrum intensity column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_ERROR
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination unit
    assert not win.all_inputs_here()  # Warning "No destination unit given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_ERROR
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination file
    assert not win.all_inputs_here()  # Warning "No destination file found" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_ERROR
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_ERROR
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.file_select_action(destination_file_path, "destination")
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination wavelength column
    assert not win.all_inputs_here()  # Warning "No destination wavelength column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_ERROR
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination wavelength linear start
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setText("")
    assert not win.all_inputs_here()  # Warning "No destination wavelength start value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_ERROR
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.dstntn_linear_start.setValue(destination_linear_start)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination wavelength linear stop
    win.dstntn_linear_stop.setText("")
    assert not win.all_inputs_here()  # Warning "No destination wavelength end value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_ERROR
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.dstntn_linear_stop.setValue(destination_linear_stop)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination wavelength linear step
    win.dstntn_linear_step.setText("")
    assert not win.all_inputs_here()  # Warning "No destination wavelength step value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_ERROR
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.dstntn_linear_step.setValue(destination_linear_step)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution type
    assert not win.all_inputs_here()  # Warning "No convolution type given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_ERROR
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution truncation
    win.conv_truncation.setText("")
    assert not win.all_inputs_here()  # Warning "No truncation given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_ERROR
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_truncation.setValue(convolution_truncation)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # width column
    assert not win.all_inputs_here()  # Warning "No width column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_ERROR
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.file_del("convolution")
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # width & top file
    assert not win.all_inputs_here()  # Warning "No width & top file found" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_ERROR
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_ERROR
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.file_select_action(destination_file_path, "convolution")
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # width column
    assert not win.all_inputs_here()  # Warning "No width column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_ERROR
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    assert not win.all_inputs_here()  # Warning "No top column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_ERROR
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution width start
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setText("")
    assert not win.all_inputs_here()  # Warning "No width start value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution width stop
    win.conv_wdth_1_stop.setText("")
    assert not win.all_inputs_here()  # Warning "No width end value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution top start
    win.conv_wdth_2_start.setText("")
    assert not win.all_inputs_here()  # Warning "No top start value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution top stop
    win.conv_wdth_2_stop.setText("")
    assert not win.all_inputs_here()  # Warning "No top end value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution width const
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setText("")
    assert not win.all_inputs_here()  # Warning "No width const value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution top const
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_2_const.setText("")
    assert not win.all_inputs_here()  # Warning "No top const value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_ERROR
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # final test (when everything is here)
    assert win.all_inputs_here()
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.close()
    # non-trapeze: Gauss + Lorentz
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = 4
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_unit = 2
    destination_file_path = "NH_case/ref_micron.txt"
    destination_wavelength_column = 1
    destination_linear_start = 1.227633
    destination_linear_stop = 2.487673
    destination_linear_step = 1.231658 - 1.227633
    convolution_type = 6
    convolution_gauss_ratio = 0.7
    convolution_truncation = 20
    convolution_width_1_column = 2
    convolution_width_1_start = 0.0051151375
    convolution_width_1_stop = 0.01036530416666667
    convolution_width_1_const = 0.01036530416666667 - 0.01036530416666667
    # asserts
    # spectrum file
    assert not win.all_inputs_here()  # Warning "No spectrum file found" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_ERROR
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_ERROR
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.file_select_action(spectrum_file_path, "spectrum")
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # spectrum unit
    assert not win.all_inputs_here()  # Warning "No spectrum unit given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_ERROR
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # spectrum wavelength column
    assert not win.all_inputs_here()  # Warning "No spectrum wavelength column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_ERROR
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # spectrum intensity column
    assert not win.all_inputs_here()  # Warning "No spectrum intensity column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_ERROR
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination unit
    assert not win.all_inputs_here()  # Warning "No destination unit given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_ERROR
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == ""
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination file
    assert not win.all_inputs_here()  # Warning "No destination file found" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_ERROR
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_ERROR
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == ""
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.file_select_action(destination_file_path, "destination")
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination wavelength column
    assert not win.all_inputs_here()  # Warning "No destination wavelength column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_ERROR
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination wavelength linear start
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setText("")
    assert not win.all_inputs_here()  # Warning "No destination wavelength start value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_ERROR
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.dstntn_linear_start.setValue(destination_linear_start)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination wavelength linear stop
    win.dstntn_linear_stop.setText("")
    assert not win.all_inputs_here()  # Warning "No destination wavelength end value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_ERROR
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.dstntn_linear_stop.setValue(destination_linear_stop)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # destination wavelength linear step
    win.dstntn_linear_step.setText("")
    assert not win.all_inputs_here()  # Warning "No destination wavelength step value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_ERROR
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.dstntn_linear_step.setValue(destination_linear_step)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution type
    assert not win.all_inputs_here()  # Warning "No convolution type given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_ERROR
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution gauss ratio
    win.conv_gauss_part.setText("")
    assert not win.all_inputs_here()  # Warning "No gauss ratio given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_ERROR
    assert win.conv_truncation.styleSheet() == main.LE_ERROR
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_gauss_part.setValue(convolution_gauss_ratio)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution truncation
    win.conv_truncation.setText("")
    assert not win.all_inputs_here()  # Warning "No truncation given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_ERROR
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_truncation.setValue(convolution_truncation)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # width column
    assert not win.all_inputs_here()  # Warning "No width column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_ERROR
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.file_del("convolution")
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # width file
    assert not win.all_inputs_here()  # Warning "No width file found" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_ERROR
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_ERROR
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.file_select_action(destination_file_path, "convolution")
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # width column
    assert not win.all_inputs_here()  # Warning "No width column given" is expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_ERROR
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution width start
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setText("")
    assert not win.all_inputs_here()  # Warning "No width start value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution width stop
    win.conv_wdth_1_stop.setText("")
    assert not win.all_inputs_here()  # Warning "No width end value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # convolution width const
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setText("")
    assert not win.all_inputs_here()  # Warning "No width const value given" and QLineEditNumber "Cannot convert '' to float" are expected
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # final test (when everything is here)
    assert win.all_inputs_here()
    assert win.ui.spctrm_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.spctrm_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.spctrm_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.spctrm_inty_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_unit.styleSheet() == main.QCB_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.dstntn_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.dstntn_wlth_clm.styleSheet() == main.QCB_NORMAL
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_type.styleSheet() == main.QCB_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_truncation.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_path_lbl.styleSheet() == main.LBL_NORMAL
    assert win.ui.conv_wdth_2_clm.styleSheet() == main.QCB_NORMAL
    assert win.ui.conv_wdth_1_clm.styleSheet() == main.QCB_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.close()


# all_inputs_correct
def test_all_inputs_correct():
    # destination: step < abs(stop-start)
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = 4
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_unit = 2
    destination_tab = 1
    destination_start = 10
    destination_stop = 5
    destination_step = 14
    convolution_type = 4
    convolution_extrapaolation_type = 4
    convolution_tab = 2
    convolution_width_1_const = 1
    # set_up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.ui.dstntn_tab.setCurrentIndex(destination_tab)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_extrap.setCurrentIndex(convolution_extrapaolation_type)
    win.ui.conv_tab.setCurrentIndex(convolution_tab)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    assert win.all_inputs_here()
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    assert not win.all_inputs_correct()  # Warning "Destination wavelength step is too big" is expected
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.close()
    # gauss ration not in [0, 1]
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = 4
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_unit = 2
    destination_tab = 1
    destination_linear_start = 1.227633
    destination_linear_stop = 2.487673
    destination_linear_step = 0.004025
    convolution_type = 6
    convolution_gauss_ratio = 1.5
    convolution_truncation = 20
    convolution_tab = 2
    convolution_width_1_const = 0.0002
    convolution_width_2_const = 0.0001
    # set up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.ui.dstntn_tab.setCurrentIndex(destination_tab)
    win.dstntn_linear_start.setValue(destination_linear_start)
    win.dstntn_linear_stop.setValue(destination_linear_stop)
    win.dstntn_linear_step.setValue(destination_linear_step)
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_gauss_part.setValue(convolution_gauss_ratio)
    win.conv_truncation.setValue(convolution_truncation)
    win.ui.conv_tab.setCurrentIndex(convolution_tab)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    assert win.all_inputs_here()
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    assert not win.all_inputs_correct()  # Warning "Convolution Gauss ration value" is expected
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_ERROR
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    # dstntn_wlth.size != conv_wdth.size: file & file
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = 4
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_unit = 2
    destination_tab = 0
    destination_file_path = "NH_case/ref_micron_cut.txt"
    destination_wavelength_column = 1
    convolution_type = 2
    convolution_extrapaolation_type = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 2
    # set_up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.ui.dstntn_tab.setCurrentIndex(destination_tab)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_extrap.setCurrentIndex(convolution_extrapaolation_type)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column)
    assert win.all_inputs_here()
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    assert not win.all_inputs_correct()  # Warning "Destination wavelength and convolution width have different sizes" is expected
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_ERROR
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_ERROR
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.close()
    # dstntn_wlth.size != conv_wdth.size: linear & file
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = 4
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_unit = 2
    destination_tab = 1
    destination_start = 10
    destination_stop = 5
    destination_step = 1
    convolution_type = 2
    convolution_extrapaolation_type = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 2
    # set_up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.ui.dstntn_tab.setCurrentIndex(destination_tab)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_extrap.setCurrentIndex(convolution_extrapaolation_type)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column)
    assert win.all_inputs_here()
    assert win.dstntn_linear_start.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_stop.styleSheet() == main.LE_NORMAL
    assert win.dstntn_linear_step.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    assert not win.all_inputs_correct()  # Warning "Destination wavelength and convolution width have different sizes" is expected
    assert win.dstntn_linear_start.styleSheet() == main.LE_ERROR
    assert win.dstntn_linear_stop.styleSheet() == main.LE_ERROR
    assert win.dstntn_linear_step.styleSheet() == main.LE_ERROR
    assert win.conv_wdth_1_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_1_stop.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_start.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_stop.styleSheet() == main.LE_NORMAL
    assert win.ui.dstntn_file.styleSheet() == main.BTN_NORMAL
    assert win.conv_gauss_part.styleSheet() == main.LE_NORMAL
    assert win.ui.conv_file.styleSheet() == main.BTN_ERROR
    assert win.conv_wdth_1_const.styleSheet() == main.LE_NORMAL
    assert win.conv_wdth_2_const.styleSheet() == main.LE_NORMAL
    win.close()
    # width >= top: file - no warning when rectangular function
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = 4
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_unit = 2
    destination_file_path = "NH_case/ref_micron.txt"
    destination_wavelength_column = 1
    convolution_type = 3
    convolution_extrapaolation_type = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 3
    convolution_width_2_column = 3
    # set_up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_extrap.setCurrentIndex(convolution_extrapaolation_type)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column)
    assert win.all_inputs_here()
    assert win.all_inputs_correct()  # No warning here!
    win.close()
    # width >= top: file
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = 4
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_unit = 2
    destination_file_path = "NH_case/ref_micron.txt"
    destination_wavelength_column = 1
    convolution_type = 3
    convolution_extrapaolation_type = 3
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 3
    convolution_width_2_column = 2
    # set_up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_extrap.setCurrentIndex(convolution_extrapaolation_type)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column)
    assert win.all_inputs_here()
    assert not win.all_inputs_correct()  # Warning "The width must be greater than the top" is expected
    win.close()
    # width >= top: linear
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = 4
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_unit = 2
    destination_file_path = "NH_case/ref_micron.txt"
    destination_wavelength_column = 1
    convolution_type = 3
    convolution_extrapaolation_type = 3
    convolution_tab = 1
    convolution_width_1_start = 5
    convolution_width_1_stop = 1
    convolution_width_2_start = 10
    convolution_width_2_stop = 0.5
    # set_up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_extrap.setCurrentIndex(convolution_extrapaolation_type)
    win.ui.conv_tab.setCurrentIndex(convolution_tab)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    assert win.all_inputs_here()
    assert not win.all_inputs_correct()  # Warning "The width must be greater than the top" is expected
    win.close()
    # width >= top: const
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    spectrum_file_path = "NH_case/spectrum_A.txt"
    spectrum_unit = 4
    spectrum_wavelength_column = 1
    spectrum_intensity_column = 2
    destination_unit = 2
    destination_file_path = "NH_case/ref_micron.txt"
    destination_wavelength_column = 1
    convolution_type = 3
    convolution_extrapaolation_type = 3
    convolution_tab = 2
    convolution_width_1_const = 2
    convolution_width_2_const = 3
    # set_up
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(spectrum_unit)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column)
    win.ui.dstntn_unit.setCurrentIndex(destination_unit)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column)
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_extrap.setCurrentIndex(convolution_extrapaolation_type)
    win.ui.conv_tab.setCurrentIndex(convolution_tab)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    assert win.all_inputs_here()
    assert not win.all_inputs_correct()  # Warning "The width must be greater than the top" is expected
    win.close()


# ConvolutionExportW
def test_ConvolutionExportW_function():
    destination_wavelength_ascending = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    destination_intensity_ascending = np.array([0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    separator = "\t"
    spectrum_file_path = "export/some_spectrum.txt"
    destination_unit_nm = "nm"
    revers_order_false = False
    result_path_increasing = "export/results/some_spectrum_conv_increasing.txt"
    result_path_decreasing = "export/results/some_spectrum_conv_decreasing.txt"
    class_result_path = "export/results/result.txt"
    # var 1
    """
        wavelength: digital, 6 digits, ascending
        intensity: digital, 9 digits
        columns: yes
        separator: as in spectrum file (\t in this example)
    """
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    win.ui.cb_wlth_format.setCurrentIndex(0)
    win.ui.cb_wlth_digits.setCurrentIndex(6)
    win.ui.cb_wlth_order.setCurrentIndex(0)
    win.ui.cb_inty_format.setCurrentIndex(0)
    win.ui.cb_inty_digits.setCurrentIndex(9)
    win.ui.cb_clmn_names.setCurrentIndex(0)
    win.ui.cb_separators.setCurrentIndex(0)
    str_from_function = win.str_to_export()
    str_result = "wavelength_nm\tintensity\n0.000000\t0.000000000\n1.000000\t1.000000000\n2.000000\t4.000000000\n3.000000\t9.000000000\n4.000000\t16.000000000\n5.000000\t25.000000000\n6.000000\t36.000000000\n7.000000\t49.000000000\n8.000000\t64.000000000\n9.000000\t81.000000000\n10.000000\t100.000000000\n"
    assert str_result == str_from_function
    win.save_and_close(class_result_path, str_from_function)
    # assert
    result_read = data_pars.DataPars(result_path_increasing, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    result_read = data_pars.DataPars(class_result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    class_result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        class_result[i] = result_data[i][1]
    assert list_compare(class_result, result, 10 ** 0)
    win.close()
    # var 2
    """
        wavelength: exponential, 0 digits, ascending
        intensity: digital, 0 digits
        columns: no
        separator: var 1 (Tab)
    """
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    win.ui.cb_wlth_format.setCurrentIndex(1)
    win.ui.cb_wlth_digits.setCurrentIndex(0)
    win.ui.cb_wlth_order.setCurrentIndex(0)
    win.ui.cb_inty_format.setCurrentIndex(0)
    win.ui.cb_inty_digits.setCurrentIndex(0)
    win.ui.cb_clmn_names.setCurrentIndex(1)
    win.ui.cb_separators.setCurrentIndex(1)
    str_from_function = win.str_to_export()
    str_result = "0e+00\t0\n1e+00\t1\n2e+00\t4\n3e+00\t9\n4e+00\t16\n5e+00\t25\n6e+00\t36\n7e+00\t49\n8e+00\t64\n9e+00\t81\n1e+01\t100\n"
    assert str_result == str_from_function
    win.save_and_close(class_result_path, str_from_function)
    # assert
    result_read = data_pars.DataPars(result_path_increasing, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    result_read = data_pars.DataPars(class_result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    class_result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        class_result[i] = result_data[i][1]
    assert list_compare(class_result, result, 10 ** 0)
    win.close()
    # var 3
    """
        wavelength: digital, 16 digits, descending
        intensity: exponential, 16 digits
        columns: yes
        separator: var 2 (Space)
    """
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    win.ui.cb_wlth_format.setCurrentIndex(0)
    win.ui.cb_wlth_digits.setCurrentIndex(16)
    win.ui.cb_wlth_order.setCurrentIndex(1)
    win.ui.cb_inty_format.setCurrentIndex(1)
    win.ui.cb_inty_digits.setCurrentIndex(16)
    win.ui.cb_clmn_names.setCurrentIndex(0)
    win.ui.cb_separators.setCurrentIndex(2)
    str_from_function = win.str_to_export()
    str_result = "wavelength_nm intensity\n10.0000000000000000 1.0000000000000000e+02\n9.0000000000000000 8.1000000000000000e+01\n8.0000000000000000 6.4000000000000000e+01\n7.0000000000000000 4.9000000000000000e+01\n6.0000000000000000 3.6000000000000000e+01\n5.0000000000000000 2.5000000000000000e+01\n4.0000000000000000 1.6000000000000000e+01\n3.0000000000000000 9.0000000000000000e+00\n2.0000000000000000 4.0000000000000000e+00\n1.0000000000000000 1.0000000000000000e+00\n0.0000000000000000 0.0000000000000000e+00\n"
    assert str_result == str_from_function
    win.save_and_close(class_result_path, str_from_function)
    # assert
    result_read = data_pars.DataPars(result_path_decreasing, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    result_read = data_pars.DataPars(class_result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    class_result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        class_result[i] = result_data[i][1]
    assert list_compare(class_result, result, 10 ** 0)
    win.close()
    # var 4
    """
        wavelength: exponential, 6 digits, descending
        intensity: exponential, 4 digits
        columns: no
        separator: var 3 (Comma)
    """
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    win.ui.cb_wlth_format.setCurrentIndex(1)
    win.ui.cb_wlth_digits.setCurrentIndex(6)
    win.ui.cb_wlth_order.setCurrentIndex(1)
    win.ui.cb_inty_format.setCurrentIndex(1)
    win.ui.cb_inty_digits.setCurrentIndex(4)
    win.ui.cb_clmn_names.setCurrentIndex(1)
    win.ui.cb_separators.setCurrentIndex(3)
    str_from_function = win.str_to_export()
    str_result = "1.000000e+01,1.0000e+02\n9.000000e+00,8.1000e+01\n8.000000e+00,6.4000e+01\n7.000000e+00,4.9000e+01\n6.000000e+00,3.6000e+01\n5.000000e+00,2.5000e+01\n4.000000e+00,1.6000e+01\n3.000000e+00,9.0000e+00\n2.000000e+00,4.0000e+00\n1.000000e+00,1.0000e+00\n0.000000e+00,0.0000e+00\n"
    assert str_result == str_from_function
    win.save_and_close(class_result_path, str_from_function)
    # assert
    result_read = data_pars.DataPars(result_path_decreasing, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    result_read = data_pars.DataPars(class_result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    class_result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        class_result[i] = result_data[i][1]
    assert list_compare(class_result, result, 10 ** 0)
    win.close()
    # var 5
    """
        wavelength: digital, 8 digits, ascending
        intensity: exponential, 10 digits
        columns: yes
        separator: var 4 (Other, ", " in this example)
    """
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    win.ui.cb_wlth_format.setCurrentIndex(0)
    win.ui.cb_wlth_digits.setCurrentIndex(8)
    win.ui.cb_wlth_order.setCurrentIndex(0)
    win.ui.cb_inty_format.setCurrentIndex(1)
    win.ui.cb_inty_digits.setCurrentIndex(10)
    win.ui.cb_clmn_names.setCurrentIndex(0)
    win.ui.cb_separators.setCurrentIndex(4)
    win.ui.pte_separator.setPlainText(", ")
    str_from_function = win.str_to_export()
    str_result = "wavelength_nm, intensity\n0.00000000, 0.0000000000e+00\n1.00000000, 1.0000000000e+00\n2.00000000, 4.0000000000e+00\n3.00000000, 9.0000000000e+00\n4.00000000, 1.6000000000e+01\n5.00000000, 2.5000000000e+01\n6.00000000, 3.6000000000e+01\n7.00000000, 4.9000000000e+01\n8.00000000, 6.4000000000e+01\n9.00000000, 8.1000000000e+01\n10.00000000, 1.0000000000e+02\n"
    assert str_result == str_from_function
    win.save_and_close(class_result_path, str_from_function)
    # assert
    result_read = data_pars.DataPars(result_path_increasing, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        result[i] = result_data[i][1]
    result_read = data_pars.DataPars(class_result_path, None)
    result_read.file_pars_f()
    result_data = result_read.file_body
    class_result = np.zeros(len(result_data))
    for i in range(len(result_data)):
        class_result[i] = result_data[i][1]
    assert list_compare(class_result, result, 10 ** 0)
    win.close()


def test_ConvolutionExportW_unit_change():
    destination_wavelength_ascending = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    destination_intensity_ascending = np.array([0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    separator = "\t"
    spectrum_file_path = "export/some_spectrum.txt"
    destination_unit_nm = "nm"
    revers_order_false = False
    """
        wavelength: digital, 6 digits, ascending
        intensity: digital, 9 digits
        columns: yes
        separator: as in spectrum file (\t in this example)
    """
    # assert: nm -> nm (default)
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    win.ui.cb_wlth_format.setCurrentIndex(0)
    win.ui.cb_wlth_digits.setCurrentIndex(6)
    win.ui.cb_wlth_order.setCurrentIndex(0)
    win.ui.cb_inty_format.setCurrentIndex(0)
    win.ui.cb_inty_digits.setCurrentIndex(9)
    win.ui.cb_clmn_names.setCurrentIndex(0)
    win.ui.cb_separators.setCurrentIndex(0)
    str_from_function = win.str_to_export()
    str_result = "wavelength_nm\tintensity\n0.000000\t0.000000000\n1.000000\t1.000000000\n2.000000\t4.000000000\n3.000000\t9.000000000\n4.000000\t16.000000000\n5.000000\t25.000000000\n6.000000\t36.000000000\n7.000000\t49.000000000\n8.000000\t64.000000000\n9.000000\t81.000000000\n10.000000\t100.000000000\n"
    assert str_from_function == str_result
    win.close()
    # assert: nm -> cm-1
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    win.ui.cb_wlth_format.setCurrentIndex(0)
    win.ui.cb_wlth_digits.setCurrentIndex(6)
    win.ui.cb_wlth_order.setCurrentIndex(0)
    win.ui.cb_inty_format.setCurrentIndex(0)
    win.ui.cb_inty_digits.setCurrentIndex(9)
    win.ui.cb_clmn_names.setCurrentIndex(0)
    win.ui.cb_separators.setCurrentIndex(0)
    win.ui.cb_wlth_unit.setCurrentIndex(0)
    str_from_function = win.str_to_export()
    str_result = "wavelength_cm-1\tintensity\n0.000000\t0.000000000\n10000000.000000\t1.000000000\n5000000.000000\t4.000000000\n3333333.333333\t9.000000000\n2500000.000000\t16.000000000\n2000000.000000\t25.000000000\n1666666.666667\t36.000000000\n1428571.428571\t49.000000000\n1250000.000000\t64.000000000\n1111111.111111\t81.000000000\n1000000.000000\t100.000000000\n"
    assert str_from_function == str_result
    win.close()
    # assert: nm -> micron
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    win.ui.cb_wlth_format.setCurrentIndex(0)
    win.ui.cb_wlth_digits.setCurrentIndex(6)
    win.ui.cb_wlth_order.setCurrentIndex(0)
    win.ui.cb_inty_format.setCurrentIndex(0)
    win.ui.cb_inty_digits.setCurrentIndex(9)
    win.ui.cb_clmn_names.setCurrentIndex(0)
    win.ui.cb_separators.setCurrentIndex(0)
    win.ui.cb_wlth_unit.setCurrentIndex(1)
    str_from_function = win.str_to_export()
    str_result = "wavelength_micron\tintensity\n0.000000\t0.000000000\n0.001000\t1.000000000\n0.002000\t4.000000000\n0.003000\t9.000000000\n0.004000\t16.000000000\n0.005000\t25.000000000\n0.006000\t36.000000000\n0.007000\t49.000000000\n0.008000\t64.000000000\n0.009000\t81.000000000\n0.010000\t100.000000000\n"
    assert str_from_function == str_result
    win.close()
    # assert: nm -> nm
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    win.ui.cb_wlth_format.setCurrentIndex(0)
    win.ui.cb_wlth_digits.setCurrentIndex(6)
    win.ui.cb_wlth_order.setCurrentIndex(0)
    win.ui.cb_inty_format.setCurrentIndex(0)
    win.ui.cb_inty_digits.setCurrentIndex(9)
    win.ui.cb_clmn_names.setCurrentIndex(0)
    win.ui.cb_separators.setCurrentIndex(0)
    win.ui.cb_wlth_unit.setCurrentIndex(2)
    str_from_function = win.str_to_export()
    str_result = "wavelength_nm\tintensity\n0.000000\t0.000000000\n1.000000\t1.000000000\n2.000000\t4.000000000\n3.000000\t9.000000000\n4.000000\t16.000000000\n5.000000\t25.000000000\n6.000000\t36.000000000\n7.000000\t49.000000000\n8.000000\t64.000000000\n9.000000\t81.000000000\n10.000000\t100.000000000\n"
    assert str_from_function == str_result
    win.close()
    # assert: nm -> A
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    win.ui.cb_wlth_format.setCurrentIndex(0)
    win.ui.cb_wlth_digits.setCurrentIndex(6)
    win.ui.cb_wlth_order.setCurrentIndex(0)
    win.ui.cb_inty_format.setCurrentIndex(0)
    win.ui.cb_inty_digits.setCurrentIndex(9)
    win.ui.cb_clmn_names.setCurrentIndex(0)
    win.ui.cb_separators.setCurrentIndex(0)
    win.ui.cb_wlth_unit.setCurrentIndex(3)
    str_from_function = win.str_to_export()
    str_result = "wavelength_A\tintensity\n0.000000\t0.000000000\n10.000000\t1.000000000\n20.000000\t4.000000000\n30.000000\t9.000000000\n40.000000\t16.000000000\n50.000000\t25.000000000\n60.000000\t36.000000000\n70.000000\t49.000000000\n80.000000\t64.000000000\n90.000000\t81.000000000\n100.000000\t100.000000000\n"
    assert str_from_function == str_result
    win.close()


def test_ConvolutionExportW_interface_and_register_save():
    destination_wavelength_ascending = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    destination_intensity_ascending = np.array([0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
    separator = "\t"
    spectrum_file_path = "export/some_spectrum.txt"
    destination_unit_nm = "nm"
    revers_order_false = False
    # register save
    """
        Last example:
            wavelength: digital, 8 digits, ascending
            intensity: exponential, 10 digits
            columns: yes
            separator: var 4 (Other, ", ")
    """
    win = main.ConvolutionExportW(destination_wavelength_ascending, destination_intensity_ascending, separator, spectrum_file_path, destination_unit_nm, revers_order_false, True)
    assert win.ui.cb_wlth_format.currentIndex() == 0
    assert win.ui.cb_wlth_digits.currentIndex() == 8
    assert win.ui.cb_wlth_order.currentIndex() == 0
    assert win.ui.cb_inty_format.currentIndex() == 1
    assert win.ui.cb_inty_digits.currentIndex() == 10
    assert win.ui.cb_clmn_names.currentIndex() == 0
    assert win.ui.cb_separators.currentIndex() == 4
    assert win.ui.pte_separator.toPlainText() == ", "
    win.close()


def test_ConvolutionExportW_ascending_descending():
    spectrum_unit = "cm-1"
    convolution_type = 1  # "Gauss function"
    destination_unit = "cm-1"
    convolution_truncation = 10
    convolution_extrapolation_type = 0  # "zeros"
    convolution_width_1_const = 1
    wavelength_format = 0
    wavelength_digits = 8
    intensity_format = 0
    intensity_digits = 8
    column_names = 1
    separator_type = 0
    result_path = "export/parabol_ascending_descending/result.txt"
    # spectrum: ascending, destination: ascending, export: ascending
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    wavelength_order = 0
    expected_path = "export/parabol_ascending_descending/aa/parabol_conv_a.txt"
    # sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## export
    win_export = main.ConvolutionExportW(win.my_conv.destination_wavelength, win.my_conv.destination_intensity,
                                         win.my_conv.spectrum_separator, win.my_conv.spectrum_file_path,
                                         win.my_conv.destination_unit, win.my_conv.revers_order_destination, True)
    win_export.ui.cb_wlth_format.setCurrentIndex(wavelength_format)
    win_export.ui.cb_wlth_digits.setCurrentIndex(wavelength_digits)
    win_export.ui.cb_wlth_order.setCurrentIndex(wavelength_order)
    win_export.ui.cb_inty_format.setCurrentIndex(intensity_format)
    win_export.ui.cb_inty_digits.setCurrentIndex(intensity_digits)
    win_export.ui.cb_clmn_names.setCurrentIndex(column_names)
    win_export.ui.cb_separators.setCurrentIndex(separator_type)
    win_export.save_and_close(result_path, win_export.str_to_export())
    # assert
    assert filecmp.cmp(expected_path, result_path, shallow=False)
    win.close()
    # spectrum: ascending, destination: ascending, export: descending
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    wavelength_order = 1
    expected_path = "export/parabol_ascending_descending/aa/parabol_conv_d.txt"
    # sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## export
    win_export = main.ConvolutionExportW(win.my_conv.destination_wavelength, win.my_conv.destination_intensity,
                                         win.my_conv.spectrum_separator, win.my_conv.spectrum_file_path,
                                         win.my_conv.destination_unit, win.my_conv.revers_order_destination, True)
    win_export.ui.cb_wlth_format.setCurrentIndex(wavelength_format)
    win_export.ui.cb_wlth_digits.setCurrentIndex(wavelength_digits)
    win_export.ui.cb_wlth_order.setCurrentIndex(wavelength_order)
    win_export.ui.cb_inty_format.setCurrentIndex(intensity_format)
    win_export.ui.cb_inty_digits.setCurrentIndex(intensity_digits)
    win_export.ui.cb_clmn_names.setCurrentIndex(column_names)
    win_export.ui.cb_separators.setCurrentIndex(separator_type)
    win_export.save_and_close(result_path, win_export.str_to_export())
    # assert
    assert filecmp.cmp(expected_path, result_path, shallow=False)
    win.close()
    # spectrum: descending, destination: ascending, export: ascending
    spectrum_file_path = "math_examples/parabol_descending.txt"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    wavelength_order = 0
    expected_path = "export/parabol_ascending_descending/da/parabol_conv_a.txt"
    # sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## export
    win_export = main.ConvolutionExportW(win.my_conv.destination_wavelength, win.my_conv.destination_intensity,
                                         win.my_conv.spectrum_separator, win.my_conv.spectrum_file_path,
                                         win.my_conv.destination_unit, win.my_conv.revers_order_destination, True)
    win_export.ui.cb_wlth_format.setCurrentIndex(wavelength_format)
    win_export.ui.cb_wlth_digits.setCurrentIndex(wavelength_digits)
    win_export.ui.cb_wlth_order.setCurrentIndex(wavelength_order)
    win_export.ui.cb_inty_format.setCurrentIndex(intensity_format)
    win_export.ui.cb_inty_digits.setCurrentIndex(intensity_digits)
    win_export.ui.cb_clmn_names.setCurrentIndex(column_names)
    win_export.ui.cb_separators.setCurrentIndex(separator_type)
    win_export.save_and_close(result_path, win_export.str_to_export())
    # assert
    assert filecmp.cmp(expected_path, result_path, shallow=False)
    win.close()
    # spectrum: descending, destination: ascending, export: descending
    spectrum_file_path = "math_examples/parabol_descending.txt"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_start = 0
    destination_stop = 10
    destination_step = 0.5
    wavelength_order = 1
    expected_path = "export/parabol_ascending_descending/da/parabol_conv_d.txt"
    # sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## export
    win_export = main.ConvolutionExportW(win.my_conv.destination_wavelength, win.my_conv.destination_intensity,
                                         win.my_conv.spectrum_separator, win.my_conv.spectrum_file_path,
                                         win.my_conv.destination_unit, win.my_conv.revers_order_destination, True)
    win_export.ui.cb_wlth_format.setCurrentIndex(wavelength_format)
    win_export.ui.cb_wlth_digits.setCurrentIndex(wavelength_digits)
    win_export.ui.cb_wlth_order.setCurrentIndex(wavelength_order)
    win_export.ui.cb_inty_format.setCurrentIndex(intensity_format)
    win_export.ui.cb_inty_digits.setCurrentIndex(intensity_digits)
    win_export.ui.cb_clmn_names.setCurrentIndex(column_names)
    win_export.ui.cb_separators.setCurrentIndex(separator_type)
    win_export.save_and_close(result_path, win_export.str_to_export())
    # assert
    assert filecmp.cmp(expected_path, result_path, shallow=False)
    win.close()
    # spectrum: ascending, destination: descending, export: ascending
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_start = 10
    destination_stop = 0
    destination_step = 0.5
    wavelength_order = 0
    expected_path = "export/parabol_ascending_descending/ad/parabol_conv_a.txt"
    # sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## export
    win_export = main.ConvolutionExportW(win.my_conv.destination_wavelength, win.my_conv.destination_intensity,
                                         win.my_conv.spectrum_separator, win.my_conv.spectrum_file_path,
                                         win.my_conv.destination_unit, win.my_conv.revers_order_destination, True)
    win_export.ui.cb_wlth_format.setCurrentIndex(wavelength_format)
    win_export.ui.cb_wlth_digits.setCurrentIndex(wavelength_digits)
    win_export.ui.cb_wlth_order.setCurrentIndex(wavelength_order)
    win_export.ui.cb_inty_format.setCurrentIndex(intensity_format)
    win_export.ui.cb_inty_digits.setCurrentIndex(intensity_digits)
    win_export.ui.cb_clmn_names.setCurrentIndex(column_names)
    win_export.ui.cb_separators.setCurrentIndex(separator_type)
    win_export.save_and_close(result_path, win_export.str_to_export())
    # assert
    assert filecmp.cmp(expected_path, result_path, shallow=False)
    win.close()
    # spectrum: ascending, destination: descending, export: descending
    spectrum_file_path = "math_examples/parabol.txt"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_start = 10
    destination_stop = 0
    destination_step = 0.5
    wavelength_order = 1
    expected_path = "export/parabol_ascending_descending/ad/parabol_conv_d.txt"
    # sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## export
    win_export = main.ConvolutionExportW(win.my_conv.destination_wavelength, win.my_conv.destination_intensity,
                                         win.my_conv.spectrum_separator, win.my_conv.spectrum_file_path,
                                         win.my_conv.destination_unit, win.my_conv.revers_order_destination, True)
    win_export.ui.cb_wlth_format.setCurrentIndex(wavelength_format)
    win_export.ui.cb_wlth_digits.setCurrentIndex(wavelength_digits)
    win_export.ui.cb_wlth_order.setCurrentIndex(wavelength_order)
    win_export.ui.cb_inty_format.setCurrentIndex(intensity_format)
    win_export.ui.cb_inty_digits.setCurrentIndex(intensity_digits)
    win_export.ui.cb_clmn_names.setCurrentIndex(column_names)
    win_export.ui.cb_separators.setCurrentIndex(separator_type)
    win_export.save_and_close(result_path, win_export.str_to_export())
    # assert
    assert filecmp.cmp(expected_path, result_path, shallow=False)
    win.close()
    # spectrum: descending, destination: descending, export: ascending
    spectrum_file_path = "math_examples/parabol_descending.txt"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_start = 10
    destination_stop = 0
    destination_step = 0.5
    wavelength_order = 0
    expected_path = "export/parabol_ascending_descending/dd/parabol_conv_a.txt"
    # sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## export
    win_export = main.ConvolutionExportW(win.my_conv.destination_wavelength, win.my_conv.destination_intensity,
                                         win.my_conv.spectrum_separator, win.my_conv.spectrum_file_path,
                                         win.my_conv.destination_unit, win.my_conv.revers_order_destination, True)
    win_export.ui.cb_wlth_format.setCurrentIndex(wavelength_format)
    win_export.ui.cb_wlth_digits.setCurrentIndex(wavelength_digits)
    win_export.ui.cb_wlth_order.setCurrentIndex(wavelength_order)
    win_export.ui.cb_inty_format.setCurrentIndex(intensity_format)
    win_export.ui.cb_inty_digits.setCurrentIndex(intensity_digits)
    win_export.ui.cb_clmn_names.setCurrentIndex(column_names)
    win_export.ui.cb_separators.setCurrentIndex(separator_type)
    win_export.save_and_close(result_path, win_export.str_to_export())
    # assert
    assert filecmp.cmp(expected_path, result_path, shallow=False)
    win.close()
    # spectrum: descending, destination: descending, export: descending
    spectrum_file_path = "math_examples/parabol_descending.txt"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_start = 10
    destination_stop = 0
    destination_step = 0.5
    wavelength_order = 1
    expected_path = "export/parabol_ascending_descending/dd/parabol_conv_d.txt"
    # sdc
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_start)
    win.dstntn_linear_stop.setValue(destination_stop)
    win.dstntn_linear_step.setValue(destination_step)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    ## calc
    win.convolution_calc()
    ## export
    win_export = main.ConvolutionExportW(win.my_conv.destination_wavelength, win.my_conv.destination_intensity,
                                         win.my_conv.spectrum_separator, win.my_conv.spectrum_file_path,
                                         win.my_conv.destination_unit, win.my_conv.revers_order_destination, True)
    win_export.ui.cb_wlth_format.setCurrentIndex(wavelength_format)
    win_export.ui.cb_wlth_digits.setCurrentIndex(wavelength_digits)
    win_export.ui.cb_wlth_order.setCurrentIndex(wavelength_order)
    win_export.ui.cb_inty_format.setCurrentIndex(intensity_format)
    win_export.ui.cb_inty_digits.setCurrentIndex(intensity_digits)
    win_export.ui.cb_clmn_names.setCurrentIndex(column_names)
    win_export.ui.cb_separators.setCurrentIndex(separator_type)
    win_export.save_and_close(result_path, win_export.str_to_export())
    # assert
    assert filecmp.cmp(expected_path, result_path, shallow=False)
    win.close()


# destination & convolution export
def test_dstntn_export_gen():
    # preset
    win = main.ConvolutionMainW()
    win.ui.instrument_preset.setCurrentIndex(1)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Gauss function\ndestination_wavelength_nm\tdestination_width\n1228.2\t5.08571\n1232.2\t5.10862\n1236.3\t5.132\n1240.4\t5.15544\n1244.6\t5.17936\n1248.7\t5.20292\n1253.0\t5.22809\n1257.3\t5.25334\n1261.6\t5.27866\n1266.0\t5.30447\n1270.4\t5.33035\n1274.8\t5.3563\n1279.3\t5.38275\n1283.8\t5.40927\n1288.3\t5.43586\n1292.9\t5.46296\n1297.5\t5.49013\n1302.2\t5.5178\n1306.9\t5.54554\n1311.6\t5.57337\n1316.3\t5.60128\n1321.0\t5.62926\n1325.8\t5.65775\n1330.6\t5.68632\n1335.5\t5.71541\n1340.3\t5.74414\n1345.2\t5.77339\n1350.1\t5.80272\n1355.0\t5.83214\n1360.0\t5.86207\n1364.9\t5.89165\n1369.9\t5.92176\n1374.9\t5.95195\n1380.0\t5.98266\n1385.0\t6.01302\n1390.1\t6.04391\n1395.2\t6.07489\n1400.3\t6.10596\n1405.4\t6.13712\n1410.5\t6.16837\n1415.7\t6.20015\n1420.8\t6.23158\n1426.0\t6.26354\n1431.2\t6.2956\n1436.5\t6.32819\n1441.7\t6.36044\n1446.9\t6.39278\n1452.2\t6.42566\n1457.5\t6.45626\n1462.8\t6.48692\n1468.1\t6.51765\n1473.4\t6.54844\n1478.8\t6.57976\n1484.1\t6.61069\n1489.5\t6.64214\n1494.9\t6.67366\n1500.3\t6.70525\n1505.7\t6.73691\n1511.2\t6.76909\n1516.6\t6.8009\n1522.1\t6.83322\n1527.6\t6.86562\n1533.1\t6.89809\n1538.6\t6.93063\n1544.1\t6.96325\n1549.7\t6.99639\n1555.2\t7.02915\n1560.8\t7.06244\n1566.4\t7.09581\n1572.0\t7.12925\n1577.7\t7.16322\n1583.3\t7.19682\n1589.0\t7.22273\n1594.7\t7.24864\n1600.4\t7.27455\n1606.1\t7.30045\n1611.9\t7.32682\n1617.6\t7.35273\n1623.4\t7.37909\n1629.2\t7.40545\n1635.0\t7.43182\n1640.9\t7.45864\n1646.7\t7.485\n1652.6\t7.49478\n1658.5\t7.49393\n1664.4\t7.48718\n1670.4\t7.45922\n1676.3\t7.44195\n1682.3\t7.42532\n1688.4\t7.40933\n1694.4\t7.39307\n1700.4\t7.37701\n1706.5\t7.36155\n1712.6\t7.34627\n1718.8\t7.33159\n1724.9\t7.31665\n1731.1\t7.30229\n1737.3\t7.2881\n1743.5\t7.27405\n1749.8\t7.27568\n1756.0\t7.2637\n1762.3\t7.26722\n1768.7\t7.27112\n1775.0\t7.27459\n1781.4\t7.27845\n1787.8\t7.28228\n1794.2\t7.28609\n1800.7\t7.29028\n1807.2\t7.29445\n1813.7\t7.29859\n1820.2\t7.30271\n1826.8\t7.3072\n1833.4\t7.31167\n1840.0\t7.3161\n1846.6\t7.32052\n1853.3\t7.3253\n1860.0\t7.34748\n1866.8\t7.37002\n1873.5\t7.39215\n1880.3\t7.41465\n1887.1\t7.43712\n1894.0\t7.45996\n1900.9\t7.48277\n1907.8\t7.50555\n1914.7\t7.52831\n1921.7\t7.55143\n1928.7\t7.57453\n1935.7\t7.5976\n1942.7\t7.62065\n1949.8\t7.64405\n1956.9\t7.66744\n1964.1\t7.69118\n1971.2\t7.71451\n1978.4\t7.7382\n1985.7\t7.76226\n1992.9\t7.78589\n2000.2\t7.80989\n2007.5\t7.83386\n2014.9\t7.8582\n2022.3\t7.8825\n2029.7\t7.90678\n2037.1\t7.93103\n2044.6\t7.95564\n2052.0\t7.98444\n2059.6\t8.00708\n2067.1\t8.02931\n2074.7\t8.05188\n2082.3\t8.07441\n2089.9\t8.0969\n2097.6\t8.11974\n2105.3\t8.14254\n2113.0\t8.16531\n2120.7\t8.18803\n2128.5\t8.2111\n2136.2\t8.23375\n2144.1\t8.25712\n2151.9\t8.28008\n2159.8\t8.30337\n2167.6\t8.32625\n2175.6\t8.34985\n2183.5\t8.37303\n2191.5\t8.40299\n2199.4\t8.43652\n2207.4\t8.47696\n2215.5\t8.52115\n2223.5\t8.5684\n2231.6\t8.61622\n2239.7\t8.66422\n2247.8\t8.7124\n2255.9\t8.76448\n2264.1\t8.81719\n2272.2\t8.86976\n2280.4\t8.92297\n2288.6\t8.97643\n2296.9\t9.03055\n2305.1\t9.08453\n2313.4\t9.13916\n2321.6\t9.19366\n2329.9\t9.24883\n2338.2\t9.30426\n2346.5\t9.35995\n2354.8\t9.41592\n2363.2\t9.47257\n2371.5\t9.52909\n2379.9\t9.58629\n2388.3\t9.64377\n2396.6\t9.70113\n2405.0\t9.75917\n2413.4\t9.81751\n2421.8\t9.87613\n2430.2\t9.93505\n2438.6\t9.99426\n2447.1\t10.05418\n2455.5\t10.11399\n2463.9\t10.17409\n2472.3\t10.2345\n2480.8\t10.29563\n2489.2\t10.35666\n"
    win.close()
    # file file: 1-6
    destination_file_path = "NH_case/ref_cm.txt"
    destination_unit = "cm-1"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_cm.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    win = main.ConvolutionMainW()
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(1)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    # assert: Gauss function
    convolution_type = 1  # "Gauss function"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Gauss function\ndestination_wavelength_cm-1\tdestination_width\n4019.821\t16.749254\n4033.525\t16.806354\n4047.308\t16.863784\n4061.183\t16.921594\n4075.142\t16.97976\n4089.2\t17.038334\n4103.347\t17.097279\n4117.585\t17.156604\n4131.91\t17.216293\n4146.317\t17.27632\n4160.8\t17.336666\n4175.378\t17.397406\n4190.049\t17.458537\n4204.801\t17.520003\n4219.639\t17.581829\n4234.563\t17.644011\n4249.567\t17.706529\n4264.651\t17.769377\n4279.818\t17.832575\n4295.073\t17.896139\n4310.412\t17.960049\n4325.832\t18.0243\n4341.322\t18.08884\n4356.892\t18.153718\n4372.544\t18.218934\n4388.282\t18.284509\n4404.097\t18.350404\n4419.993\t18.416638\n4435.963\t18.483179\n4451.999\t18.549996\n4468.108\t18.617115\n4484.305\t18.684604\n4500.58\t18.752415\n4516.93\t18.820542\n4533.353\t18.888969\n4549.833\t18.957636\n4566.385\t19.026605\n4583.027\t19.095946\n4599.738\t19.165574\n4616.522\t19.235507\n4633.379\t19.305747\n4650.304\t19.376267\n4667.279\t19.446996\n4684.332\t19.518051\n4701.466\t19.589443\n4718.668\t19.661118\n4735.936\t19.733067\n4753.263\t19.805262\n4770.662\t19.87776\n4788.132\t19.950551\n4805.659\t20.02358\n4823.247\t20.096864\n4840.904\t20.170432\n4858.624\t20.244266\n4876.417\t20.318404\n4894.264\t20.392768\n4912.175\t20.467397\n4930.145\t20.54227\n4948.185\t20.617438\n4966.289\t20.69287\n4984.453\t20.768556\n5002.674\t20.844475\n5020.952\t20.920635\n5039.296\t20.997068\n5057.696\t21.073732\n5076.16\t21.150667\n5094.685\t21.227853\n5113.264\t21.305266\n5131.895\t21.382895\n5150.596\t21.460815\n5169.342\t21.538927\n5188.156\t21.617318\n5207.032\t21.695965\n5225.96\t21.774834\n5244.941\t21.853922\n5263.989\t21.933288\n5283.095\t22.012894\n5302.258\t22.092741\n5321.467\t22.17278\n5340.742\t22.253092\n5360.079\t22.333664\n5379.471\t22.414461\n5398.918\t22.495491\n5418.421\t22.576756\n5437.98\t22.658252\n5457.607\t22.740028\n5477.285\t22.822021\n5497.009\t22.904206\n5516.8\t22.986667\n5536.66\t23.069417\n5556.577\t23.152406\n5576.567\t23.235695\n5596.613\t23.319221\n5616.715\t23.402981\n5636.871\t23.486961\n5657.107\t23.571279\n5677.402\t23.655842\n5697.752\t23.740635\n5718.161\t23.825671\n5738.657\t23.911071\n5759.208\t23.996698\n5779.819\t24.082579\n5800.515\t24.16881\n5821.274\t24.255309\n5842.111\t24.34213\n5862.995\t24.429145\n5883.969\t24.516539\n5904.993\t24.604139\n5926.087\t24.692031\n5947.259\t24.780244\n5968.499\t24.868748\n5989.814\t24.957557\n6011.23\t25.046792\n6032.698\t25.136243\n6054.262\t25.226091\n6075.873\t25.316138\n6097.587\t25.406613\n6119.348\t25.497284\n6141.208\t25.588369\n6163.138\t25.679743\n6185.164\t25.771517\n6207.278\t25.86366\n6229.474\t25.956141\n6251.766\t26.049026\n6274.128\t26.1422\n6296.587\t26.235779\n6319.111\t26.329631\n6341.733\t26.423888\n6364.449\t26.518536\n6387.25\t26.613542\n6410.162\t26.709008\n6433.173\t26.804886\n6456.278\t26.901159\n6479.475\t26.997811\n6502.767\t27.094861\n6526.141\t27.192256\n6549.616\t27.290068\n6573.196\t27.388316\n6596.876\t27.486984\n6620.662\t27.586091\n6644.558\t27.685658\n6668.569\t27.785706\n6692.665\t27.886106\n6716.869\t27.986952\n6741.161\t28.088171\n6765.57\t28.189876\n6790.083\t28.292013\n6814.7\t28.394584\n6839.445\t28.497686\n6864.285\t28.601187\n6889.244\t28.705185\n6914.305\t28.809603\n6939.447\t28.914363\n6964.715\t29.019644\n6990.074\t29.125309\n7015.55\t29.231458\n7041.138\t29.338074\n7066.823\t29.445097\n7092.631\t29.55263\n7118.532\t29.66055\n7144.521\t29.768837\n7170.607\t29.877531\n7196.797\t29.986655\n7223.09\t30.096209\n7249.471\t30.206129\n7275.966\t30.316524\n7302.538\t30.42724\n7329.207\t30.538364\n7355.965\t30.649853\n7382.771\t30.761545\n7409.68\t30.873665\n7436.647\t30.98603\n7463.711\t31.098798\n7490.839\t31.211828\n7518.034\t31.325141\n7545.274\t31.43864\n7572.591\t31.552462\n7599.928\t31.666365\n7627.311\t31.780464\n7654.735\t31.894728\n7682.185\t32.009104\n7709.678\t32.123659\n7737.183\t32.238264\n7764.711\t32.352961\n7792.228\t32.467617\n7819.745\t32.582273\n7847.242\t32.696843\n7874.698\t32.811241\n7902.134\t32.925557\n7929.529\t33.039703\n7956.861\t33.153588\n7984.153\t33.267304\n8011.35\t33.380627\n8038.469\t33.49362\n8065.492\t33.606216\n8092.37\t33.718206\n8119.137\t33.829737\n8145.757\t33.940654\n"
    # assert: triangle
    convolution_type = 2  # "triangle"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: triangle\ndestination_wavelength_cm-1\tdestination_width\n4019.821\t16.749254\n4033.525\t16.806354\n4047.308\t16.863784\n4061.183\t16.921594\n4075.142\t16.97976\n4089.2\t17.038334\n4103.347\t17.097279\n4117.585\t17.156604\n4131.91\t17.216293\n4146.317\t17.27632\n4160.8\t17.336666\n4175.378\t17.397406\n4190.049\t17.458537\n4204.801\t17.520003\n4219.639\t17.581829\n4234.563\t17.644011\n4249.567\t17.706529\n4264.651\t17.769377\n4279.818\t17.832575\n4295.073\t17.896139\n4310.412\t17.960049\n4325.832\t18.0243\n4341.322\t18.08884\n4356.892\t18.153718\n4372.544\t18.218934\n4388.282\t18.284509\n4404.097\t18.350404\n4419.993\t18.416638\n4435.963\t18.483179\n4451.999\t18.549996\n4468.108\t18.617115\n4484.305\t18.684604\n4500.58\t18.752415\n4516.93\t18.820542\n4533.353\t18.888969\n4549.833\t18.957636\n4566.385\t19.026605\n4583.027\t19.095946\n4599.738\t19.165574\n4616.522\t19.235507\n4633.379\t19.305747\n4650.304\t19.376267\n4667.279\t19.446996\n4684.332\t19.518051\n4701.466\t19.589443\n4718.668\t19.661118\n4735.936\t19.733067\n4753.263\t19.805262\n4770.662\t19.87776\n4788.132\t19.950551\n4805.659\t20.02358\n4823.247\t20.096864\n4840.904\t20.170432\n4858.624\t20.244266\n4876.417\t20.318404\n4894.264\t20.392768\n4912.175\t20.467397\n4930.145\t20.54227\n4948.185\t20.617438\n4966.289\t20.69287\n4984.453\t20.768556\n5002.674\t20.844475\n5020.952\t20.920635\n5039.296\t20.997068\n5057.696\t21.073732\n5076.16\t21.150667\n5094.685\t21.227853\n5113.264\t21.305266\n5131.895\t21.382895\n5150.596\t21.460815\n5169.342\t21.538927\n5188.156\t21.617318\n5207.032\t21.695965\n5225.96\t21.774834\n5244.941\t21.853922\n5263.989\t21.933288\n5283.095\t22.012894\n5302.258\t22.092741\n5321.467\t22.17278\n5340.742\t22.253092\n5360.079\t22.333664\n5379.471\t22.414461\n5398.918\t22.495491\n5418.421\t22.576756\n5437.98\t22.658252\n5457.607\t22.740028\n5477.285\t22.822021\n5497.009\t22.904206\n5516.8\t22.986667\n5536.66\t23.069417\n5556.577\t23.152406\n5576.567\t23.235695\n5596.613\t23.319221\n5616.715\t23.402981\n5636.871\t23.486961\n5657.107\t23.571279\n5677.402\t23.655842\n5697.752\t23.740635\n5718.161\t23.825671\n5738.657\t23.911071\n5759.208\t23.996698\n5779.819\t24.082579\n5800.515\t24.16881\n5821.274\t24.255309\n5842.111\t24.34213\n5862.995\t24.429145\n5883.969\t24.516539\n5904.993\t24.604139\n5926.087\t24.692031\n5947.259\t24.780244\n5968.499\t24.868748\n5989.814\t24.957557\n6011.23\t25.046792\n6032.698\t25.136243\n6054.262\t25.226091\n6075.873\t25.316138\n6097.587\t25.406613\n6119.348\t25.497284\n6141.208\t25.588369\n6163.138\t25.679743\n6185.164\t25.771517\n6207.278\t25.86366\n6229.474\t25.956141\n6251.766\t26.049026\n6274.128\t26.1422\n6296.587\t26.235779\n6319.111\t26.329631\n6341.733\t26.423888\n6364.449\t26.518536\n6387.25\t26.613542\n6410.162\t26.709008\n6433.173\t26.804886\n6456.278\t26.901159\n6479.475\t26.997811\n6502.767\t27.094861\n6526.141\t27.192256\n6549.616\t27.290068\n6573.196\t27.388316\n6596.876\t27.486984\n6620.662\t27.586091\n6644.558\t27.685658\n6668.569\t27.785706\n6692.665\t27.886106\n6716.869\t27.986952\n6741.161\t28.088171\n6765.57\t28.189876\n6790.083\t28.292013\n6814.7\t28.394584\n6839.445\t28.497686\n6864.285\t28.601187\n6889.244\t28.705185\n6914.305\t28.809603\n6939.447\t28.914363\n6964.715\t29.019644\n6990.074\t29.125309\n7015.55\t29.231458\n7041.138\t29.338074\n7066.823\t29.445097\n7092.631\t29.55263\n7118.532\t29.66055\n7144.521\t29.768837\n7170.607\t29.877531\n7196.797\t29.986655\n7223.09\t30.096209\n7249.471\t30.206129\n7275.966\t30.316524\n7302.538\t30.42724\n7329.207\t30.538364\n7355.965\t30.649853\n7382.771\t30.761545\n7409.68\t30.873665\n7436.647\t30.98603\n7463.711\t31.098798\n7490.839\t31.211828\n7518.034\t31.325141\n7545.274\t31.43864\n7572.591\t31.552462\n7599.928\t31.666365\n7627.311\t31.780464\n7654.735\t31.894728\n7682.185\t32.009104\n7709.678\t32.123659\n7737.183\t32.238264\n7764.711\t32.352961\n7792.228\t32.467617\n7819.745\t32.582273\n7847.242\t32.696843\n7874.698\t32.811241\n7902.134\t32.925557\n7929.529\t33.039703\n7956.861\t33.153588\n7984.153\t33.267304\n8011.35\t33.380627\n8038.469\t33.49362\n8065.492\t33.606216\n8092.37\t33.718206\n8119.137\t33.829737\n8145.757\t33.940654\n"
    # assert: trapeze
    convolution_type = 3  # "trapeze"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: trapeze\ndestination_wavelength_cm-1\tdestination_width\tdestination_top\n4019.821\t16.749254\t8.374627\n4033.525\t16.806354\t8.403177\n4047.308\t16.863784\t8.431892\n4061.183\t16.921594\t8.460797\n4075.142\t16.97976\t8.48988\n4089.2\t17.038334\t8.519167\n4103.347\t17.097279\t8.5486395\n4117.585\t17.156604\t8.578302\n4131.91\t17.216293\t8.6081465\n4146.317\t17.27632\t8.63816\n4160.8\t17.336666\t8.668333\n4175.378\t17.397406\t8.698703\n4190.049\t17.458537\t8.7292685\n4204.801\t17.520003\t8.7600015\n4219.639\t17.581829\t8.7909145\n4234.563\t17.644011\t8.8220055\n4249.567\t17.706529\t8.8532645\n4264.651\t17.769377\t8.8846885\n4279.818\t17.832575\t8.9162875\n4295.073\t17.896139\t8.9480695\n4310.412\t17.960049\t8.9800245\n4325.832\t18.0243\t9.01215\n4341.322\t18.08884\t9.04442\n4356.892\t18.153718\t9.076859\n4372.544\t18.218934\t9.109467\n4388.282\t18.284509\t9.1422545\n4404.097\t18.350404\t9.175202\n4419.993\t18.416638\t9.208319\n4435.963\t18.483179\t9.2415895\n4451.999\t18.549996\t9.274998\n4468.108\t18.617115\t9.3085575\n4484.305\t18.684604\t9.342302\n4500.58\t18.752415\t9.3762075\n4516.93\t18.820542\t9.410271\n4533.353\t18.888969\t9.4444845\n4549.833\t18.957636\t9.478818\n4566.385\t19.026605\t9.5133025\n4583.027\t19.095946\t9.547973\n4599.738\t19.165574\t9.582787\n4616.522\t19.235507\t9.6177535\n4633.379\t19.305747\t9.6528735\n4650.304\t19.376267\t9.6881335\n4667.279\t19.446996\t9.723498\n4684.332\t19.518051\t9.7590255\n4701.466\t19.589443\t9.7947215\n4718.668\t19.661118\t9.830559\n4735.936\t19.733067\t9.8665335\n4753.263\t19.805262\t9.902631\n4770.662\t19.87776\t9.93888\n4788.132\t19.950551\t9.9752755\n4805.659\t20.02358\t10.01179\n4823.247\t20.096864\t10.048432\n4840.904\t20.170432\t10.085216\n4858.624\t20.244266\t10.122133\n4876.417\t20.318404\t10.159202\n4894.264\t20.392768\t10.196384\n4912.175\t20.467397\t10.233698\n4930.145\t20.54227\t10.271135\n4948.185\t20.617438\t10.308719\n4966.289\t20.69287\t10.346435\n4984.453\t20.768556\t10.384278\n5002.674\t20.844475\t10.422237\n5020.952\t20.920635\t10.460317\n5039.296\t20.997068\t10.498534\n5057.696\t21.073732\t10.536866\n5076.16\t21.150667\t10.575333\n5094.685\t21.227853\t10.613926\n5113.264\t21.305266\t10.652633\n5131.895\t21.382895\t10.691447\n5150.596\t21.460815\t10.730407\n5169.342\t21.538927\t10.769463\n5188.156\t21.617318\t10.808659\n5207.032\t21.695965\t10.847982\n5225.96\t21.774834\t10.887417\n5244.941\t21.853922\t10.926961\n5263.989\t21.933288\t10.966644\n5283.095\t22.012894\t11.006447\n5302.258\t22.092741\t11.04637\n5321.467\t22.17278\t11.08639\n5340.742\t22.253092\t11.126546\n5360.079\t22.333664\t11.166832\n5379.471\t22.414461\t11.20723\n5398.918\t22.495491\t11.247745\n5418.421\t22.576756\t11.288378\n5437.98\t22.658252\t11.329126\n5457.607\t22.740028\t11.370014\n5477.285\t22.822021\t11.41101\n5497.009\t22.904206\t11.452103\n5516.8\t22.986667\t11.493333\n5536.66\t23.069417\t11.534708\n5556.577\t23.152406\t11.576203\n5576.567\t23.235695\t11.617847\n5596.613\t23.319221\t11.65961\n5616.715\t23.402981\t11.70149\n5636.871\t23.486961\t11.74348\n5657.107\t23.571279\t11.785639\n5677.402\t23.655842\t11.827921\n5697.752\t23.740635\t11.870317\n5718.161\t23.825671\t11.912835\n5738.657\t23.911071\t11.955535\n5759.208\t23.996698\t11.998349\n5779.819\t24.082579\t12.041289\n5800.515\t24.16881\t12.084405\n5821.274\t24.255309\t12.127654\n5842.111\t24.34213\t12.171065\n5862.995\t24.429145\t12.214572\n5883.969\t24.516539\t12.258269\n5904.993\t24.604139\t12.302069\n5926.087\t24.692031\t12.346015\n5947.259\t24.780244\t12.390122\n5968.499\t24.868748\t12.434374\n5989.814\t24.957557\t12.478778\n6011.23\t25.046792\t12.523396\n6032.698\t25.136243\t12.568121\n6054.262\t25.226091\t12.613045\n6075.873\t25.316138\t12.658069\n6097.587\t25.406613\t12.703306\n6119.348\t25.497284\t12.748642\n6141.208\t25.588369\t12.794184\n6163.138\t25.679743\t12.839871\n6185.164\t25.771517\t12.885758\n6207.278\t25.86366\t12.93183\n6229.474\t25.956141\t12.97807\n6251.766\t26.049026\t13.024513\n6274.128\t26.1422\t13.0711\n6296.587\t26.235779\t13.117889\n6319.111\t26.329631\t13.164815\n6341.733\t26.423888\t13.211944\n6364.449\t26.518536\t13.259268\n6387.25\t26.613542\t13.306771\n6410.162\t26.709008\t13.354504\n6433.173\t26.804886\t13.402443\n6456.278\t26.901159\t13.450579\n6479.475\t26.997811\t13.498905\n6502.767\t27.094861\t13.54743\n6526.141\t27.192256\t13.596128\n6549.616\t27.290068\t13.645034\n6573.196\t27.388316\t13.694158\n6596.876\t27.486984\t13.743492\n6620.662\t27.586091\t13.793045\n6644.558\t27.685658\t13.842829\n6668.569\t27.785706\t13.892853\n6692.665\t27.886106\t13.943053\n6716.869\t27.986952\t13.993476\n6741.161\t28.088171\t14.044085\n6765.57\t28.189876\t14.094938\n6790.083\t28.292013\t14.146006\n6814.7\t28.394584\t14.197292\n6839.445\t28.497686\t14.248843\n6864.285\t28.601187\t14.300593\n6889.244\t28.705185\t14.352592\n6914.305\t28.809603\t14.404801\n6939.447\t28.914363\t14.457181\n6964.715\t29.019644\t14.509822\n6990.074\t29.125309\t14.562654\n7015.55\t29.231458\t14.615729\n7041.138\t29.338074\t14.669037\n7066.823\t29.445097\t14.722548\n7092.631\t29.55263\t14.776315\n7118.532\t29.66055\t14.830275\n7144.521\t29.768837\t14.884418\n7170.607\t29.877531\t14.938765\n7196.797\t29.986655\t14.993327\n7223.09\t30.096209\t15.048104\n7249.471\t30.206129\t15.103064\n7275.966\t30.316524\t15.158262\n7302.538\t30.42724\t15.21362\n7329.207\t30.538364\t15.269182\n7355.965\t30.649853\t15.324926\n7382.771\t30.761545\t15.380772\n7409.68\t30.873665\t15.436832\n7436.647\t30.98603\t15.493015\n7463.711\t31.098798\t15.549399\n7490.839\t31.211828\t15.605914\n7518.034\t31.325141\t15.66257\n7545.274\t31.43864\t15.71932\n7572.591\t31.552462\t15.776231\n7599.928\t31.666365\t15.833182\n7627.311\t31.780464\t15.890232\n7654.735\t31.894728\t15.947364\n7682.185\t32.009104\t16.004552\n7709.678\t32.123659\t16.061829\n7737.183\t32.238264\t16.119132\n7764.711\t32.352961\t16.17648\n7792.228\t32.467617\t16.233808\n7819.745\t32.582273\t16.291136\n7847.242\t32.696843\t16.348421\n7874.698\t32.811241\t16.40562\n7902.134\t32.925557\t16.462778\n7929.529\t33.039703\t16.519851\n7956.861\t33.153588\t16.576794\n7984.153\t33.267304\t16.633652\n8011.35\t33.380627\t16.690313\n8038.469\t33.49362\t16.74681\n8065.492\t33.606216\t16.803108\n8092.37\t33.718206\t16.859103\n8119.137\t33.829737\t16.914868\n8145.757\t33.940654\t16.970327\n"
    # assert: Lorentz
    convolution_type = 4  # "Lorentz"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Lorentz function\ndestination_wavelength_cm-1\tdestination_width\n4019.821\t16.749254\n4033.525\t16.806354\n4047.308\t16.863784\n4061.183\t16.921594\n4075.142\t16.97976\n4089.2\t17.038334\n4103.347\t17.097279\n4117.585\t17.156604\n4131.91\t17.216293\n4146.317\t17.27632\n4160.8\t17.336666\n4175.378\t17.397406\n4190.049\t17.458537\n4204.801\t17.520003\n4219.639\t17.581829\n4234.563\t17.644011\n4249.567\t17.706529\n4264.651\t17.769377\n4279.818\t17.832575\n4295.073\t17.896139\n4310.412\t17.960049\n4325.832\t18.0243\n4341.322\t18.08884\n4356.892\t18.153718\n4372.544\t18.218934\n4388.282\t18.284509\n4404.097\t18.350404\n4419.993\t18.416638\n4435.963\t18.483179\n4451.999\t18.549996\n4468.108\t18.617115\n4484.305\t18.684604\n4500.58\t18.752415\n4516.93\t18.820542\n4533.353\t18.888969\n4549.833\t18.957636\n4566.385\t19.026605\n4583.027\t19.095946\n4599.738\t19.165574\n4616.522\t19.235507\n4633.379\t19.305747\n4650.304\t19.376267\n4667.279\t19.446996\n4684.332\t19.518051\n4701.466\t19.589443\n4718.668\t19.661118\n4735.936\t19.733067\n4753.263\t19.805262\n4770.662\t19.87776\n4788.132\t19.950551\n4805.659\t20.02358\n4823.247\t20.096864\n4840.904\t20.170432\n4858.624\t20.244266\n4876.417\t20.318404\n4894.264\t20.392768\n4912.175\t20.467397\n4930.145\t20.54227\n4948.185\t20.617438\n4966.289\t20.69287\n4984.453\t20.768556\n5002.674\t20.844475\n5020.952\t20.920635\n5039.296\t20.997068\n5057.696\t21.073732\n5076.16\t21.150667\n5094.685\t21.227853\n5113.264\t21.305266\n5131.895\t21.382895\n5150.596\t21.460815\n5169.342\t21.538927\n5188.156\t21.617318\n5207.032\t21.695965\n5225.96\t21.774834\n5244.941\t21.853922\n5263.989\t21.933288\n5283.095\t22.012894\n5302.258\t22.092741\n5321.467\t22.17278\n5340.742\t22.253092\n5360.079\t22.333664\n5379.471\t22.414461\n5398.918\t22.495491\n5418.421\t22.576756\n5437.98\t22.658252\n5457.607\t22.740028\n5477.285\t22.822021\n5497.009\t22.904206\n5516.8\t22.986667\n5536.66\t23.069417\n5556.577\t23.152406\n5576.567\t23.235695\n5596.613\t23.319221\n5616.715\t23.402981\n5636.871\t23.486961\n5657.107\t23.571279\n5677.402\t23.655842\n5697.752\t23.740635\n5718.161\t23.825671\n5738.657\t23.911071\n5759.208\t23.996698\n5779.819\t24.082579\n5800.515\t24.16881\n5821.274\t24.255309\n5842.111\t24.34213\n5862.995\t24.429145\n5883.969\t24.516539\n5904.993\t24.604139\n5926.087\t24.692031\n5947.259\t24.780244\n5968.499\t24.868748\n5989.814\t24.957557\n6011.23\t25.046792\n6032.698\t25.136243\n6054.262\t25.226091\n6075.873\t25.316138\n6097.587\t25.406613\n6119.348\t25.497284\n6141.208\t25.588369\n6163.138\t25.679743\n6185.164\t25.771517\n6207.278\t25.86366\n6229.474\t25.956141\n6251.766\t26.049026\n6274.128\t26.1422\n6296.587\t26.235779\n6319.111\t26.329631\n6341.733\t26.423888\n6364.449\t26.518536\n6387.25\t26.613542\n6410.162\t26.709008\n6433.173\t26.804886\n6456.278\t26.901159\n6479.475\t26.997811\n6502.767\t27.094861\n6526.141\t27.192256\n6549.616\t27.290068\n6573.196\t27.388316\n6596.876\t27.486984\n6620.662\t27.586091\n6644.558\t27.685658\n6668.569\t27.785706\n6692.665\t27.886106\n6716.869\t27.986952\n6741.161\t28.088171\n6765.57\t28.189876\n6790.083\t28.292013\n6814.7\t28.394584\n6839.445\t28.497686\n6864.285\t28.601187\n6889.244\t28.705185\n6914.305\t28.809603\n6939.447\t28.914363\n6964.715\t29.019644\n6990.074\t29.125309\n7015.55\t29.231458\n7041.138\t29.338074\n7066.823\t29.445097\n7092.631\t29.55263\n7118.532\t29.66055\n7144.521\t29.768837\n7170.607\t29.877531\n7196.797\t29.986655\n7223.09\t30.096209\n7249.471\t30.206129\n7275.966\t30.316524\n7302.538\t30.42724\n7329.207\t30.538364\n7355.965\t30.649853\n7382.771\t30.761545\n7409.68\t30.873665\n7436.647\t30.98603\n7463.711\t31.098798\n7490.839\t31.211828\n7518.034\t31.325141\n7545.274\t31.43864\n7572.591\t31.552462\n7599.928\t31.666365\n7627.311\t31.780464\n7654.735\t31.894728\n7682.185\t32.009104\n7709.678\t32.123659\n7737.183\t32.238264\n7764.711\t32.352961\n7792.228\t32.467617\n7819.745\t32.582273\n7847.242\t32.696843\n7874.698\t32.811241\n7902.134\t32.925557\n7929.529\t33.039703\n7956.861\t33.153588\n7984.153\t33.267304\n8011.35\t33.380627\n8038.469\t33.49362\n8065.492\t33.606216\n8092.37\t33.718206\n8119.137\t33.829737\n8145.757\t33.940654\n"
    # assert: Voigt
    convolution_type = 5  # "Voigt"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Voigt profile\ndestination_wavelength_cm-1\tdestination_width_Gauss\tdestination_width_Lorentz\n4019.821\t16.749254\t8.374627\n4033.525\t16.806354\t8.403177\n4047.308\t16.863784\t8.431892\n4061.183\t16.921594\t8.460797\n4075.142\t16.97976\t8.48988\n4089.2\t17.038334\t8.519167\n4103.347\t17.097279\t8.5486395\n4117.585\t17.156604\t8.578302\n4131.91\t17.216293\t8.6081465\n4146.317\t17.27632\t8.63816\n4160.8\t17.336666\t8.668333\n4175.378\t17.397406\t8.698703\n4190.049\t17.458537\t8.7292685\n4204.801\t17.520003\t8.7600015\n4219.639\t17.581829\t8.7909145\n4234.563\t17.644011\t8.8220055\n4249.567\t17.706529\t8.8532645\n4264.651\t17.769377\t8.8846885\n4279.818\t17.832575\t8.9162875\n4295.073\t17.896139\t8.9480695\n4310.412\t17.960049\t8.9800245\n4325.832\t18.0243\t9.01215\n4341.322\t18.08884\t9.04442\n4356.892\t18.153718\t9.076859\n4372.544\t18.218934\t9.109467\n4388.282\t18.284509\t9.1422545\n4404.097\t18.350404\t9.175202\n4419.993\t18.416638\t9.208319\n4435.963\t18.483179\t9.2415895\n4451.999\t18.549996\t9.274998\n4468.108\t18.617115\t9.3085575\n4484.305\t18.684604\t9.342302\n4500.58\t18.752415\t9.3762075\n4516.93\t18.820542\t9.410271\n4533.353\t18.888969\t9.4444845\n4549.833\t18.957636\t9.478818\n4566.385\t19.026605\t9.5133025\n4583.027\t19.095946\t9.547973\n4599.738\t19.165574\t9.582787\n4616.522\t19.235507\t9.6177535\n4633.379\t19.305747\t9.6528735\n4650.304\t19.376267\t9.6881335\n4667.279\t19.446996\t9.723498\n4684.332\t19.518051\t9.7590255\n4701.466\t19.589443\t9.7947215\n4718.668\t19.661118\t9.830559\n4735.936\t19.733067\t9.8665335\n4753.263\t19.805262\t9.902631\n4770.662\t19.87776\t9.93888\n4788.132\t19.950551\t9.9752755\n4805.659\t20.02358\t10.01179\n4823.247\t20.096864\t10.048432\n4840.904\t20.170432\t10.085216\n4858.624\t20.244266\t10.122133\n4876.417\t20.318404\t10.159202\n4894.264\t20.392768\t10.196384\n4912.175\t20.467397\t10.233698\n4930.145\t20.54227\t10.271135\n4948.185\t20.617438\t10.308719\n4966.289\t20.69287\t10.346435\n4984.453\t20.768556\t10.384278\n5002.674\t20.844475\t10.422237\n5020.952\t20.920635\t10.460317\n5039.296\t20.997068\t10.498534\n5057.696\t21.073732\t10.536866\n5076.16\t21.150667\t10.575333\n5094.685\t21.227853\t10.613926\n5113.264\t21.305266\t10.652633\n5131.895\t21.382895\t10.691447\n5150.596\t21.460815\t10.730407\n5169.342\t21.538927\t10.769463\n5188.156\t21.617318\t10.808659\n5207.032\t21.695965\t10.847982\n5225.96\t21.774834\t10.887417\n5244.941\t21.853922\t10.926961\n5263.989\t21.933288\t10.966644\n5283.095\t22.012894\t11.006447\n5302.258\t22.092741\t11.04637\n5321.467\t22.17278\t11.08639\n5340.742\t22.253092\t11.126546\n5360.079\t22.333664\t11.166832\n5379.471\t22.414461\t11.20723\n5398.918\t22.495491\t11.247745\n5418.421\t22.576756\t11.288378\n5437.98\t22.658252\t11.329126\n5457.607\t22.740028\t11.370014\n5477.285\t22.822021\t11.41101\n5497.009\t22.904206\t11.452103\n5516.8\t22.986667\t11.493333\n5536.66\t23.069417\t11.534708\n5556.577\t23.152406\t11.576203\n5576.567\t23.235695\t11.617847\n5596.613\t23.319221\t11.65961\n5616.715\t23.402981\t11.70149\n5636.871\t23.486961\t11.74348\n5657.107\t23.571279\t11.785639\n5677.402\t23.655842\t11.827921\n5697.752\t23.740635\t11.870317\n5718.161\t23.825671\t11.912835\n5738.657\t23.911071\t11.955535\n5759.208\t23.996698\t11.998349\n5779.819\t24.082579\t12.041289\n5800.515\t24.16881\t12.084405\n5821.274\t24.255309\t12.127654\n5842.111\t24.34213\t12.171065\n5862.995\t24.429145\t12.214572\n5883.969\t24.516539\t12.258269\n5904.993\t24.604139\t12.302069\n5926.087\t24.692031\t12.346015\n5947.259\t24.780244\t12.390122\n5968.499\t24.868748\t12.434374\n5989.814\t24.957557\t12.478778\n6011.23\t25.046792\t12.523396\n6032.698\t25.136243\t12.568121\n6054.262\t25.226091\t12.613045\n6075.873\t25.316138\t12.658069\n6097.587\t25.406613\t12.703306\n6119.348\t25.497284\t12.748642\n6141.208\t25.588369\t12.794184\n6163.138\t25.679743\t12.839871\n6185.164\t25.771517\t12.885758\n6207.278\t25.86366\t12.93183\n6229.474\t25.956141\t12.97807\n6251.766\t26.049026\t13.024513\n6274.128\t26.1422\t13.0711\n6296.587\t26.235779\t13.117889\n6319.111\t26.329631\t13.164815\n6341.733\t26.423888\t13.211944\n6364.449\t26.518536\t13.259268\n6387.25\t26.613542\t13.306771\n6410.162\t26.709008\t13.354504\n6433.173\t26.804886\t13.402443\n6456.278\t26.901159\t13.450579\n6479.475\t26.997811\t13.498905\n6502.767\t27.094861\t13.54743\n6526.141\t27.192256\t13.596128\n6549.616\t27.290068\t13.645034\n6573.196\t27.388316\t13.694158\n6596.876\t27.486984\t13.743492\n6620.662\t27.586091\t13.793045\n6644.558\t27.685658\t13.842829\n6668.569\t27.785706\t13.892853\n6692.665\t27.886106\t13.943053\n6716.869\t27.986952\t13.993476\n6741.161\t28.088171\t14.044085\n6765.57\t28.189876\t14.094938\n6790.083\t28.292013\t14.146006\n6814.7\t28.394584\t14.197292\n6839.445\t28.497686\t14.248843\n6864.285\t28.601187\t14.300593\n6889.244\t28.705185\t14.352592\n6914.305\t28.809603\t14.404801\n6939.447\t28.914363\t14.457181\n6964.715\t29.019644\t14.509822\n6990.074\t29.125309\t14.562654\n7015.55\t29.231458\t14.615729\n7041.138\t29.338074\t14.669037\n7066.823\t29.445097\t14.722548\n7092.631\t29.55263\t14.776315\n7118.532\t29.66055\t14.830275\n7144.521\t29.768837\t14.884418\n7170.607\t29.877531\t14.938765\n7196.797\t29.986655\t14.993327\n7223.09\t30.096209\t15.048104\n7249.471\t30.206129\t15.103064\n7275.966\t30.316524\t15.158262\n7302.538\t30.42724\t15.21362\n7329.207\t30.538364\t15.269182\n7355.965\t30.649853\t15.324926\n7382.771\t30.761545\t15.380772\n7409.68\t30.873665\t15.436832\n7436.647\t30.98603\t15.493015\n7463.711\t31.098798\t15.549399\n7490.839\t31.211828\t15.605914\n7518.034\t31.325141\t15.66257\n7545.274\t31.43864\t15.71932\n7572.591\t31.552462\t15.776231\n7599.928\t31.666365\t15.833182\n7627.311\t31.780464\t15.890232\n7654.735\t31.894728\t15.947364\n7682.185\t32.009104\t16.004552\n7709.678\t32.123659\t16.061829\n7737.183\t32.238264\t16.119132\n7764.711\t32.352961\t16.17648\n7792.228\t32.467617\t16.233808\n7819.745\t32.582273\t16.291136\n7847.242\t32.696843\t16.348421\n7874.698\t32.811241\t16.40562\n7902.134\t32.925557\t16.462778\n7929.529\t33.039703\t16.519851\n7956.861\t33.153588\t16.576794\n7984.153\t33.267304\t16.633652\n8011.35\t33.380627\t16.690313\n8038.469\t33.49362\t16.74681\n8065.492\t33.606216\t16.803108\n8092.37\t33.718206\t16.859103\n8119.137\t33.829737\t16.914868\n8145.757\t33.940654\t16.970327\n"
    # assert: Gauss + Lorentz
    convolution_type = 6  # "Gauss + Lorentz"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Gauss & Lorentz sum, Gauss function part: 0.5\ndestination_wavelength_cm-1\tdestination_width_Gauss\tdestination_width_Lorentz\n4019.821\t16.749254\t8.374627\n4033.525\t16.806354\t8.403177\n4047.308\t16.863784\t8.431892\n4061.183\t16.921594\t8.460797\n4075.142\t16.97976\t8.48988\n4089.2\t17.038334\t8.519167\n4103.347\t17.097279\t8.5486395\n4117.585\t17.156604\t8.578302\n4131.91\t17.216293\t8.6081465\n4146.317\t17.27632\t8.63816\n4160.8\t17.336666\t8.668333\n4175.378\t17.397406\t8.698703\n4190.049\t17.458537\t8.7292685\n4204.801\t17.520003\t8.7600015\n4219.639\t17.581829\t8.7909145\n4234.563\t17.644011\t8.8220055\n4249.567\t17.706529\t8.8532645\n4264.651\t17.769377\t8.8846885\n4279.818\t17.832575\t8.9162875\n4295.073\t17.896139\t8.9480695\n4310.412\t17.960049\t8.9800245\n4325.832\t18.0243\t9.01215\n4341.322\t18.08884\t9.04442\n4356.892\t18.153718\t9.076859\n4372.544\t18.218934\t9.109467\n4388.282\t18.284509\t9.1422545\n4404.097\t18.350404\t9.175202\n4419.993\t18.416638\t9.208319\n4435.963\t18.483179\t9.2415895\n4451.999\t18.549996\t9.274998\n4468.108\t18.617115\t9.3085575\n4484.305\t18.684604\t9.342302\n4500.58\t18.752415\t9.3762075\n4516.93\t18.820542\t9.410271\n4533.353\t18.888969\t9.4444845\n4549.833\t18.957636\t9.478818\n4566.385\t19.026605\t9.5133025\n4583.027\t19.095946\t9.547973\n4599.738\t19.165574\t9.582787\n4616.522\t19.235507\t9.6177535\n4633.379\t19.305747\t9.6528735\n4650.304\t19.376267\t9.6881335\n4667.279\t19.446996\t9.723498\n4684.332\t19.518051\t9.7590255\n4701.466\t19.589443\t9.7947215\n4718.668\t19.661118\t9.830559\n4735.936\t19.733067\t9.8665335\n4753.263\t19.805262\t9.902631\n4770.662\t19.87776\t9.93888\n4788.132\t19.950551\t9.9752755\n4805.659\t20.02358\t10.01179\n4823.247\t20.096864\t10.048432\n4840.904\t20.170432\t10.085216\n4858.624\t20.244266\t10.122133\n4876.417\t20.318404\t10.159202\n4894.264\t20.392768\t10.196384\n4912.175\t20.467397\t10.233698\n4930.145\t20.54227\t10.271135\n4948.185\t20.617438\t10.308719\n4966.289\t20.69287\t10.346435\n4984.453\t20.768556\t10.384278\n5002.674\t20.844475\t10.422237\n5020.952\t20.920635\t10.460317\n5039.296\t20.997068\t10.498534\n5057.696\t21.073732\t10.536866\n5076.16\t21.150667\t10.575333\n5094.685\t21.227853\t10.613926\n5113.264\t21.305266\t10.652633\n5131.895\t21.382895\t10.691447\n5150.596\t21.460815\t10.730407\n5169.342\t21.538927\t10.769463\n5188.156\t21.617318\t10.808659\n5207.032\t21.695965\t10.847982\n5225.96\t21.774834\t10.887417\n5244.941\t21.853922\t10.926961\n5263.989\t21.933288\t10.966644\n5283.095\t22.012894\t11.006447\n5302.258\t22.092741\t11.04637\n5321.467\t22.17278\t11.08639\n5340.742\t22.253092\t11.126546\n5360.079\t22.333664\t11.166832\n5379.471\t22.414461\t11.20723\n5398.918\t22.495491\t11.247745\n5418.421\t22.576756\t11.288378\n5437.98\t22.658252\t11.329126\n5457.607\t22.740028\t11.370014\n5477.285\t22.822021\t11.41101\n5497.009\t22.904206\t11.452103\n5516.8\t22.986667\t11.493333\n5536.66\t23.069417\t11.534708\n5556.577\t23.152406\t11.576203\n5576.567\t23.235695\t11.617847\n5596.613\t23.319221\t11.65961\n5616.715\t23.402981\t11.70149\n5636.871\t23.486961\t11.74348\n5657.107\t23.571279\t11.785639\n5677.402\t23.655842\t11.827921\n5697.752\t23.740635\t11.870317\n5718.161\t23.825671\t11.912835\n5738.657\t23.911071\t11.955535\n5759.208\t23.996698\t11.998349\n5779.819\t24.082579\t12.041289\n5800.515\t24.16881\t12.084405\n5821.274\t24.255309\t12.127654\n5842.111\t24.34213\t12.171065\n5862.995\t24.429145\t12.214572\n5883.969\t24.516539\t12.258269\n5904.993\t24.604139\t12.302069\n5926.087\t24.692031\t12.346015\n5947.259\t24.780244\t12.390122\n5968.499\t24.868748\t12.434374\n5989.814\t24.957557\t12.478778\n6011.23\t25.046792\t12.523396\n6032.698\t25.136243\t12.568121\n6054.262\t25.226091\t12.613045\n6075.873\t25.316138\t12.658069\n6097.587\t25.406613\t12.703306\n6119.348\t25.497284\t12.748642\n6141.208\t25.588369\t12.794184\n6163.138\t25.679743\t12.839871\n6185.164\t25.771517\t12.885758\n6207.278\t25.86366\t12.93183\n6229.474\t25.956141\t12.97807\n6251.766\t26.049026\t13.024513\n6274.128\t26.1422\t13.0711\n6296.587\t26.235779\t13.117889\n6319.111\t26.329631\t13.164815\n6341.733\t26.423888\t13.211944\n6364.449\t26.518536\t13.259268\n6387.25\t26.613542\t13.306771\n6410.162\t26.709008\t13.354504\n6433.173\t26.804886\t13.402443\n6456.278\t26.901159\t13.450579\n6479.475\t26.997811\t13.498905\n6502.767\t27.094861\t13.54743\n6526.141\t27.192256\t13.596128\n6549.616\t27.290068\t13.645034\n6573.196\t27.388316\t13.694158\n6596.876\t27.486984\t13.743492\n6620.662\t27.586091\t13.793045\n6644.558\t27.685658\t13.842829\n6668.569\t27.785706\t13.892853\n6692.665\t27.886106\t13.943053\n6716.869\t27.986952\t13.993476\n6741.161\t28.088171\t14.044085\n6765.57\t28.189876\t14.094938\n6790.083\t28.292013\t14.146006\n6814.7\t28.394584\t14.197292\n6839.445\t28.497686\t14.248843\n6864.285\t28.601187\t14.300593\n6889.244\t28.705185\t14.352592\n6914.305\t28.809603\t14.404801\n6939.447\t28.914363\t14.457181\n6964.715\t29.019644\t14.509822\n6990.074\t29.125309\t14.562654\n7015.55\t29.231458\t14.615729\n7041.138\t29.338074\t14.669037\n7066.823\t29.445097\t14.722548\n7092.631\t29.55263\t14.776315\n7118.532\t29.66055\t14.830275\n7144.521\t29.768837\t14.884418\n7170.607\t29.877531\t14.938765\n7196.797\t29.986655\t14.993327\n7223.09\t30.096209\t15.048104\n7249.471\t30.206129\t15.103064\n7275.966\t30.316524\t15.158262\n7302.538\t30.42724\t15.21362\n7329.207\t30.538364\t15.269182\n7355.965\t30.649853\t15.324926\n7382.771\t30.761545\t15.380772\n7409.68\t30.873665\t15.436832\n7436.647\t30.98603\t15.493015\n7463.711\t31.098798\t15.549399\n7490.839\t31.211828\t15.605914\n7518.034\t31.325141\t15.66257\n7545.274\t31.43864\t15.71932\n7572.591\t31.552462\t15.776231\n7599.928\t31.666365\t15.833182\n7627.311\t31.780464\t15.890232\n7654.735\t31.894728\t15.947364\n7682.185\t32.009104\t16.004552\n7709.678\t32.123659\t16.061829\n7737.183\t32.238264\t16.119132\n7764.711\t32.352961\t16.17648\n7792.228\t32.467617\t16.233808\n7819.745\t32.582273\t16.291136\n7847.242\t32.696843\t16.348421\n7874.698\t32.811241\t16.40562\n7902.134\t32.925557\t16.462778\n7929.529\t33.039703\t16.519851\n7956.861\t33.153588\t16.576794\n7984.153\t33.267304\t16.633652\n8011.35\t33.380627\t16.690313\n8038.469\t33.49362\t16.74681\n8065.492\t33.606216\t16.803108\n8092.37\t33.718206\t16.859103\n8119.137\t33.829737\t16.914868\n8145.757\t33.940654\t16.970327\n"
    win.close()
    # linear linear: 1-6
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_start = 5.115138
    convolution_width_1_stop = 10.365304
    convolution_width_2_start = 2.557569
    convolution_width_2_stop = 5.182652
    win = main.ConvolutionMainW()
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(1)
    win.conv_wdth_1_start.setValue(convolution_width_1_start)
    win.conv_wdth_1_stop.setValue(convolution_width_1_stop)
    win.conv_wdth_2_start.setValue(convolution_width_2_start)
    win.conv_wdth_2_stop.setValue(convolution_width_2_stop)
    # assert: Gauss function
    convolution_type = 1  # "Gauss function"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Gauss function\ndestination_wavelength_nm\tdestination_width\n1227.633\t5.115138\n1231.659\t5.1319654551282055\n1235.685\t5.14879291025641\n1239.711\t5.1656203653846156\n1243.737\t5.18244782051282\n1247.7630000000001\t5.199275275641026\n1251.789\t5.216102730769231\n1255.815\t5.232930185897436\n1259.8410000000001\t5.249757641025641\n1263.867\t5.266585096153846\n1267.893\t5.283412551282051\n1271.919\t5.300240006410256\n1275.945\t5.317067461538461\n1279.971\t5.333894916666667\n1283.997\t5.3507223717948715\n1288.0230000000001\t5.367549826923077\n1292.049\t5.384377282051282\n1296.075\t5.401204737179487\n1300.101\t5.418032192307693\n1304.127\t5.434859647435897\n1308.153\t5.451687102564103\n1312.179\t5.468514557692307\n1316.205\t5.485342012820513\n1320.231\t5.502169467948718\n1324.257\t5.518996923076923\n1328.2830000000001\t5.535824378205128\n1332.309\t5.552651833333333\n1336.335\t5.5694792884615385\n1340.361\t5.586306743589743\n1344.387\t5.603134198717949\n1348.413\t5.619961653846154\n1352.439\t5.636789108974359\n1356.4650000000001\t5.653616564102564\n1360.491\t5.67044401923077\n1364.517\t5.687271474358974\n1368.5430000000001\t5.70409892948718\n1372.569\t5.720926384615384\n1376.595\t5.73775383974359\n1380.621\t5.7545812948717945\n1384.647\t5.77140875\n1388.673\t5.7882362051282055\n1392.699\t5.80506366025641\n1396.725\t5.821891115384616\n1400.751\t5.83871857051282\n1404.777\t5.855546025641026\n1408.803\t5.87237348076923\n1412.829\t5.889200935897436\n1416.855\t5.906028391025641\n1420.881\t5.922855846153846\n1424.9070000000002\t5.939683301282051\n1428.933\t5.956510756410257\n1432.959\t5.9733382115384615\n1436.9850000000001\t5.990165666666667\n1441.011\t6.0069931217948715\n1445.037\t6.023820576923077\n1449.063\t6.040648032051282\n1453.089\t6.057475487179487\n1457.115\t6.074302942307693\n1461.141\t6.091130397435897\n1465.167\t6.107957852564103\n1469.193\t6.124785307692308\n1473.219\t6.141612762820513\n1477.2450000000001\t6.158440217948717\n1481.271\t6.175267673076923\n1485.297\t6.192095128205128\n1489.323\t6.208922583333333\n1493.3490000000002\t6.2257500384615385\n1497.375\t6.242577493589744\n1501.401\t6.259404948717949\n1505.4270000000001\t6.276232403846154\n1509.453\t6.293059858974359\n1513.479\t6.309887314102564\n1517.505\t6.326714769230769\n1521.531\t6.343542224358974\n1525.557\t6.36036967948718\n1529.583\t6.377197134615384\n1533.609\t6.39402458974359\n1537.635\t6.410852044871795\n1541.661\t6.4276795\n1545.687\t6.444506955128205\n1549.713\t6.46133441025641\n1553.739\t6.478161865384616\n1557.765\t6.49498932051282\n1561.791\t6.511816775641026\n1565.817\t6.528644230769231\n1569.843\t6.545471685897436\n1573.8690000000001\t6.562299141025641\n1577.895\t6.579126596153846\n1581.921\t6.595954051282051\n1585.9470000000001\t6.612781506410256\n1589.973\t6.6296089615384615\n1593.999\t6.646436416666667\n1598.025\t6.663263871794872\n1602.051\t6.680091326923077\n1606.077\t6.6969187820512825\n1610.103\t6.713746237179487\n1614.129\t6.730573692307692\n1618.155\t6.747401147435897\n1622.181\t6.764228602564103\n1626.2069999999999\t6.781056057692307\n1630.233\t6.797883512820513\n1634.259\t6.814710967948718\n1638.285\t6.831538423076923\n1642.3110000000001\t6.848365878205128\n1646.337\t6.865193333333333\n1650.363\t6.8820207884615385\n1654.3890000000001\t6.898848243589743\n1658.415\t6.915675698717949\n1662.441\t6.932503153846154\n1666.467\t6.949330608974359\n1670.493\t6.966158064102564\n1674.519\t6.98298551923077\n1678.545\t6.999812974358974\n1682.571\t7.01664042948718\n1686.597\t7.033467884615384\n1690.623\t7.05029533974359\n1694.649\t7.0671227948717945\n1698.675\t7.08395025\n1702.701\t7.1007777051282055\n1706.727\t7.11760516025641\n1710.7530000000002\t7.134432615384616\n1714.779\t7.151260070512821\n1718.805\t7.168087525641026\n1722.8310000000001\t7.18491498076923\n1726.857\t7.201742435897436\n1730.883\t7.218569891025641\n1734.909\t7.235397346153846\n1738.935\t7.252224801282051\n1742.961\t7.269052256410257\n1746.987\t7.2858797115384615\n1751.013\t7.302707166666666\n1755.039\t7.3195346217948725\n1759.065\t7.336362076923077\n1763.091\t7.353189532051282\n1767.117\t7.370016987179487\n1771.143\t7.386844442307693\n1775.1689999999999\t7.403671897435897\n1779.1950000000002\t7.420499352564103\n1783.221\t7.437326807692308\n1787.2469999999998\t7.454154262820513\n1791.2730000000001\t7.4709817179487175\n1795.299\t7.487809173076923\n1799.325\t7.5046366282051284\n1803.351\t7.521464083333333\n1807.377\t7.5382915384615385\n1811.403\t7.555118993589744\n1815.429\t7.571946448717949\n1819.455\t7.588773903846153\n1823.481\t7.60560135897436\n1827.507\t7.622428814102564\n1831.533\t7.639256269230769\n1835.559\t7.656083724358974\n1839.585\t7.67291117948718\n1843.6109999999999\t7.689738634615384\n1847.6370000000002\t7.70656608974359\n1851.663\t7.723393544871795\n1855.6889999999999\t7.740221\n1859.7150000000001\t7.757048455128205\n1863.741\t7.77387591025641\n1867.767\t7.790703365384616\n1871.7930000000001\t7.80753082051282\n1875.819\t7.824358275641026\n1879.845\t7.841185730769231\n1883.871\t7.858013185897436\n1887.897\t7.87484064102564\n1891.923\t7.891668096153847\n1895.949\t7.908495551282051\n1899.975\t7.925323006410256\n1904.001\t7.9421504615384615\n1908.027\t7.958977916666667\n1912.0529999999999\t7.975805371794872\n1916.079\t7.992632826923077\n1920.105\t8.009460282051283\n1924.1309999999999\t8.026287737179487\n1928.1570000000002\t8.043115192307692\n1932.183\t8.059942647435896\n1936.209\t8.076770102564103\n1940.2350000000001\t8.093597557692307\n1944.261\t8.110425012820514\n1948.287\t8.127252467948718\n1952.313\t8.144079923076923\n1956.339\t8.160907378205128\n1960.365\t8.177734833333334\n1964.391\t8.194562288461539\n1968.417\t8.211389743589743\n1972.443\t8.22821719871795\n1976.469\t8.245044653846154\n1980.495\t8.261872108974359\n1984.521\t8.278699564102563\n1988.547\t8.29552701923077\n1992.5729999999999\t8.312354474358974\n1996.5990000000002\t8.329181929487179\n2000.625\t8.346009384615385\n2004.6509999999998\t8.36283683974359\n2008.6770000000001\t8.379664294871795\n2012.703\t8.39649175\n2016.729\t8.413319205128206\n2020.755\t8.43014666025641\n2024.781\t8.446974115384617\n2028.807\t8.463801570512821\n2032.833\t8.480629025641026\n2036.859\t8.49745648076923\n2040.885\t8.514283935897435\n2044.911\t8.531111391025641\n2048.937\t8.547938846153846\n2052.9629999999997\t8.564766301282052\n2056.989\t8.581593756410257\n2061.015\t8.598421211538462\n2065.041\t8.615248666666666\n2069.067\t8.632076121794872\n2073.093\t8.648903576923077\n2077.119\t8.665731032051282\n2081.145\t8.682558487179488\n2085.1710000000003\t8.699385942307693\n2089.197\t8.716213397435897\n2093.223\t8.733040852564102\n2097.249\t8.749868307692308\n2101.275\t8.766695762820513\n2105.301\t8.783523217948717\n2109.327\t8.800350673076924\n2113.353\t8.817178128205128\n2117.379\t8.834005583333333\n2121.4049999999997\t8.850833038461538\n2125.431\t8.867660493589744\n2129.457\t8.884487948717949\n2133.483\t8.901315403846153\n2137.509\t8.91814285897436\n2141.535\t8.934970314102564\n2145.561\t8.951797769230769\n2149.587\t8.968625224358973\n2153.613\t8.98545267948718\n2157.639\t9.002280134615384\n2161.665\t9.01910758974359\n2165.691\t9.035935044871795\n2169.717\t9.0527625\n2173.743\t9.069589955128205\n2177.7690000000002\t9.08641741025641\n2181.795\t9.103244865384616\n2185.821\t9.12007232051282\n2189.8469999999998\t9.136899775641027\n2193.873\t9.153727230769231\n2197.899\t9.170554685897436\n2201.925\t9.18738214102564\n2205.951\t9.204209596153845\n2209.977\t9.221037051282051\n2214.003\t9.237864506410258\n2218.029\t9.254691961538462\n2222.055\t9.271519416666667\n2226.081\t9.288346871794872\n2230.107\t9.305174326923076\n2234.133\t9.32200178205128\n2238.159\t9.338829237179487\n2242.185\t9.355656692307694\n2246.2110000000002\t9.372484147435898\n2250.237\t9.389311602564103\n2254.263\t9.406139057692307\n2258.2889999999998\t9.422966512820512\n2262.315\t9.439793967948718\n2266.341\t9.456621423076923\n2270.367\t9.47344887820513\n2274.393\t9.490276333333334\n2278.419\t9.507103788461539\n2282.4449999999997\t9.523931243589743\n2286.471\t9.540758698717948\n2290.4970000000003\t9.557586153846154\n2294.523\t9.574413608974359\n2298.549\t9.591241064102565\n2302.575\t9.60806851923077\n2306.6009999999997\t9.624895974358974\n2310.627\t9.641723429487179\n2314.6530000000002\t9.658550884615384\n2318.679\t9.67537833974359\n2322.705\t9.692205794871795\n2326.7309999999998\t9.709033250000001\n2330.757\t9.725860705128206\n2334.783\t9.74268816025641\n2338.809\t9.759515615384615\n2342.835\t9.77634307051282\n2346.861\t9.793170525641026\n2350.8869999999997\t9.809997980769232\n2354.913\t9.826825435897437\n2358.9390000000003\t9.843652891025641\n2362.965\t9.860480346153846\n2366.991\t9.87730780128205\n2371.017\t9.894135256410257\n2375.0429999999997\t9.910962711538462\n2379.069\t9.927790166666668\n2383.0950000000003\t9.944617621794873\n2387.121\t9.961445076923077\n2391.147\t9.978272532051282\n2395.173\t9.995099987179486\n2399.199\t10.011927442307693\n2403.225\t10.028754897435897\n2407.251\t10.045582352564104\n2411.277\t10.062409807692308\n2415.303\t10.079237262820513\n2419.3289999999997\t10.096064717948718\n2423.355\t10.112892173076922\n2427.3810000000003\t10.129719628205129\n2431.407\t10.146547083333333\n2435.433\t10.16337453846154\n2439.459\t10.180201993589744\n2443.4849999999997\t10.197029448717949\n2447.511\t10.213856903846153\n2451.5370000000003\t10.230684358974358\n2455.563\t10.247511814102564\n2459.589\t10.264339269230769\n2463.615\t10.281166724358975\n2467.641\t10.29799417948718\n2471.667\t10.314821634615384\n2475.693\t10.331649089743589\n2479.719\t10.348476544871794\n2483.745\t10.365304\n"
    # assert: triangle
    convolution_type = 2  # "triangle"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: triangle\ndestination_wavelength_nm\tdestination_width\n1227.633\t5.115138\n1231.659\t5.1319654551282055\n1235.685\t5.14879291025641\n1239.711\t5.1656203653846156\n1243.737\t5.18244782051282\n1247.7630000000001\t5.199275275641026\n1251.789\t5.216102730769231\n1255.815\t5.232930185897436\n1259.8410000000001\t5.249757641025641\n1263.867\t5.266585096153846\n1267.893\t5.283412551282051\n1271.919\t5.300240006410256\n1275.945\t5.317067461538461\n1279.971\t5.333894916666667\n1283.997\t5.3507223717948715\n1288.0230000000001\t5.367549826923077\n1292.049\t5.384377282051282\n1296.075\t5.401204737179487\n1300.101\t5.418032192307693\n1304.127\t5.434859647435897\n1308.153\t5.451687102564103\n1312.179\t5.468514557692307\n1316.205\t5.485342012820513\n1320.231\t5.502169467948718\n1324.257\t5.518996923076923\n1328.2830000000001\t5.535824378205128\n1332.309\t5.552651833333333\n1336.335\t5.5694792884615385\n1340.361\t5.586306743589743\n1344.387\t5.603134198717949\n1348.413\t5.619961653846154\n1352.439\t5.636789108974359\n1356.4650000000001\t5.653616564102564\n1360.491\t5.67044401923077\n1364.517\t5.687271474358974\n1368.5430000000001\t5.70409892948718\n1372.569\t5.720926384615384\n1376.595\t5.73775383974359\n1380.621\t5.7545812948717945\n1384.647\t5.77140875\n1388.673\t5.7882362051282055\n1392.699\t5.80506366025641\n1396.725\t5.821891115384616\n1400.751\t5.83871857051282\n1404.777\t5.855546025641026\n1408.803\t5.87237348076923\n1412.829\t5.889200935897436\n1416.855\t5.906028391025641\n1420.881\t5.922855846153846\n1424.9070000000002\t5.939683301282051\n1428.933\t5.956510756410257\n1432.959\t5.9733382115384615\n1436.9850000000001\t5.990165666666667\n1441.011\t6.0069931217948715\n1445.037\t6.023820576923077\n1449.063\t6.040648032051282\n1453.089\t6.057475487179487\n1457.115\t6.074302942307693\n1461.141\t6.091130397435897\n1465.167\t6.107957852564103\n1469.193\t6.124785307692308\n1473.219\t6.141612762820513\n1477.2450000000001\t6.158440217948717\n1481.271\t6.175267673076923\n1485.297\t6.192095128205128\n1489.323\t6.208922583333333\n1493.3490000000002\t6.2257500384615385\n1497.375\t6.242577493589744\n1501.401\t6.259404948717949\n1505.4270000000001\t6.276232403846154\n1509.453\t6.293059858974359\n1513.479\t6.309887314102564\n1517.505\t6.326714769230769\n1521.531\t6.343542224358974\n1525.557\t6.36036967948718\n1529.583\t6.377197134615384\n1533.609\t6.39402458974359\n1537.635\t6.410852044871795\n1541.661\t6.4276795\n1545.687\t6.444506955128205\n1549.713\t6.46133441025641\n1553.739\t6.478161865384616\n1557.765\t6.49498932051282\n1561.791\t6.511816775641026\n1565.817\t6.528644230769231\n1569.843\t6.545471685897436\n1573.8690000000001\t6.562299141025641\n1577.895\t6.579126596153846\n1581.921\t6.595954051282051\n1585.9470000000001\t6.612781506410256\n1589.973\t6.6296089615384615\n1593.999\t6.646436416666667\n1598.025\t6.663263871794872\n1602.051\t6.680091326923077\n1606.077\t6.6969187820512825\n1610.103\t6.713746237179487\n1614.129\t6.730573692307692\n1618.155\t6.747401147435897\n1622.181\t6.764228602564103\n1626.2069999999999\t6.781056057692307\n1630.233\t6.797883512820513\n1634.259\t6.814710967948718\n1638.285\t6.831538423076923\n1642.3110000000001\t6.848365878205128\n1646.337\t6.865193333333333\n1650.363\t6.8820207884615385\n1654.3890000000001\t6.898848243589743\n1658.415\t6.915675698717949\n1662.441\t6.932503153846154\n1666.467\t6.949330608974359\n1670.493\t6.966158064102564\n1674.519\t6.98298551923077\n1678.545\t6.999812974358974\n1682.571\t7.01664042948718\n1686.597\t7.033467884615384\n1690.623\t7.05029533974359\n1694.649\t7.0671227948717945\n1698.675\t7.08395025\n1702.701\t7.1007777051282055\n1706.727\t7.11760516025641\n1710.7530000000002\t7.134432615384616\n1714.779\t7.151260070512821\n1718.805\t7.168087525641026\n1722.8310000000001\t7.18491498076923\n1726.857\t7.201742435897436\n1730.883\t7.218569891025641\n1734.909\t7.235397346153846\n1738.935\t7.252224801282051\n1742.961\t7.269052256410257\n1746.987\t7.2858797115384615\n1751.013\t7.302707166666666\n1755.039\t7.3195346217948725\n1759.065\t7.336362076923077\n1763.091\t7.353189532051282\n1767.117\t7.370016987179487\n1771.143\t7.386844442307693\n1775.1689999999999\t7.403671897435897\n1779.1950000000002\t7.420499352564103\n1783.221\t7.437326807692308\n1787.2469999999998\t7.454154262820513\n1791.2730000000001\t7.4709817179487175\n1795.299\t7.487809173076923\n1799.325\t7.5046366282051284\n1803.351\t7.521464083333333\n1807.377\t7.5382915384615385\n1811.403\t7.555118993589744\n1815.429\t7.571946448717949\n1819.455\t7.588773903846153\n1823.481\t7.60560135897436\n1827.507\t7.622428814102564\n1831.533\t7.639256269230769\n1835.559\t7.656083724358974\n1839.585\t7.67291117948718\n1843.6109999999999\t7.689738634615384\n1847.6370000000002\t7.70656608974359\n1851.663\t7.723393544871795\n1855.6889999999999\t7.740221\n1859.7150000000001\t7.757048455128205\n1863.741\t7.77387591025641\n1867.767\t7.790703365384616\n1871.7930000000001\t7.80753082051282\n1875.819\t7.824358275641026\n1879.845\t7.841185730769231\n1883.871\t7.858013185897436\n1887.897\t7.87484064102564\n1891.923\t7.891668096153847\n1895.949\t7.908495551282051\n1899.975\t7.925323006410256\n1904.001\t7.9421504615384615\n1908.027\t7.958977916666667\n1912.0529999999999\t7.975805371794872\n1916.079\t7.992632826923077\n1920.105\t8.009460282051283\n1924.1309999999999\t8.026287737179487\n1928.1570000000002\t8.043115192307692\n1932.183\t8.059942647435896\n1936.209\t8.076770102564103\n1940.2350000000001\t8.093597557692307\n1944.261\t8.110425012820514\n1948.287\t8.127252467948718\n1952.313\t8.144079923076923\n1956.339\t8.160907378205128\n1960.365\t8.177734833333334\n1964.391\t8.194562288461539\n1968.417\t8.211389743589743\n1972.443\t8.22821719871795\n1976.469\t8.245044653846154\n1980.495\t8.261872108974359\n1984.521\t8.278699564102563\n1988.547\t8.29552701923077\n1992.5729999999999\t8.312354474358974\n1996.5990000000002\t8.329181929487179\n2000.625\t8.346009384615385\n2004.6509999999998\t8.36283683974359\n2008.6770000000001\t8.379664294871795\n2012.703\t8.39649175\n2016.729\t8.413319205128206\n2020.755\t8.43014666025641\n2024.781\t8.446974115384617\n2028.807\t8.463801570512821\n2032.833\t8.480629025641026\n2036.859\t8.49745648076923\n2040.885\t8.514283935897435\n2044.911\t8.531111391025641\n2048.937\t8.547938846153846\n2052.9629999999997\t8.564766301282052\n2056.989\t8.581593756410257\n2061.015\t8.598421211538462\n2065.041\t8.615248666666666\n2069.067\t8.632076121794872\n2073.093\t8.648903576923077\n2077.119\t8.665731032051282\n2081.145\t8.682558487179488\n2085.1710000000003\t8.699385942307693\n2089.197\t8.716213397435897\n2093.223\t8.733040852564102\n2097.249\t8.749868307692308\n2101.275\t8.766695762820513\n2105.301\t8.783523217948717\n2109.327\t8.800350673076924\n2113.353\t8.817178128205128\n2117.379\t8.834005583333333\n2121.4049999999997\t8.850833038461538\n2125.431\t8.867660493589744\n2129.457\t8.884487948717949\n2133.483\t8.901315403846153\n2137.509\t8.91814285897436\n2141.535\t8.934970314102564\n2145.561\t8.951797769230769\n2149.587\t8.968625224358973\n2153.613\t8.98545267948718\n2157.639\t9.002280134615384\n2161.665\t9.01910758974359\n2165.691\t9.035935044871795\n2169.717\t9.0527625\n2173.743\t9.069589955128205\n2177.7690000000002\t9.08641741025641\n2181.795\t9.103244865384616\n2185.821\t9.12007232051282\n2189.8469999999998\t9.136899775641027\n2193.873\t9.153727230769231\n2197.899\t9.170554685897436\n2201.925\t9.18738214102564\n2205.951\t9.204209596153845\n2209.977\t9.221037051282051\n2214.003\t9.237864506410258\n2218.029\t9.254691961538462\n2222.055\t9.271519416666667\n2226.081\t9.288346871794872\n2230.107\t9.305174326923076\n2234.133\t9.32200178205128\n2238.159\t9.338829237179487\n2242.185\t9.355656692307694\n2246.2110000000002\t9.372484147435898\n2250.237\t9.389311602564103\n2254.263\t9.406139057692307\n2258.2889999999998\t9.422966512820512\n2262.315\t9.439793967948718\n2266.341\t9.456621423076923\n2270.367\t9.47344887820513\n2274.393\t9.490276333333334\n2278.419\t9.507103788461539\n2282.4449999999997\t9.523931243589743\n2286.471\t9.540758698717948\n2290.4970000000003\t9.557586153846154\n2294.523\t9.574413608974359\n2298.549\t9.591241064102565\n2302.575\t9.60806851923077\n2306.6009999999997\t9.624895974358974\n2310.627\t9.641723429487179\n2314.6530000000002\t9.658550884615384\n2318.679\t9.67537833974359\n2322.705\t9.692205794871795\n2326.7309999999998\t9.709033250000001\n2330.757\t9.725860705128206\n2334.783\t9.74268816025641\n2338.809\t9.759515615384615\n2342.835\t9.77634307051282\n2346.861\t9.793170525641026\n2350.8869999999997\t9.809997980769232\n2354.913\t9.826825435897437\n2358.9390000000003\t9.843652891025641\n2362.965\t9.860480346153846\n2366.991\t9.87730780128205\n2371.017\t9.894135256410257\n2375.0429999999997\t9.910962711538462\n2379.069\t9.927790166666668\n2383.0950000000003\t9.944617621794873\n2387.121\t9.961445076923077\n2391.147\t9.978272532051282\n2395.173\t9.995099987179486\n2399.199\t10.011927442307693\n2403.225\t10.028754897435897\n2407.251\t10.045582352564104\n2411.277\t10.062409807692308\n2415.303\t10.079237262820513\n2419.3289999999997\t10.096064717948718\n2423.355\t10.112892173076922\n2427.3810000000003\t10.129719628205129\n2431.407\t10.146547083333333\n2435.433\t10.16337453846154\n2439.459\t10.180201993589744\n2443.4849999999997\t10.197029448717949\n2447.511\t10.213856903846153\n2451.5370000000003\t10.230684358974358\n2455.563\t10.247511814102564\n2459.589\t10.264339269230769\n2463.615\t10.281166724358975\n2467.641\t10.29799417948718\n2471.667\t10.314821634615384\n2475.693\t10.331649089743589\n2479.719\t10.348476544871794\n2483.745\t10.365304\n"
    # assert: trapeze
    convolution_type = 3  # "trapeze"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: trapeze\ndestination_wavelength_nm\tdestination_width\tdestination_top\n1227.633\t5.115138\t2.557569\n1231.659\t5.1319654551282055\t2.5659827275641027\n1235.685\t5.14879291025641\t2.574396455128205\n1239.711\t5.1656203653846156\t2.5828101826923078\n1243.737\t5.18244782051282\t2.59122391025641\n1247.7630000000001\t5.199275275641026\t2.599637637820513\n1251.789\t5.216102730769231\t2.6080513653846156\n1255.815\t5.232930185897436\t2.616465092948718\n1259.8410000000001\t5.249757641025641\t2.6248788205128206\n1263.867\t5.266585096153846\t2.633292548076923\n1267.893\t5.283412551282051\t2.6417062756410257\n1271.919\t5.300240006410256\t2.650120003205128\n1275.945\t5.317067461538461\t2.6585337307692307\n1279.971\t5.333894916666667\t2.6669474583333335\n1283.997\t5.3507223717948715\t2.6753611858974358\n1288.0230000000001\t5.367549826923077\t2.6837749134615385\n1292.049\t5.384377282051282\t2.692188641025641\n1296.075\t5.401204737179487\t2.7006023685897436\n1300.101\t5.418032192307693\t2.7090160961538463\n1304.127\t5.434859647435897\t2.7174298237179486\n1308.153\t5.451687102564103\t2.7258435512820514\n1312.179\t5.468514557692307\t2.7342572788461537\n1316.205\t5.485342012820513\t2.7426710064102564\n1320.231\t5.502169467948718\t2.751084733974359\n1324.257\t5.518996923076923\t2.7594984615384615\n1328.2830000000001\t5.535824378205128\t2.767912189102564\n1332.309\t5.552651833333333\t2.7763259166666665\n1336.335\t5.5694792884615385\t2.7847396442307693\n1340.361\t5.586306743589743\t2.7931533717948716\n1344.387\t5.603134198717949\t2.8015670993589743\n1348.413\t5.619961653846154\t2.809980826923077\n1352.439\t5.636789108974359\t2.8183945544871793\n1356.4650000000001\t5.653616564102564\t2.826808282051282\n1360.491\t5.67044401923077\t2.835222009615385\n1364.517\t5.687271474358974\t2.843635737179487\n1368.5430000000001\t5.70409892948718\t2.85204946474359\n1372.569\t5.720926384615384\t2.860463192307692\n1376.595\t5.73775383974359\t2.868876919871795\n1380.621\t5.7545812948717945\t2.8772906474358972\n1384.647\t5.77140875\t2.885704375\n1388.673\t5.7882362051282055\t2.8941181025641027\n1392.699\t5.80506366025641\t2.902531830128205\n1396.725\t5.821891115384616\t2.910945557692308\n1400.751\t5.83871857051282\t2.91935928525641\n1404.777\t5.855546025641026\t2.927773012820513\n1408.803\t5.87237348076923\t2.936186740384615\n1412.829\t5.889200935897436\t2.944600467948718\n1416.855\t5.906028391025641\t2.9530141955128206\n1420.881\t5.922855846153846\t2.961427923076923\n1424.9070000000002\t5.939683301282051\t2.9698416506410257\n1428.933\t5.956510756410257\t2.9782553782051284\n1432.959\t5.9733382115384615\t2.9866691057692307\n1436.9850000000001\t5.990165666666667\t2.9950828333333335\n1441.011\t6.0069931217948715\t3.0034965608974358\n1445.037\t6.023820576923077\t3.0119102884615385\n1449.063\t6.040648032051282\t3.020324016025641\n1453.089\t6.057475487179487\t3.0287377435897436\n1457.115\t6.074302942307693\t3.0371514711538463\n1461.141\t6.091130397435897\t3.0455651987179486\n1465.167\t6.107957852564103\t3.0539789262820514\n1469.193\t6.124785307692308\t3.062392653846154\n1473.219\t6.141612762820513\t3.0708063814102564\n1477.2450000000001\t6.158440217948717\t3.0792201089743587\n1481.271\t6.175267673076923\t3.0876338365384615\n1485.297\t6.192095128205128\t3.096047564102564\n1489.323\t6.208922583333333\t3.1044612916666665\n1493.3490000000002\t6.2257500384615385\t3.1128750192307693\n1497.375\t6.242577493589744\t3.121288746794872\n1501.401\t6.259404948717949\t3.1297024743589743\n1505.4270000000001\t6.276232403846154\t3.138116201923077\n1509.453\t6.293059858974359\t3.1465299294871794\n1513.479\t6.309887314102564\t3.154943657051282\n1517.505\t6.326714769230769\t3.1633573846153844\n1521.531\t6.343542224358974\t3.171771112179487\n1525.557\t6.36036967948718\t3.18018483974359\n1529.583\t6.377197134615384\t3.188598567307692\n1533.609\t6.39402458974359\t3.197012294871795\n1537.635\t6.410852044871795\t3.2054260224358977\n1541.661\t6.4276795\t3.21383975\n1545.687\t6.444506955128205\t3.2222534775641023\n1549.713\t6.46133441025641\t3.230667205128205\n1553.739\t6.478161865384616\t3.239080932692308\n1557.765\t6.49498932051282\t3.24749466025641\n1561.791\t6.511816775641026\t3.255908387820513\n1565.817\t6.528644230769231\t3.2643221153846156\n1569.843\t6.545471685897436\t3.272735842948718\n1573.8690000000001\t6.562299141025641\t3.2811495705128206\n1577.895\t6.579126596153846\t3.289563298076923\n1581.921\t6.595954051282051\t3.2979770256410257\n1585.9470000000001\t6.612781506410256\t3.306390753205128\n1589.973\t6.6296089615384615\t3.3148044807692307\n1593.999\t6.646436416666667\t3.3232182083333335\n1598.025\t6.663263871794872\t3.331631935897436\n1602.051\t6.680091326923077\t3.3400456634615385\n1606.077\t6.6969187820512825\t3.3484593910256413\n1610.103\t6.713746237179487\t3.3568731185897436\n1614.129\t6.730573692307692\t3.365286846153846\n1618.155\t6.747401147435897\t3.3737005737179486\n1622.181\t6.764228602564103\t3.3821143012820514\n1626.2069999999999\t6.781056057692307\t3.3905280288461537\n1630.233\t6.797883512820513\t3.3989417564102564\n1634.259\t6.814710967948718\t3.407355483974359\n1638.285\t6.831538423076923\t3.4157692115384615\n1642.3110000000001\t6.848365878205128\t3.424182939102564\n1646.337\t6.865193333333333\t3.4325966666666665\n1650.363\t6.8820207884615385\t3.4410103942307693\n1654.3890000000001\t6.898848243589743\t3.4494241217948716\n1658.415\t6.915675698717949\t3.4578378493589743\n1662.441\t6.932503153846154\t3.466251576923077\n1666.467\t6.949330608974359\t3.4746653044871794\n1670.493\t6.966158064102564\t3.483079032051282\n1674.519\t6.98298551923077\t3.491492759615385\n1678.545\t6.999812974358974\t3.499906487179487\n1682.571\t7.01664042948718\t3.50832021474359\n1686.597\t7.033467884615384\t3.516733942307692\n1690.623\t7.05029533974359\t3.525147669871795\n1694.649\t7.0671227948717945\t3.5335613974358973\n1698.675\t7.08395025\t3.541975125\n1702.701\t7.1007777051282055\t3.5503888525641027\n1706.727\t7.11760516025641\t3.558802580128205\n1710.7530000000002\t7.134432615384616\t3.567216307692308\n1714.779\t7.151260070512821\t3.5756300352564105\n1718.805\t7.168087525641026\t3.584043762820513\n1722.8310000000001\t7.18491498076923\t3.592457490384615\n1726.857\t7.201742435897436\t3.600871217948718\n1730.883\t7.218569891025641\t3.6092849455128206\n1734.909\t7.235397346153846\t3.617698673076923\n1738.935\t7.252224801282051\t3.6261124006410257\n1742.961\t7.269052256410257\t3.6345261282051284\n1746.987\t7.2858797115384615\t3.6429398557692307\n1751.013\t7.302707166666666\t3.651353583333333\n1755.039\t7.3195346217948725\t3.6597673108974362\n1759.065\t7.336362076923077\t3.6681810384615385\n1763.091\t7.353189532051282\t3.676594766025641\n1767.117\t7.370016987179487\t3.6850084935897436\n1771.143\t7.386844442307693\t3.6934222211538463\n1775.1689999999999\t7.403671897435897\t3.7018359487179486\n1779.1950000000002\t7.420499352564103\t3.7102496762820514\n1783.221\t7.437326807692308\t3.718663403846154\n1787.2469999999998\t7.454154262820513\t3.7270771314102564\n1791.2730000000001\t7.4709817179487175\t3.7354908589743587\n1795.299\t7.487809173076923\t3.7439045865384615\n1799.325\t7.5046366282051284\t3.7523183141025642\n1803.351\t7.521464083333333\t3.7607320416666665\n1807.377\t7.5382915384615385\t3.7691457692307693\n1811.403\t7.555118993589744\t3.777559496794872\n1815.429\t7.571946448717949\t3.7859732243589743\n1819.455\t7.588773903846153\t3.7943869519230766\n1823.481\t7.60560135897436\t3.80280067948718\n1827.507\t7.622428814102564\t3.811214407051282\n1831.533\t7.639256269230769\t3.8196281346153844\n1835.559\t7.656083724358974\t3.828041862179487\n1839.585\t7.67291117948718\t3.83645558974359\n1843.6109999999999\t7.689738634615384\t3.844869317307692\n1847.6370000000002\t7.70656608974359\t3.853283044871795\n1851.663\t7.723393544871795\t3.8616967724358977\n1855.6889999999999\t7.740221\t3.8701105\n1859.7150000000001\t7.757048455128205\t3.8785242275641023\n1863.741\t7.77387591025641\t3.886937955128205\n1867.767\t7.790703365384616\t3.895351682692308\n1871.7930000000001\t7.80753082051282\t3.90376541025641\n1875.819\t7.824358275641026\t3.912179137820513\n1879.845\t7.841185730769231\t3.9205928653846156\n1883.871\t7.858013185897436\t3.929006592948718\n1887.897\t7.87484064102564\t3.93742032051282\n1891.923\t7.891668096153847\t3.9458340480769234\n1895.949\t7.908495551282051\t3.9542477756410257\n1899.975\t7.925323006410256\t3.962661503205128\n1904.001\t7.9421504615384615\t3.9710752307692307\n1908.027\t7.958977916666667\t3.9794889583333335\n1912.0529999999999\t7.975805371794872\t3.987902685897436\n1916.079\t7.992632826923077\t3.9963164134615385\n1920.105\t8.009460282051283\t4.004730141025641\n1924.1309999999999\t8.026287737179487\t4.013143868589744\n1928.1570000000002\t8.043115192307692\t4.021557596153846\n1932.183\t8.059942647435896\t4.029971323717948\n1936.209\t8.076770102564103\t4.038385051282051\n1940.2350000000001\t8.093597557692307\t4.046798778846154\n1944.261\t8.110425012820514\t4.055212506410257\n1948.287\t8.127252467948718\t4.063626233974359\n1952.313\t8.144079923076923\t4.0720399615384615\n1956.339\t8.160907378205128\t4.080453689102564\n1960.365\t8.177734833333334\t4.088867416666667\n1964.391\t8.194562288461539\t4.097281144230769\n1968.417\t8.211389743589743\t4.105694871794872\n1972.443\t8.22821719871795\t4.114108599358975\n1976.469\t8.245044653846154\t4.122522326923077\n1980.495\t8.261872108974359\t4.130936054487179\n1984.521\t8.278699564102563\t4.139349782051282\n1988.547\t8.29552701923077\t4.147763509615385\n1992.5729999999999\t8.312354474358974\t4.156177237179487\n1996.5990000000002\t8.329181929487179\t4.1645909647435895\n2000.625\t8.346009384615385\t4.173004692307693\n2004.6509999999998\t8.36283683974359\t4.181418419871795\n2008.6770000000001\t8.379664294871795\t4.189832147435897\n2012.703\t8.39649175\t4.198245875\n2016.729\t8.413319205128206\t4.206659602564103\n2020.755\t8.43014666025641\t4.215073330128205\n2024.781\t8.446974115384617\t4.223487057692308\n2028.807\t8.463801570512821\t4.231900785256411\n2032.833\t8.480629025641026\t4.240314512820513\n2036.859\t8.49745648076923\t4.248728240384615\n2040.885\t8.514283935897435\t4.2571419679487175\n2044.911\t8.531111391025641\t4.265555695512821\n2048.937\t8.547938846153846\t4.273969423076923\n2052.9629999999997\t8.564766301282052\t4.282383150641026\n2056.989\t8.581593756410257\t4.2907968782051285\n2061.015\t8.598421211538462\t4.299210605769231\n2065.041\t8.615248666666666\t4.307624333333333\n2069.067\t8.632076121794872\t4.316038060897436\n2073.093\t8.648903576923077\t4.3244517884615385\n2077.119\t8.665731032051282\t4.332865516025641\n2081.145\t8.682558487179488\t4.341279243589744\n2085.1710000000003\t8.699385942307693\t4.349692971153846\n2089.197\t8.716213397435897\t4.358106698717949\n2093.223\t8.733040852564102\t4.366520426282051\n2097.249\t8.749868307692308\t4.374934153846154\n2101.275\t8.766695762820513\t4.383347881410256\n2105.301\t8.783523217948717\t4.391761608974359\n2109.327\t8.800350673076924\t4.400175336538462\n2113.353\t8.817178128205128\t4.408589064102564\n2117.379\t8.834005583333333\t4.4170027916666665\n2121.4049999999997\t8.850833038461538\t4.425416519230769\n2125.431\t8.867660493589744\t4.433830246794872\n2129.457\t8.884487948717949\t4.442243974358974\n2133.483\t8.901315403846153\t4.450657701923077\n2137.509\t8.91814285897436\t4.45907142948718\n2141.535\t8.934970314102564\t4.467485157051282\n2145.561\t8.951797769230769\t4.475898884615384\n2149.587\t8.968625224358973\t4.484312612179487\n2153.613\t8.98545267948718\t4.49272633974359\n2157.639\t9.002280134615384\t4.501140067307692\n2161.665\t9.01910758974359\t4.509553794871795\n2165.691\t9.035935044871795\t4.517967522435898\n2169.717\t9.0527625\t4.52638125\n2173.743\t9.069589955128205\t4.534794977564102\n2177.7690000000002\t9.08641741025641\t4.543208705128205\n2181.795\t9.103244865384616\t4.551622432692308\n2185.821\t9.12007232051282\t4.56003616025641\n2189.8469999999998\t9.136899775641027\t4.568449887820513\n2193.873\t9.153727230769231\t4.576863615384616\n2197.899\t9.170554685897436\t4.585277342948718\n2201.925\t9.18738214102564\t4.59369107051282\n2205.951\t9.204209596153845\t4.6021047980769225\n2209.977\t9.221037051282051\t4.610518525641026\n2214.003\t9.237864506410258\t4.618932253205129\n2218.029\t9.254691961538462\t4.627345980769231\n2222.055\t9.271519416666667\t4.6357597083333335\n2226.081\t9.288346871794872\t4.644173435897436\n2230.107\t9.305174326923076\t4.652587163461538\n2234.133\t9.32200178205128\t4.66100089102564\n2238.159\t9.338829237179487\t4.669414618589744\n2242.185\t9.355656692307694\t4.677828346153847\n2246.2110000000002\t9.372484147435898\t4.686242073717949\n2250.237\t9.389311602564103\t4.694655801282051\n2254.263\t9.406139057692307\t4.703069528846154\n2258.2889999999998\t9.422966512820512\t4.711483256410256\n2262.315\t9.439793967948718\t4.719896983974359\n2266.341\t9.456621423076923\t4.7283107115384615\n2270.367\t9.47344887820513\t4.736724439102565\n2274.393\t9.490276333333334\t4.745138166666667\n2278.419\t9.507103788461539\t4.753551894230769\n2282.4449999999997\t9.523931243589743\t4.761965621794872\n2286.471\t9.540758698717948\t4.770379349358974\n2290.4970000000003\t9.557586153846154\t4.778793076923077\n2294.523\t9.574413608974359\t4.787206804487179\n2298.549\t9.591241064102565\t4.795620532051283\n2302.575\t9.60806851923077\t4.804034259615385\n2306.6009999999997\t9.624895974358974\t4.812447987179487\n2310.627\t9.641723429487179\t4.8208617147435895\n2314.6530000000002\t9.658550884615384\t4.829275442307692\n2318.679\t9.67537833974359\t4.837689169871795\n2322.705\t9.692205794871795\t4.846102897435897\n2326.7309999999998\t9.709033250000001\t4.8545166250000005\n2330.757\t9.725860705128206\t4.862930352564103\n2334.783\t9.74268816025641\t4.871344080128205\n2338.809\t9.759515615384615\t4.879757807692307\n2342.835\t9.77634307051282\t4.88817153525641\n2346.861\t9.793170525641026\t4.896585262820513\n2350.8869999999997\t9.809997980769232\t4.904998990384616\n2354.913\t9.826825435897437\t4.913412717948718\n2358.9390000000003\t9.843652891025641\t4.921826445512821\n2362.965\t9.860480346153846\t4.930240173076923\n2366.991\t9.87730780128205\t4.938653900641025\n2371.017\t9.894135256410257\t4.9470676282051285\n2375.0429999999997\t9.910962711538462\t4.955481355769231\n2379.069\t9.927790166666668\t4.963895083333334\n2383.0950000000003\t9.944617621794873\t4.972308810897436\n2387.121\t9.961445076923077\t4.980722538461539\n2391.147\t9.978272532051282\t4.989136266025641\n2395.173\t9.995099987179486\t4.997549993589743\n2399.199\t10.011927442307693\t5.005963721153846\n2403.225\t10.028754897435897\t5.014377448717949\n2407.251\t10.045582352564104\t5.022791176282052\n2411.277\t10.062409807692308\t5.031204903846154\n2415.303\t10.079237262820513\t5.0396186314102565\n2419.3289999999997\t10.096064717948718\t5.048032358974359\n2423.355\t10.112892173076922\t5.056446086538461\n2427.3810000000003\t10.129719628205129\t5.064859814102564\n2431.407\t10.146547083333333\t5.0732735416666666\n2435.433\t10.16337453846154\t5.08168726923077\n2439.459\t10.180201993589744\t5.090100996794872\n2443.4849999999997\t10.197029448717949\t5.098514724358974\n2447.511\t10.213856903846153\t5.106928451923077\n2451.5370000000003\t10.230684358974358\t5.115342179487179\n2455.563\t10.247511814102564\t5.123755907051282\n2459.589\t10.264339269230769\t5.1321696346153844\n2463.615\t10.281166724358975\t5.140583362179488\n2467.641\t10.29799417948718\t5.14899708974359\n2471.667\t10.314821634615384\t5.157410817307692\n2475.693\t10.331649089743589\t5.1658245448717945\n2479.719\t10.348476544871794\t5.174238272435897\n2483.745\t10.365304\t5.182652\n"
    # assert: Lorentz
    convolution_type = 4  # "Lorentz"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Lorentz function\ndestination_wavelength_nm\tdestination_width\n1227.633\t5.115138\n1231.659\t5.1319654551282055\n1235.685\t5.14879291025641\n1239.711\t5.1656203653846156\n1243.737\t5.18244782051282\n1247.7630000000001\t5.199275275641026\n1251.789\t5.216102730769231\n1255.815\t5.232930185897436\n1259.8410000000001\t5.249757641025641\n1263.867\t5.266585096153846\n1267.893\t5.283412551282051\n1271.919\t5.300240006410256\n1275.945\t5.317067461538461\n1279.971\t5.333894916666667\n1283.997\t5.3507223717948715\n1288.0230000000001\t5.367549826923077\n1292.049\t5.384377282051282\n1296.075\t5.401204737179487\n1300.101\t5.418032192307693\n1304.127\t5.434859647435897\n1308.153\t5.451687102564103\n1312.179\t5.468514557692307\n1316.205\t5.485342012820513\n1320.231\t5.502169467948718\n1324.257\t5.518996923076923\n1328.2830000000001\t5.535824378205128\n1332.309\t5.552651833333333\n1336.335\t5.5694792884615385\n1340.361\t5.586306743589743\n1344.387\t5.603134198717949\n1348.413\t5.619961653846154\n1352.439\t5.636789108974359\n1356.4650000000001\t5.653616564102564\n1360.491\t5.67044401923077\n1364.517\t5.687271474358974\n1368.5430000000001\t5.70409892948718\n1372.569\t5.720926384615384\n1376.595\t5.73775383974359\n1380.621\t5.7545812948717945\n1384.647\t5.77140875\n1388.673\t5.7882362051282055\n1392.699\t5.80506366025641\n1396.725\t5.821891115384616\n1400.751\t5.83871857051282\n1404.777\t5.855546025641026\n1408.803\t5.87237348076923\n1412.829\t5.889200935897436\n1416.855\t5.906028391025641\n1420.881\t5.922855846153846\n1424.9070000000002\t5.939683301282051\n1428.933\t5.956510756410257\n1432.959\t5.9733382115384615\n1436.9850000000001\t5.990165666666667\n1441.011\t6.0069931217948715\n1445.037\t6.023820576923077\n1449.063\t6.040648032051282\n1453.089\t6.057475487179487\n1457.115\t6.074302942307693\n1461.141\t6.091130397435897\n1465.167\t6.107957852564103\n1469.193\t6.124785307692308\n1473.219\t6.141612762820513\n1477.2450000000001\t6.158440217948717\n1481.271\t6.175267673076923\n1485.297\t6.192095128205128\n1489.323\t6.208922583333333\n1493.3490000000002\t6.2257500384615385\n1497.375\t6.242577493589744\n1501.401\t6.259404948717949\n1505.4270000000001\t6.276232403846154\n1509.453\t6.293059858974359\n1513.479\t6.309887314102564\n1517.505\t6.326714769230769\n1521.531\t6.343542224358974\n1525.557\t6.36036967948718\n1529.583\t6.377197134615384\n1533.609\t6.39402458974359\n1537.635\t6.410852044871795\n1541.661\t6.4276795\n1545.687\t6.444506955128205\n1549.713\t6.46133441025641\n1553.739\t6.478161865384616\n1557.765\t6.49498932051282\n1561.791\t6.511816775641026\n1565.817\t6.528644230769231\n1569.843\t6.545471685897436\n1573.8690000000001\t6.562299141025641\n1577.895\t6.579126596153846\n1581.921\t6.595954051282051\n1585.9470000000001\t6.612781506410256\n1589.973\t6.6296089615384615\n1593.999\t6.646436416666667\n1598.025\t6.663263871794872\n1602.051\t6.680091326923077\n1606.077\t6.6969187820512825\n1610.103\t6.713746237179487\n1614.129\t6.730573692307692\n1618.155\t6.747401147435897\n1622.181\t6.764228602564103\n1626.2069999999999\t6.781056057692307\n1630.233\t6.797883512820513\n1634.259\t6.814710967948718\n1638.285\t6.831538423076923\n1642.3110000000001\t6.848365878205128\n1646.337\t6.865193333333333\n1650.363\t6.8820207884615385\n1654.3890000000001\t6.898848243589743\n1658.415\t6.915675698717949\n1662.441\t6.932503153846154\n1666.467\t6.949330608974359\n1670.493\t6.966158064102564\n1674.519\t6.98298551923077\n1678.545\t6.999812974358974\n1682.571\t7.01664042948718\n1686.597\t7.033467884615384\n1690.623\t7.05029533974359\n1694.649\t7.0671227948717945\n1698.675\t7.08395025\n1702.701\t7.1007777051282055\n1706.727\t7.11760516025641\n1710.7530000000002\t7.134432615384616\n1714.779\t7.151260070512821\n1718.805\t7.168087525641026\n1722.8310000000001\t7.18491498076923\n1726.857\t7.201742435897436\n1730.883\t7.218569891025641\n1734.909\t7.235397346153846\n1738.935\t7.252224801282051\n1742.961\t7.269052256410257\n1746.987\t7.2858797115384615\n1751.013\t7.302707166666666\n1755.039\t7.3195346217948725\n1759.065\t7.336362076923077\n1763.091\t7.353189532051282\n1767.117\t7.370016987179487\n1771.143\t7.386844442307693\n1775.1689999999999\t7.403671897435897\n1779.1950000000002\t7.420499352564103\n1783.221\t7.437326807692308\n1787.2469999999998\t7.454154262820513\n1791.2730000000001\t7.4709817179487175\n1795.299\t7.487809173076923\n1799.325\t7.5046366282051284\n1803.351\t7.521464083333333\n1807.377\t7.5382915384615385\n1811.403\t7.555118993589744\n1815.429\t7.571946448717949\n1819.455\t7.588773903846153\n1823.481\t7.60560135897436\n1827.507\t7.622428814102564\n1831.533\t7.639256269230769\n1835.559\t7.656083724358974\n1839.585\t7.67291117948718\n1843.6109999999999\t7.689738634615384\n1847.6370000000002\t7.70656608974359\n1851.663\t7.723393544871795\n1855.6889999999999\t7.740221\n1859.7150000000001\t7.757048455128205\n1863.741\t7.77387591025641\n1867.767\t7.790703365384616\n1871.7930000000001\t7.80753082051282\n1875.819\t7.824358275641026\n1879.845\t7.841185730769231\n1883.871\t7.858013185897436\n1887.897\t7.87484064102564\n1891.923\t7.891668096153847\n1895.949\t7.908495551282051\n1899.975\t7.925323006410256\n1904.001\t7.9421504615384615\n1908.027\t7.958977916666667\n1912.0529999999999\t7.975805371794872\n1916.079\t7.992632826923077\n1920.105\t8.009460282051283\n1924.1309999999999\t8.026287737179487\n1928.1570000000002\t8.043115192307692\n1932.183\t8.059942647435896\n1936.209\t8.076770102564103\n1940.2350000000001\t8.093597557692307\n1944.261\t8.110425012820514\n1948.287\t8.127252467948718\n1952.313\t8.144079923076923\n1956.339\t8.160907378205128\n1960.365\t8.177734833333334\n1964.391\t8.194562288461539\n1968.417\t8.211389743589743\n1972.443\t8.22821719871795\n1976.469\t8.245044653846154\n1980.495\t8.261872108974359\n1984.521\t8.278699564102563\n1988.547\t8.29552701923077\n1992.5729999999999\t8.312354474358974\n1996.5990000000002\t8.329181929487179\n2000.625\t8.346009384615385\n2004.6509999999998\t8.36283683974359\n2008.6770000000001\t8.379664294871795\n2012.703\t8.39649175\n2016.729\t8.413319205128206\n2020.755\t8.43014666025641\n2024.781\t8.446974115384617\n2028.807\t8.463801570512821\n2032.833\t8.480629025641026\n2036.859\t8.49745648076923\n2040.885\t8.514283935897435\n2044.911\t8.531111391025641\n2048.937\t8.547938846153846\n2052.9629999999997\t8.564766301282052\n2056.989\t8.581593756410257\n2061.015\t8.598421211538462\n2065.041\t8.615248666666666\n2069.067\t8.632076121794872\n2073.093\t8.648903576923077\n2077.119\t8.665731032051282\n2081.145\t8.682558487179488\n2085.1710000000003\t8.699385942307693\n2089.197\t8.716213397435897\n2093.223\t8.733040852564102\n2097.249\t8.749868307692308\n2101.275\t8.766695762820513\n2105.301\t8.783523217948717\n2109.327\t8.800350673076924\n2113.353\t8.817178128205128\n2117.379\t8.834005583333333\n2121.4049999999997\t8.850833038461538\n2125.431\t8.867660493589744\n2129.457\t8.884487948717949\n2133.483\t8.901315403846153\n2137.509\t8.91814285897436\n2141.535\t8.934970314102564\n2145.561\t8.951797769230769\n2149.587\t8.968625224358973\n2153.613\t8.98545267948718\n2157.639\t9.002280134615384\n2161.665\t9.01910758974359\n2165.691\t9.035935044871795\n2169.717\t9.0527625\n2173.743\t9.069589955128205\n2177.7690000000002\t9.08641741025641\n2181.795\t9.103244865384616\n2185.821\t9.12007232051282\n2189.8469999999998\t9.136899775641027\n2193.873\t9.153727230769231\n2197.899\t9.170554685897436\n2201.925\t9.18738214102564\n2205.951\t9.204209596153845\n2209.977\t9.221037051282051\n2214.003\t9.237864506410258\n2218.029\t9.254691961538462\n2222.055\t9.271519416666667\n2226.081\t9.288346871794872\n2230.107\t9.305174326923076\n2234.133\t9.32200178205128\n2238.159\t9.338829237179487\n2242.185\t9.355656692307694\n2246.2110000000002\t9.372484147435898\n2250.237\t9.389311602564103\n2254.263\t9.406139057692307\n2258.2889999999998\t9.422966512820512\n2262.315\t9.439793967948718\n2266.341\t9.456621423076923\n2270.367\t9.47344887820513\n2274.393\t9.490276333333334\n2278.419\t9.507103788461539\n2282.4449999999997\t9.523931243589743\n2286.471\t9.540758698717948\n2290.4970000000003\t9.557586153846154\n2294.523\t9.574413608974359\n2298.549\t9.591241064102565\n2302.575\t9.60806851923077\n2306.6009999999997\t9.624895974358974\n2310.627\t9.641723429487179\n2314.6530000000002\t9.658550884615384\n2318.679\t9.67537833974359\n2322.705\t9.692205794871795\n2326.7309999999998\t9.709033250000001\n2330.757\t9.725860705128206\n2334.783\t9.74268816025641\n2338.809\t9.759515615384615\n2342.835\t9.77634307051282\n2346.861\t9.793170525641026\n2350.8869999999997\t9.809997980769232\n2354.913\t9.826825435897437\n2358.9390000000003\t9.843652891025641\n2362.965\t9.860480346153846\n2366.991\t9.87730780128205\n2371.017\t9.894135256410257\n2375.0429999999997\t9.910962711538462\n2379.069\t9.927790166666668\n2383.0950000000003\t9.944617621794873\n2387.121\t9.961445076923077\n2391.147\t9.978272532051282\n2395.173\t9.995099987179486\n2399.199\t10.011927442307693\n2403.225\t10.028754897435897\n2407.251\t10.045582352564104\n2411.277\t10.062409807692308\n2415.303\t10.079237262820513\n2419.3289999999997\t10.096064717948718\n2423.355\t10.112892173076922\n2427.3810000000003\t10.129719628205129\n2431.407\t10.146547083333333\n2435.433\t10.16337453846154\n2439.459\t10.180201993589744\n2443.4849999999997\t10.197029448717949\n2447.511\t10.213856903846153\n2451.5370000000003\t10.230684358974358\n2455.563\t10.247511814102564\n2459.589\t10.264339269230769\n2463.615\t10.281166724358975\n2467.641\t10.29799417948718\n2471.667\t10.314821634615384\n2475.693\t10.331649089743589\n2479.719\t10.348476544871794\n2483.745\t10.365304\n"
    # assert: Voigt
    convolution_type = 5  # "Voigt"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Voigt profile\ndestination_wavelength_nm\tdestination_width_Gauss\tdestination_width_Lorentz\n1227.633\t5.115138\t2.557569\n1231.659\t5.1319654551282055\t2.5659827275641027\n1235.685\t5.14879291025641\t2.574396455128205\n1239.711\t5.1656203653846156\t2.5828101826923078\n1243.737\t5.18244782051282\t2.59122391025641\n1247.7630000000001\t5.199275275641026\t2.599637637820513\n1251.789\t5.216102730769231\t2.6080513653846156\n1255.815\t5.232930185897436\t2.616465092948718\n1259.8410000000001\t5.249757641025641\t2.6248788205128206\n1263.867\t5.266585096153846\t2.633292548076923\n1267.893\t5.283412551282051\t2.6417062756410257\n1271.919\t5.300240006410256\t2.650120003205128\n1275.945\t5.317067461538461\t2.6585337307692307\n1279.971\t5.333894916666667\t2.6669474583333335\n1283.997\t5.3507223717948715\t2.6753611858974358\n1288.0230000000001\t5.367549826923077\t2.6837749134615385\n1292.049\t5.384377282051282\t2.692188641025641\n1296.075\t5.401204737179487\t2.7006023685897436\n1300.101\t5.418032192307693\t2.7090160961538463\n1304.127\t5.434859647435897\t2.7174298237179486\n1308.153\t5.451687102564103\t2.7258435512820514\n1312.179\t5.468514557692307\t2.7342572788461537\n1316.205\t5.485342012820513\t2.7426710064102564\n1320.231\t5.502169467948718\t2.751084733974359\n1324.257\t5.518996923076923\t2.7594984615384615\n1328.2830000000001\t5.535824378205128\t2.767912189102564\n1332.309\t5.552651833333333\t2.7763259166666665\n1336.335\t5.5694792884615385\t2.7847396442307693\n1340.361\t5.586306743589743\t2.7931533717948716\n1344.387\t5.603134198717949\t2.8015670993589743\n1348.413\t5.619961653846154\t2.809980826923077\n1352.439\t5.636789108974359\t2.8183945544871793\n1356.4650000000001\t5.653616564102564\t2.826808282051282\n1360.491\t5.67044401923077\t2.835222009615385\n1364.517\t5.687271474358974\t2.843635737179487\n1368.5430000000001\t5.70409892948718\t2.85204946474359\n1372.569\t5.720926384615384\t2.860463192307692\n1376.595\t5.73775383974359\t2.868876919871795\n1380.621\t5.7545812948717945\t2.8772906474358972\n1384.647\t5.77140875\t2.885704375\n1388.673\t5.7882362051282055\t2.8941181025641027\n1392.699\t5.80506366025641\t2.902531830128205\n1396.725\t5.821891115384616\t2.910945557692308\n1400.751\t5.83871857051282\t2.91935928525641\n1404.777\t5.855546025641026\t2.927773012820513\n1408.803\t5.87237348076923\t2.936186740384615\n1412.829\t5.889200935897436\t2.944600467948718\n1416.855\t5.906028391025641\t2.9530141955128206\n1420.881\t5.922855846153846\t2.961427923076923\n1424.9070000000002\t5.939683301282051\t2.9698416506410257\n1428.933\t5.956510756410257\t2.9782553782051284\n1432.959\t5.9733382115384615\t2.9866691057692307\n1436.9850000000001\t5.990165666666667\t2.9950828333333335\n1441.011\t6.0069931217948715\t3.0034965608974358\n1445.037\t6.023820576923077\t3.0119102884615385\n1449.063\t6.040648032051282\t3.020324016025641\n1453.089\t6.057475487179487\t3.0287377435897436\n1457.115\t6.074302942307693\t3.0371514711538463\n1461.141\t6.091130397435897\t3.0455651987179486\n1465.167\t6.107957852564103\t3.0539789262820514\n1469.193\t6.124785307692308\t3.062392653846154\n1473.219\t6.141612762820513\t3.0708063814102564\n1477.2450000000001\t6.158440217948717\t3.0792201089743587\n1481.271\t6.175267673076923\t3.0876338365384615\n1485.297\t6.192095128205128\t3.096047564102564\n1489.323\t6.208922583333333\t3.1044612916666665\n1493.3490000000002\t6.2257500384615385\t3.1128750192307693\n1497.375\t6.242577493589744\t3.121288746794872\n1501.401\t6.259404948717949\t3.1297024743589743\n1505.4270000000001\t6.276232403846154\t3.138116201923077\n1509.453\t6.293059858974359\t3.1465299294871794\n1513.479\t6.309887314102564\t3.154943657051282\n1517.505\t6.326714769230769\t3.1633573846153844\n1521.531\t6.343542224358974\t3.171771112179487\n1525.557\t6.36036967948718\t3.18018483974359\n1529.583\t6.377197134615384\t3.188598567307692\n1533.609\t6.39402458974359\t3.197012294871795\n1537.635\t6.410852044871795\t3.2054260224358977\n1541.661\t6.4276795\t3.21383975\n1545.687\t6.444506955128205\t3.2222534775641023\n1549.713\t6.46133441025641\t3.230667205128205\n1553.739\t6.478161865384616\t3.239080932692308\n1557.765\t6.49498932051282\t3.24749466025641\n1561.791\t6.511816775641026\t3.255908387820513\n1565.817\t6.528644230769231\t3.2643221153846156\n1569.843\t6.545471685897436\t3.272735842948718\n1573.8690000000001\t6.562299141025641\t3.2811495705128206\n1577.895\t6.579126596153846\t3.289563298076923\n1581.921\t6.595954051282051\t3.2979770256410257\n1585.9470000000001\t6.612781506410256\t3.306390753205128\n1589.973\t6.6296089615384615\t3.3148044807692307\n1593.999\t6.646436416666667\t3.3232182083333335\n1598.025\t6.663263871794872\t3.331631935897436\n1602.051\t6.680091326923077\t3.3400456634615385\n1606.077\t6.6969187820512825\t3.3484593910256413\n1610.103\t6.713746237179487\t3.3568731185897436\n1614.129\t6.730573692307692\t3.365286846153846\n1618.155\t6.747401147435897\t3.3737005737179486\n1622.181\t6.764228602564103\t3.3821143012820514\n1626.2069999999999\t6.781056057692307\t3.3905280288461537\n1630.233\t6.797883512820513\t3.3989417564102564\n1634.259\t6.814710967948718\t3.407355483974359\n1638.285\t6.831538423076923\t3.4157692115384615\n1642.3110000000001\t6.848365878205128\t3.424182939102564\n1646.337\t6.865193333333333\t3.4325966666666665\n1650.363\t6.8820207884615385\t3.4410103942307693\n1654.3890000000001\t6.898848243589743\t3.4494241217948716\n1658.415\t6.915675698717949\t3.4578378493589743\n1662.441\t6.932503153846154\t3.466251576923077\n1666.467\t6.949330608974359\t3.4746653044871794\n1670.493\t6.966158064102564\t3.483079032051282\n1674.519\t6.98298551923077\t3.491492759615385\n1678.545\t6.999812974358974\t3.499906487179487\n1682.571\t7.01664042948718\t3.50832021474359\n1686.597\t7.033467884615384\t3.516733942307692\n1690.623\t7.05029533974359\t3.525147669871795\n1694.649\t7.0671227948717945\t3.5335613974358973\n1698.675\t7.08395025\t3.541975125\n1702.701\t7.1007777051282055\t3.5503888525641027\n1706.727\t7.11760516025641\t3.558802580128205\n1710.7530000000002\t7.134432615384616\t3.567216307692308\n1714.779\t7.151260070512821\t3.5756300352564105\n1718.805\t7.168087525641026\t3.584043762820513\n1722.8310000000001\t7.18491498076923\t3.592457490384615\n1726.857\t7.201742435897436\t3.600871217948718\n1730.883\t7.218569891025641\t3.6092849455128206\n1734.909\t7.235397346153846\t3.617698673076923\n1738.935\t7.252224801282051\t3.6261124006410257\n1742.961\t7.269052256410257\t3.6345261282051284\n1746.987\t7.2858797115384615\t3.6429398557692307\n1751.013\t7.302707166666666\t3.651353583333333\n1755.039\t7.3195346217948725\t3.6597673108974362\n1759.065\t7.336362076923077\t3.6681810384615385\n1763.091\t7.353189532051282\t3.676594766025641\n1767.117\t7.370016987179487\t3.6850084935897436\n1771.143\t7.386844442307693\t3.6934222211538463\n1775.1689999999999\t7.403671897435897\t3.7018359487179486\n1779.1950000000002\t7.420499352564103\t3.7102496762820514\n1783.221\t7.437326807692308\t3.718663403846154\n1787.2469999999998\t7.454154262820513\t3.7270771314102564\n1791.2730000000001\t7.4709817179487175\t3.7354908589743587\n1795.299\t7.487809173076923\t3.7439045865384615\n1799.325\t7.5046366282051284\t3.7523183141025642\n1803.351\t7.521464083333333\t3.7607320416666665\n1807.377\t7.5382915384615385\t3.7691457692307693\n1811.403\t7.555118993589744\t3.777559496794872\n1815.429\t7.571946448717949\t3.7859732243589743\n1819.455\t7.588773903846153\t3.7943869519230766\n1823.481\t7.60560135897436\t3.80280067948718\n1827.507\t7.622428814102564\t3.811214407051282\n1831.533\t7.639256269230769\t3.8196281346153844\n1835.559\t7.656083724358974\t3.828041862179487\n1839.585\t7.67291117948718\t3.83645558974359\n1843.6109999999999\t7.689738634615384\t3.844869317307692\n1847.6370000000002\t7.70656608974359\t3.853283044871795\n1851.663\t7.723393544871795\t3.8616967724358977\n1855.6889999999999\t7.740221\t3.8701105\n1859.7150000000001\t7.757048455128205\t3.8785242275641023\n1863.741\t7.77387591025641\t3.886937955128205\n1867.767\t7.790703365384616\t3.895351682692308\n1871.7930000000001\t7.80753082051282\t3.90376541025641\n1875.819\t7.824358275641026\t3.912179137820513\n1879.845\t7.841185730769231\t3.9205928653846156\n1883.871\t7.858013185897436\t3.929006592948718\n1887.897\t7.87484064102564\t3.93742032051282\n1891.923\t7.891668096153847\t3.9458340480769234\n1895.949\t7.908495551282051\t3.9542477756410257\n1899.975\t7.925323006410256\t3.962661503205128\n1904.001\t7.9421504615384615\t3.9710752307692307\n1908.027\t7.958977916666667\t3.9794889583333335\n1912.0529999999999\t7.975805371794872\t3.987902685897436\n1916.079\t7.992632826923077\t3.9963164134615385\n1920.105\t8.009460282051283\t4.004730141025641\n1924.1309999999999\t8.026287737179487\t4.013143868589744\n1928.1570000000002\t8.043115192307692\t4.021557596153846\n1932.183\t8.059942647435896\t4.029971323717948\n1936.209\t8.076770102564103\t4.038385051282051\n1940.2350000000001\t8.093597557692307\t4.046798778846154\n1944.261\t8.110425012820514\t4.055212506410257\n1948.287\t8.127252467948718\t4.063626233974359\n1952.313\t8.144079923076923\t4.0720399615384615\n1956.339\t8.160907378205128\t4.080453689102564\n1960.365\t8.177734833333334\t4.088867416666667\n1964.391\t8.194562288461539\t4.097281144230769\n1968.417\t8.211389743589743\t4.105694871794872\n1972.443\t8.22821719871795\t4.114108599358975\n1976.469\t8.245044653846154\t4.122522326923077\n1980.495\t8.261872108974359\t4.130936054487179\n1984.521\t8.278699564102563\t4.139349782051282\n1988.547\t8.29552701923077\t4.147763509615385\n1992.5729999999999\t8.312354474358974\t4.156177237179487\n1996.5990000000002\t8.329181929487179\t4.1645909647435895\n2000.625\t8.346009384615385\t4.173004692307693\n2004.6509999999998\t8.36283683974359\t4.181418419871795\n2008.6770000000001\t8.379664294871795\t4.189832147435897\n2012.703\t8.39649175\t4.198245875\n2016.729\t8.413319205128206\t4.206659602564103\n2020.755\t8.43014666025641\t4.215073330128205\n2024.781\t8.446974115384617\t4.223487057692308\n2028.807\t8.463801570512821\t4.231900785256411\n2032.833\t8.480629025641026\t4.240314512820513\n2036.859\t8.49745648076923\t4.248728240384615\n2040.885\t8.514283935897435\t4.2571419679487175\n2044.911\t8.531111391025641\t4.265555695512821\n2048.937\t8.547938846153846\t4.273969423076923\n2052.9629999999997\t8.564766301282052\t4.282383150641026\n2056.989\t8.581593756410257\t4.2907968782051285\n2061.015\t8.598421211538462\t4.299210605769231\n2065.041\t8.615248666666666\t4.307624333333333\n2069.067\t8.632076121794872\t4.316038060897436\n2073.093\t8.648903576923077\t4.3244517884615385\n2077.119\t8.665731032051282\t4.332865516025641\n2081.145\t8.682558487179488\t4.341279243589744\n2085.1710000000003\t8.699385942307693\t4.349692971153846\n2089.197\t8.716213397435897\t4.358106698717949\n2093.223\t8.733040852564102\t4.366520426282051\n2097.249\t8.749868307692308\t4.374934153846154\n2101.275\t8.766695762820513\t4.383347881410256\n2105.301\t8.783523217948717\t4.391761608974359\n2109.327\t8.800350673076924\t4.400175336538462\n2113.353\t8.817178128205128\t4.408589064102564\n2117.379\t8.834005583333333\t4.4170027916666665\n2121.4049999999997\t8.850833038461538\t4.425416519230769\n2125.431\t8.867660493589744\t4.433830246794872\n2129.457\t8.884487948717949\t4.442243974358974\n2133.483\t8.901315403846153\t4.450657701923077\n2137.509\t8.91814285897436\t4.45907142948718\n2141.535\t8.934970314102564\t4.467485157051282\n2145.561\t8.951797769230769\t4.475898884615384\n2149.587\t8.968625224358973\t4.484312612179487\n2153.613\t8.98545267948718\t4.49272633974359\n2157.639\t9.002280134615384\t4.501140067307692\n2161.665\t9.01910758974359\t4.509553794871795\n2165.691\t9.035935044871795\t4.517967522435898\n2169.717\t9.0527625\t4.52638125\n2173.743\t9.069589955128205\t4.534794977564102\n2177.7690000000002\t9.08641741025641\t4.543208705128205\n2181.795\t9.103244865384616\t4.551622432692308\n2185.821\t9.12007232051282\t4.56003616025641\n2189.8469999999998\t9.136899775641027\t4.568449887820513\n2193.873\t9.153727230769231\t4.576863615384616\n2197.899\t9.170554685897436\t4.585277342948718\n2201.925\t9.18738214102564\t4.59369107051282\n2205.951\t9.204209596153845\t4.6021047980769225\n2209.977\t9.221037051282051\t4.610518525641026\n2214.003\t9.237864506410258\t4.618932253205129\n2218.029\t9.254691961538462\t4.627345980769231\n2222.055\t9.271519416666667\t4.6357597083333335\n2226.081\t9.288346871794872\t4.644173435897436\n2230.107\t9.305174326923076\t4.652587163461538\n2234.133\t9.32200178205128\t4.66100089102564\n2238.159\t9.338829237179487\t4.669414618589744\n2242.185\t9.355656692307694\t4.677828346153847\n2246.2110000000002\t9.372484147435898\t4.686242073717949\n2250.237\t9.389311602564103\t4.694655801282051\n2254.263\t9.406139057692307\t4.703069528846154\n2258.2889999999998\t9.422966512820512\t4.711483256410256\n2262.315\t9.439793967948718\t4.719896983974359\n2266.341\t9.456621423076923\t4.7283107115384615\n2270.367\t9.47344887820513\t4.736724439102565\n2274.393\t9.490276333333334\t4.745138166666667\n2278.419\t9.507103788461539\t4.753551894230769\n2282.4449999999997\t9.523931243589743\t4.761965621794872\n2286.471\t9.540758698717948\t4.770379349358974\n2290.4970000000003\t9.557586153846154\t4.778793076923077\n2294.523\t9.574413608974359\t4.787206804487179\n2298.549\t9.591241064102565\t4.795620532051283\n2302.575\t9.60806851923077\t4.804034259615385\n2306.6009999999997\t9.624895974358974\t4.812447987179487\n2310.627\t9.641723429487179\t4.8208617147435895\n2314.6530000000002\t9.658550884615384\t4.829275442307692\n2318.679\t9.67537833974359\t4.837689169871795\n2322.705\t9.692205794871795\t4.846102897435897\n2326.7309999999998\t9.709033250000001\t4.8545166250000005\n2330.757\t9.725860705128206\t4.862930352564103\n2334.783\t9.74268816025641\t4.871344080128205\n2338.809\t9.759515615384615\t4.879757807692307\n2342.835\t9.77634307051282\t4.88817153525641\n2346.861\t9.793170525641026\t4.896585262820513\n2350.8869999999997\t9.809997980769232\t4.904998990384616\n2354.913\t9.826825435897437\t4.913412717948718\n2358.9390000000003\t9.843652891025641\t4.921826445512821\n2362.965\t9.860480346153846\t4.930240173076923\n2366.991\t9.87730780128205\t4.938653900641025\n2371.017\t9.894135256410257\t4.9470676282051285\n2375.0429999999997\t9.910962711538462\t4.955481355769231\n2379.069\t9.927790166666668\t4.963895083333334\n2383.0950000000003\t9.944617621794873\t4.972308810897436\n2387.121\t9.961445076923077\t4.980722538461539\n2391.147\t9.978272532051282\t4.989136266025641\n2395.173\t9.995099987179486\t4.997549993589743\n2399.199\t10.011927442307693\t5.005963721153846\n2403.225\t10.028754897435897\t5.014377448717949\n2407.251\t10.045582352564104\t5.022791176282052\n2411.277\t10.062409807692308\t5.031204903846154\n2415.303\t10.079237262820513\t5.0396186314102565\n2419.3289999999997\t10.096064717948718\t5.048032358974359\n2423.355\t10.112892173076922\t5.056446086538461\n2427.3810000000003\t10.129719628205129\t5.064859814102564\n2431.407\t10.146547083333333\t5.0732735416666666\n2435.433\t10.16337453846154\t5.08168726923077\n2439.459\t10.180201993589744\t5.090100996794872\n2443.4849999999997\t10.197029448717949\t5.098514724358974\n2447.511\t10.213856903846153\t5.106928451923077\n2451.5370000000003\t10.230684358974358\t5.115342179487179\n2455.563\t10.247511814102564\t5.123755907051282\n2459.589\t10.264339269230769\t5.1321696346153844\n2463.615\t10.281166724358975\t5.140583362179488\n2467.641\t10.29799417948718\t5.14899708974359\n2471.667\t10.314821634615384\t5.157410817307692\n2475.693\t10.331649089743589\t5.1658245448717945\n2479.719\t10.348476544871794\t5.174238272435897\n2483.745\t10.365304\t5.182652\n"
    # assert: Gauss + Lorentz
    convolution_type = 6  # "Gauss + Lorentz"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Gauss & Lorentz sum, Gauss function part: 0.5\ndestination_wavelength_nm\tdestination_width_Gauss\tdestination_width_Lorentz\n1227.633\t5.115138\t2.557569\n1231.659\t5.1319654551282055\t2.5659827275641027\n1235.685\t5.14879291025641\t2.574396455128205\n1239.711\t5.1656203653846156\t2.5828101826923078\n1243.737\t5.18244782051282\t2.59122391025641\n1247.7630000000001\t5.199275275641026\t2.599637637820513\n1251.789\t5.216102730769231\t2.6080513653846156\n1255.815\t5.232930185897436\t2.616465092948718\n1259.8410000000001\t5.249757641025641\t2.6248788205128206\n1263.867\t5.266585096153846\t2.633292548076923\n1267.893\t5.283412551282051\t2.6417062756410257\n1271.919\t5.300240006410256\t2.650120003205128\n1275.945\t5.317067461538461\t2.6585337307692307\n1279.971\t5.333894916666667\t2.6669474583333335\n1283.997\t5.3507223717948715\t2.6753611858974358\n1288.0230000000001\t5.367549826923077\t2.6837749134615385\n1292.049\t5.384377282051282\t2.692188641025641\n1296.075\t5.401204737179487\t2.7006023685897436\n1300.101\t5.418032192307693\t2.7090160961538463\n1304.127\t5.434859647435897\t2.7174298237179486\n1308.153\t5.451687102564103\t2.7258435512820514\n1312.179\t5.468514557692307\t2.7342572788461537\n1316.205\t5.485342012820513\t2.7426710064102564\n1320.231\t5.502169467948718\t2.751084733974359\n1324.257\t5.518996923076923\t2.7594984615384615\n1328.2830000000001\t5.535824378205128\t2.767912189102564\n1332.309\t5.552651833333333\t2.7763259166666665\n1336.335\t5.5694792884615385\t2.7847396442307693\n1340.361\t5.586306743589743\t2.7931533717948716\n1344.387\t5.603134198717949\t2.8015670993589743\n1348.413\t5.619961653846154\t2.809980826923077\n1352.439\t5.636789108974359\t2.8183945544871793\n1356.4650000000001\t5.653616564102564\t2.826808282051282\n1360.491\t5.67044401923077\t2.835222009615385\n1364.517\t5.687271474358974\t2.843635737179487\n1368.5430000000001\t5.70409892948718\t2.85204946474359\n1372.569\t5.720926384615384\t2.860463192307692\n1376.595\t5.73775383974359\t2.868876919871795\n1380.621\t5.7545812948717945\t2.8772906474358972\n1384.647\t5.77140875\t2.885704375\n1388.673\t5.7882362051282055\t2.8941181025641027\n1392.699\t5.80506366025641\t2.902531830128205\n1396.725\t5.821891115384616\t2.910945557692308\n1400.751\t5.83871857051282\t2.91935928525641\n1404.777\t5.855546025641026\t2.927773012820513\n1408.803\t5.87237348076923\t2.936186740384615\n1412.829\t5.889200935897436\t2.944600467948718\n1416.855\t5.906028391025641\t2.9530141955128206\n1420.881\t5.922855846153846\t2.961427923076923\n1424.9070000000002\t5.939683301282051\t2.9698416506410257\n1428.933\t5.956510756410257\t2.9782553782051284\n1432.959\t5.9733382115384615\t2.9866691057692307\n1436.9850000000001\t5.990165666666667\t2.9950828333333335\n1441.011\t6.0069931217948715\t3.0034965608974358\n1445.037\t6.023820576923077\t3.0119102884615385\n1449.063\t6.040648032051282\t3.020324016025641\n1453.089\t6.057475487179487\t3.0287377435897436\n1457.115\t6.074302942307693\t3.0371514711538463\n1461.141\t6.091130397435897\t3.0455651987179486\n1465.167\t6.107957852564103\t3.0539789262820514\n1469.193\t6.124785307692308\t3.062392653846154\n1473.219\t6.141612762820513\t3.0708063814102564\n1477.2450000000001\t6.158440217948717\t3.0792201089743587\n1481.271\t6.175267673076923\t3.0876338365384615\n1485.297\t6.192095128205128\t3.096047564102564\n1489.323\t6.208922583333333\t3.1044612916666665\n1493.3490000000002\t6.2257500384615385\t3.1128750192307693\n1497.375\t6.242577493589744\t3.121288746794872\n1501.401\t6.259404948717949\t3.1297024743589743\n1505.4270000000001\t6.276232403846154\t3.138116201923077\n1509.453\t6.293059858974359\t3.1465299294871794\n1513.479\t6.309887314102564\t3.154943657051282\n1517.505\t6.326714769230769\t3.1633573846153844\n1521.531\t6.343542224358974\t3.171771112179487\n1525.557\t6.36036967948718\t3.18018483974359\n1529.583\t6.377197134615384\t3.188598567307692\n1533.609\t6.39402458974359\t3.197012294871795\n1537.635\t6.410852044871795\t3.2054260224358977\n1541.661\t6.4276795\t3.21383975\n1545.687\t6.444506955128205\t3.2222534775641023\n1549.713\t6.46133441025641\t3.230667205128205\n1553.739\t6.478161865384616\t3.239080932692308\n1557.765\t6.49498932051282\t3.24749466025641\n1561.791\t6.511816775641026\t3.255908387820513\n1565.817\t6.528644230769231\t3.2643221153846156\n1569.843\t6.545471685897436\t3.272735842948718\n1573.8690000000001\t6.562299141025641\t3.2811495705128206\n1577.895\t6.579126596153846\t3.289563298076923\n1581.921\t6.595954051282051\t3.2979770256410257\n1585.9470000000001\t6.612781506410256\t3.306390753205128\n1589.973\t6.6296089615384615\t3.3148044807692307\n1593.999\t6.646436416666667\t3.3232182083333335\n1598.025\t6.663263871794872\t3.331631935897436\n1602.051\t6.680091326923077\t3.3400456634615385\n1606.077\t6.6969187820512825\t3.3484593910256413\n1610.103\t6.713746237179487\t3.3568731185897436\n1614.129\t6.730573692307692\t3.365286846153846\n1618.155\t6.747401147435897\t3.3737005737179486\n1622.181\t6.764228602564103\t3.3821143012820514\n1626.2069999999999\t6.781056057692307\t3.3905280288461537\n1630.233\t6.797883512820513\t3.3989417564102564\n1634.259\t6.814710967948718\t3.407355483974359\n1638.285\t6.831538423076923\t3.4157692115384615\n1642.3110000000001\t6.848365878205128\t3.424182939102564\n1646.337\t6.865193333333333\t3.4325966666666665\n1650.363\t6.8820207884615385\t3.4410103942307693\n1654.3890000000001\t6.898848243589743\t3.4494241217948716\n1658.415\t6.915675698717949\t3.4578378493589743\n1662.441\t6.932503153846154\t3.466251576923077\n1666.467\t6.949330608974359\t3.4746653044871794\n1670.493\t6.966158064102564\t3.483079032051282\n1674.519\t6.98298551923077\t3.491492759615385\n1678.545\t6.999812974358974\t3.499906487179487\n1682.571\t7.01664042948718\t3.50832021474359\n1686.597\t7.033467884615384\t3.516733942307692\n1690.623\t7.05029533974359\t3.525147669871795\n1694.649\t7.0671227948717945\t3.5335613974358973\n1698.675\t7.08395025\t3.541975125\n1702.701\t7.1007777051282055\t3.5503888525641027\n1706.727\t7.11760516025641\t3.558802580128205\n1710.7530000000002\t7.134432615384616\t3.567216307692308\n1714.779\t7.151260070512821\t3.5756300352564105\n1718.805\t7.168087525641026\t3.584043762820513\n1722.8310000000001\t7.18491498076923\t3.592457490384615\n1726.857\t7.201742435897436\t3.600871217948718\n1730.883\t7.218569891025641\t3.6092849455128206\n1734.909\t7.235397346153846\t3.617698673076923\n1738.935\t7.252224801282051\t3.6261124006410257\n1742.961\t7.269052256410257\t3.6345261282051284\n1746.987\t7.2858797115384615\t3.6429398557692307\n1751.013\t7.302707166666666\t3.651353583333333\n1755.039\t7.3195346217948725\t3.6597673108974362\n1759.065\t7.336362076923077\t3.6681810384615385\n1763.091\t7.353189532051282\t3.676594766025641\n1767.117\t7.370016987179487\t3.6850084935897436\n1771.143\t7.386844442307693\t3.6934222211538463\n1775.1689999999999\t7.403671897435897\t3.7018359487179486\n1779.1950000000002\t7.420499352564103\t3.7102496762820514\n1783.221\t7.437326807692308\t3.718663403846154\n1787.2469999999998\t7.454154262820513\t3.7270771314102564\n1791.2730000000001\t7.4709817179487175\t3.7354908589743587\n1795.299\t7.487809173076923\t3.7439045865384615\n1799.325\t7.5046366282051284\t3.7523183141025642\n1803.351\t7.521464083333333\t3.7607320416666665\n1807.377\t7.5382915384615385\t3.7691457692307693\n1811.403\t7.555118993589744\t3.777559496794872\n1815.429\t7.571946448717949\t3.7859732243589743\n1819.455\t7.588773903846153\t3.7943869519230766\n1823.481\t7.60560135897436\t3.80280067948718\n1827.507\t7.622428814102564\t3.811214407051282\n1831.533\t7.639256269230769\t3.8196281346153844\n1835.559\t7.656083724358974\t3.828041862179487\n1839.585\t7.67291117948718\t3.83645558974359\n1843.6109999999999\t7.689738634615384\t3.844869317307692\n1847.6370000000002\t7.70656608974359\t3.853283044871795\n1851.663\t7.723393544871795\t3.8616967724358977\n1855.6889999999999\t7.740221\t3.8701105\n1859.7150000000001\t7.757048455128205\t3.8785242275641023\n1863.741\t7.77387591025641\t3.886937955128205\n1867.767\t7.790703365384616\t3.895351682692308\n1871.7930000000001\t7.80753082051282\t3.90376541025641\n1875.819\t7.824358275641026\t3.912179137820513\n1879.845\t7.841185730769231\t3.9205928653846156\n1883.871\t7.858013185897436\t3.929006592948718\n1887.897\t7.87484064102564\t3.93742032051282\n1891.923\t7.891668096153847\t3.9458340480769234\n1895.949\t7.908495551282051\t3.9542477756410257\n1899.975\t7.925323006410256\t3.962661503205128\n1904.001\t7.9421504615384615\t3.9710752307692307\n1908.027\t7.958977916666667\t3.9794889583333335\n1912.0529999999999\t7.975805371794872\t3.987902685897436\n1916.079\t7.992632826923077\t3.9963164134615385\n1920.105\t8.009460282051283\t4.004730141025641\n1924.1309999999999\t8.026287737179487\t4.013143868589744\n1928.1570000000002\t8.043115192307692\t4.021557596153846\n1932.183\t8.059942647435896\t4.029971323717948\n1936.209\t8.076770102564103\t4.038385051282051\n1940.2350000000001\t8.093597557692307\t4.046798778846154\n1944.261\t8.110425012820514\t4.055212506410257\n1948.287\t8.127252467948718\t4.063626233974359\n1952.313\t8.144079923076923\t4.0720399615384615\n1956.339\t8.160907378205128\t4.080453689102564\n1960.365\t8.177734833333334\t4.088867416666667\n1964.391\t8.194562288461539\t4.097281144230769\n1968.417\t8.211389743589743\t4.105694871794872\n1972.443\t8.22821719871795\t4.114108599358975\n1976.469\t8.245044653846154\t4.122522326923077\n1980.495\t8.261872108974359\t4.130936054487179\n1984.521\t8.278699564102563\t4.139349782051282\n1988.547\t8.29552701923077\t4.147763509615385\n1992.5729999999999\t8.312354474358974\t4.156177237179487\n1996.5990000000002\t8.329181929487179\t4.1645909647435895\n2000.625\t8.346009384615385\t4.173004692307693\n2004.6509999999998\t8.36283683974359\t4.181418419871795\n2008.6770000000001\t8.379664294871795\t4.189832147435897\n2012.703\t8.39649175\t4.198245875\n2016.729\t8.413319205128206\t4.206659602564103\n2020.755\t8.43014666025641\t4.215073330128205\n2024.781\t8.446974115384617\t4.223487057692308\n2028.807\t8.463801570512821\t4.231900785256411\n2032.833\t8.480629025641026\t4.240314512820513\n2036.859\t8.49745648076923\t4.248728240384615\n2040.885\t8.514283935897435\t4.2571419679487175\n2044.911\t8.531111391025641\t4.265555695512821\n2048.937\t8.547938846153846\t4.273969423076923\n2052.9629999999997\t8.564766301282052\t4.282383150641026\n2056.989\t8.581593756410257\t4.2907968782051285\n2061.015\t8.598421211538462\t4.299210605769231\n2065.041\t8.615248666666666\t4.307624333333333\n2069.067\t8.632076121794872\t4.316038060897436\n2073.093\t8.648903576923077\t4.3244517884615385\n2077.119\t8.665731032051282\t4.332865516025641\n2081.145\t8.682558487179488\t4.341279243589744\n2085.1710000000003\t8.699385942307693\t4.349692971153846\n2089.197\t8.716213397435897\t4.358106698717949\n2093.223\t8.733040852564102\t4.366520426282051\n2097.249\t8.749868307692308\t4.374934153846154\n2101.275\t8.766695762820513\t4.383347881410256\n2105.301\t8.783523217948717\t4.391761608974359\n2109.327\t8.800350673076924\t4.400175336538462\n2113.353\t8.817178128205128\t4.408589064102564\n2117.379\t8.834005583333333\t4.4170027916666665\n2121.4049999999997\t8.850833038461538\t4.425416519230769\n2125.431\t8.867660493589744\t4.433830246794872\n2129.457\t8.884487948717949\t4.442243974358974\n2133.483\t8.901315403846153\t4.450657701923077\n2137.509\t8.91814285897436\t4.45907142948718\n2141.535\t8.934970314102564\t4.467485157051282\n2145.561\t8.951797769230769\t4.475898884615384\n2149.587\t8.968625224358973\t4.484312612179487\n2153.613\t8.98545267948718\t4.49272633974359\n2157.639\t9.002280134615384\t4.501140067307692\n2161.665\t9.01910758974359\t4.509553794871795\n2165.691\t9.035935044871795\t4.517967522435898\n2169.717\t9.0527625\t4.52638125\n2173.743\t9.069589955128205\t4.534794977564102\n2177.7690000000002\t9.08641741025641\t4.543208705128205\n2181.795\t9.103244865384616\t4.551622432692308\n2185.821\t9.12007232051282\t4.56003616025641\n2189.8469999999998\t9.136899775641027\t4.568449887820513\n2193.873\t9.153727230769231\t4.576863615384616\n2197.899\t9.170554685897436\t4.585277342948718\n2201.925\t9.18738214102564\t4.59369107051282\n2205.951\t9.204209596153845\t4.6021047980769225\n2209.977\t9.221037051282051\t4.610518525641026\n2214.003\t9.237864506410258\t4.618932253205129\n2218.029\t9.254691961538462\t4.627345980769231\n2222.055\t9.271519416666667\t4.6357597083333335\n2226.081\t9.288346871794872\t4.644173435897436\n2230.107\t9.305174326923076\t4.652587163461538\n2234.133\t9.32200178205128\t4.66100089102564\n2238.159\t9.338829237179487\t4.669414618589744\n2242.185\t9.355656692307694\t4.677828346153847\n2246.2110000000002\t9.372484147435898\t4.686242073717949\n2250.237\t9.389311602564103\t4.694655801282051\n2254.263\t9.406139057692307\t4.703069528846154\n2258.2889999999998\t9.422966512820512\t4.711483256410256\n2262.315\t9.439793967948718\t4.719896983974359\n2266.341\t9.456621423076923\t4.7283107115384615\n2270.367\t9.47344887820513\t4.736724439102565\n2274.393\t9.490276333333334\t4.745138166666667\n2278.419\t9.507103788461539\t4.753551894230769\n2282.4449999999997\t9.523931243589743\t4.761965621794872\n2286.471\t9.540758698717948\t4.770379349358974\n2290.4970000000003\t9.557586153846154\t4.778793076923077\n2294.523\t9.574413608974359\t4.787206804487179\n2298.549\t9.591241064102565\t4.795620532051283\n2302.575\t9.60806851923077\t4.804034259615385\n2306.6009999999997\t9.624895974358974\t4.812447987179487\n2310.627\t9.641723429487179\t4.8208617147435895\n2314.6530000000002\t9.658550884615384\t4.829275442307692\n2318.679\t9.67537833974359\t4.837689169871795\n2322.705\t9.692205794871795\t4.846102897435897\n2326.7309999999998\t9.709033250000001\t4.8545166250000005\n2330.757\t9.725860705128206\t4.862930352564103\n2334.783\t9.74268816025641\t4.871344080128205\n2338.809\t9.759515615384615\t4.879757807692307\n2342.835\t9.77634307051282\t4.88817153525641\n2346.861\t9.793170525641026\t4.896585262820513\n2350.8869999999997\t9.809997980769232\t4.904998990384616\n2354.913\t9.826825435897437\t4.913412717948718\n2358.9390000000003\t9.843652891025641\t4.921826445512821\n2362.965\t9.860480346153846\t4.930240173076923\n2366.991\t9.87730780128205\t4.938653900641025\n2371.017\t9.894135256410257\t4.9470676282051285\n2375.0429999999997\t9.910962711538462\t4.955481355769231\n2379.069\t9.927790166666668\t4.963895083333334\n2383.0950000000003\t9.944617621794873\t4.972308810897436\n2387.121\t9.961445076923077\t4.980722538461539\n2391.147\t9.978272532051282\t4.989136266025641\n2395.173\t9.995099987179486\t4.997549993589743\n2399.199\t10.011927442307693\t5.005963721153846\n2403.225\t10.028754897435897\t5.014377448717949\n2407.251\t10.045582352564104\t5.022791176282052\n2411.277\t10.062409807692308\t5.031204903846154\n2415.303\t10.079237262820513\t5.0396186314102565\n2419.3289999999997\t10.096064717948718\t5.048032358974359\n2423.355\t10.112892173076922\t5.056446086538461\n2427.3810000000003\t10.129719628205129\t5.064859814102564\n2431.407\t10.146547083333333\t5.0732735416666666\n2435.433\t10.16337453846154\t5.08168726923077\n2439.459\t10.180201993589744\t5.090100996794872\n2443.4849999999997\t10.197029448717949\t5.098514724358974\n2447.511\t10.213856903846153\t5.106928451923077\n2451.5370000000003\t10.230684358974358\t5.115342179487179\n2455.563\t10.247511814102564\t5.123755907051282\n2459.589\t10.264339269230769\t5.1321696346153844\n2463.615\t10.281166724358975\t5.140583362179488\n2467.641\t10.29799417948718\t5.14899708974359\n2471.667\t10.314821634615384\t5.157410817307692\n2475.693\t10.331649089743589\t5.1658245448717945\n2479.719\t10.348476544871794\t5.174238272435897\n2483.745\t10.365304\t5.182652\n"
    win.close()
    # linear const: 1-6
    destination_unit = "nm"
    destination_wavelength_start = 1227.633
    destination_wavelength_stop = 2487.673
    destination_wavelength_step = 4.026
    convolution_extrapolation_type = 0  # "zeros"
    convolution_gauss_ratio = 0
    convolution_truncation = 3
    convolution_width_1_const = 7.740221
    convolution_width_2_const = 3.8701105
    win = main.ConvolutionMainW()
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(3)
    win.ui.dstntn_tab.setCurrentIndex(1)
    win.dstntn_linear_start.setValue(destination_wavelength_start)
    win.dstntn_linear_stop.setValue(destination_wavelength_stop)
    win.dstntn_linear_step.setValue(destination_wavelength_step)
    ## convolution
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(2)
    win.conv_wdth_1_const.setValue(convolution_width_1_const)
    win.conv_wdth_2_const.setValue(convolution_width_2_const)
    # assert: Gauss function
    convolution_type = 1  # "Gauss function"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Gauss function\ndestination_wavelength_nm\tdestination_width\n1227.633\t7.740221\n1231.659\t7.740221\n1235.685\t7.740221\n1239.711\t7.740221\n1243.737\t7.740221\n1247.7630000000001\t7.740221\n1251.789\t7.740221\n1255.815\t7.740221\n1259.8410000000001\t7.740221\n1263.867\t7.740221\n1267.893\t7.740221\n1271.919\t7.740221\n1275.945\t7.740221\n1279.971\t7.740221\n1283.997\t7.740221\n1288.0230000000001\t7.740221\n1292.049\t7.740221\n1296.075\t7.740221\n1300.101\t7.740221\n1304.127\t7.740221\n1308.153\t7.740221\n1312.179\t7.740221\n1316.205\t7.740221\n1320.231\t7.740221\n1324.257\t7.740221\n1328.2830000000001\t7.740221\n1332.309\t7.740221\n1336.335\t7.740221\n1340.361\t7.740221\n1344.387\t7.740221\n1348.413\t7.740221\n1352.439\t7.740221\n1356.4650000000001\t7.740221\n1360.491\t7.740221\n1364.517\t7.740221\n1368.5430000000001\t7.740221\n1372.569\t7.740221\n1376.595\t7.740221\n1380.621\t7.740221\n1384.647\t7.740221\n1388.673\t7.740221\n1392.699\t7.740221\n1396.725\t7.740221\n1400.751\t7.740221\n1404.777\t7.740221\n1408.803\t7.740221\n1412.829\t7.740221\n1416.855\t7.740221\n1420.881\t7.740221\n1424.9070000000002\t7.740221\n1428.933\t7.740221\n1432.959\t7.740221\n1436.9850000000001\t7.740221\n1441.011\t7.740221\n1445.037\t7.740221\n1449.063\t7.740221\n1453.089\t7.740221\n1457.115\t7.740221\n1461.141\t7.740221\n1465.167\t7.740221\n1469.193\t7.740221\n1473.219\t7.740221\n1477.2450000000001\t7.740221\n1481.271\t7.740221\n1485.297\t7.740221\n1489.323\t7.740221\n1493.3490000000002\t7.740221\n1497.375\t7.740221\n1501.401\t7.740221\n1505.4270000000001\t7.740221\n1509.453\t7.740221\n1513.479\t7.740221\n1517.505\t7.740221\n1521.531\t7.740221\n1525.557\t7.740221\n1529.583\t7.740221\n1533.609\t7.740221\n1537.635\t7.740221\n1541.661\t7.740221\n1545.687\t7.740221\n1549.713\t7.740221\n1553.739\t7.740221\n1557.765\t7.740221\n1561.791\t7.740221\n1565.817\t7.740221\n1569.843\t7.740221\n1573.8690000000001\t7.740221\n1577.895\t7.740221\n1581.921\t7.740221\n1585.9470000000001\t7.740221\n1589.973\t7.740221\n1593.999\t7.740221\n1598.025\t7.740221\n1602.051\t7.740221\n1606.077\t7.740221\n1610.103\t7.740221\n1614.129\t7.740221\n1618.155\t7.740221\n1622.181\t7.740221\n1626.2069999999999\t7.740221\n1630.233\t7.740221\n1634.259\t7.740221\n1638.285\t7.740221\n1642.3110000000001\t7.740221\n1646.337\t7.740221\n1650.363\t7.740221\n1654.3890000000001\t7.740221\n1658.415\t7.740221\n1662.441\t7.740221\n1666.467\t7.740221\n1670.493\t7.740221\n1674.519\t7.740221\n1678.545\t7.740221\n1682.571\t7.740221\n1686.597\t7.740221\n1690.623\t7.740221\n1694.649\t7.740221\n1698.675\t7.740221\n1702.701\t7.740221\n1706.727\t7.740221\n1710.7530000000002\t7.740221\n1714.779\t7.740221\n1718.805\t7.740221\n1722.8310000000001\t7.740221\n1726.857\t7.740221\n1730.883\t7.740221\n1734.909\t7.740221\n1738.935\t7.740221\n1742.961\t7.740221\n1746.987\t7.740221\n1751.013\t7.740221\n1755.039\t7.740221\n1759.065\t7.740221\n1763.091\t7.740221\n1767.117\t7.740221\n1771.143\t7.740221\n1775.1689999999999\t7.740221\n1779.1950000000002\t7.740221\n1783.221\t7.740221\n1787.2469999999998\t7.740221\n1791.2730000000001\t7.740221\n1795.299\t7.740221\n1799.325\t7.740221\n1803.351\t7.740221\n1807.377\t7.740221\n1811.403\t7.740221\n1815.429\t7.740221\n1819.455\t7.740221\n1823.481\t7.740221\n1827.507\t7.740221\n1831.533\t7.740221\n1835.559\t7.740221\n1839.585\t7.740221\n1843.6109999999999\t7.740221\n1847.6370000000002\t7.740221\n1851.663\t7.740221\n1855.6889999999999\t7.740221\n1859.7150000000001\t7.740221\n1863.741\t7.740221\n1867.767\t7.740221\n1871.7930000000001\t7.740221\n1875.819\t7.740221\n1879.845\t7.740221\n1883.871\t7.740221\n1887.897\t7.740221\n1891.923\t7.740221\n1895.949\t7.740221\n1899.975\t7.740221\n1904.001\t7.740221\n1908.027\t7.740221\n1912.0529999999999\t7.740221\n1916.079\t7.740221\n1920.105\t7.740221\n1924.1309999999999\t7.740221\n1928.1570000000002\t7.740221\n1932.183\t7.740221\n1936.209\t7.740221\n1940.2350000000001\t7.740221\n1944.261\t7.740221\n1948.287\t7.740221\n1952.313\t7.740221\n1956.339\t7.740221\n1960.365\t7.740221\n1964.391\t7.740221\n1968.417\t7.740221\n1972.443\t7.740221\n1976.469\t7.740221\n1980.495\t7.740221\n1984.521\t7.740221\n1988.547\t7.740221\n1992.5729999999999\t7.740221\n1996.5990000000002\t7.740221\n2000.625\t7.740221\n2004.6509999999998\t7.740221\n2008.6770000000001\t7.740221\n2012.703\t7.740221\n2016.729\t7.740221\n2020.755\t7.740221\n2024.781\t7.740221\n2028.807\t7.740221\n2032.833\t7.740221\n2036.859\t7.740221\n2040.885\t7.740221\n2044.911\t7.740221\n2048.937\t7.740221\n2052.9629999999997\t7.740221\n2056.989\t7.740221\n2061.015\t7.740221\n2065.041\t7.740221\n2069.067\t7.740221\n2073.093\t7.740221\n2077.119\t7.740221\n2081.145\t7.740221\n2085.1710000000003\t7.740221\n2089.197\t7.740221\n2093.223\t7.740221\n2097.249\t7.740221\n2101.275\t7.740221\n2105.301\t7.740221\n2109.327\t7.740221\n2113.353\t7.740221\n2117.379\t7.740221\n2121.4049999999997\t7.740221\n2125.431\t7.740221\n2129.457\t7.740221\n2133.483\t7.740221\n2137.509\t7.740221\n2141.535\t7.740221\n2145.561\t7.740221\n2149.587\t7.740221\n2153.613\t7.740221\n2157.639\t7.740221\n2161.665\t7.740221\n2165.691\t7.740221\n2169.717\t7.740221\n2173.743\t7.740221\n2177.7690000000002\t7.740221\n2181.795\t7.740221\n2185.821\t7.740221\n2189.8469999999998\t7.740221\n2193.873\t7.740221\n2197.899\t7.740221\n2201.925\t7.740221\n2205.951\t7.740221\n2209.977\t7.740221\n2214.003\t7.740221\n2218.029\t7.740221\n2222.055\t7.740221\n2226.081\t7.740221\n2230.107\t7.740221\n2234.133\t7.740221\n2238.159\t7.740221\n2242.185\t7.740221\n2246.2110000000002\t7.740221\n2250.237\t7.740221\n2254.263\t7.740221\n2258.2889999999998\t7.740221\n2262.315\t7.740221\n2266.341\t7.740221\n2270.367\t7.740221\n2274.393\t7.740221\n2278.419\t7.740221\n2282.4449999999997\t7.740221\n2286.471\t7.740221\n2290.4970000000003\t7.740221\n2294.523\t7.740221\n2298.549\t7.740221\n2302.575\t7.740221\n2306.6009999999997\t7.740221\n2310.627\t7.740221\n2314.6530000000002\t7.740221\n2318.679\t7.740221\n2322.705\t7.740221\n2326.7309999999998\t7.740221\n2330.757\t7.740221\n2334.783\t7.740221\n2338.809\t7.740221\n2342.835\t7.740221\n2346.861\t7.740221\n2350.8869999999997\t7.740221\n2354.913\t7.740221\n2358.9390000000003\t7.740221\n2362.965\t7.740221\n2366.991\t7.740221\n2371.017\t7.740221\n2375.0429999999997\t7.740221\n2379.069\t7.740221\n2383.0950000000003\t7.740221\n2387.121\t7.740221\n2391.147\t7.740221\n2395.173\t7.740221\n2399.199\t7.740221\n2403.225\t7.740221\n2407.251\t7.740221\n2411.277\t7.740221\n2415.303\t7.740221\n2419.3289999999997\t7.740221\n2423.355\t7.740221\n2427.3810000000003\t7.740221\n2431.407\t7.740221\n2435.433\t7.740221\n2439.459\t7.740221\n2443.4849999999997\t7.740221\n2447.511\t7.740221\n2451.5370000000003\t7.740221\n2455.563\t7.740221\n2459.589\t7.740221\n2463.615\t7.740221\n2467.641\t7.740221\n2471.667\t7.740221\n2475.693\t7.740221\n2479.719\t7.740221\n2483.745\t7.740221\n"
    # assert: triangle
    convolution_type = 2  # "triangle"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: triangle\ndestination_wavelength_nm\tdestination_width\n1227.633\t7.740221\n1231.659\t7.740221\n1235.685\t7.740221\n1239.711\t7.740221\n1243.737\t7.740221\n1247.7630000000001\t7.740221\n1251.789\t7.740221\n1255.815\t7.740221\n1259.8410000000001\t7.740221\n1263.867\t7.740221\n1267.893\t7.740221\n1271.919\t7.740221\n1275.945\t7.740221\n1279.971\t7.740221\n1283.997\t7.740221\n1288.0230000000001\t7.740221\n1292.049\t7.740221\n1296.075\t7.740221\n1300.101\t7.740221\n1304.127\t7.740221\n1308.153\t7.740221\n1312.179\t7.740221\n1316.205\t7.740221\n1320.231\t7.740221\n1324.257\t7.740221\n1328.2830000000001\t7.740221\n1332.309\t7.740221\n1336.335\t7.740221\n1340.361\t7.740221\n1344.387\t7.740221\n1348.413\t7.740221\n1352.439\t7.740221\n1356.4650000000001\t7.740221\n1360.491\t7.740221\n1364.517\t7.740221\n1368.5430000000001\t7.740221\n1372.569\t7.740221\n1376.595\t7.740221\n1380.621\t7.740221\n1384.647\t7.740221\n1388.673\t7.740221\n1392.699\t7.740221\n1396.725\t7.740221\n1400.751\t7.740221\n1404.777\t7.740221\n1408.803\t7.740221\n1412.829\t7.740221\n1416.855\t7.740221\n1420.881\t7.740221\n1424.9070000000002\t7.740221\n1428.933\t7.740221\n1432.959\t7.740221\n1436.9850000000001\t7.740221\n1441.011\t7.740221\n1445.037\t7.740221\n1449.063\t7.740221\n1453.089\t7.740221\n1457.115\t7.740221\n1461.141\t7.740221\n1465.167\t7.740221\n1469.193\t7.740221\n1473.219\t7.740221\n1477.2450000000001\t7.740221\n1481.271\t7.740221\n1485.297\t7.740221\n1489.323\t7.740221\n1493.3490000000002\t7.740221\n1497.375\t7.740221\n1501.401\t7.740221\n1505.4270000000001\t7.740221\n1509.453\t7.740221\n1513.479\t7.740221\n1517.505\t7.740221\n1521.531\t7.740221\n1525.557\t7.740221\n1529.583\t7.740221\n1533.609\t7.740221\n1537.635\t7.740221\n1541.661\t7.740221\n1545.687\t7.740221\n1549.713\t7.740221\n1553.739\t7.740221\n1557.765\t7.740221\n1561.791\t7.740221\n1565.817\t7.740221\n1569.843\t7.740221\n1573.8690000000001\t7.740221\n1577.895\t7.740221\n1581.921\t7.740221\n1585.9470000000001\t7.740221\n1589.973\t7.740221\n1593.999\t7.740221\n1598.025\t7.740221\n1602.051\t7.740221\n1606.077\t7.740221\n1610.103\t7.740221\n1614.129\t7.740221\n1618.155\t7.740221\n1622.181\t7.740221\n1626.2069999999999\t7.740221\n1630.233\t7.740221\n1634.259\t7.740221\n1638.285\t7.740221\n1642.3110000000001\t7.740221\n1646.337\t7.740221\n1650.363\t7.740221\n1654.3890000000001\t7.740221\n1658.415\t7.740221\n1662.441\t7.740221\n1666.467\t7.740221\n1670.493\t7.740221\n1674.519\t7.740221\n1678.545\t7.740221\n1682.571\t7.740221\n1686.597\t7.740221\n1690.623\t7.740221\n1694.649\t7.740221\n1698.675\t7.740221\n1702.701\t7.740221\n1706.727\t7.740221\n1710.7530000000002\t7.740221\n1714.779\t7.740221\n1718.805\t7.740221\n1722.8310000000001\t7.740221\n1726.857\t7.740221\n1730.883\t7.740221\n1734.909\t7.740221\n1738.935\t7.740221\n1742.961\t7.740221\n1746.987\t7.740221\n1751.013\t7.740221\n1755.039\t7.740221\n1759.065\t7.740221\n1763.091\t7.740221\n1767.117\t7.740221\n1771.143\t7.740221\n1775.1689999999999\t7.740221\n1779.1950000000002\t7.740221\n1783.221\t7.740221\n1787.2469999999998\t7.740221\n1791.2730000000001\t7.740221\n1795.299\t7.740221\n1799.325\t7.740221\n1803.351\t7.740221\n1807.377\t7.740221\n1811.403\t7.740221\n1815.429\t7.740221\n1819.455\t7.740221\n1823.481\t7.740221\n1827.507\t7.740221\n1831.533\t7.740221\n1835.559\t7.740221\n1839.585\t7.740221\n1843.6109999999999\t7.740221\n1847.6370000000002\t7.740221\n1851.663\t7.740221\n1855.6889999999999\t7.740221\n1859.7150000000001\t7.740221\n1863.741\t7.740221\n1867.767\t7.740221\n1871.7930000000001\t7.740221\n1875.819\t7.740221\n1879.845\t7.740221\n1883.871\t7.740221\n1887.897\t7.740221\n1891.923\t7.740221\n1895.949\t7.740221\n1899.975\t7.740221\n1904.001\t7.740221\n1908.027\t7.740221\n1912.0529999999999\t7.740221\n1916.079\t7.740221\n1920.105\t7.740221\n1924.1309999999999\t7.740221\n1928.1570000000002\t7.740221\n1932.183\t7.740221\n1936.209\t7.740221\n1940.2350000000001\t7.740221\n1944.261\t7.740221\n1948.287\t7.740221\n1952.313\t7.740221\n1956.339\t7.740221\n1960.365\t7.740221\n1964.391\t7.740221\n1968.417\t7.740221\n1972.443\t7.740221\n1976.469\t7.740221\n1980.495\t7.740221\n1984.521\t7.740221\n1988.547\t7.740221\n1992.5729999999999\t7.740221\n1996.5990000000002\t7.740221\n2000.625\t7.740221\n2004.6509999999998\t7.740221\n2008.6770000000001\t7.740221\n2012.703\t7.740221\n2016.729\t7.740221\n2020.755\t7.740221\n2024.781\t7.740221\n2028.807\t7.740221\n2032.833\t7.740221\n2036.859\t7.740221\n2040.885\t7.740221\n2044.911\t7.740221\n2048.937\t7.740221\n2052.9629999999997\t7.740221\n2056.989\t7.740221\n2061.015\t7.740221\n2065.041\t7.740221\n2069.067\t7.740221\n2073.093\t7.740221\n2077.119\t7.740221\n2081.145\t7.740221\n2085.1710000000003\t7.740221\n2089.197\t7.740221\n2093.223\t7.740221\n2097.249\t7.740221\n2101.275\t7.740221\n2105.301\t7.740221\n2109.327\t7.740221\n2113.353\t7.740221\n2117.379\t7.740221\n2121.4049999999997\t7.740221\n2125.431\t7.740221\n2129.457\t7.740221\n2133.483\t7.740221\n2137.509\t7.740221\n2141.535\t7.740221\n2145.561\t7.740221\n2149.587\t7.740221\n2153.613\t7.740221\n2157.639\t7.740221\n2161.665\t7.740221\n2165.691\t7.740221\n2169.717\t7.740221\n2173.743\t7.740221\n2177.7690000000002\t7.740221\n2181.795\t7.740221\n2185.821\t7.740221\n2189.8469999999998\t7.740221\n2193.873\t7.740221\n2197.899\t7.740221\n2201.925\t7.740221\n2205.951\t7.740221\n2209.977\t7.740221\n2214.003\t7.740221\n2218.029\t7.740221\n2222.055\t7.740221\n2226.081\t7.740221\n2230.107\t7.740221\n2234.133\t7.740221\n2238.159\t7.740221\n2242.185\t7.740221\n2246.2110000000002\t7.740221\n2250.237\t7.740221\n2254.263\t7.740221\n2258.2889999999998\t7.740221\n2262.315\t7.740221\n2266.341\t7.740221\n2270.367\t7.740221\n2274.393\t7.740221\n2278.419\t7.740221\n2282.4449999999997\t7.740221\n2286.471\t7.740221\n2290.4970000000003\t7.740221\n2294.523\t7.740221\n2298.549\t7.740221\n2302.575\t7.740221\n2306.6009999999997\t7.740221\n2310.627\t7.740221\n2314.6530000000002\t7.740221\n2318.679\t7.740221\n2322.705\t7.740221\n2326.7309999999998\t7.740221\n2330.757\t7.740221\n2334.783\t7.740221\n2338.809\t7.740221\n2342.835\t7.740221\n2346.861\t7.740221\n2350.8869999999997\t7.740221\n2354.913\t7.740221\n2358.9390000000003\t7.740221\n2362.965\t7.740221\n2366.991\t7.740221\n2371.017\t7.740221\n2375.0429999999997\t7.740221\n2379.069\t7.740221\n2383.0950000000003\t7.740221\n2387.121\t7.740221\n2391.147\t7.740221\n2395.173\t7.740221\n2399.199\t7.740221\n2403.225\t7.740221\n2407.251\t7.740221\n2411.277\t7.740221\n2415.303\t7.740221\n2419.3289999999997\t7.740221\n2423.355\t7.740221\n2427.3810000000003\t7.740221\n2431.407\t7.740221\n2435.433\t7.740221\n2439.459\t7.740221\n2443.4849999999997\t7.740221\n2447.511\t7.740221\n2451.5370000000003\t7.740221\n2455.563\t7.740221\n2459.589\t7.740221\n2463.615\t7.740221\n2467.641\t7.740221\n2471.667\t7.740221\n2475.693\t7.740221\n2479.719\t7.740221\n2483.745\t7.740221\n"
    # assert: trapeze
    convolution_type = 3  # "trapeze"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: trapeze\ndestination_wavelength_nm\tdestination_width\tdestination_top\n1227.633\t7.740221\t3.8701105\n1231.659\t7.740221\t3.8701105\n1235.685\t7.740221\t3.8701105\n1239.711\t7.740221\t3.8701105\n1243.737\t7.740221\t3.8701105\n1247.7630000000001\t7.740221\t3.8701105\n1251.789\t7.740221\t3.8701105\n1255.815\t7.740221\t3.8701105\n1259.8410000000001\t7.740221\t3.8701105\n1263.867\t7.740221\t3.8701105\n1267.893\t7.740221\t3.8701105\n1271.919\t7.740221\t3.8701105\n1275.945\t7.740221\t3.8701105\n1279.971\t7.740221\t3.8701105\n1283.997\t7.740221\t3.8701105\n1288.0230000000001\t7.740221\t3.8701105\n1292.049\t7.740221\t3.8701105\n1296.075\t7.740221\t3.8701105\n1300.101\t7.740221\t3.8701105\n1304.127\t7.740221\t3.8701105\n1308.153\t7.740221\t3.8701105\n1312.179\t7.740221\t3.8701105\n1316.205\t7.740221\t3.8701105\n1320.231\t7.740221\t3.8701105\n1324.257\t7.740221\t3.8701105\n1328.2830000000001\t7.740221\t3.8701105\n1332.309\t7.740221\t3.8701105\n1336.335\t7.740221\t3.8701105\n1340.361\t7.740221\t3.8701105\n1344.387\t7.740221\t3.8701105\n1348.413\t7.740221\t3.8701105\n1352.439\t7.740221\t3.8701105\n1356.4650000000001\t7.740221\t3.8701105\n1360.491\t7.740221\t3.8701105\n1364.517\t7.740221\t3.8701105\n1368.5430000000001\t7.740221\t3.8701105\n1372.569\t7.740221\t3.8701105\n1376.595\t7.740221\t3.8701105\n1380.621\t7.740221\t3.8701105\n1384.647\t7.740221\t3.8701105\n1388.673\t7.740221\t3.8701105\n1392.699\t7.740221\t3.8701105\n1396.725\t7.740221\t3.8701105\n1400.751\t7.740221\t3.8701105\n1404.777\t7.740221\t3.8701105\n1408.803\t7.740221\t3.8701105\n1412.829\t7.740221\t3.8701105\n1416.855\t7.740221\t3.8701105\n1420.881\t7.740221\t3.8701105\n1424.9070000000002\t7.740221\t3.8701105\n1428.933\t7.740221\t3.8701105\n1432.959\t7.740221\t3.8701105\n1436.9850000000001\t7.740221\t3.8701105\n1441.011\t7.740221\t3.8701105\n1445.037\t7.740221\t3.8701105\n1449.063\t7.740221\t3.8701105\n1453.089\t7.740221\t3.8701105\n1457.115\t7.740221\t3.8701105\n1461.141\t7.740221\t3.8701105\n1465.167\t7.740221\t3.8701105\n1469.193\t7.740221\t3.8701105\n1473.219\t7.740221\t3.8701105\n1477.2450000000001\t7.740221\t3.8701105\n1481.271\t7.740221\t3.8701105\n1485.297\t7.740221\t3.8701105\n1489.323\t7.740221\t3.8701105\n1493.3490000000002\t7.740221\t3.8701105\n1497.375\t7.740221\t3.8701105\n1501.401\t7.740221\t3.8701105\n1505.4270000000001\t7.740221\t3.8701105\n1509.453\t7.740221\t3.8701105\n1513.479\t7.740221\t3.8701105\n1517.505\t7.740221\t3.8701105\n1521.531\t7.740221\t3.8701105\n1525.557\t7.740221\t3.8701105\n1529.583\t7.740221\t3.8701105\n1533.609\t7.740221\t3.8701105\n1537.635\t7.740221\t3.8701105\n1541.661\t7.740221\t3.8701105\n1545.687\t7.740221\t3.8701105\n1549.713\t7.740221\t3.8701105\n1553.739\t7.740221\t3.8701105\n1557.765\t7.740221\t3.8701105\n1561.791\t7.740221\t3.8701105\n1565.817\t7.740221\t3.8701105\n1569.843\t7.740221\t3.8701105\n1573.8690000000001\t7.740221\t3.8701105\n1577.895\t7.740221\t3.8701105\n1581.921\t7.740221\t3.8701105\n1585.9470000000001\t7.740221\t3.8701105\n1589.973\t7.740221\t3.8701105\n1593.999\t7.740221\t3.8701105\n1598.025\t7.740221\t3.8701105\n1602.051\t7.740221\t3.8701105\n1606.077\t7.740221\t3.8701105\n1610.103\t7.740221\t3.8701105\n1614.129\t7.740221\t3.8701105\n1618.155\t7.740221\t3.8701105\n1622.181\t7.740221\t3.8701105\n1626.2069999999999\t7.740221\t3.8701105\n1630.233\t7.740221\t3.8701105\n1634.259\t7.740221\t3.8701105\n1638.285\t7.740221\t3.8701105\n1642.3110000000001\t7.740221\t3.8701105\n1646.337\t7.740221\t3.8701105\n1650.363\t7.740221\t3.8701105\n1654.3890000000001\t7.740221\t3.8701105\n1658.415\t7.740221\t3.8701105\n1662.441\t7.740221\t3.8701105\n1666.467\t7.740221\t3.8701105\n1670.493\t7.740221\t3.8701105\n1674.519\t7.740221\t3.8701105\n1678.545\t7.740221\t3.8701105\n1682.571\t7.740221\t3.8701105\n1686.597\t7.740221\t3.8701105\n1690.623\t7.740221\t3.8701105\n1694.649\t7.740221\t3.8701105\n1698.675\t7.740221\t3.8701105\n1702.701\t7.740221\t3.8701105\n1706.727\t7.740221\t3.8701105\n1710.7530000000002\t7.740221\t3.8701105\n1714.779\t7.740221\t3.8701105\n1718.805\t7.740221\t3.8701105\n1722.8310000000001\t7.740221\t3.8701105\n1726.857\t7.740221\t3.8701105\n1730.883\t7.740221\t3.8701105\n1734.909\t7.740221\t3.8701105\n1738.935\t7.740221\t3.8701105\n1742.961\t7.740221\t3.8701105\n1746.987\t7.740221\t3.8701105\n1751.013\t7.740221\t3.8701105\n1755.039\t7.740221\t3.8701105\n1759.065\t7.740221\t3.8701105\n1763.091\t7.740221\t3.8701105\n1767.117\t7.740221\t3.8701105\n1771.143\t7.740221\t3.8701105\n1775.1689999999999\t7.740221\t3.8701105\n1779.1950000000002\t7.740221\t3.8701105\n1783.221\t7.740221\t3.8701105\n1787.2469999999998\t7.740221\t3.8701105\n1791.2730000000001\t7.740221\t3.8701105\n1795.299\t7.740221\t3.8701105\n1799.325\t7.740221\t3.8701105\n1803.351\t7.740221\t3.8701105\n1807.377\t7.740221\t3.8701105\n1811.403\t7.740221\t3.8701105\n1815.429\t7.740221\t3.8701105\n1819.455\t7.740221\t3.8701105\n1823.481\t7.740221\t3.8701105\n1827.507\t7.740221\t3.8701105\n1831.533\t7.740221\t3.8701105\n1835.559\t7.740221\t3.8701105\n1839.585\t7.740221\t3.8701105\n1843.6109999999999\t7.740221\t3.8701105\n1847.6370000000002\t7.740221\t3.8701105\n1851.663\t7.740221\t3.8701105\n1855.6889999999999\t7.740221\t3.8701105\n1859.7150000000001\t7.740221\t3.8701105\n1863.741\t7.740221\t3.8701105\n1867.767\t7.740221\t3.8701105\n1871.7930000000001\t7.740221\t3.8701105\n1875.819\t7.740221\t3.8701105\n1879.845\t7.740221\t3.8701105\n1883.871\t7.740221\t3.8701105\n1887.897\t7.740221\t3.8701105\n1891.923\t7.740221\t3.8701105\n1895.949\t7.740221\t3.8701105\n1899.975\t7.740221\t3.8701105\n1904.001\t7.740221\t3.8701105\n1908.027\t7.740221\t3.8701105\n1912.0529999999999\t7.740221\t3.8701105\n1916.079\t7.740221\t3.8701105\n1920.105\t7.740221\t3.8701105\n1924.1309999999999\t7.740221\t3.8701105\n1928.1570000000002\t7.740221\t3.8701105\n1932.183\t7.740221\t3.8701105\n1936.209\t7.740221\t3.8701105\n1940.2350000000001\t7.740221\t3.8701105\n1944.261\t7.740221\t3.8701105\n1948.287\t7.740221\t3.8701105\n1952.313\t7.740221\t3.8701105\n1956.339\t7.740221\t3.8701105\n1960.365\t7.740221\t3.8701105\n1964.391\t7.740221\t3.8701105\n1968.417\t7.740221\t3.8701105\n1972.443\t7.740221\t3.8701105\n1976.469\t7.740221\t3.8701105\n1980.495\t7.740221\t3.8701105\n1984.521\t7.740221\t3.8701105\n1988.547\t7.740221\t3.8701105\n1992.5729999999999\t7.740221\t3.8701105\n1996.5990000000002\t7.740221\t3.8701105\n2000.625\t7.740221\t3.8701105\n2004.6509999999998\t7.740221\t3.8701105\n2008.6770000000001\t7.740221\t3.8701105\n2012.703\t7.740221\t3.8701105\n2016.729\t7.740221\t3.8701105\n2020.755\t7.740221\t3.8701105\n2024.781\t7.740221\t3.8701105\n2028.807\t7.740221\t3.8701105\n2032.833\t7.740221\t3.8701105\n2036.859\t7.740221\t3.8701105\n2040.885\t7.740221\t3.8701105\n2044.911\t7.740221\t3.8701105\n2048.937\t7.740221\t3.8701105\n2052.9629999999997\t7.740221\t3.8701105\n2056.989\t7.740221\t3.8701105\n2061.015\t7.740221\t3.8701105\n2065.041\t7.740221\t3.8701105\n2069.067\t7.740221\t3.8701105\n2073.093\t7.740221\t3.8701105\n2077.119\t7.740221\t3.8701105\n2081.145\t7.740221\t3.8701105\n2085.1710000000003\t7.740221\t3.8701105\n2089.197\t7.740221\t3.8701105\n2093.223\t7.740221\t3.8701105\n2097.249\t7.740221\t3.8701105\n2101.275\t7.740221\t3.8701105\n2105.301\t7.740221\t3.8701105\n2109.327\t7.740221\t3.8701105\n2113.353\t7.740221\t3.8701105\n2117.379\t7.740221\t3.8701105\n2121.4049999999997\t7.740221\t3.8701105\n2125.431\t7.740221\t3.8701105\n2129.457\t7.740221\t3.8701105\n2133.483\t7.740221\t3.8701105\n2137.509\t7.740221\t3.8701105\n2141.535\t7.740221\t3.8701105\n2145.561\t7.740221\t3.8701105\n2149.587\t7.740221\t3.8701105\n2153.613\t7.740221\t3.8701105\n2157.639\t7.740221\t3.8701105\n2161.665\t7.740221\t3.8701105\n2165.691\t7.740221\t3.8701105\n2169.717\t7.740221\t3.8701105\n2173.743\t7.740221\t3.8701105\n2177.7690000000002\t7.740221\t3.8701105\n2181.795\t7.740221\t3.8701105\n2185.821\t7.740221\t3.8701105\n2189.8469999999998\t7.740221\t3.8701105\n2193.873\t7.740221\t3.8701105\n2197.899\t7.740221\t3.8701105\n2201.925\t7.740221\t3.8701105\n2205.951\t7.740221\t3.8701105\n2209.977\t7.740221\t3.8701105\n2214.003\t7.740221\t3.8701105\n2218.029\t7.740221\t3.8701105\n2222.055\t7.740221\t3.8701105\n2226.081\t7.740221\t3.8701105\n2230.107\t7.740221\t3.8701105\n2234.133\t7.740221\t3.8701105\n2238.159\t7.740221\t3.8701105\n2242.185\t7.740221\t3.8701105\n2246.2110000000002\t7.740221\t3.8701105\n2250.237\t7.740221\t3.8701105\n2254.263\t7.740221\t3.8701105\n2258.2889999999998\t7.740221\t3.8701105\n2262.315\t7.740221\t3.8701105\n2266.341\t7.740221\t3.8701105\n2270.367\t7.740221\t3.8701105\n2274.393\t7.740221\t3.8701105\n2278.419\t7.740221\t3.8701105\n2282.4449999999997\t7.740221\t3.8701105\n2286.471\t7.740221\t3.8701105\n2290.4970000000003\t7.740221\t3.8701105\n2294.523\t7.740221\t3.8701105\n2298.549\t7.740221\t3.8701105\n2302.575\t7.740221\t3.8701105\n2306.6009999999997\t7.740221\t3.8701105\n2310.627\t7.740221\t3.8701105\n2314.6530000000002\t7.740221\t3.8701105\n2318.679\t7.740221\t3.8701105\n2322.705\t7.740221\t3.8701105\n2326.7309999999998\t7.740221\t3.8701105\n2330.757\t7.740221\t3.8701105\n2334.783\t7.740221\t3.8701105\n2338.809\t7.740221\t3.8701105\n2342.835\t7.740221\t3.8701105\n2346.861\t7.740221\t3.8701105\n2350.8869999999997\t7.740221\t3.8701105\n2354.913\t7.740221\t3.8701105\n2358.9390000000003\t7.740221\t3.8701105\n2362.965\t7.740221\t3.8701105\n2366.991\t7.740221\t3.8701105\n2371.017\t7.740221\t3.8701105\n2375.0429999999997\t7.740221\t3.8701105\n2379.069\t7.740221\t3.8701105\n2383.0950000000003\t7.740221\t3.8701105\n2387.121\t7.740221\t3.8701105\n2391.147\t7.740221\t3.8701105\n2395.173\t7.740221\t3.8701105\n2399.199\t7.740221\t3.8701105\n2403.225\t7.740221\t3.8701105\n2407.251\t7.740221\t3.8701105\n2411.277\t7.740221\t3.8701105\n2415.303\t7.740221\t3.8701105\n2419.3289999999997\t7.740221\t3.8701105\n2423.355\t7.740221\t3.8701105\n2427.3810000000003\t7.740221\t3.8701105\n2431.407\t7.740221\t3.8701105\n2435.433\t7.740221\t3.8701105\n2439.459\t7.740221\t3.8701105\n2443.4849999999997\t7.740221\t3.8701105\n2447.511\t7.740221\t3.8701105\n2451.5370000000003\t7.740221\t3.8701105\n2455.563\t7.740221\t3.8701105\n2459.589\t7.740221\t3.8701105\n2463.615\t7.740221\t3.8701105\n2467.641\t7.740221\t3.8701105\n2471.667\t7.740221\t3.8701105\n2475.693\t7.740221\t3.8701105\n2479.719\t7.740221\t3.8701105\n2483.745\t7.740221\t3.8701105\n"
    # assert: Lorentz
    convolution_type = 4  # "Lorentz"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Lorentz function\ndestination_wavelength_nm\tdestination_width\n1227.633\t7.740221\n1231.659\t7.740221\n1235.685\t7.740221\n1239.711\t7.740221\n1243.737\t7.740221\n1247.7630000000001\t7.740221\n1251.789\t7.740221\n1255.815\t7.740221\n1259.8410000000001\t7.740221\n1263.867\t7.740221\n1267.893\t7.740221\n1271.919\t7.740221\n1275.945\t7.740221\n1279.971\t7.740221\n1283.997\t7.740221\n1288.0230000000001\t7.740221\n1292.049\t7.740221\n1296.075\t7.740221\n1300.101\t7.740221\n1304.127\t7.740221\n1308.153\t7.740221\n1312.179\t7.740221\n1316.205\t7.740221\n1320.231\t7.740221\n1324.257\t7.740221\n1328.2830000000001\t7.740221\n1332.309\t7.740221\n1336.335\t7.740221\n1340.361\t7.740221\n1344.387\t7.740221\n1348.413\t7.740221\n1352.439\t7.740221\n1356.4650000000001\t7.740221\n1360.491\t7.740221\n1364.517\t7.740221\n1368.5430000000001\t7.740221\n1372.569\t7.740221\n1376.595\t7.740221\n1380.621\t7.740221\n1384.647\t7.740221\n1388.673\t7.740221\n1392.699\t7.740221\n1396.725\t7.740221\n1400.751\t7.740221\n1404.777\t7.740221\n1408.803\t7.740221\n1412.829\t7.740221\n1416.855\t7.740221\n1420.881\t7.740221\n1424.9070000000002\t7.740221\n1428.933\t7.740221\n1432.959\t7.740221\n1436.9850000000001\t7.740221\n1441.011\t7.740221\n1445.037\t7.740221\n1449.063\t7.740221\n1453.089\t7.740221\n1457.115\t7.740221\n1461.141\t7.740221\n1465.167\t7.740221\n1469.193\t7.740221\n1473.219\t7.740221\n1477.2450000000001\t7.740221\n1481.271\t7.740221\n1485.297\t7.740221\n1489.323\t7.740221\n1493.3490000000002\t7.740221\n1497.375\t7.740221\n1501.401\t7.740221\n1505.4270000000001\t7.740221\n1509.453\t7.740221\n1513.479\t7.740221\n1517.505\t7.740221\n1521.531\t7.740221\n1525.557\t7.740221\n1529.583\t7.740221\n1533.609\t7.740221\n1537.635\t7.740221\n1541.661\t7.740221\n1545.687\t7.740221\n1549.713\t7.740221\n1553.739\t7.740221\n1557.765\t7.740221\n1561.791\t7.740221\n1565.817\t7.740221\n1569.843\t7.740221\n1573.8690000000001\t7.740221\n1577.895\t7.740221\n1581.921\t7.740221\n1585.9470000000001\t7.740221\n1589.973\t7.740221\n1593.999\t7.740221\n1598.025\t7.740221\n1602.051\t7.740221\n1606.077\t7.740221\n1610.103\t7.740221\n1614.129\t7.740221\n1618.155\t7.740221\n1622.181\t7.740221\n1626.2069999999999\t7.740221\n1630.233\t7.740221\n1634.259\t7.740221\n1638.285\t7.740221\n1642.3110000000001\t7.740221\n1646.337\t7.740221\n1650.363\t7.740221\n1654.3890000000001\t7.740221\n1658.415\t7.740221\n1662.441\t7.740221\n1666.467\t7.740221\n1670.493\t7.740221\n1674.519\t7.740221\n1678.545\t7.740221\n1682.571\t7.740221\n1686.597\t7.740221\n1690.623\t7.740221\n1694.649\t7.740221\n1698.675\t7.740221\n1702.701\t7.740221\n1706.727\t7.740221\n1710.7530000000002\t7.740221\n1714.779\t7.740221\n1718.805\t7.740221\n1722.8310000000001\t7.740221\n1726.857\t7.740221\n1730.883\t7.740221\n1734.909\t7.740221\n1738.935\t7.740221\n1742.961\t7.740221\n1746.987\t7.740221\n1751.013\t7.740221\n1755.039\t7.740221\n1759.065\t7.740221\n1763.091\t7.740221\n1767.117\t7.740221\n1771.143\t7.740221\n1775.1689999999999\t7.740221\n1779.1950000000002\t7.740221\n1783.221\t7.740221\n1787.2469999999998\t7.740221\n1791.2730000000001\t7.740221\n1795.299\t7.740221\n1799.325\t7.740221\n1803.351\t7.740221\n1807.377\t7.740221\n1811.403\t7.740221\n1815.429\t7.740221\n1819.455\t7.740221\n1823.481\t7.740221\n1827.507\t7.740221\n1831.533\t7.740221\n1835.559\t7.740221\n1839.585\t7.740221\n1843.6109999999999\t7.740221\n1847.6370000000002\t7.740221\n1851.663\t7.740221\n1855.6889999999999\t7.740221\n1859.7150000000001\t7.740221\n1863.741\t7.740221\n1867.767\t7.740221\n1871.7930000000001\t7.740221\n1875.819\t7.740221\n1879.845\t7.740221\n1883.871\t7.740221\n1887.897\t7.740221\n1891.923\t7.740221\n1895.949\t7.740221\n1899.975\t7.740221\n1904.001\t7.740221\n1908.027\t7.740221\n1912.0529999999999\t7.740221\n1916.079\t7.740221\n1920.105\t7.740221\n1924.1309999999999\t7.740221\n1928.1570000000002\t7.740221\n1932.183\t7.740221\n1936.209\t7.740221\n1940.2350000000001\t7.740221\n1944.261\t7.740221\n1948.287\t7.740221\n1952.313\t7.740221\n1956.339\t7.740221\n1960.365\t7.740221\n1964.391\t7.740221\n1968.417\t7.740221\n1972.443\t7.740221\n1976.469\t7.740221\n1980.495\t7.740221\n1984.521\t7.740221\n1988.547\t7.740221\n1992.5729999999999\t7.740221\n1996.5990000000002\t7.740221\n2000.625\t7.740221\n2004.6509999999998\t7.740221\n2008.6770000000001\t7.740221\n2012.703\t7.740221\n2016.729\t7.740221\n2020.755\t7.740221\n2024.781\t7.740221\n2028.807\t7.740221\n2032.833\t7.740221\n2036.859\t7.740221\n2040.885\t7.740221\n2044.911\t7.740221\n2048.937\t7.740221\n2052.9629999999997\t7.740221\n2056.989\t7.740221\n2061.015\t7.740221\n2065.041\t7.740221\n2069.067\t7.740221\n2073.093\t7.740221\n2077.119\t7.740221\n2081.145\t7.740221\n2085.1710000000003\t7.740221\n2089.197\t7.740221\n2093.223\t7.740221\n2097.249\t7.740221\n2101.275\t7.740221\n2105.301\t7.740221\n2109.327\t7.740221\n2113.353\t7.740221\n2117.379\t7.740221\n2121.4049999999997\t7.740221\n2125.431\t7.740221\n2129.457\t7.740221\n2133.483\t7.740221\n2137.509\t7.740221\n2141.535\t7.740221\n2145.561\t7.740221\n2149.587\t7.740221\n2153.613\t7.740221\n2157.639\t7.740221\n2161.665\t7.740221\n2165.691\t7.740221\n2169.717\t7.740221\n2173.743\t7.740221\n2177.7690000000002\t7.740221\n2181.795\t7.740221\n2185.821\t7.740221\n2189.8469999999998\t7.740221\n2193.873\t7.740221\n2197.899\t7.740221\n2201.925\t7.740221\n2205.951\t7.740221\n2209.977\t7.740221\n2214.003\t7.740221\n2218.029\t7.740221\n2222.055\t7.740221\n2226.081\t7.740221\n2230.107\t7.740221\n2234.133\t7.740221\n2238.159\t7.740221\n2242.185\t7.740221\n2246.2110000000002\t7.740221\n2250.237\t7.740221\n2254.263\t7.740221\n2258.2889999999998\t7.740221\n2262.315\t7.740221\n2266.341\t7.740221\n2270.367\t7.740221\n2274.393\t7.740221\n2278.419\t7.740221\n2282.4449999999997\t7.740221\n2286.471\t7.740221\n2290.4970000000003\t7.740221\n2294.523\t7.740221\n2298.549\t7.740221\n2302.575\t7.740221\n2306.6009999999997\t7.740221\n2310.627\t7.740221\n2314.6530000000002\t7.740221\n2318.679\t7.740221\n2322.705\t7.740221\n2326.7309999999998\t7.740221\n2330.757\t7.740221\n2334.783\t7.740221\n2338.809\t7.740221\n2342.835\t7.740221\n2346.861\t7.740221\n2350.8869999999997\t7.740221\n2354.913\t7.740221\n2358.9390000000003\t7.740221\n2362.965\t7.740221\n2366.991\t7.740221\n2371.017\t7.740221\n2375.0429999999997\t7.740221\n2379.069\t7.740221\n2383.0950000000003\t7.740221\n2387.121\t7.740221\n2391.147\t7.740221\n2395.173\t7.740221\n2399.199\t7.740221\n2403.225\t7.740221\n2407.251\t7.740221\n2411.277\t7.740221\n2415.303\t7.740221\n2419.3289999999997\t7.740221\n2423.355\t7.740221\n2427.3810000000003\t7.740221\n2431.407\t7.740221\n2435.433\t7.740221\n2439.459\t7.740221\n2443.4849999999997\t7.740221\n2447.511\t7.740221\n2451.5370000000003\t7.740221\n2455.563\t7.740221\n2459.589\t7.740221\n2463.615\t7.740221\n2467.641\t7.740221\n2471.667\t7.740221\n2475.693\t7.740221\n2479.719\t7.740221\n2483.745\t7.740221\n"
    # assert: Voigt
    convolution_type = 5  # "Voigt"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Voigt profile\ndestination_wavelength_nm\tdestination_width_Gauss\tdestination_width_Lorentz\n1227.633\t7.740221\t3.8701105\n1231.659\t7.740221\t3.8701105\n1235.685\t7.740221\t3.8701105\n1239.711\t7.740221\t3.8701105\n1243.737\t7.740221\t3.8701105\n1247.7630000000001\t7.740221\t3.8701105\n1251.789\t7.740221\t3.8701105\n1255.815\t7.740221\t3.8701105\n1259.8410000000001\t7.740221\t3.8701105\n1263.867\t7.740221\t3.8701105\n1267.893\t7.740221\t3.8701105\n1271.919\t7.740221\t3.8701105\n1275.945\t7.740221\t3.8701105\n1279.971\t7.740221\t3.8701105\n1283.997\t7.740221\t3.8701105\n1288.0230000000001\t7.740221\t3.8701105\n1292.049\t7.740221\t3.8701105\n1296.075\t7.740221\t3.8701105\n1300.101\t7.740221\t3.8701105\n1304.127\t7.740221\t3.8701105\n1308.153\t7.740221\t3.8701105\n1312.179\t7.740221\t3.8701105\n1316.205\t7.740221\t3.8701105\n1320.231\t7.740221\t3.8701105\n1324.257\t7.740221\t3.8701105\n1328.2830000000001\t7.740221\t3.8701105\n1332.309\t7.740221\t3.8701105\n1336.335\t7.740221\t3.8701105\n1340.361\t7.740221\t3.8701105\n1344.387\t7.740221\t3.8701105\n1348.413\t7.740221\t3.8701105\n1352.439\t7.740221\t3.8701105\n1356.4650000000001\t7.740221\t3.8701105\n1360.491\t7.740221\t3.8701105\n1364.517\t7.740221\t3.8701105\n1368.5430000000001\t7.740221\t3.8701105\n1372.569\t7.740221\t3.8701105\n1376.595\t7.740221\t3.8701105\n1380.621\t7.740221\t3.8701105\n1384.647\t7.740221\t3.8701105\n1388.673\t7.740221\t3.8701105\n1392.699\t7.740221\t3.8701105\n1396.725\t7.740221\t3.8701105\n1400.751\t7.740221\t3.8701105\n1404.777\t7.740221\t3.8701105\n1408.803\t7.740221\t3.8701105\n1412.829\t7.740221\t3.8701105\n1416.855\t7.740221\t3.8701105\n1420.881\t7.740221\t3.8701105\n1424.9070000000002\t7.740221\t3.8701105\n1428.933\t7.740221\t3.8701105\n1432.959\t7.740221\t3.8701105\n1436.9850000000001\t7.740221\t3.8701105\n1441.011\t7.740221\t3.8701105\n1445.037\t7.740221\t3.8701105\n1449.063\t7.740221\t3.8701105\n1453.089\t7.740221\t3.8701105\n1457.115\t7.740221\t3.8701105\n1461.141\t7.740221\t3.8701105\n1465.167\t7.740221\t3.8701105\n1469.193\t7.740221\t3.8701105\n1473.219\t7.740221\t3.8701105\n1477.2450000000001\t7.740221\t3.8701105\n1481.271\t7.740221\t3.8701105\n1485.297\t7.740221\t3.8701105\n1489.323\t7.740221\t3.8701105\n1493.3490000000002\t7.740221\t3.8701105\n1497.375\t7.740221\t3.8701105\n1501.401\t7.740221\t3.8701105\n1505.4270000000001\t7.740221\t3.8701105\n1509.453\t7.740221\t3.8701105\n1513.479\t7.740221\t3.8701105\n1517.505\t7.740221\t3.8701105\n1521.531\t7.740221\t3.8701105\n1525.557\t7.740221\t3.8701105\n1529.583\t7.740221\t3.8701105\n1533.609\t7.740221\t3.8701105\n1537.635\t7.740221\t3.8701105\n1541.661\t7.740221\t3.8701105\n1545.687\t7.740221\t3.8701105\n1549.713\t7.740221\t3.8701105\n1553.739\t7.740221\t3.8701105\n1557.765\t7.740221\t3.8701105\n1561.791\t7.740221\t3.8701105\n1565.817\t7.740221\t3.8701105\n1569.843\t7.740221\t3.8701105\n1573.8690000000001\t7.740221\t3.8701105\n1577.895\t7.740221\t3.8701105\n1581.921\t7.740221\t3.8701105\n1585.9470000000001\t7.740221\t3.8701105\n1589.973\t7.740221\t3.8701105\n1593.999\t7.740221\t3.8701105\n1598.025\t7.740221\t3.8701105\n1602.051\t7.740221\t3.8701105\n1606.077\t7.740221\t3.8701105\n1610.103\t7.740221\t3.8701105\n1614.129\t7.740221\t3.8701105\n1618.155\t7.740221\t3.8701105\n1622.181\t7.740221\t3.8701105\n1626.2069999999999\t7.740221\t3.8701105\n1630.233\t7.740221\t3.8701105\n1634.259\t7.740221\t3.8701105\n1638.285\t7.740221\t3.8701105\n1642.3110000000001\t7.740221\t3.8701105\n1646.337\t7.740221\t3.8701105\n1650.363\t7.740221\t3.8701105\n1654.3890000000001\t7.740221\t3.8701105\n1658.415\t7.740221\t3.8701105\n1662.441\t7.740221\t3.8701105\n1666.467\t7.740221\t3.8701105\n1670.493\t7.740221\t3.8701105\n1674.519\t7.740221\t3.8701105\n1678.545\t7.740221\t3.8701105\n1682.571\t7.740221\t3.8701105\n1686.597\t7.740221\t3.8701105\n1690.623\t7.740221\t3.8701105\n1694.649\t7.740221\t3.8701105\n1698.675\t7.740221\t3.8701105\n1702.701\t7.740221\t3.8701105\n1706.727\t7.740221\t3.8701105\n1710.7530000000002\t7.740221\t3.8701105\n1714.779\t7.740221\t3.8701105\n1718.805\t7.740221\t3.8701105\n1722.8310000000001\t7.740221\t3.8701105\n1726.857\t7.740221\t3.8701105\n1730.883\t7.740221\t3.8701105\n1734.909\t7.740221\t3.8701105\n1738.935\t7.740221\t3.8701105\n1742.961\t7.740221\t3.8701105\n1746.987\t7.740221\t3.8701105\n1751.013\t7.740221\t3.8701105\n1755.039\t7.740221\t3.8701105\n1759.065\t7.740221\t3.8701105\n1763.091\t7.740221\t3.8701105\n1767.117\t7.740221\t3.8701105\n1771.143\t7.740221\t3.8701105\n1775.1689999999999\t7.740221\t3.8701105\n1779.1950000000002\t7.740221\t3.8701105\n1783.221\t7.740221\t3.8701105\n1787.2469999999998\t7.740221\t3.8701105\n1791.2730000000001\t7.740221\t3.8701105\n1795.299\t7.740221\t3.8701105\n1799.325\t7.740221\t3.8701105\n1803.351\t7.740221\t3.8701105\n1807.377\t7.740221\t3.8701105\n1811.403\t7.740221\t3.8701105\n1815.429\t7.740221\t3.8701105\n1819.455\t7.740221\t3.8701105\n1823.481\t7.740221\t3.8701105\n1827.507\t7.740221\t3.8701105\n1831.533\t7.740221\t3.8701105\n1835.559\t7.740221\t3.8701105\n1839.585\t7.740221\t3.8701105\n1843.6109999999999\t7.740221\t3.8701105\n1847.6370000000002\t7.740221\t3.8701105\n1851.663\t7.740221\t3.8701105\n1855.6889999999999\t7.740221\t3.8701105\n1859.7150000000001\t7.740221\t3.8701105\n1863.741\t7.740221\t3.8701105\n1867.767\t7.740221\t3.8701105\n1871.7930000000001\t7.740221\t3.8701105\n1875.819\t7.740221\t3.8701105\n1879.845\t7.740221\t3.8701105\n1883.871\t7.740221\t3.8701105\n1887.897\t7.740221\t3.8701105\n1891.923\t7.740221\t3.8701105\n1895.949\t7.740221\t3.8701105\n1899.975\t7.740221\t3.8701105\n1904.001\t7.740221\t3.8701105\n1908.027\t7.740221\t3.8701105\n1912.0529999999999\t7.740221\t3.8701105\n1916.079\t7.740221\t3.8701105\n1920.105\t7.740221\t3.8701105\n1924.1309999999999\t7.740221\t3.8701105\n1928.1570000000002\t7.740221\t3.8701105\n1932.183\t7.740221\t3.8701105\n1936.209\t7.740221\t3.8701105\n1940.2350000000001\t7.740221\t3.8701105\n1944.261\t7.740221\t3.8701105\n1948.287\t7.740221\t3.8701105\n1952.313\t7.740221\t3.8701105\n1956.339\t7.740221\t3.8701105\n1960.365\t7.740221\t3.8701105\n1964.391\t7.740221\t3.8701105\n1968.417\t7.740221\t3.8701105\n1972.443\t7.740221\t3.8701105\n1976.469\t7.740221\t3.8701105\n1980.495\t7.740221\t3.8701105\n1984.521\t7.740221\t3.8701105\n1988.547\t7.740221\t3.8701105\n1992.5729999999999\t7.740221\t3.8701105\n1996.5990000000002\t7.740221\t3.8701105\n2000.625\t7.740221\t3.8701105\n2004.6509999999998\t7.740221\t3.8701105\n2008.6770000000001\t7.740221\t3.8701105\n2012.703\t7.740221\t3.8701105\n2016.729\t7.740221\t3.8701105\n2020.755\t7.740221\t3.8701105\n2024.781\t7.740221\t3.8701105\n2028.807\t7.740221\t3.8701105\n2032.833\t7.740221\t3.8701105\n2036.859\t7.740221\t3.8701105\n2040.885\t7.740221\t3.8701105\n2044.911\t7.740221\t3.8701105\n2048.937\t7.740221\t3.8701105\n2052.9629999999997\t7.740221\t3.8701105\n2056.989\t7.740221\t3.8701105\n2061.015\t7.740221\t3.8701105\n2065.041\t7.740221\t3.8701105\n2069.067\t7.740221\t3.8701105\n2073.093\t7.740221\t3.8701105\n2077.119\t7.740221\t3.8701105\n2081.145\t7.740221\t3.8701105\n2085.1710000000003\t7.740221\t3.8701105\n2089.197\t7.740221\t3.8701105\n2093.223\t7.740221\t3.8701105\n2097.249\t7.740221\t3.8701105\n2101.275\t7.740221\t3.8701105\n2105.301\t7.740221\t3.8701105\n2109.327\t7.740221\t3.8701105\n2113.353\t7.740221\t3.8701105\n2117.379\t7.740221\t3.8701105\n2121.4049999999997\t7.740221\t3.8701105\n2125.431\t7.740221\t3.8701105\n2129.457\t7.740221\t3.8701105\n2133.483\t7.740221\t3.8701105\n2137.509\t7.740221\t3.8701105\n2141.535\t7.740221\t3.8701105\n2145.561\t7.740221\t3.8701105\n2149.587\t7.740221\t3.8701105\n2153.613\t7.740221\t3.8701105\n2157.639\t7.740221\t3.8701105\n2161.665\t7.740221\t3.8701105\n2165.691\t7.740221\t3.8701105\n2169.717\t7.740221\t3.8701105\n2173.743\t7.740221\t3.8701105\n2177.7690000000002\t7.740221\t3.8701105\n2181.795\t7.740221\t3.8701105\n2185.821\t7.740221\t3.8701105\n2189.8469999999998\t7.740221\t3.8701105\n2193.873\t7.740221\t3.8701105\n2197.899\t7.740221\t3.8701105\n2201.925\t7.740221\t3.8701105\n2205.951\t7.740221\t3.8701105\n2209.977\t7.740221\t3.8701105\n2214.003\t7.740221\t3.8701105\n2218.029\t7.740221\t3.8701105\n2222.055\t7.740221\t3.8701105\n2226.081\t7.740221\t3.8701105\n2230.107\t7.740221\t3.8701105\n2234.133\t7.740221\t3.8701105\n2238.159\t7.740221\t3.8701105\n2242.185\t7.740221\t3.8701105\n2246.2110000000002\t7.740221\t3.8701105\n2250.237\t7.740221\t3.8701105\n2254.263\t7.740221\t3.8701105\n2258.2889999999998\t7.740221\t3.8701105\n2262.315\t7.740221\t3.8701105\n2266.341\t7.740221\t3.8701105\n2270.367\t7.740221\t3.8701105\n2274.393\t7.740221\t3.8701105\n2278.419\t7.740221\t3.8701105\n2282.4449999999997\t7.740221\t3.8701105\n2286.471\t7.740221\t3.8701105\n2290.4970000000003\t7.740221\t3.8701105\n2294.523\t7.740221\t3.8701105\n2298.549\t7.740221\t3.8701105\n2302.575\t7.740221\t3.8701105\n2306.6009999999997\t7.740221\t3.8701105\n2310.627\t7.740221\t3.8701105\n2314.6530000000002\t7.740221\t3.8701105\n2318.679\t7.740221\t3.8701105\n2322.705\t7.740221\t3.8701105\n2326.7309999999998\t7.740221\t3.8701105\n2330.757\t7.740221\t3.8701105\n2334.783\t7.740221\t3.8701105\n2338.809\t7.740221\t3.8701105\n2342.835\t7.740221\t3.8701105\n2346.861\t7.740221\t3.8701105\n2350.8869999999997\t7.740221\t3.8701105\n2354.913\t7.740221\t3.8701105\n2358.9390000000003\t7.740221\t3.8701105\n2362.965\t7.740221\t3.8701105\n2366.991\t7.740221\t3.8701105\n2371.017\t7.740221\t3.8701105\n2375.0429999999997\t7.740221\t3.8701105\n2379.069\t7.740221\t3.8701105\n2383.0950000000003\t7.740221\t3.8701105\n2387.121\t7.740221\t3.8701105\n2391.147\t7.740221\t3.8701105\n2395.173\t7.740221\t3.8701105\n2399.199\t7.740221\t3.8701105\n2403.225\t7.740221\t3.8701105\n2407.251\t7.740221\t3.8701105\n2411.277\t7.740221\t3.8701105\n2415.303\t7.740221\t3.8701105\n2419.3289999999997\t7.740221\t3.8701105\n2423.355\t7.740221\t3.8701105\n2427.3810000000003\t7.740221\t3.8701105\n2431.407\t7.740221\t3.8701105\n2435.433\t7.740221\t3.8701105\n2439.459\t7.740221\t3.8701105\n2443.4849999999997\t7.740221\t3.8701105\n2447.511\t7.740221\t3.8701105\n2451.5370000000003\t7.740221\t3.8701105\n2455.563\t7.740221\t3.8701105\n2459.589\t7.740221\t3.8701105\n2463.615\t7.740221\t3.8701105\n2467.641\t7.740221\t3.8701105\n2471.667\t7.740221\t3.8701105\n2475.693\t7.740221\t3.8701105\n2479.719\t7.740221\t3.8701105\n2483.745\t7.740221\t3.8701105\n"
    # assert: Gauss + Lorentz
    convolution_type = 6  # "Gauss + Lorentz"
    win.conv_type.setCurrentIndex(convolution_type)
    assert win.prepare_destination_wavelength_to_export() == "convolution function: Gauss & Lorentz sum, Gauss function part: 0.5\ndestination_wavelength_nm\tdestination_width_Gauss\tdestination_width_Lorentz\n1227.633\t7.740221\t3.8701105\n1231.659\t7.740221\t3.8701105\n1235.685\t7.740221\t3.8701105\n1239.711\t7.740221\t3.8701105\n1243.737\t7.740221\t3.8701105\n1247.7630000000001\t7.740221\t3.8701105\n1251.789\t7.740221\t3.8701105\n1255.815\t7.740221\t3.8701105\n1259.8410000000001\t7.740221\t3.8701105\n1263.867\t7.740221\t3.8701105\n1267.893\t7.740221\t3.8701105\n1271.919\t7.740221\t3.8701105\n1275.945\t7.740221\t3.8701105\n1279.971\t7.740221\t3.8701105\n1283.997\t7.740221\t3.8701105\n1288.0230000000001\t7.740221\t3.8701105\n1292.049\t7.740221\t3.8701105\n1296.075\t7.740221\t3.8701105\n1300.101\t7.740221\t3.8701105\n1304.127\t7.740221\t3.8701105\n1308.153\t7.740221\t3.8701105\n1312.179\t7.740221\t3.8701105\n1316.205\t7.740221\t3.8701105\n1320.231\t7.740221\t3.8701105\n1324.257\t7.740221\t3.8701105\n1328.2830000000001\t7.740221\t3.8701105\n1332.309\t7.740221\t3.8701105\n1336.335\t7.740221\t3.8701105\n1340.361\t7.740221\t3.8701105\n1344.387\t7.740221\t3.8701105\n1348.413\t7.740221\t3.8701105\n1352.439\t7.740221\t3.8701105\n1356.4650000000001\t7.740221\t3.8701105\n1360.491\t7.740221\t3.8701105\n1364.517\t7.740221\t3.8701105\n1368.5430000000001\t7.740221\t3.8701105\n1372.569\t7.740221\t3.8701105\n1376.595\t7.740221\t3.8701105\n1380.621\t7.740221\t3.8701105\n1384.647\t7.740221\t3.8701105\n1388.673\t7.740221\t3.8701105\n1392.699\t7.740221\t3.8701105\n1396.725\t7.740221\t3.8701105\n1400.751\t7.740221\t3.8701105\n1404.777\t7.740221\t3.8701105\n1408.803\t7.740221\t3.8701105\n1412.829\t7.740221\t3.8701105\n1416.855\t7.740221\t3.8701105\n1420.881\t7.740221\t3.8701105\n1424.9070000000002\t7.740221\t3.8701105\n1428.933\t7.740221\t3.8701105\n1432.959\t7.740221\t3.8701105\n1436.9850000000001\t7.740221\t3.8701105\n1441.011\t7.740221\t3.8701105\n1445.037\t7.740221\t3.8701105\n1449.063\t7.740221\t3.8701105\n1453.089\t7.740221\t3.8701105\n1457.115\t7.740221\t3.8701105\n1461.141\t7.740221\t3.8701105\n1465.167\t7.740221\t3.8701105\n1469.193\t7.740221\t3.8701105\n1473.219\t7.740221\t3.8701105\n1477.2450000000001\t7.740221\t3.8701105\n1481.271\t7.740221\t3.8701105\n1485.297\t7.740221\t3.8701105\n1489.323\t7.740221\t3.8701105\n1493.3490000000002\t7.740221\t3.8701105\n1497.375\t7.740221\t3.8701105\n1501.401\t7.740221\t3.8701105\n1505.4270000000001\t7.740221\t3.8701105\n1509.453\t7.740221\t3.8701105\n1513.479\t7.740221\t3.8701105\n1517.505\t7.740221\t3.8701105\n1521.531\t7.740221\t3.8701105\n1525.557\t7.740221\t3.8701105\n1529.583\t7.740221\t3.8701105\n1533.609\t7.740221\t3.8701105\n1537.635\t7.740221\t3.8701105\n1541.661\t7.740221\t3.8701105\n1545.687\t7.740221\t3.8701105\n1549.713\t7.740221\t3.8701105\n1553.739\t7.740221\t3.8701105\n1557.765\t7.740221\t3.8701105\n1561.791\t7.740221\t3.8701105\n1565.817\t7.740221\t3.8701105\n1569.843\t7.740221\t3.8701105\n1573.8690000000001\t7.740221\t3.8701105\n1577.895\t7.740221\t3.8701105\n1581.921\t7.740221\t3.8701105\n1585.9470000000001\t7.740221\t3.8701105\n1589.973\t7.740221\t3.8701105\n1593.999\t7.740221\t3.8701105\n1598.025\t7.740221\t3.8701105\n1602.051\t7.740221\t3.8701105\n1606.077\t7.740221\t3.8701105\n1610.103\t7.740221\t3.8701105\n1614.129\t7.740221\t3.8701105\n1618.155\t7.740221\t3.8701105\n1622.181\t7.740221\t3.8701105\n1626.2069999999999\t7.740221\t3.8701105\n1630.233\t7.740221\t3.8701105\n1634.259\t7.740221\t3.8701105\n1638.285\t7.740221\t3.8701105\n1642.3110000000001\t7.740221\t3.8701105\n1646.337\t7.740221\t3.8701105\n1650.363\t7.740221\t3.8701105\n1654.3890000000001\t7.740221\t3.8701105\n1658.415\t7.740221\t3.8701105\n1662.441\t7.740221\t3.8701105\n1666.467\t7.740221\t3.8701105\n1670.493\t7.740221\t3.8701105\n1674.519\t7.740221\t3.8701105\n1678.545\t7.740221\t3.8701105\n1682.571\t7.740221\t3.8701105\n1686.597\t7.740221\t3.8701105\n1690.623\t7.740221\t3.8701105\n1694.649\t7.740221\t3.8701105\n1698.675\t7.740221\t3.8701105\n1702.701\t7.740221\t3.8701105\n1706.727\t7.740221\t3.8701105\n1710.7530000000002\t7.740221\t3.8701105\n1714.779\t7.740221\t3.8701105\n1718.805\t7.740221\t3.8701105\n1722.8310000000001\t7.740221\t3.8701105\n1726.857\t7.740221\t3.8701105\n1730.883\t7.740221\t3.8701105\n1734.909\t7.740221\t3.8701105\n1738.935\t7.740221\t3.8701105\n1742.961\t7.740221\t3.8701105\n1746.987\t7.740221\t3.8701105\n1751.013\t7.740221\t3.8701105\n1755.039\t7.740221\t3.8701105\n1759.065\t7.740221\t3.8701105\n1763.091\t7.740221\t3.8701105\n1767.117\t7.740221\t3.8701105\n1771.143\t7.740221\t3.8701105\n1775.1689999999999\t7.740221\t3.8701105\n1779.1950000000002\t7.740221\t3.8701105\n1783.221\t7.740221\t3.8701105\n1787.2469999999998\t7.740221\t3.8701105\n1791.2730000000001\t7.740221\t3.8701105\n1795.299\t7.740221\t3.8701105\n1799.325\t7.740221\t3.8701105\n1803.351\t7.740221\t3.8701105\n1807.377\t7.740221\t3.8701105\n1811.403\t7.740221\t3.8701105\n1815.429\t7.740221\t3.8701105\n1819.455\t7.740221\t3.8701105\n1823.481\t7.740221\t3.8701105\n1827.507\t7.740221\t3.8701105\n1831.533\t7.740221\t3.8701105\n1835.559\t7.740221\t3.8701105\n1839.585\t7.740221\t3.8701105\n1843.6109999999999\t7.740221\t3.8701105\n1847.6370000000002\t7.740221\t3.8701105\n1851.663\t7.740221\t3.8701105\n1855.6889999999999\t7.740221\t3.8701105\n1859.7150000000001\t7.740221\t3.8701105\n1863.741\t7.740221\t3.8701105\n1867.767\t7.740221\t3.8701105\n1871.7930000000001\t7.740221\t3.8701105\n1875.819\t7.740221\t3.8701105\n1879.845\t7.740221\t3.8701105\n1883.871\t7.740221\t3.8701105\n1887.897\t7.740221\t3.8701105\n1891.923\t7.740221\t3.8701105\n1895.949\t7.740221\t3.8701105\n1899.975\t7.740221\t3.8701105\n1904.001\t7.740221\t3.8701105\n1908.027\t7.740221\t3.8701105\n1912.0529999999999\t7.740221\t3.8701105\n1916.079\t7.740221\t3.8701105\n1920.105\t7.740221\t3.8701105\n1924.1309999999999\t7.740221\t3.8701105\n1928.1570000000002\t7.740221\t3.8701105\n1932.183\t7.740221\t3.8701105\n1936.209\t7.740221\t3.8701105\n1940.2350000000001\t7.740221\t3.8701105\n1944.261\t7.740221\t3.8701105\n1948.287\t7.740221\t3.8701105\n1952.313\t7.740221\t3.8701105\n1956.339\t7.740221\t3.8701105\n1960.365\t7.740221\t3.8701105\n1964.391\t7.740221\t3.8701105\n1968.417\t7.740221\t3.8701105\n1972.443\t7.740221\t3.8701105\n1976.469\t7.740221\t3.8701105\n1980.495\t7.740221\t3.8701105\n1984.521\t7.740221\t3.8701105\n1988.547\t7.740221\t3.8701105\n1992.5729999999999\t7.740221\t3.8701105\n1996.5990000000002\t7.740221\t3.8701105\n2000.625\t7.740221\t3.8701105\n2004.6509999999998\t7.740221\t3.8701105\n2008.6770000000001\t7.740221\t3.8701105\n2012.703\t7.740221\t3.8701105\n2016.729\t7.740221\t3.8701105\n2020.755\t7.740221\t3.8701105\n2024.781\t7.740221\t3.8701105\n2028.807\t7.740221\t3.8701105\n2032.833\t7.740221\t3.8701105\n2036.859\t7.740221\t3.8701105\n2040.885\t7.740221\t3.8701105\n2044.911\t7.740221\t3.8701105\n2048.937\t7.740221\t3.8701105\n2052.9629999999997\t7.740221\t3.8701105\n2056.989\t7.740221\t3.8701105\n2061.015\t7.740221\t3.8701105\n2065.041\t7.740221\t3.8701105\n2069.067\t7.740221\t3.8701105\n2073.093\t7.740221\t3.8701105\n2077.119\t7.740221\t3.8701105\n2081.145\t7.740221\t3.8701105\n2085.1710000000003\t7.740221\t3.8701105\n2089.197\t7.740221\t3.8701105\n2093.223\t7.740221\t3.8701105\n2097.249\t7.740221\t3.8701105\n2101.275\t7.740221\t3.8701105\n2105.301\t7.740221\t3.8701105\n2109.327\t7.740221\t3.8701105\n2113.353\t7.740221\t3.8701105\n2117.379\t7.740221\t3.8701105\n2121.4049999999997\t7.740221\t3.8701105\n2125.431\t7.740221\t3.8701105\n2129.457\t7.740221\t3.8701105\n2133.483\t7.740221\t3.8701105\n2137.509\t7.740221\t3.8701105\n2141.535\t7.740221\t3.8701105\n2145.561\t7.740221\t3.8701105\n2149.587\t7.740221\t3.8701105\n2153.613\t7.740221\t3.8701105\n2157.639\t7.740221\t3.8701105\n2161.665\t7.740221\t3.8701105\n2165.691\t7.740221\t3.8701105\n2169.717\t7.740221\t3.8701105\n2173.743\t7.740221\t3.8701105\n2177.7690000000002\t7.740221\t3.8701105\n2181.795\t7.740221\t3.8701105\n2185.821\t7.740221\t3.8701105\n2189.8469999999998\t7.740221\t3.8701105\n2193.873\t7.740221\t3.8701105\n2197.899\t7.740221\t3.8701105\n2201.925\t7.740221\t3.8701105\n2205.951\t7.740221\t3.8701105\n2209.977\t7.740221\t3.8701105\n2214.003\t7.740221\t3.8701105\n2218.029\t7.740221\t3.8701105\n2222.055\t7.740221\t3.8701105\n2226.081\t7.740221\t3.8701105\n2230.107\t7.740221\t3.8701105\n2234.133\t7.740221\t3.8701105\n2238.159\t7.740221\t3.8701105\n2242.185\t7.740221\t3.8701105\n2246.2110000000002\t7.740221\t3.8701105\n2250.237\t7.740221\t3.8701105\n2254.263\t7.740221\t3.8701105\n2258.2889999999998\t7.740221\t3.8701105\n2262.315\t7.740221\t3.8701105\n2266.341\t7.740221\t3.8701105\n2270.367\t7.740221\t3.8701105\n2274.393\t7.740221\t3.8701105\n2278.419\t7.740221\t3.8701105\n2282.4449999999997\t7.740221\t3.8701105\n2286.471\t7.740221\t3.8701105\n2290.4970000000003\t7.740221\t3.8701105\n2294.523\t7.740221\t3.8701105\n2298.549\t7.740221\t3.8701105\n2302.575\t7.740221\t3.8701105\n2306.6009999999997\t7.740221\t3.8701105\n2310.627\t7.740221\t3.8701105\n2314.6530000000002\t7.740221\t3.8701105\n2318.679\t7.740221\t3.8701105\n2322.705\t7.740221\t3.8701105\n2326.7309999999998\t7.740221\t3.8701105\n2330.757\t7.740221\t3.8701105\n2334.783\t7.740221\t3.8701105\n2338.809\t7.740221\t3.8701105\n2342.835\t7.740221\t3.8701105\n2346.861\t7.740221\t3.8701105\n2350.8869999999997\t7.740221\t3.8701105\n2354.913\t7.740221\t3.8701105\n2358.9390000000003\t7.740221\t3.8701105\n2362.965\t7.740221\t3.8701105\n2366.991\t7.740221\t3.8701105\n2371.017\t7.740221\t3.8701105\n2375.0429999999997\t7.740221\t3.8701105\n2379.069\t7.740221\t3.8701105\n2383.0950000000003\t7.740221\t3.8701105\n2387.121\t7.740221\t3.8701105\n2391.147\t7.740221\t3.8701105\n2395.173\t7.740221\t3.8701105\n2399.199\t7.740221\t3.8701105\n2403.225\t7.740221\t3.8701105\n2407.251\t7.740221\t3.8701105\n2411.277\t7.740221\t3.8701105\n2415.303\t7.740221\t3.8701105\n2419.3289999999997\t7.740221\t3.8701105\n2423.355\t7.740221\t3.8701105\n2427.3810000000003\t7.740221\t3.8701105\n2431.407\t7.740221\t3.8701105\n2435.433\t7.740221\t3.8701105\n2439.459\t7.740221\t3.8701105\n2443.4849999999997\t7.740221\t3.8701105\n2447.511\t7.740221\t3.8701105\n2451.5370000000003\t7.740221\t3.8701105\n2455.563\t7.740221\t3.8701105\n2459.589\t7.740221\t3.8701105\n2463.615\t7.740221\t3.8701105\n2467.641\t7.740221\t3.8701105\n2471.667\t7.740221\t3.8701105\n2475.693\t7.740221\t3.8701105\n2479.719\t7.740221\t3.8701105\n2483.745\t7.740221\t3.8701105\n"
    win.close()


# Fool problems
def test_monocolumn():
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/dstntn_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    # conv_core calc
    my_conv = conv_core.ConvolutionCore()
    my_conv.tests_are_running = True
    my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(spectrum_unit, spectrum_file_path, spectrum_wavelength_column, spectrum_intensity_column, "", np.NAN)
    my_conv.destination_setter_from_file(destination_unit, destination_file_path, destination_wavelength_column)
    my_conv.convolution_setter_width_from_file(convolution_type - 1, convolution_gauss_ratio, convolution_truncation, convolution_extrapolation_type, convolution_file_path, convolution_width_1_column, np.NAN)
    my_conv.convolution_stack()
    result = my_conv.destination_intensity_getter()
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), result, 10 ** 0)
    win.close()


def test_empty_files():
    # spectrum
    spectrum_file_path = "NH_case/empty.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/dstntn_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), np.zeros(0), 10 ** 0)
    win.close()
    # destination
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/empty.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 1  # "Gauss function"
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/ref_micron.txt"
    convolution_width_1_column = 1
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), np.zeros(0), 10 ** 0)
    win.close()
    # convolution
    spectrum_file_path = "NH_case/spectrum_cm.txt"
    spectrum_unit = "cm-1"
    spectrum_wavelength_column = 0
    spectrum_intensity_column = 1
    destination_file_path = "NH_case/dstntn_micron.txt"
    destination_unit = "micron"
    destination_wavelength_column = 0
    convolution_extrapolation_type = 0  # "zeros"
    convolution_type = 3  # trapeze
    convolution_gauss_ratio = 0
    convolution_truncation = 10
    convolution_file_path = "NH_case/empty.txt"
    convolution_width_1_column = 1
    convolution_width_2_column = 2
    # sdc, dcs
    win = main.ConvolutionMainW()
    win.tests_are_running = True
    ## sdc
    ## spectrum
    win.file_select_action(spectrum_file_path, "spectrum")
    win.ui.spctrm_unit.setCurrentIndex(1)
    win.ui.spctrm_wlth_clm.setCurrentIndex(spectrum_wavelength_column + 1)
    win.ui.spctrm_inty_clm.setCurrentIndex(spectrum_intensity_column + 1)
    ## destination
    win.ui.dstntn_unit.setCurrentIndex(2)
    win.ui.dstntn_tab.setCurrentIndex(0)
    win.file_select_action(destination_file_path, "destination")
    win.ui.dstntn_wlth_clm.setCurrentIndex(destination_wavelength_column + 1)
    ## convolution
    win.conv_type.setCurrentIndex(convolution_type)
    win.conv_truncation.setValue(convolution_truncation)
    win.conv_extrap.setCurrentIndex(convolution_extrapolation_type)
    win.ui.conv_tab.setCurrentIndex(0)
    win.file_select_action(convolution_file_path, "convolution")
    win.ui.conv_wdth_1_clm.setCurrentIndex(convolution_width_1_column + 1)
    win.ui.conv_wdth_2_clm.setCurrentIndex(convolution_width_2_column + 1)
    ## calc
    win.convolution_calc()
    ## assert
    assert list_compare(win.my_conv.destination_intensity_getter(), np.zeros(0), 10 ** 0)
    win.close()
