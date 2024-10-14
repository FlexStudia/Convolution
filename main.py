# coding: utf-8

"""
    This is the  code of the interface.
    For calculations, it relies on conv_core.py, to which the task of convolution calculation is delegated.
    Here is the PyQt5-based interface only.
    If you are developing your own interface, you should work with conv_core.py and use this code only as example.
"""

# PACKAGES
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QLabel, QComboBox, QAction
from PyQt5.QtCore import Qt, QSettings, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys
import os
import numpy as np
import pyqtgraph as pg
from functools import partial

# TEMPLATES
from templates.mw import Ui_MainWindow as Ui_MainWindow
from templates.ew import Ui_Dialog as Ui_ExportWindow
from templates.help import Ui_QDialog as Ui_HelpWindow

# MODULES
import conv_core
from tools.array_tools import is_array_empty
from tools.data_pars import DataPars as DataPars
from tools.str_and_float import float_to_str, is_int, is_float
from QLabelClickable import QLabelClickable as QLabelClickable
from QLineEditNumber import QLineEditNumber as QLineEditNumber

# PRESETS
from presets import LEISA_New_Horizons
from presets import SuperCam_VIS

# GLOBALS
version = "1.8.1"
copyright = "<a href='https:www.gnu.org/licenses/gpl-3.0.html'>The GNU General Public License v3.0</a>"
author_mail = "<a href='mailto: flex.studia.dev@gmail.com'>flex.studia.dev@gmail.com</a>"
bug_support_mail = "<a href='mailto: flex.studia.help@gmail.com'>flex.studia.help@gmail.com</a>"
github_url = "https:github.com/FlexStudia/Convolution"
__app_name__ = "Spectrum convolution"
__org_name__ = "Flex Studia Dev"
__org_site__ = github_url
settings = QSettings(__org_name__, __app_name__)

# styles
INPUTS_STYLE = {
    # general
    "color_normal": "#007BA0",
    "color_normal_hover": "#006685",
    "color_error": "#DB0800",
    "color_error_hover": "#D50700",
    "background_error": "#FFF0F0",
    "background_error_hover": "#FFEBEA",
    "border_radius": "5px",
    "border_width_normal": "1px",
    "border_width_error": "2px",
    "border_width_error_hover": "3px",
    "padding_normal": "2px",
    # buttons
    "btn_color_background_normal": "#D0E0E0",
    "btn_color_background_normal_hover": "#CBDADA",
    "btn_padding_big": "15px",
    # label
    "lbl_color_normal" : "#000000",
    "lbl_color_error" : "#D80700",
    "lbl_font-size": 8,
    # input fields
    "field_color_background_normal": "#FFFFFF",
    "field_color_background_normal_hover": "#F3F3F3",
    "input_font_size": 10,
    "input_font_size_px": "12px",
    "field_min-size": 0,
    "field_max-size": 16777215,
    "filed-size_medium": 180,
    "filed-size_large": 200,
}
BTN_BIG = ("QPushButton{border: %(border_width_normal)s solid %(color_normal)s; border-radius: %(border_radius)s; background: %(btn_color_background_normal)s; padding: %(btn_padding_big)s;}"
           "QPushButton:hover{border: %(border_width_error)s solid %(color_normal_hover)s; border-radius: %(border_radius)s; background: %(btn_color_background_normal_hover)s; padding: %(btn_padding_big)s;}" % INPUTS_STYLE)
BTN_NORMAL = ("QPushButton{border: %(border_width_normal)s solid %(color_normal)s; border-radius: %(border_radius)s; background: %(btn_color_background_normal)s; padding: %(padding_normal)s;}"
              "QPushButton:hover{border: %(border_width_error)s solid %(color_normal_hover)s; border-radius: %(border_radius)s; background: %(btn_color_background_normal_hover)s; padding: %(padding_normal)s;}" % INPUTS_STYLE)
BTN_ERROR = ("QPushButton{border: %(border_width_error)s solid %(color_error)s; border-radius: %(border_radius)s; background: %(background_error)s; padding: %(padding_normal)s;}"
             "QPushButton:hover{border: %(border_width_error_hover)s solid %(color_error_hover)s; border-radius: %(border_radius)s; background: %(background_error_hover)s; padding: %(padding_normal)s;}" % INPUTS_STYLE)
LBL_NORMAL = "QLabel{color: %(lbl_color_normal)s;}" % INPUTS_STYLE
LBL_ERROR = "QLabel{color: %(lbl_color_error)s;}" % INPUTS_STYLE
QCB_NORMAL = ("QComboBox{border: %(border_width_normal)s solid %(color_normal)s; border-radius: %(border_radius)s; background: %(field_color_background_normal)s; padding: %(padding_normal)s; font-size: %(input_font_size_px)s;}"
              "QComboBox:hover{border: %(border_width_error)s solid %(color_normal_hover)s; border-radius: %(border_radius)s; background: %(field_color_background_normal_hover)s; padding: %(padding_normal)s; font-size: %(input_font_size_px)s;}" % INPUTS_STYLE)
QCB_ERROR = ("QComboBox{border: %(border_width_error)s solid %(color_error)s; border-radius: %(border_radius)s; background: %(background_error)s; padding: %(padding_normal)s; font-size: %(input_font_size_px)s;}"
             "QComboBox:hover{border: %(border_width_error_hover)s solid %(color_error_hover)s; border-radius: %(border_radius)s; background: %(background_error_hover)s; padding: %(padding_normal)s; font-size: %(input_font_size_px)s;}" % INPUTS_STYLE)
LE_NORMAL = ("QLineEdit{border: %(border_width_normal)s solid %(color_normal)s; border-radius: %(border_radius)s; background: %(field_color_background_normal)s; padding: %(padding_normal)s; font-size: %(input_font_size_px)s;}"
             "QLineEdit:hover{border: %(border_width_error)s solid %(color_normal_hover)s; border-radius: %(border_radius)s; background: %(field_color_background_normal_hover)s; padding: %(padding_normal)s; font-size: %(input_font_size_px)s;}" % INPUTS_STYLE)
LE_ERROR = ("QLineEdit{border: %(border_width_error)s solid %(color_error)s; border-radius: %(border_radius)s; background: %(background_error)s; padding: %(padding_normal)s; font-size: %(input_font_size_px)s;}"
            "QLineEdit:hover{border: %(border_width_error_hover)s solid %(color_error_hover)s; border-radius: %(border_radius)s; background: %(background_error_hover)s; padding: %(padding_normal)s; font-size: %(input_font_size_px)s;}" % INPUTS_STYLE)
BTN_X_STYLE = {
    "maximum-width": 15,
    "font-size": 8,
}
GRAPH_STYLE = {
    "antialiasing": True,
    "background-color": '#FFFFFF',
    "font-color": '#000000',
    "font-size": '13px',
    "spectrum-color": (31, 119, 180),
    "spectrum-width": 2,
    "destination-color": (105, 66, 20),
    "destination-width": 3,
    "convolution-color": (255, 127, 14),
    "convolution-width": 3,
}
GRAPH_TEXT = {
    "y-axe": 'Intensity',
    "x-axe": 'Wavelength',
    "spectrum-line": "Initial spectrum",
    "destination-line": "Destination interval",
    "convolution-line": "Convolution of the spectrum",
}

# other constants
UNITS = ["cm-1", "micron", "nm", "A"]
CONVOLUTION_TYPES = ["Gauss function", "triangle", "trapeze", "Lorentz function", "Voigt profile", "Gauss & Lorentz sum"]
EXTRAPOLATION_TYPES = ["zeros", "constant", "average constant", "linear regression"]



