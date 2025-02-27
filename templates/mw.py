# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1172, 970)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.main_horozontal_grid = QtWidgets.QWidget(MainWindow)
        self.main_horozontal_grid.setObjectName("main_horozontal_grid")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_horozontal_grid)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_grid = QtWidgets.QGridLayout()
        self.main_grid.setObjectName("main_grid")
        self.graphWidget = PlotWidget(self.main_horozontal_grid)
        self.graphWidget.setMinimumSize(QtCore.QSize(900, 650))
        self.graphWidget.setObjectName("graphWidget")
        self.main_grid.addWidget(self.graphWidget, 2, 1, 1, 1)
        self.side_bar_vl = QtWidgets.QVBoxLayout()
        self.side_bar_vl.setObjectName("side_bar_vl")
        self.label_3 = QtWidgets.QLabel(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.side_bar_vl.addWidget(self.label_3)
        self.spctrm_file = QtWidgets.QPushButton(self.main_horozontal_grid)
        self.spctrm_file.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spctrm_file.setFont(font)
        self.spctrm_file.setObjectName("spctrm_file")
        self.side_bar_vl.addWidget(self.spctrm_file)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spctrm_path_lbl = QtWidgets.QLabel(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spctrm_path_lbl.setFont(font)
        self.spctrm_path_lbl.setObjectName("spctrm_path_lbl")
        self.horizontalLayout_3.addWidget(self.spctrm_path_lbl)
        self.side_bar_vl.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.spctrm_unit = QtWidgets.QComboBox(self.main_horozontal_grid)
        self.spctrm_unit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.spctrm_unit.setObjectName("spctrm_unit")
        self.gridLayout.addWidget(self.spctrm_unit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spctrm_wlth_clm = QtWidgets.QComboBox(self.main_horozontal_grid)
        self.spctrm_wlth_clm.setMaximumSize(QtCore.QSize(300, 16777215))
        self.spctrm_wlth_clm.setObjectName("spctrm_wlth_clm")
        self.gridLayout.addWidget(self.spctrm_wlth_clm, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.spctrm_inty_clm = QtWidgets.QComboBox(self.main_horozontal_grid)
        self.spctrm_inty_clm.setMaximumSize(QtCore.QSize(300, 16777215))
        self.spctrm_inty_clm.setObjectName("spctrm_inty_clm")
        self.gridLayout.addWidget(self.spctrm_inty_clm, 2, 1, 1, 1)
        self.side_bar_vl.addLayout(self.gridLayout)
        self.line_4 = QtWidgets.QFrame(self.main_horozontal_grid)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.side_bar_vl.addWidget(self.line_4)
        self.label_10 = QtWidgets.QLabel(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.side_bar_vl.addWidget(self.label_10)
        self.spctrm_tab = QtWidgets.QTabWidget(self.main_horozontal_grid)
        self.spctrm_tab.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.spctrm_tab.setFont(font)
        self.spctrm_tab.setTabPosition(QtWidgets.QTabWidget.West)
        self.spctrm_tab.setObjectName("spctrm_tab")
        self.spctrm_file_tab = QtWidgets.QWidget()
        self.spctrm_file_tab.setObjectName("spctrm_file_tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.spctrm_file_tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.spctrm_wdth_file = QtWidgets.QPushButton(self.spctrm_file_tab)
        self.spctrm_wdth_file.setObjectName("spctrm_wdth_file")
        self.verticalLayout_9.addWidget(self.spctrm_wdth_file)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spctrm_wdth_path_lbl = QtWidgets.QLabel(self.spctrm_file_tab)
        self.spctrm_wdth_path_lbl.setObjectName("spctrm_wdth_path_lbl")
        self.horizontalLayout.addWidget(self.spctrm_wdth_path_lbl)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.spctrm_file_tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.spctrm_wdth_clm = QtWidgets.QComboBox(self.spctrm_file_tab)
        self.spctrm_wdth_clm.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spctrm_wdth_clm.setFont(font)
        self.spctrm_wdth_clm.setObjectName("spctrm_wdth_clm")
        self.gridLayout_2.addWidget(self.spctrm_wdth_clm, 0, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.spctrm_tab.addTab(self.spctrm_file_tab, "")
        self.spctrm_const_tab = QtWidgets.QWidget()
        self.spctrm_const_tab.setObjectName("spctrm_const_tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.spctrm_const_tab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.spctrm_const_grid = QtWidgets.QGridLayout()
        self.spctrm_const_grid.setObjectName("spctrm_const_grid")
        self.verticalLayout_10.addLayout(self.spctrm_const_grid)
        spacerItem1 = QtWidgets.QSpacerItem(20, 109, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.spctrm_tab.addTab(self.spctrm_const_tab, "")
        self.side_bar_vl.addWidget(self.spctrm_tab)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.side_bar_vl.addItem(spacerItem2)
        self.line = QtWidgets.QFrame(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.side_bar_vl.addWidget(self.line)
        self.label_16 = QtWidgets.QLabel(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.side_bar_vl.addWidget(self.label_16)
        self.btn_param_load = QtWidgets.QPushButton(self.main_horozontal_grid)
        self.btn_param_load.setObjectName("btn_param_load")
        self.side_bar_vl.addWidget(self.btn_param_load)
        self.btn_param_save = QtWidgets.QPushButton(self.main_horozontal_grid)
        self.btn_param_save.setObjectName("btn_param_save")
        self.side_bar_vl.addWidget(self.btn_param_save)
        spacerItem3 = QtWidgets.QSpacerItem(241, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.side_bar_vl.addItem(spacerItem3)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_21 = QtWidgets.QLabel(self.main_horozontal_grid)
        self.label_21.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 0, 0, 1, 1)
        self.instrument_preset = QtWidgets.QComboBox(self.main_horozontal_grid)
        self.instrument_preset.setMaximumSize(QtCore.QSize(300, 16777215))
        self.instrument_preset.setObjectName("instrument_preset")
        self.gridLayout_5.addWidget(self.instrument_preset, 0, 1, 1, 1)
        self.side_bar_vl.addLayout(self.gridLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.side_bar_vl.addItem(spacerItem4)
        self.line_3 = QtWidgets.QFrame(self.main_horozontal_grid)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.side_bar_vl.addWidget(self.line_3)
        self.label_4 = QtWidgets.QLabel(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.side_bar_vl.addWidget(self.label_4)
        self.dstntn_tab = QtWidgets.QTabWidget(self.main_horozontal_grid)
        self.dstntn_tab.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dstntn_tab.setFont(font)
        self.dstntn_tab.setTabPosition(QtWidgets.QTabWidget.West)
        self.dstntn_tab.setObjectName("dstntn_tab")
        self.dstntn_file_tab = QtWidgets.QWidget()
        self.dstntn_file_tab.setObjectName("dstntn_file_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dstntn_file_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dstntn_file = QtWidgets.QPushButton(self.dstntn_file_tab)
        self.dstntn_file.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dstntn_file.setFont(font)
        self.dstntn_file.setObjectName("dstntn_file")
        self.verticalLayout_4.addWidget(self.dstntn_file, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dstntn_path_lbl = QtWidgets.QLabel(self.dstntn_file_tab)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.dstntn_path_lbl.setFont(font)
        self.dstntn_path_lbl.setObjectName("dstntn_path_lbl")
        self.horizontalLayout_4.addWidget(self.dstntn_path_lbl, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_17 = QtWidgets.QLabel(self.dstntn_file_tab)
        self.label_17.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)
        self.dstntn_wlth_clm = QtWidgets.QComboBox(self.dstntn_file_tab)
        self.dstntn_wlth_clm.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dstntn_wlth_clm.setFont(font)
        self.dstntn_wlth_clm.setObjectName("dstntn_wlth_clm")
        self.gridLayout_6.addWidget(self.dstntn_wlth_clm, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.dstntn_tab.addTab(self.dstntn_file_tab, "")
        self.dstntn_linear_tab = QtWidgets.QWidget()
        self.dstntn_linear_tab.setObjectName("dstntn_linear_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dstntn_linear_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.dstntn_linear_grid = QtWidgets.QGridLayout()
        self.dstntn_linear_grid.setObjectName("dstntn_linear_grid")
        self.verticalLayout_5.addLayout(self.dstntn_linear_grid)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.dstntn_tab.addTab(self.dstntn_linear_tab, "")
        self.side_bar_vl.addWidget(self.dstntn_tab)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.dstntn_unit = QtWidgets.QComboBox(self.main_horozontal_grid)
        self.dstntn_unit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.dstntn_unit.setObjectName("dstntn_unit")
        self.gridLayout_8.addWidget(self.dstntn_unit, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.main_horozontal_grid)
        self.label_19.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_8.addWidget(self.label_19, 0, 0, 1, 1)
        self.side_bar_vl.addLayout(self.gridLayout_8)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.side_bar_vl.addItem(spacerItem7)
        self.line_2 = QtWidgets.QFrame(self.main_horozontal_grid)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.side_bar_vl.addWidget(self.line_2)
        self.label_5 = QtWidgets.QLabel(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.side_bar_vl.addWidget(self.label_5)
        self.conv_params_grid = QtWidgets.QGridLayout()
        self.conv_params_grid.setObjectName("conv_params_grid")
        self.side_bar_vl.addLayout(self.conv_params_grid)
        self.conv_tab = QtWidgets.QTabWidget(self.main_horozontal_grid)
        self.conv_tab.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.conv_tab.setFont(font)
        self.conv_tab.setTabPosition(QtWidgets.QTabWidget.West)
        self.conv_tab.setObjectName("conv_tab")
        self.conv_file_tab = QtWidgets.QWidget()
        self.conv_file_tab.setObjectName("conv_file_tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.conv_file_tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.conv_file = QtWidgets.QPushButton(self.conv_file_tab)
        self.conv_file.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.conv_file.setFont(font)
        self.conv_file.setObjectName("conv_file")
        self.verticalLayout_6.addWidget(self.conv_file, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.conv_path_lbl = QtWidgets.QLabel(self.conv_file_tab)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.conv_path_lbl.setFont(font)
        self.conv_path_lbl.setObjectName("conv_path_lbl")
        self.horizontalLayout_5.addWidget(self.conv_path_lbl, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.conv_wdth_1_clm = QtWidgets.QComboBox(self.conv_file_tab)
        self.conv_wdth_1_clm.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.conv_wdth_1_clm.setFont(font)
        self.conv_wdth_1_clm.setObjectName("conv_wdth_1_clm")
        self.gridLayout_7.addWidget(self.conv_wdth_1_clm, 0, 1, 1, 1)
        self.conv_wdth_1_lbl = QtWidgets.QLabel(self.conv_file_tab)
        self.conv_wdth_1_lbl.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.conv_wdth_1_lbl.setFont(font)
        self.conv_wdth_1_lbl.setObjectName("conv_wdth_1_lbl")
        self.gridLayout_7.addWidget(self.conv_wdth_1_lbl, 0, 0, 1, 1)
        self.conv_wdth_2_lbl = QtWidgets.QLabel(self.conv_file_tab)
        self.conv_wdth_2_lbl.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.conv_wdth_2_lbl.setFont(font)
        self.conv_wdth_2_lbl.setObjectName("conv_wdth_2_lbl")
        self.gridLayout_7.addWidget(self.conv_wdth_2_lbl, 1, 0, 1, 1)
        self.conv_wdth_2_clm = QtWidgets.QComboBox(self.conv_file_tab)
        self.conv_wdth_2_clm.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.conv_wdth_2_clm.setFont(font)
        self.conv_wdth_2_clm.setObjectName("conv_wdth_2_clm")
        self.gridLayout_7.addWidget(self.conv_wdth_2_clm, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.conv_tab.addTab(self.conv_file_tab, "")
        self.conv_linear_tab = QtWidgets.QWidget()
        self.conv_linear_tab.setObjectName("conv_linear_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.conv_linear_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.conv_linear_grid = QtWidgets.QGridLayout()
        self.conv_linear_grid.setObjectName("conv_linear_grid")
        self.verticalLayout_7.addLayout(self.conv_linear_grid)
        spacerItem9 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.conv_tab.addTab(self.conv_linear_tab, "")
        self.conv_const_tab = QtWidgets.QWidget()
        self.conv_const_tab.setObjectName("conv_const_tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.conv_const_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.conv_const_grid = QtWidgets.QGridLayout()
        self.conv_const_grid.setObjectName("conv_const_grid")
        self.verticalLayout_8.addLayout(self.conv_const_grid)
        spacerItem10 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem10)
        self.conv_tab.addTab(self.conv_const_tab, "")
        self.side_bar_vl.addWidget(self.conv_tab)
        spacerItem11 = QtWidgets.QSpacerItem(241, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.side_bar_vl.addItem(spacerItem11)
        self.main_grid.addLayout(self.side_bar_vl, 2, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.main_grid)
        self.buttons_hl = QtWidgets.QHBoxLayout()
        self.buttons_hl.setObjectName("buttons_hl")
        self.btn_dstntn_export = QtWidgets.QPushButton(self.main_horozontal_grid)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_dstntn_export.setFont(font)
        self.btn_dstntn_export.setObjectName("btn_dstntn_export")
        self.buttons_hl.addWidget(self.btn_dstntn_export)
        self.btn_calc = QtWidgets.QPushButton(self.main_horozontal_grid)
        self.btn_calc.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_calc.setFont(font)
        self.btn_calc.setObjectName("btn_calc")
        self.buttons_hl.addWidget(self.btn_calc)
        self.btn_export = QtWidgets.QPushButton(self.main_horozontal_grid)
        self.btn_export.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_export.setFont(font)
        self.btn_export.setObjectName("btn_export")
        self.buttons_hl.addWidget(self.btn_export)
        self.verticalLayout_2.addLayout(self.buttons_hl)
        MainWindow.setCentralWidget(self.main_horozontal_grid)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1172, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.spctrm_tab.setCurrentIndex(0)
        self.dstntn_tab.setCurrentIndex(0)
        self.conv_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.spctrm_file, self.spctrm_unit)
        MainWindow.setTabOrder(self.spctrm_unit, self.spctrm_wlth_clm)
        MainWindow.setTabOrder(self.spctrm_wlth_clm, self.spctrm_inty_clm)
        MainWindow.setTabOrder(self.spctrm_inty_clm, self.spctrm_tab)
        MainWindow.setTabOrder(self.spctrm_tab, self.spctrm_wdth_file)
        MainWindow.setTabOrder(self.spctrm_wdth_file, self.spctrm_wdth_clm)
        MainWindow.setTabOrder(self.spctrm_wdth_clm, self.btn_param_load)
        MainWindow.setTabOrder(self.btn_param_load, self.btn_param_save)
        MainWindow.setTabOrder(self.btn_param_save, self.instrument_preset)
        MainWindow.setTabOrder(self.instrument_preset, self.dstntn_tab)
        MainWindow.setTabOrder(self.dstntn_tab, self.dstntn_file)
        MainWindow.setTabOrder(self.dstntn_file, self.dstntn_wlth_clm)
        MainWindow.setTabOrder(self.dstntn_wlth_clm, self.dstntn_unit)
        MainWindow.setTabOrder(self.dstntn_unit, self.conv_tab)
        MainWindow.setTabOrder(self.conv_tab, self.conv_file)
        MainWindow.setTabOrder(self.conv_file, self.conv_wdth_1_clm)
        MainWindow.setTabOrder(self.conv_wdth_1_clm, self.conv_wdth_2_clm)
        MainWindow.setTabOrder(self.conv_wdth_2_clm, self.btn_dstntn_export)
        MainWindow.setTabOrder(self.btn_dstntn_export, self.btn_calc)
        MainWindow.setTabOrder(self.btn_calc, self.btn_export)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "High-resolution spectrum"))
        self.spctrm_file.setText(_translate("MainWindow", "Select spectrum file"))
        self.spctrm_path_lbl.setText(_translate("MainWindow", "no file selected"))
        self.label_2.setText(_translate("MainWindow", "wavelength\n"
"column"))
        self.label.setText(_translate("MainWindow", "unit"))
        self.label_6.setText(_translate("MainWindow", "intensity\n"
"column"))
        self.label_10.setText(_translate("MainWindow", "Spectrum width (optional)"))
        self.spctrm_wdth_file.setText(_translate("MainWindow", "Select spectrum width file"))
        self.spctrm_wdth_path_lbl.setText(_translate("MainWindow", "no file selected"))
        self.label_9.setText(_translate("MainWindow", "width\n"
"column"))
        self.spctrm_tab.setTabText(self.spctrm_tab.indexOf(self.spctrm_file_tab), _translate("MainWindow", "file"))
        self.spctrm_tab.setTabText(self.spctrm_tab.indexOf(self.spctrm_const_tab), _translate("MainWindow", "const"))
        self.label_16.setText(_translate("MainWindow", "Convolution parameters"))
        self.btn_param_load.setText(_translate("MainWindow", "Import convolution parameters"))
        self.btn_param_save.setText(_translate("MainWindow", "Export convolution parameters"))
        self.label_21.setText(_translate("MainWindow", "preset"))
        self.label_4.setText(_translate("MainWindow", "Destination wavelength"))
        self.dstntn_file.setText(_translate("MainWindow", "Select destination wavelength file"))
        self.dstntn_path_lbl.setText(_translate("MainWindow", "no file selected"))
        self.label_17.setText(_translate("MainWindow", "wavelength\n"
"column"))
        self.dstntn_tab.setTabText(self.dstntn_tab.indexOf(self.dstntn_file_tab), _translate("MainWindow", "file"))
        self.dstntn_tab.setTabText(self.dstntn_tab.indexOf(self.dstntn_linear_tab), _translate("MainWindow", "linear"))
        self.label_19.setText(_translate("MainWindow", "unit"))
        self.label_5.setText(_translate("MainWindow", "Convolution function"))
        self.conv_file.setText(_translate("MainWindow", "Select width file"))
        self.conv_path_lbl.setText(_translate("MainWindow", "no file selected"))
        self.conv_wdth_1_lbl.setText(_translate("MainWindow", "width\n"
"column"))
        self.conv_wdth_2_lbl.setText(_translate("MainWindow", "top\n"
"column"))
        self.conv_tab.setTabText(self.conv_tab.indexOf(self.conv_file_tab), _translate("MainWindow", "file"))
        self.conv_tab.setTabText(self.conv_tab.indexOf(self.conv_linear_tab), _translate("MainWindow", "linear"))
        self.conv_tab.setTabText(self.conv_tab.indexOf(self.conv_const_tab), _translate("MainWindow", "const"))
        self.btn_dstntn_export.setText(_translate("MainWindow", "Export destination wavelength, width and top"))
        self.btn_calc.setText(_translate("MainWindow", "Calculate the convolution"))
        self.btn_export.setText(_translate("MainWindow", "Export the calculation result"))
from pyqtgraph import PlotWidget