class ConvolutionMainW(QtWidgets.QMainWindow):
    def __init__(self):
        super(ConvolutionMainW, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        screenGeometry = QApplication.primaryScreen().geometry()
        self.resize(screenGeometry.width(), screenGeometry.height())
        self.showMaximized()
        # globals
        self.set_globals()
        # window
        self.setWindowTitle(f"{__app_name__} v.{version}")
        # menu
        self.create_menu()
        # UI
        self.set_ui()
        # buttons
        self.ui.btn_dstntn_export.setStyleSheet(BTN_BIG)
        self.ui.btn_dstntn_export.clicked.connect(self.destination_export)
        self.ui.btn_calc.setStyleSheet(BTN_BIG)
        self.ui.btn_calc.clicked.connect(self.convolution_calc)
        self.ui.btn_export.setStyleSheet(BTN_BIG)
        self.ui.btn_export.clicked.connect(self.convoluted_spectrum_export)

    # INTERFACE
    def set_globals(self):
        """
            Initializes various global flags, parameters, and user interface elements.

        """
        # flags
        self.tests_are_running = False
        self.convolution_is_calculated = False
        ## conv_core class instance
        self.my_conv = conv_core.ConvolutionCore()
        self.my_conv.parent_window_setter(self)
        # commons
        self.truncations_dict = {
            "Gauss": 10,
            "triangle": 3,
            "trapeze": 3,
            "Lorentz": 15,
            "Voigt": 15
        }
        self.conservation_tolerance = 0.1
        # fields that will be created (not provided via the UI template)
        self.spctrm_wdth_const = QLineEditNumber(self)
        self.dstntn_linear_start = QLineEditNumber(self)
        self.dstntn_linear_stop = QLineEditNumber(self)
        self.dstntn_linear_step = QLineEditNumber(self)
        self.conv_type = QComboBox(self)
        self.gauss_part_lbl = QLabel(self)
        self.conv_gauss_part = QLineEditNumber(self)
        self.conv_truncation = QLineEditNumber(self)
        self.conv_extrap = QComboBox(self)
        self.conv_wdth_1_start_lbl = QLabel(self)
        self.conv_wdth_1_start = QLineEditNumber(self)
        self.conv_wdth_1_stop_lbl = QLabel(self)
        self.conv_wdth_1_stop = QLineEditNumber(self)
        self.conv_wdth_2_start_lbl = QLabel(self)
        self.conv_wdth_2_start = QLineEditNumber(self)
        self.conv_wdth_2_stop_lbl = QLabel(self)
        self.conv_wdth_2_stop = QLineEditNumber(self)
        self.conv_wdth_1_const_lbl = QLabel(self)
        self.conv_wdth_1_const = QLineEditNumber(self)
        self.conv_wdth_2_const_lbl = QLabel(self)
        self.conv_wdth_2_const = QLineEditNumber(self)

    def create_menu(self):
        """
            Creates and sets up the application's help menu.

            This function adds an 'About' action to the help menu and connects this
            action to the show_about handler.

        :return: None
        """
        try:
            extractAction = QAction("&About", self)
            extractAction.setStatusTip('About The App')
            extractAction.triggered.connect(self.show_about)
            self.statusBar()
            mainMenu = self.menuBar()
            fileMenu = mainMenu.addMenu('&Help')
            fileMenu.addAction(extractAction)
        except Exception as e:
            message = f"Error in create_menu:\n{e}"
            print(message)
            self.show_error_dialog(message)

    def show_dialog(self, message, title, icon, buttons=QMessageBox.Ok):
        """
            Show a message dialog to the user.

            This function displays a message dialog with the specified message, title, icon, and buttons.
            It ensures that the dialog is only shown when tests are not running.

        :param message: str
            The message to display in the dialog.
        :param title: str
            The title of the dialog window.
        :param icon: QMessageBox.Icon
            The icon to display in the dialog.
        :param buttons: QMessageBox.StandardButtons, optional
            The buttons to display in the dialog. Default is QMessageBox.Ok.
        :return: int
            The result of the dialog execution, which corresponds to the button clicked by the user.
        """
        if not self.tests_are_running:
            dlg = QMessageBox(self)
            dlg.setWindowTitle(title)
            dlg.setText(message)
            dlg.setIcon(icon)
            dlg.setStandardButtons(buttons)
            return dlg.exec()

    def show_info_dialog(self, message, title="Ok!"):
        """
            Display an informational dialog.

        :param message: str
        	The main text to be displayed in the dialog box.
        :param title: str
        	The title of the informational dialog box. Default is 'Ok!'.
        :return: None
        """
        self.show_dialog(message, title, QMessageBox.Icon.Information)

    def show_error_dialog(self, message, title="Error!"):
        """
            Displays an error dialog.

        :param message: str
        	A string containing the error message to be displayed in the dialog.
        :param title: str, optional
        	A string containing the title of the dialog box. Default is "Error!".
        :return: None
        """
        self.show_dialog(message, title, QMessageBox.Icon.Critical)

    def show_about(self):
        """
            Displays the 'About' information dialog for the application.

            This function shows an information dialog containing details about the application including its name, version,
            author details, copyright information, and support contacts.

        :return: None
        """
        try:
            message_text = (f"<b>{__app_name__}</b> v.{version}"
                            f"<p>Copyright: {copyright}</p>"
                            f"<p><a href='{github_url}'>GitHub repository</a> (program code and more information)</p>"
                            f"<p>Created by Gorbacheva Maria ({author_mail})</p>"
                            "<p>Scientific base by Bernard Schmitt, IPAG (<a href='mailto: bernard.schmitt@univ-grenoble-alpes.fr'>bernard.schmitt@univ-grenoble-alpes.fr</a>)</p>"
                            f"<p>For any questions and bug reports, please, mail at {bug_support_mail}</p>"
                            "<p>In case of a bug, please report it and specify your operating system, "
                            "provide a detailed description of the problem with screenshots "
                            "and the files used and produced, if possible. Your contribution matters to make this program better!</p>")
            self.show_info_dialog(message_text, "About")
        except Exception as e:
            message = f"Error in show_about: {e}"
            print(message)
            self.show_error_dialog(message)

    def set_ui(self):
        """
            Configures the UI elements by initializing various components.

            This function attempts to set up the graphical elements, spectrum,
            spectrum width, presets, destination, and convolution settings.

        :return: None
        """
        try:
            self.set_graph()
            self.set_spectrum()
            self.set_spectrum_width()
            self.set_presets()
            self.set_destination()
            self.set_convolution()
        except Exception as e:
            message = f"Error in set_ui: {e}"
            print(message)
            self.show_error_dialog(message)

    # graph
    def set_graph(self):
        """
            Sets up the graph with various styles and plot items.

            This function configures the graph with predefined styles including background color,
            font color, and size. It also initializes the necessary plot items for spectrum,
            destination, and convolution lines, and adds them to the graph.

        :return: None
        """
        try:
            pg.setConfigOptions(antialias=GRAPH_STYLE["antialiasing"])
            # style
            self.ui.graphWidget.addLegend()
            self.ui.graphWidget.addItem(pg.GridItem())
            self.ui.graphWidget.setBackground(GRAPH_STYLE["background-color"])
            styles = {'color': GRAPH_STYLE["font-color"], 'font-size': GRAPH_STYLE["font-size"]}
            self.ui.graphWidget.setLabel('left', GRAPH_TEXT["y-axe"], **styles)
            self.ui.graphWidget.setLabel('bottom', GRAPH_TEXT["x-axe"], **styles)
            plot_item = self.ui.graphWidget.getPlotItem()
            plot_item.setContentsMargins(30, 30, 30, 30)
            ## spectrum
            pen_st = pg.mkPen(color=GRAPH_STYLE["spectrum-color"], width=GRAPH_STYLE["spectrum-width"])
            self.spectrum_graph = pg.PlotCurveItem(clear=True, pen=pen_st, name=GRAPH_TEXT["spectrum-line"])
            self.ui.graphWidget.addItem(self.spectrum_graph)
            ## destination
            pen_st = pg.mkPen(color=GRAPH_STYLE["destination-color"], width=GRAPH_STYLE["destination-width"])
            self.destination_graph = pg.PlotCurveItem(clear=True, pen=pen_st, name=GRAPH_TEXT["destination-line"])
            self.ui.graphWidget.addItem(self.destination_graph)
            self.inf_left = pg.InfiniteLine(0)
            self.inf_right = pg.InfiniteLine(0)
            ## convolution
            pen_st = pg.mkPen(color=GRAPH_STYLE["convolution-color"], width=GRAPH_STYLE["convolution-width"])
            self.convolution_graph = pg.PlotCurveItem(clear=True, pen=pen_st, name=GRAPH_TEXT["convolution-line"])
            self.ui.graphWidget.addItem(self.convolution_graph)
            ## help
            self.add_helper("graph")
        except Exception as e:
            message = f"Error in set_graph: {e}"
            print(message)
            self.show_error_dialog(message)

    # spectrum
    def set_spectrum(self):
        """
            Sets up the spectrum data and its associated UI components.

            This function configures the spectrum file selector button,
            adds the 'x' delete button for the spectrum, and populates the units
            and columns for the spectrum data.

        :return: None
        """
        try:
            # dialog btn
            self.ui.spctrm_file.setStyleSheet(BTN_NORMAL)
            self.ui.spctrm_file.clicked.connect(lambda: self.file_select("spectrum"))
            # x btn
            self.add_x_button("spectrum")
            # units
            self.fill_columns(UNITS, "spectrum_units", "Select unit", True)
            # columns
            self.fill_columns([], "spectrum", first_set=True)
        except Exception as e:
            message = f"Error in set_spectrum: {e}"
            print(message)
            self.show_error_dialog(message)

    # spectrum width
    def set_spectrum_width(self):
        """
            Sets up the spectrum width configuration in the user interface.

            This function configures the button, column, and input field for the spectrum width.

        :return: None
        """
        try:
            # dialog btn
            self.ui.spctrm_wdth_file.setStyleSheet(BTN_NORMAL)
            self.ui.spctrm_wdth_file.clicked.connect(lambda: self.file_select("spectrum_width"))
            # x btn
            self.add_x_button("spectrum_width")
            # column
            self.fill_columns([], "spectrum_width", first_set=True)
            # constant
            self.set_input_field("spectrum_width", self.spctrm_wdth_const, "")
        except Exception as e:
            message = f"Error in set_spectrum_width: {e}"
            print(message)
            self.show_error_dialog(message)

    # presets
    def set_presets(self):
        """
            Sets up the presets.

            This function configures the UI for importing/exporting destination and convolution settings, as well as instrument presets.

        :return: None
        """
        try:
            # import/export the UI form input
            self.set_UI_input_import_export()
            # instrument presets
            self.instrument_preset_set_up()
        except Exception as e:
            message = f"Error in set_presets: {e}"
            print(message)
            self.show_error_dialog(message)

    # destination
    def set_destination(self):
        """
            Sets up the destination UI elements.

            This function configures the destination tab and its components such as file selection button,
            start/stop/step input fields, and units dropdown. It initializes these UI elements with default
            values and connects them to appropriate event handlers.

        :return: None
        """
        try:
            ## tab
            self.ui.dstntn_tab.currentChanged.connect(self.destination_plot)
            ## dialog btn
            self.ui.dstntn_file.setStyleSheet(BTN_NORMAL)
            self.ui.dstntn_file.clicked.connect(lambda: self.file_select("destination"))
            # x btn
            self.add_x_button("destination")
            # column
            self.fill_columns([], "destination", first_set=True)
            # start
            self.set_input_field("destination_start", self.dstntn_linear_start, 0)
            # stop
            self.set_input_field("destination_stop", self.dstntn_linear_stop, 10)
            # step
            self.set_input_field("destination_step", self.dstntn_linear_step, 0.1)
            ## units
            self.fill_columns(UNITS, "destination_units", "Select unit", True)
        except Exception as e:
            message = f"Error in set_destination: {e}"
            print(message)
            self.show_error_dialog(message)

    # convolution
    def set_convolution(self):
        """
            Configure the convolution UI elements.

            This function sets various convolution parameters such as type, Gauss ratio, truncation, and extrapolation.
            It also configures the related UI elements such as buttons and dropdown menus, ensuring they are connected
            with the appropriate actions and default values. Additionally, this function fills in columns and associates
            relevant events to the convolution-specific UI components.

        :return: None
        """
        try:
            # convolution
            ## type
            self.set_input_field("convolution_type", self.conv_type, CONVOLUTION_TYPES)
            ## type help
            self.add_helper("convolution_type")
            ## gauss ratio
            self.set_input_field("convolution_ratio", self.conv_gauss_part, 0.5, self.gauss_part_lbl)
            ## truncation
            self.set_input_field("convolution_truncation", self.conv_truncation, 10)
            ## truncation help
            self.add_helper("convolution_truncation")
            ## extrapolation
            self.set_input_field("convolution_extrapolation", self.conv_extrap, EXTRAPOLATION_TYPES)
            ## extrapolation help
            self.add_helper("convolution_extrapolation")
            ## dialog btn
            self.ui.conv_file.setStyleSheet(BTN_NORMAL)
            self.ui.conv_file.clicked.connect(lambda: self.file_select("convolution"))
            ## x btn
            self.add_x_button("convolution")
            # columns
            self.fill_columns([], "convolution", first_set=True)
            ## width column
            self.ui.conv_wdth_1_clm.currentIndexChanged.connect(lambda: self.convolution_state_toggle(self.ui.conv_wdth_1_clm))
            ## top column
            self.ui.conv_wdth_2_lbl.hide()
            self.ui.conv_wdth_2_clm.hide()
            self.ui.conv_wdth_2_clm.currentIndexChanged.connect(lambda: self.convolution_state_toggle(self.ui.conv_wdth_2_clm))
            # width start
            self.set_input_field("convolution_width_start", self.conv_wdth_1_start, 0, self.conv_wdth_1_start_lbl)
            # width stop
            self.set_input_field("convolution_width_stop", self.conv_wdth_1_stop, 5, self.conv_wdth_1_stop_lbl)
            # top start
            self.set_input_field("convolution_top_start", self.conv_wdth_2_start, 0, self.conv_wdth_2_start_lbl)
            # top stop
            self.set_input_field("convolution_top_stop", self.conv_wdth_2_stop, 2.5, self.conv_wdth_2_stop_lbl)
            # width start
            self.set_input_field("convolution_width_const", self.conv_wdth_1_const, 2.5, self.conv_wdth_1_const_lbl)
            # top start
            self.set_input_field("convolution_top_const", self.conv_wdth_2_const, 1.5, self.conv_wdth_2_const_lbl)
        except Exception as e:
            message = f"Error in set_convolution: {e}"
            print(message)
            self.show_error_dialog(message)

    # accessories
    def add_helper(self, action_type):
        """
            Adds a clickable help icon to the specified UI grid based on the action type.

            This function dynamically adds a help icon with a tooltip and connects it
            to the corresponding help action based on the given action type. It also specifies
            the position within the grid where the help icon should appear and its alignment.

        :param action_type: str
            Specifies the type of action which determines the grid position, tooltip,
            and click behavior of the help icon.
        :return: None
        """
        try:
            uis = {
                # graph
                "graph_grid": self.ui.main_grid,
                "graph_grid_row": 0,
                "graph_grid_column": 2,
                "graph_hint": "About graph",
                "graph_action": self.graph_help,
                # convolution_type
                "convolution_type_grid": self.ui.conv_params_grid,
                "convolution_type_grid_row": 0,
                "convolution_type_grid_column": 2,
                "convolution_type_hint": "About convolution functions",
                "convolution_type_action": self.convolution_functions_help,
                # convolution_truncation
                "convolution_truncation_grid": self.ui.conv_params_grid,
                "convolution_truncation_grid_row": 2,
                "convolution_truncation_grid_column": 2,
                "convolution_truncation_hint": "About truncation",
                "convolution_truncation_action": self.truncation_help,
                # convolution_extrapolation
                "convolution_extrapolation_grid": self.ui.conv_params_grid,
                "convolution_extrapolation_grid_row": 3,
                "convolution_extrapolation_grid_column": 2,
                "convolution_extrapolation_hint": "About extrapolations",
                "convolution_extrapolation_action": self.extrapolation_help,
            }
            help_element = QLabelClickable(self)
            help_element.setObjectName(f"{action_type}_help")
            uis[f"{action_type}_grid"].addWidget(help_element, uis[f"{action_type}_grid_row"], uis[f"{action_type}_grid_column"], Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
            help_element.setPixmap(QPixmap('img/questions.png').scaled(20, 20))
            help_element.setCursor(Qt.CursorShape.PointingHandCursor)
            help_element.setToolTip(uis[f"{action_type}_hint"])
            help_element.clicked.connect(uis[f"{action_type}_action"])
        except Exception as e:
            message = f"Error in add_helper: {e}"
            print(message)
            self.show_error_dialog(message)

    def file_select(self, action_type):
        """
            Facilitates the selection of a file and handles actions based on the provided action type.

            This function opens a QFileDialog for the user to select a file. Depending on the selected file and the action type, it performs
            specific actions such as file reading or handling errors.

        :param action_type: str
            Type of action to be performed. It affects the directory opened in the dialog and subsequent UI updates.

        :return: None
            The function returns nothing but updates the UI components and sets specific actions based on the selected file and action type.
        """
        try:
            dir_name = settings.value(action_type + "_dir") if settings.value(action_type + "_dir") else ""
            file_path, _ = QFileDialog.getOpenFileName(self, "Select a file", dir_name, "Text documents (*.txt *.csv *tsv);;All files (*.*)")
            if os.path.isfile(file_path):
                if action_type in ["destination", "convolution"]:
                    self.ui.instrument_preset.setCurrentIndex(0)
                self.file_select_action(file_path, action_type)
        except Exception as e:
            message = f"Error in file_select for {action_type}: {e}"
            print(message)
            self.show_error_dialog(message)

    def file_select_action(self, file_path, action_type):
        """
            Handles the selection and processing of a specified file based on the action type.

            This function first checks if the given file path points to an existing file. If so, it updates file settings
            and labels, processes column counts, fills relevant columns, updates related fields, handles flags and warnings,
            and finally plots actions based on the action type.

        :param file_path: str
        	The path to the file to be processed.
        :param action_type: str
        	The type of action to be performed on the file.

        :return: None
        """
        try:
            if os.path.isfile(file_path):
                self.update_file_settings_and_labels(file_path, action_type)
                column_count_list = self.column_count(file_path)
                self.fill_columns(column_count_list, action_type)
                self.related_fields_update(action_type, file_path, column_count_list)
                self.flags_and_warning_updates(action_type)
                self.plot_action(action_type)
        except Exception as e:
            message = f"Error in file_select_action for {action_type}: {e}"
            print(message)
            self.show_error_dialog(message)

    def update_file_settings_and_labels(self, file_path, action_type):
        """
            Updates file settings and associated labels based on the action type.

            This function updates the file path settings and modifies corresponding UI labels
            depending on the type of file being processed (e.g., spectrum, spectrum_width, destination, or convolution).
            It also ensures that the directory paths are stored in settings and handles potential errors.

        :param file_path: str
            The file path to be updated in settings and used to set the label.
        :param action_type: str
            The type of action which determines which file path and label to update.
            Possible values include "spectrum", "spectrum_width", "destination", and "convolution".
        :return: None
        """
        try:
            if action_type == "spectrum":
                self.my_conv.spectrum_file_path = file_path
            elif action_type == "spectrum_width":
                self.my_conv.spectrum_width_path = file_path
            elif action_type == "destination":
                self.my_conv.destination_file_path = file_path
            elif action_type == "convolution":
                self.my_conv.convolution_file_path = file_path
            lbls = {
                "spectrum": self.ui.spctrm_path_lbl,
                "spectrum_width": self.ui.spctrm_wdth_path_lbl,
                "destination": self.ui.dstntn_path_lbl,
                "convolution": self.ui.conv_path_lbl,
            }
            settings.setValue(f"{action_type}_dir", file_path[:file_path.rfind("/")])
            if action_type in lbls:
                lbls[action_type].setText(file_path[file_path.rfind("/") + 1:])
        except Exception as e:
            message = f"Error in update_file_settings_and_labels for {action_type}: {e}"
            print(message)
            self.show_error_dialog(message)

    def column_count(self, file_path):
        """
            Returns the list of column numbers if data is present in the file.

            This function reads data from the specified file and returns a list
            of column numbers based on the data. If no data is found, an error
            dialog is shown, and an empty list is returned.

        :param file_path: str
            The path to the file containing data.

        :return: list
            A list of column numbers as strings if data is found.
            An empty list if no data is found or an error occurs.
        """
        try:
            file_data = self.get_file_data(file_path)
            column_count_list = []
            if len(file_data) > 0:
                for i in range(len(file_data[0])):
                    column_count_list.append(str(i + 1))
                return column_count_list
            else:
                self.show_error_dialog(f"No data found in the file at\n{file_path}!", "Warning")
                return []
        except Exception as e:
            message = f"Error in column_count: {e}"
            print(message)
            self.show_error_dialog(message)

    def get_file_data(self, file_path):
        """
            Fetch the parsed data from a specified file.

            This function attempts to read and parse data from the given file path
            using the DataPars class. If an error occurs during the process, it
            captures the exception and displays an error message.

        :param file_path: str
        	Path to the file that needs to be read and parsed.

        :return: np.array
        	Parsed content of the specified file.
        """
        try:
            data_read = DataPars(file_path, self)
            data_read.file_pars_f()
            return data_read.file_body
        except Exception as e:
            message = f"Error in get_file_data: {e}"
            print(message)
            self.show_error_dialog(message)

    def fill_columns(self, column_count_list, action_type, default_text="Select column", first_set=False):
        """
            Fills UI elements based on the specified action type and column count list.

            This function updates various UI components with a list of column names or default text.
            The behavior of the function changes based on the action type specified.
            If the first_set flag is true, it also connects combo box index changes to corresponding plot functions.

        :param column_count_list: list of str
            List of column names to insert into the combo boxes.
        :param action_type: str
            Defines which set of UI elements to update, e.g., 'spectrum', 'convolution_type'.
        :param default_text: str, optional
            Default text to insert into the combo boxes as the very first element (default is "Select column").
        :param first_set: bool, optional
            If True, additional operations like setting stylesheet and connecting signals for plots are performed (default is False).
        :return: None
        """
        try:
            UI_to_fill = {
                "spectrum": [self.ui.spctrm_wlth_clm, self.ui.spctrm_inty_clm],
                "spectrum_units": [self.ui.spctrm_unit],
                "spectrum_width": [self.ui.spctrm_wdth_clm],
                "destination": [self.ui.dstntn_wlth_clm],
                "destination_units": [self.ui.dstntn_unit],
                "convolution": [self.ui.conv_wdth_1_clm, self.ui.conv_wdth_2_clm],
                "convolution_type": [self.conv_type],
                "convolution_extrapolation": [self.conv_extrap],
            }
            plots = {
                "spectrum": self.spectrum_plot,
                "spectrum_units": self.spectrum_plot,
                "destination": self.destination_plot,
                "destination_units": self.destination_plot,
            }
            if action_type == "convolution_type":
                default_text = "Select a function"
            if action_type in UI_to_fill:
                for i in range(len(UI_to_fill[action_type])):
                    UI_to_fill[action_type][i].clear()
                    UI_to_fill[action_type][i].insertItem(0, default_text)
                    if first_set:
                        UI_to_fill[action_type][i].setStyleSheet(QCB_NORMAL)
                        if action_type in plots:
                            UI_to_fill[action_type][i].currentIndexChanged.connect(plots[action_type])
                    if not is_array_empty(column_count_list):
                        UI_to_fill[action_type][i].setStyleSheet(QCB_NORMAL)
                        UI_to_fill[action_type][i].insertItems(1, column_count_list)
                    UI_to_fill[action_type][i].setCurrentIndex(0)
            # if action_type in plots and not first_set:
            #     plots[action_type]()
        except Exception as e:
            message = f"Error in fill_columns: {e}"
            print(message)
            self.show_error_dialog(message)

    def related_fields_update(self, action_type, file_path, column_count_list):
        """
            Updates fields and settings based on the given action type and file parameters.

            This function handles the updating of file settings, labels, and fills column data
            according to the given action type. It also handles possible exceptions by displaying
            an error message.

        :param action_type: str
            The type of action to perform, can be "spectrum" or "destination".
        :param file_path: str
            The file path associated with the given action type.
        :param column_count_list: list
            A list of column counts to be processed and filled.
        :return: None
        """
        try:
            if action_type == "spectrum" and not self.my_conv.spectrum_width_path != "" and len(column_count_list) >= 3:
                self.update_file_settings_and_labels(file_path, "spectrum_width")
                self.fill_columns(column_count_list, "spectrum_width")
            if action_type == "destination" and self.my_conv.convolution_file_path == "" and len(column_count_list) > 1 and self.ui.conv_tab.currentIndex() == 0:
                self.update_file_settings_and_labels(file_path, "convolution")
                self.fill_columns(column_count_list, "convolution")
                self.convolution_file_warning_update()
        except Exception as e:
            message = f"Error in related_fields_update: {e}"
            print(message)
            self.show_error_dialog(message)

    def flags_and_warning_updates(self, action_type):
        """
            Updates flags and warning indicators based on the given action type.

            This function adjusts the setup flags and updates the UI warning indicators
            for either 'spectrum', 'destination', or 'convolution' configurations.
            If the action type is 'destination', it also checks if a convolution file exists and updates the warnings.

        :param action_type: str
            The type of action triggering the update. Possible values are 'spectrum', 'destination', and 'convolution'.
        :return: None
        """
        try:
            if action_type == "spectrum":
                self.my_conv.spectrum_set_up = False
            elif action_type == "destination":
                self.my_conv.destination_set_up = False
            warning_btn = {
                "spectrum": self.ui.spctrm_file,
                "destination": self.ui.dstntn_file,
                "convolution": self.ui.conv_file,
            }
            warning_lbl = {
                "spectrum": self.ui.spctrm_path_lbl,
                "destination": self.ui.dstntn_path_lbl,
                "convolution": self.ui.conv_path_lbl,
            }
            if action_type in warning_btn:
                warning_btn[action_type].setStyleSheet(BTN_NORMAL)
            if action_type in warning_lbl:
                warning_lbl[action_type].setStyleSheet(LBL_NORMAL)
            if action_type == "destination" and os.path.isfile(self.my_conv.convolution_file_path):
                self.convolution_file_warning_update()
        except Exception as e:
            message = f"Error in flags_and_warning_updates: {e}"
            print(message)
            self.show_error_dialog(message)

    def convolution_file_warning_update(self):
        """
            Updates the style of the convolution file UI elements to normal.

            This function sets the stylesheet of several convolution file related UI elements
            to their respective normal styles.

        :return: None
            The function returns nothing, but updates the UI styles and may display an error dialog.
        """
        try:
            self.ui.conv_file.setStyleSheet(BTN_NORMAL)
            self.ui.conv_path_lbl.setStyleSheet(LBL_NORMAL)
            self.ui.conv_wdth_1_clm.setStyleSheet(QCB_NORMAL)
            self.ui.conv_wdth_2_clm.setStyleSheet(QCB_NORMAL)
        except Exception as e:
            message = f"Error in convolution_file_warning_update: {e}"
            print(message)
            self.show_error_dialog(message)

    def plot_action(self, action_type):
        """
        	Creates the specified type of plot based on the input action type.

        	This function determines the type of plot to generate by matching the provided
        	action type with predefined plot options. If the action type matches one of the
        	defined plot types, it calls the respective plotting function.

        :param action_type: str
            Type of action to determine which plot to display ("spectrum" or "destination").

        :return: None
        """
        try:
            plot_types = {
                "spectrum": self.spectrum_plot,
                "destination": self.destination_plot,
            }
            if action_type in plot_types:
                plot_types[action_type]()
        except Exception as e:
            message = f"Error in plot_action: {e}"
            print(message)
            self.show_error_dialog(message)

    def add_x_button(self, action_type):
        """
            Adds a delete button with an "x" label to a specified layout.

            The function dynamically creates a clickable "x" delete button
            and appends it to one of the specified layouts based on the
            action_type provided. The button is configured with specific
            styles and a font size. When clicked, it triggers a deletion
            action associated with the action_type.

        :param action_type: str
        	The key representing the layout to which the "x" button should be added.
        	Valid keys are "spectrum", "spectrum_width", "destination", "convolution".

        :return: None
        """
        try:
            layouts = {
                "spectrum": self.ui.horizontalLayout_3,
                "spectrum_width": self.ui.horizontalLayout,
                "destination": self.ui.horizontalLayout_4,
                "convolution": self.ui.horizontalLayout_5,
            }
            file_del = QLabelClickable(self)
            file_del.setObjectName(f"{action_type}_file_del")
            file_del.setText("X")
            file_del.setCursor(Qt.CursorShape.PointingHandCursor)
            file_del.setMaximumWidth(BTN_X_STYLE["maximum-width"])
            font = QtGui.QFont()
            font.setPointSize(BTN_X_STYLE["font-size"])
            file_del.setFont(font)
            layouts[action_type].addWidget(file_del)
            file_del.clicked.connect(lambda: self.file_del(action_type))
        except Exception as e:
            message = f"Error in add_x_button: {e}"
            print(message)
            self.show_error_dialog(message)

    def file_del(self, action_type):
        """
            Deletes the file path associated with the given action type and updates the UI accordingly.

            This function resets the file path for the specified action type, updates the corresponding UI labels,
            and resets styles if necessary. It also handles updating columns with empty data.

        :param action_type: str
            The type of action for which the file path should be deleted. This can be one of "spectrum",
            "spectrum_width", "destination", or "convolution".
        :return: None
        """
        try:
            if action_type == "spectrum":
                self.my_conv.spectrum_file_path = ""
            elif action_type == "spectrum_width":
                self.my_conv.spectrum_width_path = ""
            elif action_type == "destination":
                self.ui.instrument_preset.setCurrentIndex(0)
                self.my_conv.destination_file_path = ""
            elif action_type == "convolution":
                self.ui.instrument_preset.setCurrentIndex(0)
                self.my_conv.convolution_file_path = ""
            lbls = {
                "spectrum": self.ui.spctrm_path_lbl,
                "spectrum_width": self.ui.spctrm_wdth_path_lbl,
                "destination": self.ui.dstntn_path_lbl,
                "convolution": self.ui.conv_path_lbl,
            }
            styles = {
                "spectrum": self.reset_spectrum_style,
                "destination": self.reset_destination_style,
                "convolution": self.reset_convolution_style,
            }
            if action_type in lbls:
                lbls[action_type].setText("no file selected")
            if action_type in styles:
                styles[action_type]()
            self.fill_columns([], action_type)
        except Exception as e:
            message = f"Error in file_del: {e}"
            print(message)
            self.show_error_dialog(message)

    def spectrum_plot(self):
        """
        	This function handles the plotting of the spectrum by resetting warnings, resetting plot data, and reading the spectrum.

        	The function is responsible for managing the process of plotting spectrum data. It first resets any existing warnings,
        	resets the plot data to ensure that the plot is updated with the latest data, and then performs the spectrum reading operation.

        :return: None
        """
        try:
            self.spectrum_reset_warnings()
            self.spectrum_reset_plot_data()
            self.spectrum_read()
        except Exception as e:
            message = f"Error in spectrum_plot: {e}"
            print(message)
            self.show_error_dialog(message)

    def spectrum_reset_warnings(self):
        """
            Resets warning styles for spectrum-related UI elements.

            This function checks the current indices of spectrum-related UI components
            and resets their styles to normal if they meet certain conditions.

        :return: None
        """
        try:
            if self.ui.spctrm_unit.currentIndex() > 0:
                self.ui.spctrm_unit.setStyleSheet(QCB_NORMAL)
            if self.ui.spctrm_wlth_clm.currentIndex() > 0:
                self.ui.spctrm_wlth_clm.setStyleSheet(QCB_NORMAL)
            if self.ui.spctrm_inty_clm.currentIndex() > 0:
                self.ui.spctrm_inty_clm.setStyleSheet(QCB_NORMAL)
        except Exception as e:
            message = f"Error in spectrum_reset_warnings: {e}"
            print(message)
            self.show_error_dialog(message)

    def spectrum_reset_plot_data(self):
        """
            Resets the data for the spectrum and convolution graphs to empty lists.

            This function clears the data points in both the spectrum_graph and convolution_graph.

        :return: None
        """
        try:
            self.spectrum_graph.setData([], [])
            self.convolution_graph.setData([], [])
        except Exception as e:
            message = f"Error in spectrum_reset_plot_data: {e}"
            print(message)
            self.show_error_dialog(message)

    def destination_plot(self):
        """
            Generates and displays a destination plot.

            This function resets necessary internal states and reads destination data before
            generating the plot.

        :return: None
        """
        try:
            self.destination_reset_warnings()
            self.destination_reset_plot_data()
            self.destination_read()
        except Exception as e:
            message = f"Error in destination_plot: {e}"
            print(message)
            self.show_error_dialog(message)

    def destination_reset_warnings(self):
        """
            Resets warning indicators for destination settings.

            This function checks various UI elements such as dropdowns and linear step, stop, and start values to ensure
            they meet specified conditions. If the conditions are met, it resets their styles to indicate a normal state.

        :return: None
        """
        try:
            if self.ui.dstntn_unit.currentIndex() > 0:
                self.ui.dstntn_unit.setStyleSheet(QCB_NORMAL)
            if self.ui.dstntn_wlth_clm.currentIndex() > 0:
                self.ui.dstntn_wlth_clm.setStyleSheet(QCB_NORMAL)
            if (not np.isnan(self.dstntn_linear_step.value()) and not np.isnan(self.dstntn_linear_stop.value()) and not np.isnan(self.dstntn_linear_start.value())
                    and self.dstntn_linear_step.value() <= np.fabs(self.dstntn_linear_stop.value() - self.dstntn_linear_start.value())):
                self.dstntn_linear_step.setStyleSheet(LE_NORMAL)
        except Exception as e:
            message = f"Error in destination_reset_warnings: {e}"
            print(message)
            self.show_error_dialog(message)

    def destination_reset_plot_data(self):
        """
            Reset plot data for destination and convolution graphs.

            This function clears the data for destination and convolution graphs, and removes
            specific items from the user interface graph widget.

        :return: None
        """
        try:
            self.destination_graph.setData([], [])
            self.convolution_graph.setData([], [])
            self.ui.graphWidget.removeItem(self.inf_left)
            self.ui.graphWidget.removeItem(self.inf_right)
        except Exception as e:
            message = f"Error in destination_reset_plot_data: {e}"
            print(message)
            self.show_error_dialog(message)

    def set_input_field(self, action_type, field_ref, default_value, lbl_ref=None):
        """
            Sets up and configures an input field based on the specified action type.

            This method configures an input field by creating a dictionary of field settings and
            delegating the setup to helper methods for label and field settings.

        :param action_type: str
            Type of action for which the input field is being set up.
        :param field_ref: object
            Reference to the field that needs to be set up.
        :param default_value: any
            The default value to be set for the input field.
        :param lbl_ref: object, optional
            Reference to the label associated with the input field.

        :return: None
        """
        try:
            fields_dict = {
                # spectrum_width
                "spectrum_width_text": "width value\n(optional)",
                "spectrum_width_grid": self.ui.spctrm_const_grid,
                "spectrum_width_row": 0,
                "spectrum_width_size": "medium",
                "spectrum_width_function": lambda: self.field_warning_toggle(field_ref),
                # destination_start
                "destination_start_text": "start",
                "destination_start_grid": self.ui.dstntn_linear_grid,
                "destination_start_row": 0,
                "destination_start_size": "medium",
                "destination_start_plot": self.destination_plot,
                "destination_start_function": lambda: self.field_warning_toggle(field_ref),
                # destination_stop
                "destination_stop_text": "end",
                "destination_stop_grid": self.ui.dstntn_linear_grid,
                "destination_stop_row": 1,
                "destination_stop_size": "medium",
                "destination_stop_plot": self.destination_plot,
                "destination_stop_function": lambda: self.field_warning_toggle(field_ref),
                # destination_step
                "destination_step_text": "step",
                "destination_step_grid": self.ui.dstntn_linear_grid,
                "destination_step_row": 2,
                "destination_step_size": "medium",
                "destination_step_plot": self.destination_plot,
                "destination_step_function": lambda: self.field_warning_toggle(field_ref),
                # convolution_type
                "convolution_type_text": "function",
                "convolution_type_grid": self.ui.conv_params_grid,
                "convolution_type_row": 0,
                "convolution_type_size": "large",
                "convolution_type_function": self.convolution_type_toggle,
                # convolution_ratio
                "convolution_ratio_text": "Gauss\nratio",
                "convolution_ratio_grid": self.ui.conv_params_grid,
                "convolution_ratio_row": 1,
                "convolution_ratio_size": "large",
                "convolution_ratio_function": lambda: self.field_warning_toggle(field_ref),
                # convolution_truncation
                "convolution_truncation_text": "truncation",
                "convolution_truncation_grid": self.ui.conv_params_grid,
                "convolution_truncation_row": 2,
                "convolution_truncation_size": "large",
                "convolution_truncation_function": lambda: self.field_warning_toggle(field_ref),
                # convolution_extrapolation
                "convolution_extrapolation_text": "extrapolation",
                "convolution_extrapolation_grid": self.ui.conv_params_grid,
                "convolution_extrapolation_row": 3,
                "convolution_extrapolation_size": "large",
                # convolution_width_start
                "convolution_width_start_text": "width start",
                "convolution_width_start_grid": self.ui.conv_linear_grid,
                "convolution_width_start_row": 0,
                "convolution_width_start_size": "medium",
                "convolution_width_start_function": lambda: self.field_warning_toggle(field_ref),
                # convolution_width_stop
                "convolution_width_stop_text": "width end",
                "convolution_width_stop_grid": self.ui.conv_linear_grid,
                "convolution_width_stop_row": 1,
                "convolution_width_stop_size": "medium",
                "convolution_width_stop_function": lambda: self.field_warning_toggle(field_ref),
                # convolution_top_start
                "convolution_top_start_text": "top start",
                "convolution_top_start_grid": self.ui.conv_linear_grid,
                "convolution_top_start_row": 2,
                "convolution_top_start_size": "medium",
                "convolution_top_start_function": lambda: self.field_warning_toggle(field_ref),
                # convolution_top_stop
                "convolution_top_stop_text": "top end",
                "convolution_top_stop_grid": self.ui.conv_linear_grid,
                "convolution_top_stop_row": 3,
                "convolution_top_stop_size": "medium",
                "convolution_top_stop_function": lambda: self.field_warning_toggle(field_ref),
                # convolution_width_const
                "convolution_width_const_text": "width value",
                "convolution_width_const_grid": self.ui.conv_const_grid,
                "convolution_width_const_row": 0,
                "convolution_width_const_size": "medium",
                "convolution_width_const_function": lambda: self.field_warning_toggle(field_ref),
                # convolution_top_const
                "convolution_top_const_text": "top value",
                "convolution_top_const_grid": self.ui.conv_const_grid,
                "convolution_top_const_row": 1,
                "convolution_top_const_size": "medium",
                "convolution_top_const_function": lambda: self.field_warning_toggle(field_ref),
            }
            self.set_label(action_type, fields_dict, lbl_ref)
            self.set_field(action_type, field_ref, default_value, fields_dict)
        except Exception as e:
            message = f"Error in set_input_field: {e}"
            print(message)
            self.show_error_dialog(message)

    def set_label(self, action_type, fields_dict, lbl_ref=None):
        """
            Creates or modifies a QLabel widget for given action type.

            Sets a QLabel's properties and adds it to a specified grid layout based on the action_type, with optional hiding for specific action types.

        :param action_type: str
        	The type of action to determine label settings.
        :param fields_dict: dict
        	A dictionary containing relevant settings and UI objects for the label.
        :param lbl_ref: QLabel, optional
        	An optional reference to an existing QLabel to modify.

        :return: None
        """
        try:
            if not lbl_ref:
                const_lbl = QLabel(self)
            else:
                const_lbl = lbl_ref
            const_lbl.setObjectName(f"{action_type}_lbl")
            const_lbl.setText(fields_dict[f"{action_type}_text"])
            fields_dict[f"{action_type}_grid"].addWidget(const_lbl, fields_dict[f"{action_type}_row"], 0, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignLeft)
            font = QtGui.QFont()
            font.setPointSize(INPUTS_STYLE["lbl_font-size"])
            if action_type in ["convolution_ratio", "convolution_top_start", "convolution_top_stop", "convolution_top_const"]:
                const_lbl.hide()
        except Exception as e:
            message = f"Error in set_label: {e}"
            print(message)
            self.show_error_dialog(message)

    def set_field(self, action_type, field_ref, default_value, fields_dict):
        """
            Sets up a field with specific properties based on the action type and adds it to a grid layout.

        :param action_type: str
        	Type of the action which determines the properties and behavior of the field.
        :param field_ref: QtWidget
        	A reference to the field widget that will be configured.
        :param default_value: any
        	The default value to be set for the field. Could be of various types such as list or float.
        :param fields_dict: dict
        	A dictionary containing layout and size information for various action types, as well as associated functions.

        :return: None
        """
        try:
            # naming
            field_ref.setObjectName(f"{action_type}_field")
            # grid
            fields_dict[f"{action_type}_grid"].addWidget(field_ref, fields_dict[f"{action_type}_row"], 1, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignLeft)
            # style
            field_ref.setMinimumSize(QSize(INPUTS_STYLE[f"filed-size_{fields_dict[f'{action_type}_size']}"], INPUTS_STYLE["field_min-size"]))
            field_ref.setMaximumSize(QSize(INPUTS_STYLE[f"filed-size_{fields_dict[f'{action_type}_size']}"], INPUTS_STYLE["field_max-size"]))
            font = QtGui.QFont()
            font.setPointSize(INPUTS_STYLE["input_font_size"])
            field_ref.setFont(font)
            if type(default_value) != list:
                field_ref.setStyleSheet(LE_NORMAL)
            else:
                field_ref.setStyleSheet(QCB_NORMAL)
            if action_type in ["convolution_ratio", "convolution_top_start", "convolution_top_stop", "convolution_top_const"]:
                field_ref.hide()
            if action_type == "convolution_ratio":
                field_ref.setToolTip("must be between 0 and 1")
            # value
            if type(default_value) == list:
                self.fill_columns(default_value, action_type, "", True)
                if action_type == "convolution_extrapolation":
                    field_ref.removeItem(0)
            elif is_float(default_value):
                field_ref.setValue(default_value)
            else:
                field_ref.setText(default_value)
            # functions
            if f"{action_type}_plot" in fields_dict.keys():
                field_ref.editingFinished.connect(fields_dict[f"{action_type}_plot"])
            if f"{action_type}_function" in fields_dict.keys():
                if type(default_value) != list:
                    field_ref.textChanged.connect(fields_dict[f"{action_type}_function"])
                else:
                    field_ref.currentIndexChanged.connect(fields_dict[f"{action_type}_function"])
        except Exception as e:
            message = f"Error in set_field: {e}"
            print(message)
            self.show_error_dialog(message)

    def field_warning_toggle(self, widget):  # for the QLineEdit fields only
        """
            Sets the stylesheet of a QLineEdit widget based on its value.

            This function updates the widget's stylesheet to indicate normal or error state
            depending on the value it holds. For the conv_gauss_part widget, it also updates
            the conv_truncation value based on certain conditions. If any exception occurs,
            it displays an error dialog with the appropriate message.

        :param widget: QLineEdit
            The widget whose value and style are being checked and updated.

        :return: None
        """
        try:
            widget.setStyleSheet(LE_NORMAL)
            if np.isnan(widget.value()):
                widget.setStyleSheet(LE_ERROR)
            if widget == self.conv_gauss_part:
                if widget.value() < 0 or widget.value() > 1:
                    widget.setStyleSheet(LE_ERROR)
                else:
                    self.conv_truncation.setValue(self.conv_gauss_part.value() * self.truncations_dict["Gauss"] + (1 - self.conv_gauss_part.value()) * self.truncations_dict["Lorentz"])
            if widget == self.spctrm_wdth_const and widget.text() == "":
                widget.setStyleSheet(LE_NORMAL)
        except Exception as e:
            message = f"Error in field_warning_toggle: {e}"
            print(message)
            self.show_error_dialog(message)

    def set_UI_input_import_export(self):
        """
            Initializes the UI components for importing and exporting parameters.

            This function sets the stylesheet for the load and save buttons and connects
            their click events to the appropriate actions for importing and exporting presets.

        :return: None
        """
        try:
            self.ui.btn_param_load.setStyleSheet(BTN_NORMAL)
            self.ui.btn_param_load.clicked.connect(self.import_a_preset)
            self.ui.btn_param_save.setStyleSheet(BTN_NORMAL)
            self.ui.btn_param_save.clicked.connect(self.export_a_preset)
        except Exception as e:
            message = f"Error in set_UI_input_import_export: {e}"
            print(message)
            self.show_error_dialog(message)

    def import_a_preset(self):
        """
            Handles the action of importing a preset file.

            This function opens a file dialog to select a preset file, checks its existence,
            updates the settings with the directory path, and triggers the import function.

        :return: None
        """
        try:
            if settings.value("import_preset_dir"):
                file_path, _ = QFileDialog.getOpenFileName(self, "Select a preset file", settings.value("import_preset_dir"), "Text documents (*.txt *.csv *tsv);;All files (*.*)")
            else:
                file_path, _ = QFileDialog.getOpenFileName(self, "Select a preset file", "", "Text documents (*.txt *.csv *tsv);;All files (*.*)")
            if os.path.isfile(file_path):
                settings.setValue("import_preset_dir", file_path[:file_path.rfind("/")])
                self.import_a_preset_action(file_path)
        except Exception as e:
            message = f"Error in import_a_preset: {e}"
            print(message)
            self.show_error_dialog(message)

    def import_a_preset_action(self, file_path):
        """
        	Handles the import action for a preset configuration from a file.

        	This function reads a given file, checks whether it's a valid preset file, and if so,
        	it updates various UI elements based on the values read from the file.

        :param file_path: str
            Path to the preset file to be imported.

        :return: None
        """
        try:
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf8") as file:
                    file_content = file.readlines()
                if len(file_content) == 24:
                    # preset
                    preset_name = file_content[0][file_content[0].find(":") + 1:].strip()
                    if preset_name != "":
                        if preset_name == "LEISA New Horizons":
                            self.ui.instrument_preset.setCurrentIndex(1)
                        elif preset_name == "SuperCam/VIS":
                            self.ui.instrument_preset.setCurrentIndex(2)
                    else:
                        self.ui.instrument_preset.setCurrentIndex(0)
                        def get_element_from_file(file_content, file_content_index, max_value, input_type, field_to_fill, default_value):
                            def parse_and_set(value, max_value, setter, default_value):
                                if not np.isnan(max_value):
                                    if 0 <= value < max_value:
                                        setter(value)
                                    else:
                                        setter(default_value)
                                else:
                                    setter(value)
                            value_str = file_content[file_content_index][file_content[file_content_index].find(":") + 1:].strip()
                            if input_type == "qcb" and is_int(value_str):
                                parse_and_set(int(value_str), max_value, field_to_fill.setCurrentIndex, default_value)
                            elif input_type == "le" and is_float(value_str):
                                parse_and_set(float(value_str), max_value, field_to_fill.setValue, default_value)
                            else:
                                if input_type == "qcb":
                                    field_to_fill.setCurrentIndex(default_value)
                                elif input_type == "le":
                                    field_to_fill.setValue(default_value)
                        def file_action(file_content, file_content_index, file_read_action, file_dell_action):
                            path_str = file_content[file_content_index][file_content[file_content_index].find(":") + 1:].strip()
                            if os.path.isfile(path_str):
                                file_read_action(path_str)
                            else:
                                file_dell_action()
                        # destination wavelength
                        ## unit
                        get_element_from_file(file_content, 2, self.ui.dstntn_unit.count(), "qcb", self.ui.dstntn_unit, 0)
                        ## tab
                        get_element_from_file(file_content, 3, self.ui.dstntn_tab.count(), "qcb", self.ui.dstntn_tab, 0)
                        ## from file
                        file_action(file_content, 4, partial(self.file_select_action, action_type="destination"), partial(self.file_del, action_type="destination"))
                        ## wlth column
                        get_element_from_file(file_content, 5, self.ui.dstntn_wlth_clm.count(), "qcb", self.ui.dstntn_wlth_clm, 0)
                        ## wlth start
                        get_element_from_file(file_content, 6, np.NAN, "le", self.dstntn_linear_start, 0)
                        ## wlth stop
                        get_element_from_file(file_content, 7, np.NAN, "le", self.dstntn_linear_stop, 10)
                        ## wlth step
                        get_element_from_file(file_content, 8, np.NAN, "le", self.dstntn_linear_step, 0.1)
                        # convolution
                        ## tab
                        get_element_from_file(file_content, 10, self.ui.conv_tab.count(), "qcb", self.ui.conv_tab, 0)
                        ## type
                        get_element_from_file(file_content, 11, self.conv_type.count(), "qcb", self.conv_type, 0)
                        ## gauss ratio
                        get_element_from_file(file_content, 12, 1, "le", self.conv_gauss_part, 0.5)
                        ## truncation
                        get_element_from_file(file_content, 13, np.NAN, "le", self.conv_truncation, 3)
                        ## extrapolation type
                        get_element_from_file(file_content, 14, self.conv_extrap.count(), "qcb", self.conv_extrap, 0)
                        ## from file
                        file_action(file_content, 15, partial(self.file_select_action, action_type="convolution"), partial(self.file_del, action_type="convolution"))
                        ## from file: width column
                        get_element_from_file(file_content, 16, self.ui.conv_wdth_1_clm.count(), "qcb", self.ui.conv_wdth_1_clm, 0)
                        ## from file: top column
                        get_element_from_file(file_content, 17, self.ui.conv_wdth_2_clm.count(), "qcb", self.ui.conv_wdth_2_clm, 0)
                        ## linear
                        get_element_from_file(file_content, 18, np.NAN, "le", self.conv_wdth_1_start, 0)
                        get_element_from_file(file_content, 19, np.NAN, "le", self.conv_wdth_1_stop, 5)
                        get_element_from_file(file_content, 20, np.NAN, "le", self.conv_wdth_2_start, 0)
                        get_element_from_file(file_content, 21, np.NAN, "le", self.conv_wdth_2_stop, 2.5)
                        ## const
                        get_element_from_file(file_content, 22, np.NAN, "le", self.conv_wdth_1_const, 2.5)
                        get_element_from_file(file_content, 23, np.NAN, "le", self.conv_wdth_2_const, 1.5)
                else:
                    message = "Wrong file format!"
                    print(message)
                    self.show_error_dialog(message)
        except Exception as e:
            message = f"Error in import_a_preset_action: {e}"
            print(message)
            self.show_error_dialog(message)

    def export_a_preset(self):
        """
            Exports the current preset to a text file.

            This function allows the user to export the current convolution preset settings
            to a specified text file. If a directory for exporting presets has been
            previously set, it will use that directory; otherwise, it will prompt the
            user to specify a file location and name.

        :return: None
        """
        try:
            if settings.value("export_preset_dir"):
                file_name, _ = QFileDialog.getSaveFileName(self, "Save File", settings.value("export_preset_dir") + "/convolution_preset.txt", "Text Files (*.txt)")
            else:
                file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "convolution_preset.txt", "Text Files (*.txt)",)
            if file_name:
                settings.setValue("export_preset_dir", file_name[:file_name.rfind("/")])
                str_to_export = self.export_a_preset_action()
                with open(file_name, 'w+') as file_output:
                    file_output.write(str_to_export)
        except Exception as e:
            message = f"Error in export_a_preset: {e}"
            print(message)
            self.show_error_dialog(message)

    def export_a_preset_action(self):
        """
            Exports a preset action configuration as a formatted string.

            This function collects various settings and configurations from the user
            interface and the internal state, then assembles them into a formatted string
            representing the current preset action.

        :return str_to_export: str
        	The formatted string containing the preset action configuration.
        """
        try:
            str_to_export = ""
            # preset
            str_to_export = str_to_export + "preset: "
            if self.ui.instrument_preset.currentIndex() > 0:
                str_to_export = str_to_export + f"{self.preset_name}"
            str_to_export = str_to_export + "\n"
            # destination wavelength
            str_to_export = str_to_export + "destination\n"
            ## unit
            str_to_export = str_to_export + f"\tunit: {self.ui.dstntn_unit.currentIndex()}\n"
            ## tab
            str_to_export = str_to_export + f"\ttab: {self.ui.dstntn_tab.currentIndex()}\n"
            ## from file
            str_to_export = str_to_export + f"\tpath: {self.my_conv.destination_file_path}\n"
            ## wlth column
            str_to_export = str_to_export + f"\tcolumn: {self.ui.dstntn_wlth_clm.currentIndex()}\n"
            ## wlth start
            str_to_export = str_to_export + f"\tstart: {self.dstntn_linear_start.value()}\n"
            ## wlth stop
            str_to_export = str_to_export + f"\tend: {self.dstntn_linear_stop.value()}\n"
            ## wlth step
            str_to_export = str_to_export + f"\tstep: {self.dstntn_linear_step.value()}\n"
            # convolution
            str_to_export = str_to_export + "convolution\n"
            ## tab
            str_to_export = str_to_export + f"\ttab: {self.ui.conv_tab.currentIndex()}\n"
            ## type
            str_to_export = str_to_export + f"\tfunction: {self.conv_type.currentIndex()}\n"
            ## gauss ratio
            str_to_export = str_to_export + f"\tratio: {self.conv_gauss_part.value()}\n"
            ## truncation
            str_to_export = str_to_export + f"\ttruncation: {self.conv_truncation.value()}\n"
            ## extrapolation type
            str_to_export = str_to_export + f"\textrapolation: {self.conv_extrap.currentIndex()}\n"
            ## from file
            str_to_export = str_to_export + f"\tpath: {self.my_conv.convolution_file_path}\n"
            ## from file: width column
            str_to_export = str_to_export + f"\twidth_1 column: {self.ui.conv_wdth_1_clm.currentIndex()}\n"
            ## from file: top column
            str_to_export = str_to_export + f"\twidth_2 column: {self.ui.conv_wdth_2_clm.currentIndex()}\n"
            ## linear
            str_to_export = str_to_export + f"\twidth_1 start: {self.conv_wdth_1_start.value()}\n"
            str_to_export = str_to_export + f"\twidth_1 end: {self.conv_wdth_1_stop.value()}\n"
            str_to_export = str_to_export + f"\twidth_2 start: {self.conv_wdth_2_start.value()}\n"
            str_to_export = str_to_export + f"\twidth_2 end: {self.conv_wdth_2_stop.value()}\n"
            ## const
            str_to_export = str_to_export + f"\twidth_1 const: {self.conv_wdth_1_const.value()}\n"
            str_to_export = str_to_export + f"\twidth_2 const: {self.conv_wdth_2_const.value()}\n"
            return str_to_export
        except Exception as e:
            message = f"Error in export_a_preset_action: {e}"
            print(message)
            self.show_error_dialog(message)

    def instrument_preset_set_up(self):
        """
            Initializes the instrument preset dropdown menu in the UI.

            Sets up the dropdown menu by inserting predefined instrument preset options and connects
            the selection event to the corresponding handler. Resets the preset activation flag and
            preset name.

        :return: None
        """
        try:
            self.is_preset_activated = False
            self.preset_name = ""
            self.ui.instrument_preset.setStyleSheet(QCB_NORMAL)
            self.ui.instrument_preset.insertItem(0, "Select an instrument preset")
            self.ui.instrument_preset.insertItem(1, "LEISA lowres/highres - New Horizons")
            self.ui.instrument_preset.insertItem(2, "SuperCam/VIS")
            self.ui.instrument_preset.currentIndexChanged.connect(self.preset_selected)
        except Exception as e:
            message = f"Error in instrument_preset_set_up: {e}"
            print(message)
            self.show_error_dialog(message)

    def preset_selected(self):
        """
            Perform setup of instrument presets and clean up the UI afterward.

            This function sets up instrument presets and performs necessary
            UI cleanup operations.

        :return: None
        """
        try:
            self.set_up_instrument_presets()
            self.clean_up_UI_after_instrument_preset()
        except Exception as e:
            message = f"Error in preset_selected: {e}"
            print(message)
            self.show_error_dialog(message)

    def set_up_instrument_presets(self):
        """
            Sets up instrument presets based on the user's selection in the GUI.

            This function handles the configuration of different instrument presets such as "LEISA New Horizons" and "SuperCam/VIS".
            It fetches preset values and sets up the user interface and internal convolution parameters using these values.

        :return: None
        """
        try:
            if self.ui.instrument_preset.currentIndex() == 1:
                preset_values = {
                    "name": "LEISA New Horizons",
                    "unit": LEISA_New_Horizons.unit,
                    "unit_code": LEISA_New_Horizons.unit_code,
                    "wavelength": LEISA_New_Horizons.destination_wavelength,
                    "conv_type_code": LEISA_New_Horizons.convolution_type_code,
                    "truncation": self.truncations_dict["Gauss"],
                    "gauss_ratio": 0.5,
                    "extrapolation": 0,
                    "width_1": LEISA_New_Horizons.convolution_width,
                    "width_2": np.NAN,
                }
                self.set_UI_via_instrument_preset(**{key: preset_values[key] for key in ["name", "unit_code", "conv_type_code"]})
                self.set_my_conv_via_instrument_preset(**{key: preset_values[key] for key in ["unit", "wavelength", "conv_type_code", "truncation", "gauss_ratio", "extrapolation", "width_1", "width_2"]})
            elif self.ui.instrument_preset.currentIndex() == 2:
                preset_values = {
                    "name": "SuperCam/VIS",
                    "unit": SuperCam_VIS.unit,
                    "unit_code": SuperCam_VIS.unit_code,
                    "wavelength": SuperCam_VIS.destination_wavelength,
                    "conv_type_code": SuperCam_VIS.convolution_type_code,
                    "truncation": self.truncations_dict["trapeze"],
                    "gauss_ratio": 0,
                    "extrapolation": 0,
                    "width_1": SuperCam_VIS.convolution_width_1,
                    "width_2": SuperCam_VIS.convolution_width_2,
                }
                self.set_UI_via_instrument_preset(**{key: preset_values[key] for key in ["name", "unit_code", "conv_type_code"]})
                self.set_my_conv_via_instrument_preset(**{key: preset_values[key] for key in ["unit", "wavelength", "conv_type_code", "truncation", "gauss_ratio", "extrapolation", "width_1", "width_2"]})
        except Exception as e:
            message = f"Error in set_up_instrument_presets: {e}"
            print(message)
            self.show_error_dialog(message)

    def set_UI_via_instrument_preset(self, name, unit_code, conv_type_code):
        """
            Sets the user interface elements based on the provided instrument preset parameters.

            This function updates the user interface with the name, unit code, and conversion type code.

        :param name: str
        	Name of the instrument preset to be set in the UI.
        :param unit_code: int
        	Index of the destination unit set in the UI.
        :param conv_type_code: int
        	Index of the conversion type set in the UI.
        :return: None
        """
        try:
            self.preset_name = name
            self.ui.dstntn_unit.setCurrentIndex(unit_code)
            self.ui.dstntn_path_lbl.setText(f"{name} data")
            self.conv_type.setCurrentIndex(conv_type_code)
            self.ui.conv_path_lbl.setText(f"{name} data")
        except Exception as e:
            message = f"Error in set_UI_via_instrument_preset: {e}"
            print(message)
            self.show_error_dialog(message)

    def set_my_conv_via_instrument_preset(self, unit, wavelength, conv_type_code, truncation, gauss_ratio, extrapolation, width_1, width_2):
        """
            Set the my_conv parameters using the given instrument preset values.

            This function initializes the convolution parameters of the my_conv object based on
            specified unit, wavelength, and various convolution parameters.

        :param unit: str
            The target unit for the convolution.
        :param wavelength: np.array
            The destination wavelength array.
        :param conv_type_code: int
            The code representing the convolution type, adjusted by subtracting 1.
        :param truncation: float
            The truncation value for the convolution.
        :param gauss_ratio: float
            The Gauss ratio to be used in the convolution.
        :param extrapolation: int
            The extrapolation type for the convolution.
        :param width_1: np.array
            The first width for the convolution.
        :param width_2: np.array
            The second width for the convolution.
        :return: None
        """
        try:
            self.my_conv.destination_unit = unit
            self.my_conv.destination_wavelength = wavelength
            self.my_conv.convolution_type = conv_type_code - 1
            self.my_conv.convolution_truncation = truncation
            self.my_conv.convolution_gauss_ratio = gauss_ratio
            self.my_conv.convolution_extrapolation_type = extrapolation
            self.my_conv.convolution_width_1 = width_1
            self.my_conv.convolution_width_2 = width_2
        except Exception as e:
            message = f"Error in set_my_conv_via_instrument_preset: {e}"
            print(message)
            self.show_error_dialog(message)

    def clean_up_UI_after_instrument_preset(self):
        """
            Clean up and update the user interface based on the current instrument preset selection status.

            If an instrument preset is selected, this function will update the UI to match the preset configuration
            and disable unnecessary inputs. If no instrument preset is selected, it resets the corresponding data and re-enables inputs.

        :return: None
        """
        try:
            if self.ui.instrument_preset.currentIndex() > 0:  # an instrument preset is selected
                # set flags
                self.is_preset_activated = True
                # select file tabs
                self.ui.dstntn_tab.setCurrentIndex(0)
                self.ui.conv_tab.setCurrentIndex(0)
                # disable unnecessary inputs
                self.ui.dstntn_unit.setDisabled(True)
                self.ui.dstntn_wlth_clm.setDisabled(True)
                self.ui.conv_wdth_1_clm.setDisabled(True)
                self.ui.conv_wdth_2_clm.setDisabled(True)
                # clean up the columns
                self.fill_columns([], "destination", default_text="--")
                self.fill_columns([], "convolution", default_text="--")
                # plot the result
                self.destination_plot()
            else:  # no instrument preset is selected
                self.is_preset_activated = False
                self.preset_name = ""
                # clean up my_conv data
                self.my_conv.destination_unit = ""
                self.my_conv.destination_wavelength = np.zeros(0)
                self.my_conv.convolution_type = ""
                self.my_conv.convolution_width_1 = np.zeros(0)
                self.my_conv.convolution_width_2 = np.zeros(0)
                # re-enable disabled inputs
                self.ui.dstntn_unit.setDisabled(False)
                self.ui.dstntn_wlth_clm.setDisabled(False)
                self.ui.conv_wdth_1_clm.setDisabled(False)
                self.ui.conv_wdth_2_clm.setDisabled(False)
                # re-set up UI
                self.ui.dstntn_unit.setCurrentIndex(0)
                self.ui.dstntn_path_lbl.setText("no file selected")
                self.conv_type.setCurrentIndex(0)
                self.ui.conv_path_lbl.setText("no file selected")
        except Exception as e:
            message = f"Error in clean_up_UI_after_instrument_preset: {e}"
            print(message)
            self.show_error_dialog(message)

    def spectrum_graph_plot(self):
        """
            Plots the spectrum graph with the updated data.

            This function updates the graph with new spectrum data,
            handling unit label changes based on whether a destination
            unit is set.

        :return: None
        """
        try:
            # add new data to the graph
            self.spectrum_graph.setData(self.my_conv.spectrum_wavelength_original, self.my_conv.spectrum_intensity)
            # if destination is set up -> change x-axe unit, otherwise keep the spectrum unit
            if self.my_conv.destination_set_up:
                self.ui.graphWidget.setLabel("bottom", f"{GRAPH_TEXT['x-axe']}, {self.my_conv.destination_unit}")
            else:
                self.ui.graphWidget.setLabel("bottom", f"{GRAPH_TEXT['x-axe']}, {self.my_conv.spectrum_unit_original}")
        except Exception as e:
            message = f"Error in spectrum_graph_plot: {e}"
            print(message)
            self.show_error_dialog(message)

    def destination_graph_plot(self):
        """
            Plots the destination graph and manages its elements in the graph widget.

            This function plots the destination wavelengths data on the graph widget.
            It also initializes and sets the infinite lines marking the edges of the destination wavelengths
            and updates the graph widget's bottom label to display the unit of wavelength.

        :return: None
        """
        try:
            self.spectrum_plot()
            self.destination_graph.setData(self.my_conv.destination_wavelength, np.zeros(len(self.my_conv.destination_wavelength)))
            self.ui.graphWidget.removeItem(self.inf_left)
            self.ui.graphWidget.removeItem(self.inf_right)
            pen_st = pg.mkPen(color=(105, 66, 20), width=1)
            if len(self.my_conv.destination_wavelength):
                self.inf_left = pg.InfiniteLine(pos=self.my_conv.destination_wavelength[0], pen=pen_st)
                self.inf_right = pg.InfiniteLine(pos=self.my_conv.destination_wavelength[-1], pen=pen_st)
                self.ui.graphWidget.addItem(self.inf_left)
                self.ui.graphWidget.addItem(self.inf_right)
            self.ui.graphWidget.setLabel("bottom", f"Wavelength, {self.my_conv.destination_unit}")
        except Exception as e:
            message = f"Error in destination_graph_plot: {e}"
            print(message)
            self.show_error_dialog(message)

    def convolution_state_toggle(self, widget_name):
        """
            Toggle the state of the convolution settings based on given widget values.

            This function checks the style sheet of the provided widget and updates it
            based on certain conditions. It ensures that the widget is set to its normal
            style if the conditions are met, otherwise it keeps the error style.

        :param widget_name: QWidget
            The widget whose state and style need to be toggled.
        :return: None
        """
        try:
            if widget_name.styleSheet() in [LE_ERROR, QCB_ERROR]:
                if (widget_name == self.ui.conv_wdth_1_clm
                        and self.ui.conv_wdth_1_clm.currentIndex() > 0):
                    self.ui.conv_wdth_1_clm.setStyleSheet(QCB_NORMAL)
                elif (widget_name == self.ui.conv_wdth_2_clm
                      and self.ui.conv_wdth_2_clm.currentIndex() > 0):
                    self.ui.conv_wdth_2_clm.setStyleSheet(QCB_NORMAL)
                elif (widget_name in [self.conv_wdth_1_start, self.conv_wdth_1_stop, self.conv_wdth_2_start, self.conv_wdth_2_stop]
                      and (self.conv_wdth_1_start.value() > self.conv_wdth_2_start.value() and self.conv_wdth_1_stop.value() > self.conv_wdth_2_stop.value())):
                    self.conv_wdth_1_start.setStyleSheet(LE_NORMAL)
                    self.conv_wdth_1_stop.setStyleSheet(LE_NORMAL)
                    self.conv_wdth_2_start.setStyleSheet(LE_NORMAL)
                    self.conv_wdth_2_stop.setStyleSheet(LE_NORMAL)
                elif (widget_name in [self.conv_wdth_1_const, self.conv_wdth_2_const]
                      and self.conv_wdth_1_const.value() > self.conv_wdth_2_const.value()):
                        self.conv_wdth_1_const.setStyleSheet(LE_NORMAL)
                        self.conv_wdth_2_const.setStyleSheet(LE_NORMAL)
        except Exception as e:
            message = f"Error in convolution_state_toggle: {e}"
            print(message)
            self.show_error_dialog(message)

    def convolution_type_toggle(self):
        """
            Toggles convolution type settings and updates UI elements accordingly.

            This method adjusts the convolution type based on the selected index and updates related UI components.
            It sets default truncation values depending on the convolution type, disables certain options based on the preset,
            and shows or hides specific labels and inputs.

        :return: None
        """
        try:
            # style reset
            if self.conv_type.currentIndex() > 0:
                self.conv_type.setStyleSheet(QCB_NORMAL)
            # truncation
            if self.conv_type.currentIndex() == 1:  # Gauss function
                self.conv_truncation.setValue(self.truncations_dict["Gauss"])
            elif self.conv_type.currentIndex() == 2:  # triangle
                self.conv_truncation.setValue(self.truncations_dict["triangle"])
            elif self.conv_type.currentIndex() == 3:  # trapeze
                self.conv_truncation.setValue(self.truncations_dict["trapeze"])
            elif self.conv_type.currentIndex() == 4:  # Lorentz
                self.conv_truncation.setValue(self.truncations_dict["Lorentz"])
            elif self.conv_type.currentIndex() == 5:  # Voigt
                self.conv_truncation.setValue(self.truncations_dict["Voigt"])
            elif self.conv_type.currentIndex() == 6:  # Gauss+Lorentz
                self.conv_truncation.setValue(self.conv_gauss_part.value() * self.truncations_dict["Gauss"] + (1 - self.conv_gauss_part.value()) * self.truncations_dict["Lorentz"])
            # preset toggle
            self.conv_type.setDisabled(False)
            self.conv_type.model().item(3).setEnabled(True)
            self.conv_type.model().item(5).setEnabled(True)
            self.conv_type.model().item(6).setEnabled(True)
            if self.preset_name == "LEISA New Horizons":
                self.conv_type.model().item(3).setEnabled(False)
                self.conv_type.model().item(5).setEnabled(False)
                self.conv_type.model().item(6).setEnabled(False)
            elif self.preset_name == "SuperCam/VIS":
                self.conv_type.setDisabled(True)
            # show/hide width_2
            if self.conv_type.currentIndex() in [3, 5, 6]:  # trapeze, Voigt, Gauss+Lorentz
                self.ui.conv_wdth_2_lbl.show()
                self.ui.conv_wdth_2_clm.show()
                self.conv_wdth_2_start_lbl.show()
                self.conv_wdth_2_start.show()
                self.conv_wdth_2_stop_lbl.show()
                self.conv_wdth_2_stop.show()
                self.conv_wdth_2_const_lbl.show()
                self.conv_wdth_2_const.show()
            else:
                self.ui.conv_wdth_2_lbl.hide()
                self.ui.conv_wdth_2_clm.hide()
                self.conv_wdth_2_start_lbl.hide()
                self.conv_wdth_2_start.hide()
                self.conv_wdth_2_stop_lbl.hide()
                self.conv_wdth_2_stop.hide()
                self.conv_wdth_2_const_lbl.hide()
                self.conv_wdth_2_const.hide()
            # show/hide Gauss ratio
            if self.conv_type.currentIndex() == 6:  # Gauss+Lorentz
                self.gauss_part_lbl.show()
                self.conv_gauss_part.show()
            else:
                self.gauss_part_lbl.hide()
                self.conv_gauss_part.hide()
            # labels toggle
            if self.conv_type.currentIndex() in [5, 6]:
                self.ui.conv_wdth_1_lbl.setText("Gauss width\ncolumn")
                self.ui.conv_wdth_2_lbl.setText("Lorentz width\ncolumn")
                self.conv_wdth_1_start_lbl.setText("Gauss width\nstart")
                self.conv_wdth_2_start_lbl.setText("Lorentz width\nstart")
                self.conv_wdth_1_stop_lbl.setText("Gauss width\nend")
                self.conv_wdth_2_stop_lbl.setText("Lorentz width\nend")
                self.conv_wdth_1_const_lbl.setText("Gauss width\nvalue")
                self.conv_wdth_2_const_lbl.setText("Lorentz width\nvalue")
            else:
                self.ui.conv_wdth_1_lbl.setText("width\ncolumn")
                self.ui.conv_wdth_2_lbl.setText("top\ncolumn")
                self.conv_wdth_1_start_lbl.setText("width start")
                self.conv_wdth_2_start_lbl.setText("top start")
                self.conv_wdth_1_stop_lbl.setText("width end")
                self.conv_wdth_2_stop_lbl.setText("top end")
                self.conv_wdth_1_const_lbl.setText("width value")
                self.conv_wdth_2_const_lbl.setText("top value")
        except Exception as e:
            message = f"Error in convolution_type_toggle: {e}"
            print(message)
            self.show_error_dialog(message)

    # VERIFICATIONS
    def all_inputs_here(self):
        """
        	Check if all required inputs are present for various stages.

        	The function checks the presence of required inputs for spectrum, destination, and convolution stages.
        	If any of these inputs are missing, it returns False.

        :return: bool
            True if all inputs are present, otherwise False.
        """
        try:
            if not self.all_inputs_here_spectrum():
                return False
            if not self.all_inputs_here_destination():
                return False
            if not self.all_inputs_here_convolution():
                return False
            return True
        except Exception as e:
            message = f"Error in all_inputs_here: {e}"
            print(message)
            self.show_error_dialog(message)
            return False

    def all_inputs_here_spectrum(self):
        """
            Verifies if all required spectrum inputs are provided.

            This function checks for the presence and correct setting of essential spectrum elements
            like file paths, unit selections, and column assignments. If any required input is missing
            or incorrectly set, an error dialog is shown, and the respective element is highlighted.

        :return: bool
            Returns True if all required inputs are correctly provided, otherwise returns False.
        """
        try:
            verifications = {
                "file":
                    {"element": self.ui.spctrm_file,
                     "label": self.ui.spctrm_path_lbl,
                     "condition": self.my_conv.spectrum_file_path == "",
                     "warning": "No spectrum file found!\nTo continue, please select a spectrum file.",
                     "style": BTN_ERROR},
                "unit":
                    {"element": self.ui.spctrm_unit,
                     "label": None,
                     "condition": self.ui.spctrm_unit.currentIndex() <= 0,
                     "warning": "No spectrum unit given!\nTo continue, please select a spectrum unit.",
                     "style": QCB_ERROR},
                "wavelength":
                    {"element": self.ui.spctrm_wlth_clm,
                     "label": None,
                     "condition": self.ui.spctrm_wlth_clm.currentIndex() <= 0,
                     "warning": "No spectrum wavelength column given!\nTo continue, please select a wavelength column.",
                     "style": QCB_ERROR},
                "intensity":
                    {"element": self.ui.spctrm_inty_clm,
                     "label": None,
                     "condition": self.ui.spctrm_inty_clm.currentIndex() <= 0,
                     "warning": "No spectrum intensity column given!\nTo continue, please select an intensity column.",
                     "style": QCB_ERROR},
            }
            for verification in verifications.values():
                if verification["condition"]:
                    self.show_error_dialog(verification["warning"], "Warning")
                    verification["element"].setStyleSheet(verification["style"])
                    verification["element"].setFocus()
                    if verification["label"]:
                        verification["label"].setStyleSheet(LBL_ERROR)
                    return False
            # reset all styles if no error
            self.reset_spectrum_style()
            return True
        except Exception as e:
            message = f"Error in all_inputs_here_spectrum: {e}"
            print(message)
            self.show_error_dialog(message)
            return False

    def reset_spectrum_style(self):
        """
            Resets the style of various spectrum UI elements to their default states.

            This function iterates over a predefined set of user interface elements related to the spectrum
            and resets their styles to default values stored in constants.

        :return: None
        """
        try:
            elements = {
                "file":
                    {"element": self.ui.spctrm_file,
                     "style": BTN_NORMAL},
                "label":
                    {"element": self.ui.spctrm_path_lbl,
                     "style": LBL_NORMAL},
                "unit":
                    {"element": self.ui.spctrm_unit,
                     "style": QCB_NORMAL},
                "wavelength":
                    {"element": self.ui.spctrm_wlth_clm,
                     "style": QCB_NORMAL},
                "intensity":
                    {"element": self.ui.spctrm_inty_clm,
                     "style": QCB_NORMAL},
            }
            for item in elements.values():
                item["element"].setStyleSheet(item["style"])
        except Exception as e:
            message = f"Error in reset_spectrum_style: {e}"
            print(message)
            self.show_error_dialog(message)
            return False

    def all_inputs_here_destination(self):
        """
            Performs input validation for destination-related fields.

            This function checks various input fields related to destination settings,
            validates their content, and displays error dialogs if any validation fails.
            Appropriate styles are applied to elements to indicate errors.


        :return: bool
            True if all inputs are valid, False if any validation fails and an error dialog is displayed.
        """
        try:
            verifications = {
                "unit":
                    {"element": self.ui.dstntn_unit,
                     "label": None,
                     "condition": self.ui.dstntn_unit.currentIndex() <= 0,
                     "warning": "No destination unit given!\nTo continue, please select a destination unit.",
                     "style": QCB_ERROR},
                "file":
                    {"element": self.ui.dstntn_file,
                     "label": self.ui.dstntn_path_lbl,
                     "condition": not self.is_preset_activated and self.my_conv.destination_file_path == "",
                     "warning": "No destination file found!\nTo continue, please select a destination file.",
                     "style": BTN_ERROR},
                "wavelength":
                    {"element": self.ui.dstntn_wlth_clm,
                     "label": None,
                     "condition": not self.is_preset_activated and self.ui.dstntn_wlth_clm.currentIndex() <= 0,
                     "warning": "No destination wavelength column given!\nTo continue, please select a wavelength column.",
                     "style": QCB_ERROR},
                "start":
                    {"element": self.dstntn_linear_start,
                     "label": None,
                     "condition": np.isnan(self.dstntn_linear_start.value()),
                     "warning": "No correct destination wavelength start value given!\nTo continue, please enter a start value.",
                     "style": LE_ERROR},
                "stop":
                    {"element": self.dstntn_linear_stop,
                     "label": None,
                     "condition": np.isnan(self.dstntn_linear_stop.value()),
                     "warning": "No correct destination wavelength end value given!\nTo continue, please enter an end value.",
                     "style": LE_ERROR},
                "step":
                    {"element": self.dstntn_linear_step,
                     "label": None,
                     "condition": np.isnan(self.dstntn_linear_step.value()),
                     "warning": "No correct destination wavelength step value given!\nTo continue, please enter a step value.",
                     "style": LE_ERROR},
            }
            extra_conditions = {
                "unit": True,
                "file": self.ui.dstntn_tab.currentIndex() <= 0,
                "wavelength": self.ui.dstntn_tab.currentIndex() <= 0,
                "start": self.ui.dstntn_tab.currentIndex() == 1,
                "stop": self.ui.dstntn_tab.currentIndex() == 1,
                "step": self.ui.dstntn_tab.currentIndex() == 1,
            }
            for key, verification in verifications.items():
                if extra_conditions[key] and verification["condition"]:
                    self.show_error_dialog(verification["warning"], "Warning")
                    verification["element"].setStyleSheet(verification["style"])
                    verification["element"].setFocus()
                    if verification["label"]:
                        verification["label"].setStyleSheet(LBL_ERROR)
                    return False
            # reset all styles if no error
            self.reset_destination_style()
            return True
        except Exception as e:
            message = f"Error in all_inputs_here_destination: {e}"
            print(message)
            self.show_error_dialog(message)
            return False

    def reset_destination_style(self):
        """
            Resets the style of destination elements to their default settings.

            This function iterates over specific UI elements and sets their styles
            back to predefined default styles.

        :return: None
        """
        try:
            elements = {
                "unit":
                    {"element": self.ui.dstntn_unit,
                     "style": QCB_NORMAL},
                "file":
                    {"element": self.ui.dstntn_file,
                     "style": BTN_NORMAL},
                "label":
                    {"element": self.ui.dstntn_path_lbl,
                     "style": LBL_NORMAL},
                "wavelength":
                    {"element": self.ui.dstntn_wlth_clm,
                     "style": QCB_NORMAL},
                "start":
                    {"element": self.dstntn_linear_start,
                     "style": LE_NORMAL},
                "stop":
                    {"element": self.dstntn_linear_stop,
                     "style": LE_NORMAL},
                "step":
                    {"element": self.dstntn_linear_step,
                     "style": LE_NORMAL},
            }
            for item in elements.values():
                item["element"].setStyleSheet(item["style"])
        except Exception as e:
            message = f"Error in reset_destination_style: {e}"
            print(message)
            self.show_error_dialog(message)

    def all_inputs_here_convolution(self):
        """
            Validates all inputs required for convolution settings.

            This function checks each required input related to convolution and confirms if they meet specified conditions. If
            conditions are not met, the function creates corresponding warnings and styles the input fields to indicate errors.

        :return: None
        """
        try:
            verifications = {
                "type":
                    {"element": self.conv_type,
                     "label": None,
                     "condition": self.conv_type.currentIndex() <= 0,
                     "warning": "No convolution type given!\nTo continue, please select a convolution type.",
                     "style": QCB_ERROR},
                "ratio":
                    {"element": self.conv_gauss_part,
                     "label": None,
                     "condition": np.isnan(self.conv_gauss_part.value()),
                     "warning": "No Gauss ratio value given!\nTo continue, please enter a value.",
                     "style": LE_ERROR},
                "truncation":
                    {"element": self.conv_truncation,
                     "label": None,
                     "condition": np.isnan(self.conv_truncation.value()),
                     "warning": "No truncation value given!\nTo continue, please enter a value.",
                     "style": LE_ERROR},
                "file":
                    {"element": self.ui.conv_file,
                     "label": self.ui.conv_path_lbl,
                     "condition": not self.is_preset_activated and self.my_conv.convolution_file_path == "",
                     "warning": None,
                     "style": BTN_ERROR},
                "width":
                    {"element": self.ui.conv_wdth_1_clm,
                     "label": None,
                     "condition": not self.is_preset_activated and self.ui.conv_wdth_1_clm.currentIndex() <= 0,
                     "warning": None,
                     "style": QCB_ERROR},
                "top":
                    {"element": self.ui.conv_wdth_2_clm,
                     "label": None,
                     "condition": not self.is_preset_activated and self.ui.conv_wdth_2_clm.currentIndex() <= 0,
                     "warning": None,
                     "style": QCB_ERROR},
                "width_start":
                    {"element": self.conv_wdth_1_start,
                     "label": None,
                     "condition": np.isnan(self.conv_wdth_1_start.value()),
                     "warning": None,
                     "style": LE_ERROR},
                "width_stop":
                    {"element": self.conv_wdth_1_stop,
                     "label": None,
                     "condition": np.isnan(self.conv_wdth_1_stop.value()),
                     "warning": None,
                     "style": LE_ERROR},
                "top_start":
                    {"element": self.conv_wdth_2_start,
                     "label": None,
                     "condition": np.isnan(self.conv_wdth_2_start.value()),
                     "warning": None,
                     "style": LE_ERROR},
                "top_stop":
                    {"element": self.conv_wdth_2_stop,
                     "label": None,
                     "condition": np.isnan(self.conv_wdth_2_stop.value()),
                     "warning": None,
                     "style": LE_ERROR},
                "width_const":
                    {"element": self.conv_wdth_1_const,
                     "label": None,
                     "condition": np.isnan(self.conv_wdth_1_const.value()),
                     "warning": None,
                     "style": LE_ERROR},
                "top_const":
                    {"element": self.conv_wdth_2_const,
                     "label": None,
                     "condition": np.isnan(self.conv_wdth_2_const.value()),
                     "warning": None,
                     "style": LE_ERROR},
            }
            extra_conditions = {
                "type": True,
                "ratio": True,
                "truncation": True,
                "file": self.ui.conv_tab.currentIndex() <= 0,
                "width": self.ui.conv_tab.currentIndex() <= 0,
                "top": self.ui.conv_tab.currentIndex() <= 0 and self.conv_type.currentIndex() in [3, 5, 6],
                "width_start": self.ui.conv_tab.currentIndex() == 1,
                "width_stop": self.ui.conv_tab.currentIndex() == 1,
                "top_start": self.ui.conv_tab.currentIndex() == 1 and self.conv_type.currentIndex() in [3, 5, 6],
                "top_stop": self.ui.conv_tab.currentIndex() == 1 and self.conv_type.currentIndex() in [3, 5, 6],
                "width_const": self.ui.conv_tab.currentIndex() == 2,
                "top_const": self.ui.conv_tab.currentIndex() == 2 and self.conv_type.currentIndex() in [3, 5, 6],
            }
            warning_conditions = {
                "file": {
                    "trapeze": {
                        "condition": self.conv_type.currentIndex() == 3,
                        "warning": "No width & top file found!\nTo continue, please select a width & top file.",
                    },
                    "GL": {
                        "condition": self.conv_type.currentIndex() in [5, 6],
                        "warning": "No widths file found!\nTo continue, please select a width file.",
                    },
                    "other": {
                        "condition": self.conv_type.currentIndex() not in [3, 5, 6],
                        "warning": "No width file found!\nTo continue, please select a width file.",
                    },
                },
                "width": {
                    "trapeze": {
                        "condition": self.conv_type.currentIndex() == 3,
                        "warning": "No width column given!\nTo continue, please select a width column.",
                    },
                    "GL": {
                        "condition": self.conv_type.currentIndex() in [5, 6],
                        "warning": "No Gauss function width column given!\nTo continue, please select a width column.",
                    },
                    "other": {
                        "condition": self.conv_type.currentIndex() not in [3, 5, 6],
                        "warning": "No width column given!\nTo continue, please select a width column.",
                    },
                },
                "top": {
                    "trapeze": {
                        "condition": self.conv_type.currentIndex() == 3,
                        "warning": "No top column given!\nTo continue, please select a top column.",
                    },
                    "GL": {
                        "condition": self.conv_type.currentIndex() in [5, 6],
                        "warning": "No Lorentz function width column given!\nTo continue, please select a width column.",
                    },
                },
                "width_start": {
                    "not-GL": {
                        "condition": self.conv_type.currentIndex() not in [5, 6],
                        "warning": "No correct width start value given!\nTo continue, please enter a start value.",
                    },
                    "GL": {
                        "condition": self.conv_type.currentIndex() in [5, 6],
                        "warning": "No correct Gauss function width start value given!\nTo continue, please enter a start value.",
                    },
                },
                "width_stop": {
                    "not-GL": {
                        "condition": self.conv_type.currentIndex() not in [5, 6],
                        "warning": "No correct width end value given!\nTo continue, please enter an end value.",
                    },
                    "GL": {
                        "condition": self.conv_type.currentIndex() in [5, 6],
                        "warning": "No correct Gauss function width end value given!\nTo continue, please enter an end value.",
                    },
                },
                "top_start": {
                    "trapeze": {
                        "condition": self.conv_type.currentIndex() == 3,
                        "warning": "No correct top start value given!\nTo continue, please enter a start value.",
                    },
                    "GL": {
                        "condition": self.conv_type.currentIndex() in [5, 6],
                        "warning": "No correct Lorentz function width start value given!\nTo continue, please enter a start value.",
                    },
                },
                "top_stop": {
                    "trapeze": {
                        "condition": self.conv_type.currentIndex() == 3,
                        "warning": "No correct top end value given!\nTo continue, please enter an end value.",
                    },
                    "GL": {
                        "condition": self.conv_type.currentIndex() in [5, 6],
                        "warning": "No correct Lorentz function width end value given!\nTo continue, please enter an end value.",
                    },
                },
                "width_const": {
                    "not-GL": {
                        "condition": self.conv_type.currentIndex() not in [5, 6],
                        "warning": "No correct width constant value given!\nTo continue, please enter a value.",
                    },
                    "GL": {
                        "condition": self.conv_type.currentIndex() in [5, 6],
                        "warning": "No correct Gauss function width constant value given!\nTo continue, please enter a value.",
                    },
                },
                "top_const": {
                    "trapeze": {
                        "condition": self.conv_type.currentIndex() == 3,
                        "warning": "No correct top constant value given!\nTo continue, please enter a value.",
                    },
                    "GL": {
                        "condition": self.conv_type.currentIndex() in [5, 6],
                        "warning": "No correct Lorentz function width constant value given!\nTo continue, please enter a value.",
                    },
                },
            }
            for key, verification in verifications.items():
                if extra_conditions[key] and verification["condition"]:
                    if verification["warning"]:
                        self.show_error_dialog(verification["warning"], "Warning")
                    else:
                        for key_war in warning_conditions[key]:
                            if warning_conditions[key][key_war]["condition"]:
                                self.show_error_dialog(warning_conditions[key][key_war]["warning"], "Warning")
                                break
                    verification["element"].setStyleSheet(verification["style"])
                    verification["element"].setFocus()
                    if verification["label"]:
                        verification["label"].setStyleSheet(LBL_ERROR)
                    return False
            # reset all styles if no error
            self.reset_convolution_style()
            return True
        except Exception as e:
            message = f"Error in all_inputs_here_convolution: {e}"
            print(message)
            self.show_error_dialog(message)
            return False

    def reset_convolution_style(self):
        """
            Resets the styles of convolution elements to their default state.

            This function sets the style for a variety of convolution-related UI elements to predefined styles.

        :return: None
        """
        try:
            elements = {
                "type":
                    {"element": self.conv_type,
                     "style": QCB_NORMAL},
                "ratio":
                    {"element": self.conv_gauss_part,
                     "style": LE_NORMAL},
                "truncation":
                    {"element": self.conv_truncation,
                     "style": LE_NORMAL},
                "file":
                    {"element": self.ui.conv_file,
                     "style": BTN_NORMAL},
                "label":
                    {"element": self.ui.conv_path_lbl,
                     "style": LBL_NORMAL},
                "width":
                    {"element": self.ui.conv_wdth_1_clm,
                     "style": QCB_NORMAL},
                "top":
                    {"element": self.ui.conv_wdth_2_clm,
                     "style": QCB_NORMAL},
                "width_start":
                    {"element": self.conv_wdth_1_start,
                     "style": LE_NORMAL},
                "width_stop":
                    {"element": self.conv_wdth_1_stop,
                     "style": LE_NORMAL},
                "top_start":
                    {"element": self.conv_wdth_2_start,
                     "style": LE_NORMAL},
                "top_stop":
                    {"element": self.conv_wdth_2_stop,
                     "style": LE_NORMAL},
                "width_const":
                    {"element": self.conv_wdth_1_const,
                     "style": LE_NORMAL},
                "top_const":
                    {"element": self.conv_wdth_2_const,
                     "style": LE_NORMAL},
            }
            for item in elements.values():
                item["element"].setStyleSheet(item["style"])
        except Exception as e:
            message = f"Error in reset_convolution_style: {e}"
            print(message)
            self.show_error_dialog(message)

    def all_inputs_correct(self):
        """
            Checks if all input parameters are correct and updates the UI accordingly.

            This function verifies multiple input conditions related to destination and convolution parameters.
            Specific checks are performed based on the type of destination and convolution selected.
            If any condition fails, it updates the UI elements to reflect the error and shows an appropriate error dialog.

        :return: bool
        	Returns True if all inputs are correct, otherwise False.
        """
        try:
            self.spectrum_read()
            self.destination_read()
            self.conv_read()
            there_is_width_top_problem = False
            if self.conv_type.currentIndex() == 3:
                for i in range(len(self.my_conv.convolution_width_1)):
                    if self.my_conv.convolution_width_1[i] < self.my_conv.convolution_width_2[i]:
                        there_is_width_top_problem = True
                        break
            destination_cases = {
                "file": {
                    "condition": self.ui.dstntn_tab.currentIndex() <= 0,
                    "focus": self.ui.dstntn_file,
                    "elements": [self.ui.dstntn_file],
                    "styles": [BTN_ERROR],
                },
                "linear": {
                    "condition": self.ui.dstntn_tab.currentIndex() == 1,
                    "focus": self.dstntn_linear_start,
                    "elements": [self.dstntn_linear_start, self.dstntn_linear_stop, self.dstntn_linear_step],
                    "styles": [LE_ERROR, LE_ERROR, LE_ERROR],
                }
            }
            convolution_cases = {
                "file": {
                    "condition": self.ui.conv_tab.currentIndex() <= 0,
                    "focus": self.ui.conv_file,
                    "elements": [self.ui.conv_file],
                    "styles": [BTN_ERROR]
                },
                "linear": {
                    "condition": self.ui.conv_tab.currentIndex() == 1,
                    "focus": self.conv_wdth_1_start,
                    "elements": [self.conv_wdth_1_start, self.conv_wdth_1_stop, self.conv_wdth_2_start, self.conv_wdth_2_stop],
                    "styles": [LE_ERROR, LE_ERROR, LE_ERROR, LE_ERROR]
                },
                "const": {
                    "condition": self.ui.conv_tab.currentIndex() == 2,
                    "focus": self.conv_wdth_1_const,
                    "elements": [self.conv_wdth_1_const, self.conv_wdth_2_const],
                    "styles": [LE_ERROR, LE_ERROR]
                },
            }
            verifications = {
                "destination step": {
                    "condition": self.ui.dstntn_tab.currentIndex() == 1 and self.dstntn_linear_step.value() > np.fabs(self.dstntn_linear_stop.value() - self.dstntn_linear_start.value()),
                    "warning": "Destination wavelength step is too big!\nTo continue, please enter a correct step value.",
                    "focus": self.dstntn_linear_step,
                    "elements": [self.dstntn_linear_step],
                    "styles": [LE_ERROR],
                },
                "convolution ratio": {
                    "condition": self.conv_gauss_part.value() < 0 or self.conv_gauss_part.value() > 1,
                    "warning": "Gauss ration must be between 0 and 1!\nTo continue, please enter a correct value.",
                    "focus": self.conv_gauss_part,
                    "elements": [self.conv_gauss_part],
                    "styles": [LE_ERROR],
                },
                "convolution truncation < 0": {
                    "condition": self.conv_truncation.value() <= 0,
                    "warning": "Truncation must be grater than 0!\nTo continue, please enter a correct value.",
                    "focus": self.conv_truncation,
                    "elements": [self.conv_truncation],
                    "styles": [LE_ERROR],
                },
                "destination wavelength size != convolution width size": {
                    "condition": len(self.my_conv.destination_wavelength)!= len(self.my_conv.convolution_width_1),
                    "warning": "Destination wavelength and convolution width have different sizes!\nTo continue, please fix this problem.",
                    "focus": destination_cases,
                    "elements": convolution_cases,
                    "styles": None,
                },
                "width < top": {
                    "condition": there_is_width_top_problem,
                    "warning": "The width must be greater than the top!\nTo continue, please fix this problem.",
                    "focus": convolution_cases,
                    "elements": convolution_cases,
                    "styles": None,
                },
            }
            for verification in verifications.values():
                if verification["condition"]:
                    self.show_error_dialog(verification["warning"], "Warning")
                    if verification["styles"]:
                        verification["focus"].setFocus()
                        for i, element in enumerate(verification["elements"]):
                            element.setStyleSheet(verification["styles"][i])
                        return False
                    else:
                        if verification["focus"] != verification["elements"]:
                            for value_1 in verification["focus"].values():
                                for value_2 in verification["elements"].values():
                                    if value_1["condition"] and value_2["condition"]:
                                        value_1["focus"].setFocus()
                                        for i, element in enumerate(value_1["elements"]):
                                            element.setStyleSheet(value_1["styles"][i])
                                        for i, element in enumerate(value_2["elements"]):
                                            element.setStyleSheet(value_2["styles"][i])
                                        return False
                        else:
                            for value in verification["focus"].values():
                                if value["condition"]:
                                    value["focus"].setFocus()
                                    for i, element in enumerate(value["elements"]):
                                        element.setStyleSheet(value["styles"][i])
                                    return False
            self.reset_destination_style()
            self.reset_convolution_style()
            return True
        except Exception as e:
            message = f"Error in all_inputs_correct: {e}"
            print(message)
            self.show_error_dialog(message)
            return False

    # DATA READERS
    def spectrum_read(self):
        """
            Set spectrum within the my_conv (ConvolutionCore instance).

            This function checks for the existence of spectrum files and uses user-defined settings to read spectrum width directly from files,
            set it using a constant value, or put it to np.NaN is no spectrum width is provided. It then plots the spectrum graph based on the processed data.

        :return: None
        	The function returns nothing, but creates changes by reading the spectrum file, processing the data, and plotting the graph.
        """
        try:
            if os.path.isfile(self.my_conv.spectrum_file_path) and self.ui.spctrm_unit.currentIndex() > 0 and self.ui.spctrm_wlth_clm.currentIndex() > 0 and self.ui.spctrm_inty_clm.currentIndex() > 0:
                if self.ui.spctrm_tab.currentIndex() <= 0:
                    if os.path.isfile(self.my_conv.spectrum_width_path) and self.ui.spctrm_wdth_clm.currentIndex() >= 1:
                        self.my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(self.ui.spctrm_unit.currentText(), self.my_conv.spectrum_file_path, self.ui.spctrm_wlth_clm.currentIndex() - 1, self.ui.spctrm_inty_clm.currentIndex() - 1, self.my_conv.spectrum_width_path, self.ui.spctrm_wdth_clm.currentIndex() - 1)
                        self.spectrum_graph_plot()
                    else:
                        self.my_conv.spectrum_setter_spectrum_from_file_and_its_width_from_file(self.ui.spctrm_unit.currentText(), self.my_conv.spectrum_file_path, self.ui.spctrm_wlth_clm.currentIndex() - 1, self.ui.spctrm_inty_clm.currentIndex() - 1, "", np.NAN)
                        self.spectrum_graph_plot()
                else:
                    if not np.isnan(self.spctrm_wdth_const.value()):
                        self.my_conv.spectrum_setter_spectrum_from_file_and_its_width_constant(self.ui.spctrm_unit.currentText(), self.my_conv.spectrum_file_path, self.ui.spctrm_wlth_clm.currentIndex() - 1, self.ui.spctrm_inty_clm.currentIndex() - 1, self.spctrm_wdth_const.value())
                        self.spectrum_graph_plot()
                    else:
                        self.my_conv.spectrum_setter_spectrum_from_file_and_its_width_constant(self.ui.spctrm_unit.currentText(), self.my_conv.spectrum_file_path, self.ui.spctrm_wlth_clm.currentIndex() - 1, self.ui.spctrm_inty_clm.currentIndex() - 1, np.NAN)
                        self.spectrum_graph_plot()
        except Exception as e:
            message = f"Error in spectrum_read: {e}"
            print(message)
            self.show_error_dialog(message)

    def destination_read(self):
        """
            Reads and sets the destination based on user selections and input values.

            This function handles different behaviors depending on the tab and input the user has selected.
            It actions my_conv to reads the destination file, also it sets the destination parameters and plots the destination graph.

        :return: None
        """
        try:
            if self.ui.dstntn_tab.currentIndex() <= 0:
                if not self.is_preset_activated:
                    if os.path.isfile(self.my_conv.destination_file_path) and self.ui.dstntn_unit.currentIndex() > 0 and self.ui.dstntn_wlth_clm.currentIndex() > 0:
                        self.my_conv.destination_setter_from_file(self.ui.dstntn_unit.currentText(), self.my_conv.destination_file_path, self.ui.dstntn_wlth_clm.currentIndex() - 1)
                        self.destination_graph_plot()
                else:
                    self.my_conv.destination_unit = self.ui.dstntn_unit.currentText()
                    self.my_conv.destination_intensity = np.zeros(0)
                    self.my_conv.destination_final_set_up()
                    self.destination_graph_plot()
            elif self.ui.dstntn_tab.currentIndex() == 1:
                if self.ui.dstntn_unit.currentIndex() > 0 and np.fabs(self.dstntn_linear_stop.value() - self.dstntn_linear_start.value()) >= self.dstntn_linear_step.value():
                    self.my_conv.destination_setter_linear_function(self.ui.dstntn_unit.currentText(), self.dstntn_linear_start.value(), self.dstntn_linear_stop.value(), self.dstntn_linear_step.value())
                    self.destination_graph_plot()
        except Exception as e:
            message = f"Error in destination_read: {e}"
            print(message)
            self.show_error_dialog(message)

    def conv_read(self):
        try:
            if self.ui.conv_tab.currentIndex() == 0:
                if not self.is_preset_activated:
                    self.my_conv.convolution_setter_width_from_file(self.conv_type.currentIndex() - 1, self.conv_gauss_part.value(), self.conv_truncation.value(), self.conv_extrap.currentIndex(), self.my_conv.convolution_file_path, self.ui.conv_wdth_1_clm.currentIndex() - 1, self.ui.conv_wdth_2_clm.currentIndex() - 1)
                else:
                    self.my_conv.convolution_type = self.conv_type.currentIndex() - 1
                    self.my_conv.convolution_gauss_ratio = self.conv_gauss_part.value()
                    self.my_conv.convolution_truncation = self.conv_truncation.value()
                    self.my_conv.convolution_extrapolation_type = self.conv_extrap.currentIndex()
                    self.my_conv.convolution_final_set_up()
            elif self.ui.conv_tab.currentIndex() == 1:
                self.my_conv.convolution_setter_width_linear_function(self.conv_type.currentIndex() - 1, self.conv_gauss_part.value(), self.conv_truncation.value(), self.conv_extrap.currentIndex(), self.conv_wdth_1_start.value(), self.conv_wdth_1_stop.value(), self.conv_wdth_2_start.value(), self.conv_wdth_2_stop.value())
            elif self.ui.conv_tab.currentIndex() == 2:
                self.my_conv.convolution_setter_width_constant(self.conv_type.currentIndex() - 1, self.conv_gauss_part.value(), self.conv_truncation.value(), self.conv_extrap.currentIndex(), self.conv_wdth_1_const.value(), self.conv_wdth_2_const.value())
        except Exception as e:
            message = f"Error in conv_read: {e}"
            print(message)
            self.show_error_dialog(message)

    # CONVOLUTION CALC
    def convolution_calc(self):
        """
            Perform convolution calculations if applicable and update the graph and status.

            This function verifies the presence and correctness of all required inputs,
            checks the applicability of convolution, and performs the necessary calculations
            if the conditions are met. It updates the graph with the convolution results
            and displays informational or error dialogs based on the results.

        :return: None
            The function returns nothing, but updates the graph and status based on the
            convolution calculation results.
        """
        try:
            if self.all_inputs_here():  # are there all inputs?
                if self.all_inputs_correct():  # are all inputs correct?
                    if self.convolution_applicability_and_extrapolation():  # do calculations if convolution is applicable (or forced by the user)
                        self.my_conv.convolution_calc()
                        self.convolution_graph.setData(self.my_conv.destination_wavelength, self.my_conv.destination_intensity)
                        self.convolution_is_calculated = True
                        if not self.tests_are_running:
                            if self.conservation_tolerance < 100 * np.fabs(1 - self.my_conv.destination_surface_area / self.my_conv.spectrum_surface_area):
                                self.show_error_dialog("The conditions for the applicability of convolution are not fulfilled:"
                                                  "\nthe area under the curve is not preserved.\n"
                                                  "\nThe difference between the area under the curve for the convolution result"
                                                  f"\nand for the high-resolution spectrum is {100 * np.fabs(1 - self.my_conv.destination_surface_area / self.my_conv.spectrum_surface_area):.4f} %.\n"
                                                  "\n\n(Here we should advise what to do, but I don't know what to write here).", "Warning")
                            self.show_info_dialog("Test parameters:\n"
                                           f"\nNormalization (mean): {self.my_conv.mean_truncated_convolution_function_area}\n"
                                           f"\nSpectrum area: {self.my_conv.spectrum_surface_area}\n"
                                           f"\nDestination area: {self.my_conv.destination_surface_area}\n"
                                           f"\nDestination/spectrum area: {100 * self.my_conv.destination_surface_area / self.my_conv.spectrum_surface_area:.4f} %", "Test window")
        except Exception as e:
            message = f"Error in convolution_calc: {e}"
            print(message)
            self.show_error_dialog(message)

    # APPLICABILITY & EXTRAPOLATION
    def convolution_applicability_and_extrapolation(self):
        """
            Checks the applicability of convolution based on specific conditions and handles extrapolation if necessary.

            The function verifies various conditions to determine if convolution can be applied with the given parameters.
            It displays warnings and confirmations for conditions that are not met and requires user confirmation to proceed.
            If all conditions are met or the user chooses to proceed despite the warnings, the function allows convolution to happen.
            It also handles spectrum extrapolation if required.

        :return: bool
        	True if convolution can proceed, False otherwise.
        """
        try:
            if not self.tests_are_running:
                # garbage warnings
                if self.my_conv.spectrum_garbage:
                    reply = QMessageBox.question(self, "Spectrum non-numeric fragments", "In the spectrum file, some non-numeric fragments (text or NaN) were detected in the data block\n"
                                                                                         "or the data block has an inhomogeneous format.\n"
                                                                                         "These fragments were ignored. Some data may be lost.\n"
                                                                                         "Would you like to calculate with the rest of data?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                    if reply != QMessageBox.StandardButton.Yes:
                        return False
                if self.my_conv.spectrum_width_garbage:
                    reply = QMessageBox.question(self, "Spectrum width non-numeric fragments", "In the spectrum width file, some non-numeric fragments (text or NaN) were detected in the data block\n"
                                                                                               "or the data block has an inhomogeneous format.\n"
                                                                                               "These fragments were ignored. Some data may be lost.\n"
                                                                                               "Would you like to calculate with the rest of data?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                    if reply != QMessageBox.StandardButton.Yes:
                        return False
                if self.my_conv.destination_garbage:
                    reply = QMessageBox.question(self, "Destination non-numeric fragments", "In the destination file, some non-numeric fragments (text or NaN) were detected in the data block\n"
                                                                                             "or the data block has an inhomogeneous format.\n"
                                                                                             "These fragments were ignored. Some data may be lost.\n"
                                                                                             "Would you like to calculate with the rest of data?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                    if reply != QMessageBox.StandardButton.Yes:
                        return False
                if self.my_conv.convolution_width_garbage:
                    reply = QMessageBox.question(self, "Convolution width non-numeric fragments", "In the convolution width(s) file, some non-numeric fragments (text or NaN) were detected in the data block\n"
                                                                                                  "or the data block has an inhomogeneous format.\n"
                                                                                                  "These fragments were ignored. Some data may be lost.\n"
                                                                                                  "Would you like to calculate with the rest of data?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                    if reply != QMessageBox.StandardButton.Yes:
                        return False
                # linear destination warning
                if self.my_conv.linear_destination_warning:
                    reply = QMessageBox.question(self, "Linear destination warning", "With the given start and end values for the destination, the step value is not included in the start-end interval an integer number of times.\n"
                                                                                     "Therefore, the interval will be shortened to contain the integer number of steps."
                                                                                     f"\nThe last destination wavelength value is {self.my_conv.last_destination_value}{self.ui.dstntn_unit.currentText()}."
                                                                                     "\n\nCalculate it this way?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                    if reply != QMessageBox.StandardButton.Yes:
                        return False
                # width > 2 * step
                if not self.my_conv.convolution_width_and_destination_step_verification():
                    reply = QMessageBox.question(self, "width < 2 * step!", "One of conditions for the applicability of convolution is not fulfilled."
                                                                            "\nThe sampling step of the destination spectrum did not satisfy the sampling condition (step ~ 0.5 resolution (FWHM)) to garant high photometric accuracy."
                                                                            "\n\nCalculate it anyway?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                    if reply != QMessageBox.StandardButton.Yes:
                        return False
                # T > n * width
                if not self.my_conv.truncation_and_width_condition():
                    n = self.my_conv.n_truncation_values[self.my_conv.convolution_type]
                    reply = QMessageBox.question(self, f"truncation < {n} * width!", "One of conditions for the applicability of convolution is not fulfilled."
                                                                                     "\nThe current truncation of the convolution function did not garant high photometric accuracy."
                                                                                     f"\nIt must be greater than {n} times the resolution (FWHM)."
                                                                                     "\n\nCalculate it anyway?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                    if reply != QMessageBox.StandardButton.Yes:
                        return False
                # width_d > width_s
                if (self.ui.spctrm_tab.currentIndex() <= 0 and self.ui.spctrm_wdth_clm.currentIndex() > 0) or (self.ui.spctrm_tab.currentIndex() == 1 and not np.isnan(self.spctrm_wdth_const.value())):
                    str_interval, len_interval_array = self.my_conv.width_condition()
                    if str_interval:
                        reply = QMessageBox.question(self, "width condition", "One of conditions for the applicability of convolution is not fulfilled."
                                                                              "\nThe resolution of the destination spectrum is higher (lower FWHM) than that of the original data, at least over part of the spectrum:"
                                                                              f"\n{str_interval} {self.my_conv.spectrum_unit_original}."
                                                                              f"\nSpurious results may occurs in {'this range' if len_interval_array == 2 else 'these ranges'}."
                                                                              "\n\nCalculate it anyway?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                        if reply != QMessageBox.StandardButton.Yes:
                            return False
                # extrapolation
                if self.data_extrapolation_verif():
                    reply = QMessageBox.question(self, "Extrapolation?", "There's not enough data in the spectrum.\n" + "\n".join(self.my_conv.spectrum_wavelength_bounds_check()) + "\n\nDo you want to extrapolate it?",
                                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)
                    if reply == QMessageBox.StandardButton.Yes:
                        self.my_conv.spectrum_extrapolation()
                    elif reply == QMessageBox.StandardButton.Cancel:
                        return False
            else:
                self.my_conv.spectrum_extrapolation()
            return True
        except Exception as e:
            print(f"Error in mx:convolution_applicability_and_extrapolation: {e}")
            return False

    def data_extrapolation_verif(self):
        """
            Verify the validity of the data extrapolation.

            This function checks if the spectrum wavelength bounds are within acceptable limits.
            It attempts to validate the data and returns a boolean indicating the success of the validation.

        :return: bool
            A boolean value indicating whether the data extrapolation is valid.
        """
        try:
            if self.my_conv.spectrum_wavelength_bounds_check():
                return True
            return False
        except Exception as e:
            print(f"Error in mx:data_extrapolation_verif: {e}")
            return False

    def destination_export(self):
        """
            Exports the destination wavelength to a text file.

            This function generates a string for export, prompts the user to name and save the file
            via a file dialog, and writes the string to the specified file location.

        :return: None
        """
        try:
            # str to export
            str_to_export = self.prepare_destination_wavelength_to_export()
            if str_to_export:
                # file name
                if settings.value("export_destination_dir"):
                    save_file_name = settings.value("export_destination_dir") + "/" + "destination_convolution_export.txt"
                else:
                    save_file_name = "destination_convolution_export.txt"
                # file dialog
                file_name, _ = QFileDialog.getSaveFileName(self, "Save File", save_file_name, "Text Files (*.txt)",)
                # save
                if file_name:
                    settings.setValue("export_destination_dir", file_name[:file_name.rfind("/")])
                    with open(file_name, 'w+') as file_output:
                        file_output.write(str_to_export)
        except Exception as e:
            message = f"Error in destination_export: {e}"
            print(message)
            self.show_error_dialog(message)

    def prepare_destination_wavelength_to_export(self):
        """
            Prepares a formatted string for destination wavelength to export based on given inputs.

            This function checks whether all the necessary inputs for destination and convolution are present and correct.
            If the inputs are in place and valid, it prepares a string containing relevant convolution data, headers, and formatted
            destination wavelength values ready for export.

        :return str_result: str
        	A formatted string containing convolution function details and destination wavelength data or an error message string.
        """
        try:
            str_result = ""
            if self.all_inputs_here_destination() and self.all_inputs_here_convolution():
                if self.all_inputs_correct():
                    # header
                    str_result = str_result + f"convolution function: {self.conv_type.currentText()}"
                    if self.conv_type.currentIndex() == 6:
                        str_result = str_result + f", Gauss function part: {self.conv_gauss_part.value()}"
                    str_result = str_result + f"\n"
                    file_separator = "\t"
                    if self.conv_type.currentIndex() != 3:
                        if self.conv_type.currentIndex() in [5, 6]:
                            str_result = str_result + f"destination_wavelength_{self.ui.dstntn_unit.currentText()}{file_separator}destination_width_Gauss{file_separator}destination_width_Lorentz\n"
                        else:
                            str_result = str_result + f"destination_wavelength_{self.ui.dstntn_unit.currentText()}{file_separator}destination_width\n"
                    else:
                        str_result = str_result + f"destination_wavelength_{self.ui.dstntn_unit.currentText()}{file_separator}destination_width{file_separator}destination_top\n"
                    # data
                    for i in range(len(self.my_conv.destination_wavelength)):
                        str_result = str_result + f"{self.my_conv.destination_wavelength[i]}"
                        str_result = str_result + f"{file_separator}"
                        if len(self.my_conv.convolution_width_1) == len(self.my_conv.destination_wavelength):
                            str_result = str_result + f"{self.my_conv.convolution_width_1[i]}"
                        else:
                            str_result = str_result + f"0"
                        if self.conv_type.currentIndex() in [3, 5, 6]:
                            str_result = str_result + f"{file_separator}"
                            if len(self.my_conv.convolution_width_2) == len(self.my_conv.destination_wavelength):
                                str_result = str_result + f"{self.my_conv.convolution_width_2[i]}"
                            else:
                                str_result = str_result + f"0"
                        str_result = str_result + f"\n"
            return str_result
        except Exception as e:
            message = f"Error in prepare_destination_wavelength_to_export: {e}"
            print(message)
            self.show_error_dialog(message)
            return ""

    def convoluted_spectrum_export(self):
        """
            Exports the convoluted spectrum if it has been calculated.

            This function attempts to export the convolution results to a file.
            If the convolution has not been calculated, an error dialog is shown.

        :return: None
        """
        try:
            if self.convolution_is_calculated:
                ConvolutionExportW(self.my_conv.destination_wavelength, self.my_conv.destination_intensity,
                                   self.my_conv.spectrum_separator, self.my_conv.spectrum_file_path,
                                   self.my_conv.destination_unit, self.my_conv.revers_order_destination)
            else:
                self.show_error_dialog("Nothing to export yet!\n")
        except Exception as e:
            message = f"Error in convoluted_spectrum_export: {e}"
            print(message)
            self.show_error_dialog(message)

    @staticmethod
    def graph_help():
        """
        	Starts GraphHelp class that generates a window with information on how to use the graph.
        """
        GraphHelp()

    @staticmethod
    def convolution_functions_help():
        """
        	Runs ConvolutionFunctionsHelp class that generates a window detailing the convolutional futures.
        """
        ConvolutionFunctionsHelp()

    @staticmethod
    def truncation_help():
        """
            Launches TruncationHelp class that shows a window where one can learn more about truncation.
        """
        TruncationHelp()

    @staticmethod
    def extrapolation_help():
        """
            Invokes ExtrapolationHelp class that generates a window where one can learn about the extrapolation methods proposed in the given project.
        """
        ExtrapolationHelp()


class ConvolutionExportW(QtWidgets.QDialog):
    def __init__(self, destination_wavelength, destination_intensity, separator, spectrum_file_path, destination_unit, revers_order, tests_are_running=False):
        super(ConvolutionExportW, self).__init__()
        self.ui = Ui_ExportWindow()
        self.ui.setupUi(self)
        self.class_setter(destination_wavelength, destination_intensity, separator, spectrum_file_path, destination_unit, revers_order, tests_are_running)
        self.setWindowTitle("Export parameters")
        self.set_UI()
        # buttons
        self.ui.btn_export.setStyleSheet(BTN_BIG)
        self.ui.btn_export.clicked.connect(self.export)
        # WINDOW show
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        if not tests_are_running:
            self.show()
            self.exec()

    def class_setter(self, destination_wavelength, destination_intensity, separator, spectrum_file_path, destination_unit, revers_order, tests_are_running):
        """
            Sets the attributes of the class based on the provided parameters.

            This function initializes or updates the class attributes with the given
            parameters. It sets attributes for wavelength, intensity, separator,
            spectrum file path, unit, order of data, and test running status.

        :param destination_wavelength: np.array
            Wavelength data.
        :param destination_intensity: np.array
            Intensity data .
        :param separator: str
            Separator to be used for data handling.
        :param spectrum_file_path: str
            Path to the spectrum file.
        :param destination_unit: str
            Unit to be used for the data.
        :param revers_order: bool
            Boolean indicating if the order of data should be reversed.
        :param tests_are_running: bool
            Boolean indicating if the tests are running.
        :return: None
        """
        try:
            self.wavelength = destination_wavelength
            self.intensity = destination_intensity
            self.separator = separator
            self.spectrum_path = spectrum_file_path
            self.order = revers_order
            self.unit = destination_unit
            self.tests_are_running = tests_are_running
        except Exception as e:
            print(f"Error in export:class_setter: {e}")

    def set_UI(self):
        """
            Sets up the user interface for exporting parameters of the convolution result for the high-resolution spectrum.

            This function initializes various UI components such as the title, spectrum, intensity, and separator.

        :return: None
        """
        try:
            # title
            self.ui.title.setText(f"Export parameters for the convolution result for the high-resolution spectrum:\n{self.spectrum_path}")
            # spectrum
            self.set_UI_spectrum()
            # intensity
            self.set_UI_intensity()
            # separator
            self.set_UI_separator()
        except Exception as e:
            print(f"Error in export:set_UI: {e}")

    def set_UI_spectrum(self):
        """
            Sets the UI spectrum.

            This function sets up various UI components related to the wavelength spectrum such as
            units, format, digits, and order. It assigns default values and configurations for
            each component and handles settings based on given parameters.

        :return: None
        """
        try:
            # unit
            self.ui.cb_wlth_unit.setStyleSheet(QCB_NORMAL)
            unit_list = ["cm-1", "micron", "nm", "A"]
            self.ui.cb_wlth_unit.insertItems(0, unit_list)
            index_set_choice = {
                "cm-1": 0,
                "micron": 1,
                "nm": 2,
                "A": 3,
            }
            self.ui.cb_wlth_unit.setCurrentIndex(index_set_choice[self.unit])
            # format
            self.set_format(self.ui.cb_wlth_format, "wavelength format")
            # digits
            self.set_digits(self.ui.cb_wlth_digits, "wavelength digits")
            # order
            self.ui.cb_wlth_order.setStyleSheet(QCB_NORMAL)
            order_list = ["ascending", "descending"]
            self.ui.cb_wlth_order.insertItems(0, order_list)
            default_order = 1 if self.order or self.unit == "cm-1" else 0
            self.set_settings_for_QCB(self.ui.cb_wlth_order, "wavelength order", default_order)
        except Exception as e:
            print(f"Error in export:set_UI_spectrum: {e}")

    def set_UI_intensity(self):
        """
            Configures the UI elements related to intensity settings.

            This method sets the format and digits for intensity, and updates the style
            and options for the column names combobox element.

        :return: None
        """
        try:
            # format
            self.set_format(self.ui.cb_inty_format, "intensity format")
            # digits
            self.set_digits(self.ui.cb_inty_digits, "intensity digits")
            # column names
            self.ui.cb_clmn_names.setStyleSheet(QCB_NORMAL)
            names_options = ["with column names", "no column names"]
            self.ui.cb_clmn_names.insertItems(0, names_options)
            self.set_settings_for_QCB(self.ui.cb_clmn_names, "column names", 0)
        except Exception as e:
            print(f"Error in export:set_UI_intensity: {e}")

    def set_UI_separator(self):
        """
            Sets up the UI components for the separator selection.

            This function configures the UI dropdown for separator selection, connects necessary signals,
            and sets initial values based on application settings. It also manages the visibility and
            text of the custom separator text box based on saved settings.

        :return: None
        """
        try:
            self.ui.cb_separators.setStyleSheet(QCB_NORMAL)
            separators_list = ["as in the spectrum file", "Tab", "Space", "Comma", "Other"]
            self.ui.cb_separators.insertItems(0, separators_list)
            self.ui.cb_separators.currentIndexChanged.connect(self.separator_toggle)
            self.set_settings_for_QCB(self.ui.cb_separators, "separator", 0)
            self.ui.pte_separator.hide()
            if settings.value("export_parameters") and "separator" in settings.value("export_parameters").keys() and settings.value("export_parameters")["separator"] == 4:
                self.ui.pte_separator.show()
            if settings.value("export_parameters") and "custom separator" in settings.value("export_parameters").keys():
                self.ui.pte_separator.setPlainText(settings.value("export_parameters")["custom separator"])
        except Exception as e:
            print(f"Error in export:set_UI_separator: {e}")

    def set_format(self, format_field, settings_parameter):
        """
            Set the format of the given field and update settings accordingly.

            This function sets the style of the format_field widget, inserts a predefined
            list of formatting options into it, and sets the settings based on the selected option.

        :param format_field: QComboBox
            The widget field where the format options will be set.
        :param settings_parameter: str
            The settings parameter that will be updated based on the format selected.

        :return: None
        """
        try:
            format_field.setStyleSheet(QCB_NORMAL)
            format_list = ["decimal (0.12345)", "exponential (1.2345e-01)"]
            format_field.insertItems(0, format_list)
            self.set_settings_for_QCB(format_field, settings_parameter, 0)
        except Exception as e:
            print(f"Error in export:set_format: {e}")

    def set_digits(self, digits_field, settings_parameter):
        """
            Set the digits combo box with a list of digit options and apply settings.

            This function sets the style of the given digits combo box, populates it
            with digit options, and then applies certain settings.

        :param digits_field: QComboBox
        	This is the combo box where digit options are set.
        :param settings_parameter: ParameterType
        	Specific settings to be applied to the combo box.

        :return: None
        """
        try:
            digits_field.setStyleSheet(QCB_NORMAL)
            digit_list = [str(i) for i in range(0, 17)]
            digits_field.insertItems(1, digit_list)
            self.set_settings_for_QCB(digits_field, settings_parameter, 6)
        except Exception as e:
            print(f"Error in export:set_digits: {e}")

    @staticmethod
    def set_settings_for_QCB(field, settings_parameter, default_value):
        """
        	Sets the settings for a given field from QSettings or defaults if not found.

        	This function attempts to set the current index of a field based on parameters stored in QSettings.
        	If the parameter is not found in the settings, a default value is used instead.

        :param field: QComboBox
            The QComboBox field to set the index for.
        :param settings_parameter: str
            The key to look up in the QSettings export_parameters dictionary.
        :param default_value: int
            The default index value to set if the settings parameter is not found.

        :return: None
        """
        try:
            if settings.value("export_parameters") and settings_parameter in settings.value("export_parameters").keys():
                field.setCurrentIndex(settings.value("export_parameters")[settings_parameter])
            else:
                field.setCurrentIndex(default_value)
        except Exception as e:
            print(f"Error in export:set_settings_for_QCB: {e}")

    def show_error_dialog(self, message, title="Error!"):
        """
            Show an error dialog with a critical icon.

            Displays an error message in a dialog box with an optional title.

        :param message: str
        	Message to be displayed in the dialog box.
        :param title: str, optional
        	Title of the dialog box. Default is "Error!".

        :return: None
        """
        try:
            if not self.tests_are_running:
                dlg = QMessageBox(self)
                dlg.setWindowTitle(title)
                dlg.setText(message)
                dlg.setIcon(QMessageBox.Icon.Critical)
                dlg.exec()
        except Exception as e:
            print(f"Error in export:show_error_dialog: {e}")

    def separator_toggle(self):
        """
            Toggles the visibility of the pte_separator widget based on the current index of cb_separators.

            This function checks the current index of the combo box (cb_separators) and shows or hides
            the pte_separator widget accordingly.

        :return: None
        """
        try:
            if self.ui.cb_separators.currentIndex() == 4:
                self.ui.pte_separator.show()
            else:
                self.ui.pte_separator.hide()
        except Exception as e:
            message = f"Error in export:separator_toggle: {e}"
            print(message)
            self.show_error_dialog(message)

    def export(self):
        """
            Exports a string to a text file.

            The function generates a string to be exported and determines the file name
            based on user settings and the current spectrum path. It then opens a file dialog
            to save the file, and once saved, it closes the file.

        :return: None
        """
        try:
            # str to export
            export_str = self.str_to_export()
            # file name
            if settings.value("export_dir"):
                save_file_name = settings.value("export_dir") + self.spectrum_path[self.spectrum_path.rfind('/'):self.spectrum_path.rfind('.')] + f"_conv_{self.ui.cb_wlth_unit.currentText()}.txt"
            else:
                save_file_name = self.spectrum_path[:self.spectrum_path.rfind('.')] + "_conv.txt"
            # file dialog
            file_name, _ = QFileDialog.getSaveFileName(self, "Save File", save_file_name, "Text Files (*.txt)")
            # export & close
            self.save_and_close(file_name, export_str)
        except Exception as e:
            message = f"Error in export:export: {e}"
            print(message)
            self.show_error_dialog(message)

    def save_and_close(self, file_path, export_str):
        """
            Saves the export string to the specified file and updates settings.

            This function writes the provided export string to the given file, updates relevant
            settings, and closes the current interface.

        :param file_path: str
        	The file path in which to save the export string.
        :param export_str: str
        	The content to be written to the specified file.
        :return: None
        """
        try:
            if file_path:
                settings.setValue("export_dir", file_path[:file_path.rfind("/")])
                with open(file_path, 'w+') as file_output:
                    file_output.write(export_str)
                param_dict = {"wavelength format": self.ui.cb_wlth_format.currentIndex(),
                              "wavelength digits": self.ui.cb_wlth_digits.currentIndex(),
                              "wavelength order": self.ui.cb_wlth_order.currentIndex(),
                              "intensity format": self.ui.cb_inty_format.currentIndex(),
                              "intensity digits": self.ui.cb_inty_digits.currentIndex(),
                              "column names": self.ui.cb_clmn_names.currentIndex(),
                              "separator": self.ui.cb_separators.currentIndex(),
                              "custom separator": self.ui.pte_separator.toPlainText()}
                settings.setValue("export_parameters", param_dict)
                self.close()
        except Exception as e:
            message = f"Error in export:save_and_close: {e}"
            print(message)
            self.show_error_dialog(message)

    def str_to_export(self):
        """
            Constructs and formats a string representation of wavelength and intensity data for export.

            The function processes the wavelength and intensity attributes of the instance, applying
            selected formatting options for separators, units, and order. It also formats the data
            according to user-specified precision and notation styles before assembling the output string.

        :return: str
        	The fully formatted string ready for export, containing wavelength and intensity data.
        """
        try:
            # str to export
            export_str = ""
            ## separator
            separator_options = {
                0: self.separator,
                1: "\t",
                2: " ",
                3: ",",
                4: self.ui.pte_separator.toPlainText(),
            }
            separator = separator_options[self.ui.cb_separators.currentIndex()]
            ## units
            if self.unit != self.ui.cb_wlth_unit.currentText():
                self.wavelength = conv_core.change_unit(self.wavelength, self.unit, self.ui.cb_wlth_unit.currentText())
            ## order
            if self.ui.cb_wlth_order.currentIndex() <= 0:
                if len(self.wavelength) > 1 and self.wavelength[0] > self.wavelength[1]:
                    self.wavelength = np.flip(self.wavelength)
                    self.intensity = np.flip(self.intensity)
            elif self.ui.cb_wlth_order.currentIndex() == 1:
                if len(self.wavelength) > 1 and self.wavelength[0] < self.wavelength[1]:
                    self.wavelength = np.flip(self.wavelength)
                    self.intensity = np.flip(self.intensity)
            ## columns names
            if self.ui.cb_clmn_names.currentIndex() == 0:
                export_str = export_str + f"wavelength_{self.ui.cb_wlth_unit.currentText()}{separator}intensity\n"
            ## data to str
            for i in range(len(self.wavelength)):
                if self.ui.cb_wlth_format.currentIndex() == 0:
                    export_str = export_str + float_to_str(self.wavelength[i], self.ui.cb_wlth_digits.currentIndex(), "f")
                elif self.ui.cb_wlth_format.currentIndex() == 1:
                    export_str = export_str + float_to_str(self.wavelength[i], self.ui.cb_wlth_digits.currentIndex(), "e")
                export_str = export_str + separator
                if self.ui.cb_inty_format.currentIndex() == 0:
                    export_str = export_str + float_to_str(self.intensity[i], self.ui.cb_inty_digits.currentIndex(), "f")
                elif self.ui.cb_inty_format.currentIndex() == 1:
                    export_str = export_str + float_to_str(self.intensity[i], self.ui.cb_inty_digits.currentIndex(), "e")
                export_str = export_str + "\n"
            return export_str
        except Exception as e:
            message = f"Error in export:str_to_export: {e}"
            print(message)
            self.show_error_dialog(message)
            return ""


class GraphHelp(QtWidgets.QDialog):
    """
        help window for the graphs
    """
    def __init__(self):
        super(GraphHelp, self).__init__()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self)
        # GUI
        # title
        self.setWindowTitle(f'Graph help')
        win_width = 900
        self.resize(win_width, 700)
        self.browser = QWebEngineView()
        self.browser.resize(win_width, 700)
        html_content = "<!DOCTYPE html><html><style>.center {display: block; margin-left: auto; margin-right: auto;} .plot {max-width:700px;}</style><body style='font-family: sans-serif; background-color: #F0F0F0;'>"
        html_content = html_content + "<p>Some tips on how to use the graph:</p>"
        # Legend
        html_content = html_content + "<h2>Legend</h2>"
        html_content = html_content + "<p>To move the legend, drag and drop it.</p>"
        html_content = html_content + "<img class = 'center, plot' src='img/graph/legend.gif' alt='about the graph legend'/>"
        # Zoom
        html_content = html_content + "<h2>Zoom</h2>"
        html_content = html_content + "<p>To zoom in or out, move your mouse where you want to zoom and scroll on the graph.</p>"
        html_content = html_content + "<p>To pan, click and drug the graph.</p>"
        html_content = html_content + "<img class = 'center, plot' src='img/graph/zoom_pan.gif' alt='about the graph zoom & pan'/>"
        # Horizontal and vertical zooms
        html_content = html_content + "<h2>Horizontal and vertical zooms</h2>"
        html_content = html_content + "<p>To scale only horizontally or vertically, scroll on the axes.</p>"
        html_content = html_content + "<img class = 'center, plot' src='img/graph/zoom_v_h.gif' alt='about the graph horizontal zoom'/>"
        # Zoom reset
        html_content = html_content + "<h2>Zoom reset</h2>"
        html_content = html_content + "<p>To reset a zoom, click on 'A' in the lower left corner.</p>"
        html_content = html_content + "<img class = 'center, plot' src='img/graph/zoom_reset.gif' alt='about the graph re-zoom'/>"
        # Context menu
        html_content = html_content + "<h2>Context menu</h2>"
        html_content = html_content + "<p>Our graphical tool has a context menu (invoked by right-clicking on the graph) containing a number of useful functions.</p>"
        html_content = html_content + "<p>For example, the x-axis inversion. By default, our graph shows the wavelength increasing from left to right. However, to work with cm-1, it may be convenient to invert the wavelength so that it increases from right to left.</p>"
        html_content = html_content + "<img class = 'center, plot' src='img/graph/context_menu.gif' alt='about the graph context menu'/>"
        html_content = html_content + "<p>It is also worth mentioning the possibility to export the graph in jpg, png or svg formats, also available from the context menu.</p>"
        # body close
        html_content = html_content + "</body></html>"
        self.browser.setHtml(html_content,  baseUrl=QUrl.fromLocalFile(os.getcwd()+os.path.sep))
        self.ui.vl_info_box.insertWidget(0, self.browser, 0, Qt.AlignmentFlag.AlignCenter)
        # QDialog show
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.show()
        self.exec()


class ConvolutionFunctionsHelp(QtWidgets.QDialog):
    """
        help window for the convolution functions
    """
    def __init__(self):
        super(ConvolutionFunctionsHelp, self).__init__()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self)
        # GUI
        # title
        self.setWindowTitle(f'Convolution function help')
        win_width = 800
        self.resize(win_width, 550)
        self.browser = QWebEngineView()
        self.browser.resize(win_width, 550)
        html_content = "<!DOCTYPE html><html><style>.center {display: block; margin-left: auto; margin-right: auto;} .plot {max-width:700px;}</style><body style='font-family: sans-serif; background-color: #F0F0F0;'>"
        html_content = html_content + "<p>More information about the convolution functions used in our programme:</p>"
        # Gauss
        html_content = html_content + "<h2>Gauss function</h2>"
        html_content = html_content + "<p>The Gauss function is defined in its standard way:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/gauss.png' alt='Gauss function formula'/>"
        html_content = html_content + "<p>Here sigma is the standard deviation. It is related to the Full width at half maximum (FWHM) by the next formula:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/gauss_sigma.png' alt='sigma & FWHM formula for Gauss'/>"
        html_content = html_content + "<p>FWHM should be entered into the programme and then it will be converted to sigma by our algorithm.</p>"
        html_content = html_content + "<p>Here is a plot of the Gaussian function depending on sigma and mean:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/gauss_plot.png' alt='Gauss function plot'/>"
        # triangle
        html_content = html_content + "<h2>Triangle function</h2>"
        html_content = html_content + "<p>The triangle function is zero wherever the condition is satisfied:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/triangle_condition.png' alt='triangle condition formula'/>"
        html_content = html_content + "<p>The straight brackets here denote the modulus, i.e. the positive value.</p>"
        html_content = html_content + "<p>Otherwise it is equal to</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/triangle.png' alt='triangle function formula'/>"
        html_content = html_content + "<p>The sigma parameter is related to the Full width at half maximum (FWHM) by the following formula:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/FWHM_sigma.png' alt='sigma & FWHM formula for triangle'/>"
        html_content = html_content + "<p>As before FWHM should be entered into the programme and then it will be converted to sigma by our algorithm.</p>"
        html_content = html_content + "<p>Here is a plot of the triangle function depending on sigma and mean:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/triangle_plot.png' alt='triangle function plot'/>"
        # trapeze
        html_content = html_content + "<h2>Trapeze function</h2>"
        html_content = html_content + "<p>The trapeze function is zero wherever the condition is satisfied:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/trapeze_condition.png' alt='trapeze condition formula'/>"
        html_content = html_content + "<p>The straight brackets here denote the modulus, i.e. the positive value.</p>"
        html_content = html_content + "<p>If</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/trapeze_top_condition.png' alt='trapeze top formula'/>"
        html_content = html_content + "<p>than the trapeze function is constant:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/trapeze_top.png' alt='trapeze top formula'/>"
        html_content = html_content + "<p>For other values of x it is equal to</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/trapeze.png' alt='trapeze function formula'/>"
        html_content = html_content + "<p>The sigma parameter is related to the Full width at half maximum (FWHM) by the formula:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/FWHM_sigma.png' alt='sigma & FWHM formula for trapeze'/>"
        html_content = html_content + "<p>As usual FWHM should be entered into the programme and then it will be converted to sigma by our algorithm.</p>"
        html_content = html_content + "<p>Here is a plot of the trapeze function depending on sigma and mean:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/trapeze_plot.png' alt='trapeze function plot'/>"
        # Lorentz
        html_content = html_content + "<h2>Lorentz function</h2>"
        html_content = html_content + "<p>First of all, this function is also called Lorentz distribution, Cauchy-Lorentz distribution, Lorentzian function, and Breit-Wigner distribution. In mathematics it is known as the Cauchy distribution.</p>"
        html_content = html_content + "<p>In our programme we used the standard definition of this function, which is:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/lorentz.png' alt='Lorentz function formula'/>"
        html_content = html_content + "<p>Here mean is the location parameter, specifying the location of the peak of the distribution, and gamma is the scale parameter. The gamma is related to the Full width at half maximum (FWHM) by the formula:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/FWHM_gamma_Lorentz.png' alt='gamma & FWHM formula for Lorentz'/>"
        html_content = html_content + "<p>As before FWHM should be entered into the programme and then it will be converted to gamma by our algorithm.</p>"
        html_content = html_content + "<p>Here is a plot of the Lorentz function depending on gamma and mean:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/lorentz_plot.png' alt='Lorentz function plot'/>"
        # Voigt profile
        html_content = html_content + "<h2>Voigt profile</h2>"
        html_content = html_content + "<p>The Voigt profile is a probability distribution given by a convolution of a Lorentz distribution and a Gaussian distribution.</p>"
        html_content = html_content + "<p>In our programme we apply its expression through the real part Re of the Faddeeva function w(z):</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/voigt.png' alt='Voigt profile formula'/>"
        html_content = html_content + "<p>Here z is</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/z.png' alt='z variable definition'/>"
        html_content = html_content + "<p>To work with the Faddeeva function, we use the numpy module, which is a benchmark in scientific computing in Python.</p>"
        html_content = html_content + "<p>Since there are two functions involved in creating the Voigt profile, the Lorentz function and the Gaussian function, each must have its own Full width at half maximum (FWHM).</p>"
        html_content = html_content + "<p>The FWHM of each of these functions is related to the sigma of the Gaussian function and the gamma of the Lorentz function in the same way as before:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/FWHM_sigma_Gauss.png' alt='sigma & FWHM formula for the Gauss function'/>"
        html_content = html_content + "<img class = 'center' src='img/convolution/FWHM_gamma_Lorentz.png' alt='gamma & FWHM formula for the Lorentz function'/>"
        html_content = html_content + "<p>As with all other functions, FWHM should be entered into the programme and then it will be converted to gamma and sigma by our algorithm.</p>"
        html_content = html_content + "<p>As can be expected, in extreme cases, if sigma is zero, the Voigt profile turns into the Lorentz function, and if gamma is zero, into the Gauss function.</p>"
        html_content = html_content + "<p>Here is a plot of the Voigt profile depending on gamma, sigma, and mean:</p>"
        html_content = html_content + "<img class = 'center, plot' src='img/convolution/voigt_plot.png' alt='Voigt profile plot'/>"
        html_content = html_content + "<p>And here is another graph where you can better see the effect of sigma and gamma</p>"
        html_content = html_content + "<img class = 'center, plot' src='img/convolution/voigt_sigma_gamma_plot.png' alt='Voigt profile plot and sigma and gamma influence'/>"
        # pseudo-Voigt profile
        html_content = html_content + "<h2>Sum of the Lorentz and Gauss functions</h2>"
        html_content = html_content + "<p>Also called pseudo-Voigt profile. It is defined by the sum of the Lorentz and Gauss functions:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/pseudovoigt_1.png' alt='pseudo-Voigt profile formula: part 1'/>"
        html_content = html_content + "<img class = 'center' src='img/convolution/pseudovoigt_2.png' alt='pseudo-Voigt profile formula: part 2'/>"
        html_content = html_content + "<p>Here, g varies from 0 to 1 and denotes the contribution part of the Gauss function.</p>"
        html_content = html_content + "<p>As for the Voigt profile, the Lorentz function and the Gaussian function must have their own Full width at half maximum (FWHM).</p>"
        html_content = html_content + "<p>The FWHM of each of these functions is related to the sigma (of the Gauss function) and the gamma (of the Lorentz function) in the usual way:</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/FWHM_sigma_Gauss.png' alt='sigma & FWHM formula for the Gauss function'/>"
        html_content = html_content + "<img class = 'center' src='img/convolution/FWHM_gamma_Lorentz.png' alt='gamma & FWHM formula for the Lorentz function'/>"
        html_content = html_content + "<p>As before, FWHM should be entered into the programme and then it will be converted to gamma and sigma by our algorithm.</p>"
        html_content = html_content + "<p>Here is a plot of the pseudo-Voigt profile depending on gamma, sigma, and mean:</p>"
        html_content = html_content + "<img class = 'center, plot' src='img/convolution/pseudovoigt_plot.png' alt='Voigt profile plot'/>"
        html_content = html_content + "<p>This graph shows the influence of sigma and gamma parameters:</p>"
        html_content = html_content + "<img class = 'center, plot' src='img/convolution/pseudovoigt_sigma_gamma_plot.png' alt='Voigt profile plot: sigma and gamma influence'/>"
        html_content = html_content + "<p>Finally, here's a graph where you can see the impact of the g part of the Gaussian function:</p>"
        html_content = html_content + "<img class = 'center, plot' src='img/convolution/pseudovoigt_g_plot.png' alt='Voigt profile plot: Gauss function part influence'/>"
        # one plot
        html_content = html_content + "<h2>All functions plot</h2>"
        html_content = html_content + "<p>To compare the behaviour of these functions, it is interesting to show their common graph.</p>"
        html_content = html_content + "<img class = 'center' src='img/convolution/all_plot.png' alt='plot of all convolution functions'/>"
        html_content = html_content + "<p>It can be seen that the Voigt profile has the longest 'wings' and the geometric functions decline faster than the others.</p>"
        # normalization
        html_content = html_content + "<h2>Normalization</h2>"
        html_content = html_content + "<p>All these functions are normalised, their integral in the range from minus to plus infinity is equal to one.</p>"
        html_content = html_content + ("<p>When calculating convolution, it is not possible to use the interval from plus to minus infinity. Therefore, the calculation interval is limited. "
                                       "The parameter the truncation is used to define this limitation. "
                                       "Of course, the convolution function is not normalised to 1 in any possible interval. "
                                       "Our algorithm takes this into account and normalises the convolution function accordingly. "
                                       "So it is always normalised to 1 at any value of the truncation.</p>")
        html_content = html_content + "<p>More about the truncation and its effect on convolution can be found in <a href='truncation_page.html'>the relevant part of the help</>.</p>"
        # body close
        html_content = html_content + "</body></html>"
        self.browser.setHtml(html_content, baseUrl=QUrl.fromLocalFile(os.getcwd() + os.path.sep))
        self.ui.vl_info_box.insertWidget(0, self.browser, 0, Qt.AlignmentFlag.AlignCenter)
        self.browser.urlChanged.connect(self.url_change)
        # QDialog show
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.show()
        self.exec()

    def url_change(self):
        if "truncation_page.html" in str(self.browser.url()):
            self.close()
            TruncationHelp()


class TruncationHelp(QtWidgets.QDialog):
    """
        help window for the truncation
    """
    def __init__(self):
        super(TruncationHelp, self).__init__()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self)
        # GUI
        # title
        self.setWindowTitle(f'Truncation help')
        win_width = 800
        self.resize(win_width, 550)
        self.browser = QWebEngineView()
        self.browser.resize(win_width, 550)
        html_content = "<!DOCTYPE html><html><style>.center {display: block; margin-left: auto; margin-right: auto;}</style><body style='font-family: sans-serif; background-color: #F0F0F0;'>"
        html_content = html_content + "<p>More information about the truncation:</p>"
        # truncation
        html_content = html_content + "<h2>What is and why truncation</h2>"
        html_content = html_content + ("<p>The easiest way to explain it is to use the Gauss function as an example. "
                                       "This function is defined through the parameter sigma (standard deviation) in the range from minus to plus infinity.</p>")
        html_content = html_content + "<img class = 'center' src='img/truncation/gauss_plot.png' alt='Gauss function plot'/>"
        html_content = html_content + "<p>However, it is known that 99.6% of this curve lies within plus or minus 3 sigma relative to the position of its peak mean.</p>"
        html_content = html_content + "<img class = 'center' src='img/truncation/goss_sigma_plot.png' alt='Gauss plot and its sigma'/>"
        html_content = html_content + "<p>From both physics and computer science perspectives, it is hard if possible to deal with infinite data.</p>"
        html_content = html_content + "<p>Then, if we are satisfied with 99.6% accuracy, it would be convenient to work with a Gauss function within plus or minus 3 sigma.</p>"
        html_content = html_content + "<p>In this case truncation is equal to 3.</p>"
        html_content = html_content + "<p>Recall that for the Gauss function sigma is related to the Full width at half maximum (FWHM):</p>"
        html_content = html_content + "<img class = 'center' src='img/truncation/FWHM_sigma_Gauss.png' alt='sigma & FWHM formula for the Gauss function'/>"
        html_content = html_content + "<p>You can learn about the relationship of other convolution functions to the FWHM in <a href='convolution_functions.html'>the help on convolution function</a>.</p>"
        html_content = html_content + ("<p>To summarise: the truncation is the amount of sigma (or gamma for the Lorentz funcion) - and hence FWHM - by which we constrain the convolution function "
                                       "in order to simplify and speed up the computation, but also not to go beyond the available physical data.</p>")
        # normalization
        html_content = html_content + "<h2>Truncation and normalization</h2>"
        html_content = html_content + "<p>All convolution functions are normalised to 1 between plus and minus infinity.</p>"
        html_content = html_content + "<p>If we introduce the truncation, this property is obviously broken.</p>"
        html_content = html_content + "<p>Here is a plot of the dependence of the normalisation on the truncation for our convolution functions:</p>"
        html_content = html_content + "<img class = 'center' src='img/truncation/truncation_normalization.png' alt='Normalization and truncation'/>"
        html_content = html_content + ("<p>To keep the convolution function normalised to 1, our algorithm computes the normalisation value for the selected truncation and normalises to it. "
                                       "Thus, the convolution functions always remain normalised to 1.</p>")
        html_content = html_content + ("<p>It turns out that truncation does not change the normalisation. But does it mean that one can choose any value? No. "
                                       "You should also consider the effect of truncation on the resulting curve.</p>")
        # conservation
        html_content = html_content + "<h2>Truncation and conservation</h2>"
        html_content = html_content + "<p>The main advantage of convolution over, say, the decimation, is the maximally possible preservation of the area under the curve for the convoluted data.</p>"
        html_content = html_content + "<p>The following graph shows the difference between the high-resolution, convoluted and decimated curves.</p>"
        html_content = html_content + "<img class = 'center' src='img/truncation/convolution_vs_decimation.png' alt='convolution vs decimation example'/>"
        html_content = html_content + ("<p>If the resolution is lowered by a factor of 100, the area under the convoluted curve will be almost the same."
                                       "But reducing the resolution by 1000 times will create a gap: 99.99% for the convoluted curve and 99.83% for the decimated one.</p>")
        html_content = html_content + ("<p>To summarise: the use of convolution is more desirable than the decimation. "
                                       "But what about the truncation? Does it affect the preservation of the area under the convoluted curve? "
                                       "The short answer is yes.</p>")
        html_content = html_content + "<p>To explore this question, we considered two cases, the Dirac peak and the real case of the LEISA New Horizons data.</p>"
        html_content = html_content + "<p>The Dirac peak represents the point where the signal is different from zero:</p>"
        html_content = html_content + "<img class = 'center' src='img/truncation/Dirac_plot.png' alt='Dirac signal plot'/>"
        html_content = html_content + "<p>Physically, the Dirac peak is an idealised single signal, infinitely narrow and undistorted by noise.</p>"
        html_content = html_content + ("<p>Our tests of this case showed that the area under the curve as a function of the truncation will depend on many factors: "
                                       "from the type of the convolution function and its FWHM to the destination interval and its position relative to the Dirac peak.</p>")
        html_content = html_content + "<p>In the general outline, this dependence will look like this:</p>"
        html_content = html_content + "<img class = 'center' src='img/truncation/Dirac_truncation_conservation.png' alt='Truncation and conservation plot for the Dirac spike'/>"
        html_content = html_content + "<p>It can be seen that the graph has three parts.</p>"
        html_content = html_content + "<p>The beginning: a low truncation value start with a characteristic 'jagged' pattern.</p>"
        html_content = html_content + "<p>The middle: some medium truncation values where the area is best preserved.</p>"
        html_content = html_content + "<p>The ending: high values of truncation, where gradual divergence begins. Note that it does not always go in the direction of area loss; sometimes it starts to accumulate.</p>"
        html_content = html_content + "<p>Thus, we can conclude that there is some truncation interval where this parameter is most optimal.</p>"
        html_content = html_content + ("<p>For the Dirac peak we have found an empirical low, allowing us to estimate the truncation that sets the upper limit. "
                                       "We did not succeed in doing the same for the lower one.</p>")
        html_content = html_content + "<p>We do not present these results here because they cannot be extended to real cases. After all, the Dirac peak is an idealised signal.</p>"
        html_content = html_content + "<p>Our conclusions can only serve as a hypothesis that too low and too high values of truncation may lead to non-preservation of the area under the curve.</p>"
        html_content = html_content + "<p>In the real case of LEISA New Horizons data, the dependence of the area under the curve as a function of the truncation looks like this:</p>"
        html_content = html_content + "<img class = 'center' src='img/truncation/NH_truncation_conservation.png' alt='Truncation and conservation plot for the LEISA New Horizons data'/>"
        html_content = html_content + "<p>And zooming on the guide line:</p>"
        html_content = html_content + "<img class = 'center' src='img/truncation/NH_truncation_conservation_zoom.png' alt='Zoom on truncation and conservation plot for the LEISA New Horizons data'/>"
        html_content = html_content + "<p>The difference from the same plot for the Dirac peak is obvious; the area under the curve for the LEISA New Horizons data is preserved almost everywhere.</p>"
        html_content = html_content + ("<p>How then to determine the ideal truncation value for your data? "
                                       "Unfortunately, there is no exact equation. "
                                       "At the upper limit, you should avoid extrapolating too much. On the lower one, keep an eye on the appearance of the convoluted curve.</p>")
        html_content = html_content + ("<p>We provide recommended values of truncation, which are the result of our empirical experience in applying convolution to real data. "
                                       "However, you should treat them as recommendations.</p>")
        # body close
        html_content = html_content + "</body></html>"
        self.browser.setHtml(html_content, baseUrl=QUrl.fromLocalFile(os.getcwd() + os.path.sep))
        self.ui.vl_info_box.insertWidget(0, self.browser, 0, Qt.AlignmentFlag.AlignCenter)
        self.browser.urlChanged.connect(self.url_change)
        # QDialog show
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.show()
        self.exec()

    def url_change(self):
        if "convolution_functions.html" in str(self.browser.url()):
            self.close()
            ConvolutionFunctionsHelp()


class ExtrapolationHelp(QtWidgets.QDialog):
    """
        help window for the extrapolation
    """
    def __init__(self):
        super(ExtrapolationHelp, self).__init__()
        self.ui = Ui_HelpWindow()
        self.ui = Ui_HelpWindow()
        self.ui.setupUi(self)
        # GUI
        # title
        self.setWindowTitle(f'Extrapolation modes help')
        win_width = 800
        self.resize(win_width, 550)
        self.browser = QWebEngineView()
        self.browser.resize(win_width, 550)
        html_content = "<!DOCTYPE html><html><style>.center {display: block; margin-left: auto; margin-right: auto;} .plot {width: 100%; max-width:700px;}</style><body style='font-family: sans-serif; background-color: #F0F0F0;'>"
        html_content = html_content + "<p>More information about extrapolation:</p>"
        # extrapolation
        html_content = html_content + "<h2>Why extrapolate</h2>"
        html_content = html_content + "<p>In <a href='truncation_page.html'>the part on truncation</a> we mentioned that laboratory data are defined on a finite segment of the spectrum, whereas convolution functions are defined from plus to minus infinity.</p>"
        html_content = html_content + "<p>This is why we need to 'truncate' the convolution function, which is what the truncation parameter is for.</p>"
        html_content = html_content + "<p>However, sometimes it is necessary to calculate within the limits beyond the available data. And if one knows how the high-resolution spectrum behaves (remains constant, resembles a straight line, etc.), one can 'invent' the missing data by extrapolation.</p>"
        html_content = html_content + "<p>Of course, the result obtained in this way will be different from the case if we had all the necessary data - especially at the edges. However, in some cases this effect may be minimal and therefore acceptable. Or the edges of the spectrum are not important and can be ignored.</p>"
        # our extrapolations
        html_content = html_content + "<h2>Our extrapolation modes</h2>"
        html_content = html_content + "<p>Our algorithm has the following extrapolation methods:</p>"
        html_content = html_content + "<p>* 'Zero': all missing data is replaced with zeros. This is the default extrapolation mod.</p>"
        html_content = html_content + "<p>* 'Constant': all missing data are replaced by the last known value.</p>"
        html_content = html_content + "<p>* 'Average constant': the same as in the previous case, with the only difference that the constant value is the average of the last 5 points.</p>"
        html_content = html_content + "<p>* 'Linear regression': the line satisfying the linear regression condition on the last 5 points.</p>"
        html_content = html_content + "<p>It should be noted that, as can be expected, if there is enough data for calculation, no extrapolation is performed. In addition, our programme gives the choice of whether to extrapolate or not. In case of refusal, if there is not enough data, the result will correspond to extrapolation in mode 'zero'.</p>"
        html_content = html_content + "<p>It is currently not possible to select different extrapolation methods for the left and right edges of the original data. This feature can be added in our programme later if demanded.</p>"
        # body close
        html_content = html_content + "</body></html>"
        self.browser.setHtml(html_content, baseUrl=QUrl.fromLocalFile(os.getcwd() + os.path.sep))
        self.ui.vl_info_box.insertWidget(0, self.browser, 0, Qt.AlignmentFlag.AlignCenter)
        self.browser.urlChanged.connect(self.url_change)
        # QDialog show
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.show()
        self.exec()

    def url_change(self):
        if "truncation_page.html" in str(self.browser.url()):
            self.close()
            TruncationHelp()


# APP RUN
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = ConvolutionMainW()
    win.setWindowFlags(Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
    win.show()
    sys.exit(app.exec())
