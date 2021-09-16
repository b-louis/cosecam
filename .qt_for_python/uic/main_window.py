# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1023, 898)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_3.addWidget(self.label_23)

        self.comboBox_type_in = QComboBox(self.groupBox)
        self.comboBox_type_in.setObjectName(u"comboBox_type_in")

        self.verticalLayout_3.addWidget(self.comboBox_type_in)

        self.line_5 = QFrame(self.groupBox)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.toolButton_in_rasters = QToolButton(self.groupBox)
        self.toolButton_in_rasters.setObjectName(u"toolButton_in_rasters")

        self.horizontalLayout_4.addWidget(self.toolButton_in_rasters)

        self.lineEdit_root = QLineEdit(self.groupBox)
        self.lineEdit_root.setObjectName(u"lineEdit_root")

        self.horizontalLayout_4.addWidget(self.lineEdit_root)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.label_dataset = QLabel(self.groupBox)
        self.label_dataset.setObjectName(u"label_dataset")

        self.verticalLayout_3.addWidget(self.label_dataset)

        self.lineEdit_dataset = QLineEdit(self.groupBox)
        self.lineEdit_dataset.setObjectName(u"lineEdit_dataset")

        self.verticalLayout_3.addWidget(self.lineEdit_dataset)

        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_4)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.checkBox_input_points = QCheckBox(self.groupBox)
        self.checkBox_input_points.setObjectName(u"checkBox_input_points")
        self.checkBox_input_points.setEnabled(False)
        self.checkBox_input_points.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_input_points.setAutoFillBackground(False)
        self.checkBox_input_points.setChecked(False)
        self.checkBox_input_points.setTristate(False)

        self.verticalLayout_3.addWidget(self.checkBox_input_points)

        self.horizontalWidget_input_points = QWidget(self.groupBox)
        self.horizontalWidget_input_points.setObjectName(u"horizontalWidget_input_points")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget_input_points)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolButton_in_points = QToolButton(self.horizontalWidget_input_points)
        self.toolButton_in_points.setObjectName(u"toolButton_in_points")

        self.horizontalLayout_5.addWidget(self.toolButton_in_points)

        self.lineEdit_input_points = QLineEdit(self.horizontalWidget_input_points)
        self.lineEdit_input_points.setObjectName(u"lineEdit_input_points")

        self.horizontalLayout_5.addWidget(self.lineEdit_input_points)


        self.verticalLayout_3.addWidget(self.horizontalWidget_input_points)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.toolButton_out_rasters = QToolButton(self.groupBox)
        self.toolButton_out_rasters.setObjectName(u"toolButton_out_rasters")

        self.horizontalLayout_10.addWidget(self.toolButton_out_rasters)

        self.lineEdit_output_rasters = QLineEdit(self.groupBox)
        self.lineEdit_output_rasters.setObjectName(u"lineEdit_output_rasters")

        self.horizontalLayout_10.addWidget(self.lineEdit_output_rasters)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.comboBox_format = QComboBox(self.groupBox)
        self.comboBox_format.setObjectName(u"comboBox_format")

        self.verticalLayout_3.addWidget(self.comboBox_format)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.comboBox_mode = QComboBox(self.groupBox)
        self.comboBox_mode.setObjectName(u"comboBox_mode")
        self.comboBox_mode.setEnabled(False)

        self.verticalLayout_3.addWidget(self.comboBox_mode)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.lineEdit_srs_epsg = QLineEdit(self.groupBox_2)
        self.lineEdit_srs_epsg.setObjectName(u"lineEdit_srs_epsg")
        self.lineEdit_srs_epsg.setMaxLength(32767)
        self.lineEdit_srs_epsg.setReadOnly(False)

        self.verticalLayout_4.addWidget(self.lineEdit_srs_epsg)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.lineEdit_tgt_epsg = QLineEdit(self.groupBox_2)
        self.lineEdit_tgt_epsg.setObjectName(u"lineEdit_tgt_epsg")
        self.lineEdit_tgt_epsg.setMaxLength(32767)
        self.lineEdit_tgt_epsg.setFrame(True)

        self.verticalLayout_4.addWidget(self.lineEdit_tgt_epsg)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.comboBox_elevation_type = QComboBox(self.groupBox_2)
        self.comboBox_elevation_type.setObjectName(u"comboBox_elevation_type")
        self.comboBox_elevation_type.setEnabled(False)

        self.verticalLayout_4.addWidget(self.comboBox_elevation_type)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.toolButton_elev = QToolButton(self.groupBox_2)
        self.toolButton_elev.setObjectName(u"toolButton_elev")

        self.horizontalLayout_6.addWidget(self.toolButton_elev)

        self.lineEdit_elev_file = QLineEdit(self.groupBox_2)
        self.lineEdit_elev_file.setObjectName(u"lineEdit_elev_file")

        self.horizontalLayout_6.addWidget(self.lineEdit_elev_file)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_5 = QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_9.addWidget(self.label_20)

        self.comboBox_gcps_methods = QComboBox(self.groupBox_4)
        self.comboBox_gcps_methods.setObjectName(u"comboBox_gcps_methods")
        self.comboBox_gcps_methods.setEnabled(False)

        self.verticalLayout_9.addWidget(self.comboBox_gcps_methods)

        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_9.addWidget(self.label_21)

        self.comboBox_rpcs_methods = QComboBox(self.groupBox_4)
        self.comboBox_rpcs_methods.setObjectName(u"comboBox_rpcs_methods")
        self.comboBox_rpcs_methods.setEnabled(False)

        self.verticalLayout_9.addWidget(self.comboBox_rpcs_methods)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_9.addWidget(self.label_17)

        self.comboBox_ortho_methods = QComboBox(self.groupBox_4)
        self.comboBox_ortho_methods.setObjectName(u"comboBox_ortho_methods")
        self.comboBox_ortho_methods.setEnabled(False)

        self.verticalLayout_9.addWidget(self.comboBox_ortho_methods)

        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_9.addWidget(self.label_19)

        self.lineEdit_gdal_format = QLineEdit(self.groupBox_4)
        self.lineEdit_gdal_format.setObjectName(u"lineEdit_gdal_format")

        self.verticalLayout_9.addWidget(self.lineEdit_gdal_format)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_8.addWidget(self.label_15)

        self.comboBox_descriptors = QComboBox(self.groupBox_3)
        self.comboBox_descriptors.setObjectName(u"comboBox_descriptors")

        self.verticalLayout_8.addWidget(self.comboBox_descriptors)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_8.addWidget(self.label_22)

        self.comboBox_matchers = QComboBox(self.groupBox_3)
        self.comboBox_matchers.addItem("")
        self.comboBox_matchers.addItem("")
        self.comboBox_matchers.setObjectName(u"comboBox_matchers")

        self.verticalLayout_8.addWidget(self.comboBox_matchers)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_8.addWidget(self.label_16)

        self.doubleSpinBox_matchd = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_matchd.setObjectName(u"doubleSpinBox_matchd")
        self.doubleSpinBox_matchd.setDecimals(2)
        self.doubleSpinBox_matchd.setMaximum(999.990000000000009)
        self.doubleSpinBox_matchd.setSingleStep(0.010000000000000)
        self.doubleSpinBox_matchd.setValue(0.100000000000000)

        self.verticalLayout_8.addWidget(self.doubleSpinBox_matchd)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_8.addWidget(self.label_18)

        self.spinBox_minmatches = QSpinBox(self.groupBox_3)
        self.spinBox_minmatches.setObjectName(u"spinBox_minmatches")
        self.spinBox_minmatches.setEnabled(False)
        self.spinBox_minmatches.setMaximum(100000)
        self.spinBox_minmatches.setValue(10)

        self.verticalLayout_8.addWidget(self.spinBox_minmatches)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textBrowser = QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setTabChangesFocus(False)
        self.textBrowser.setUndoRedoEnabled(False)
        self.textBrowser.setReadOnly(True)

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textBrowser_2 = QTextBrowser(self.tab_4)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.horizontalLayout_3.addWidget(self.textBrowser_2)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.progressBar)

        self.pushButton_run = QPushButton(self.centralwidget)
        self.pushButton_run.setObjectName(u"pushButton_run")

        self.horizontalLayout.addWidget(self.pushButton_run)

        self.pushButton_cancel = QPushButton(self.centralwidget)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1023, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Orthorectification", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Type of input", None))
        self.comboBox_type_in.setCurrentText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Root Folder", None))
        self.toolButton_in_rasters.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_root.setText(QCoreApplication.translate("MainWindow", u"H:/images_database", None))
        self.label_dataset.setText(QCoreApplication.translate("MainWindow", u"Dataset name", None))
        self.lineEdit_dataset.setText(QCoreApplication.translate("MainWindow", u"124_paris_1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Input Points :", None))
        self.checkBox_input_points.setText(QCoreApplication.translate("MainWindow", u"enable", None))
        self.toolButton_in_points.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Output folder", None))
        self.toolButton_out_rasters.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_output_rasters.setText(QCoreApplication.translate("MainWindow", u"H:/images_database/test_paris", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Output Format", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Output Mode", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GDAL", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Source EPSG", None))
        self.lineEdit_srs_epsg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"default 4326", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Target EPSG", None))
        self.lineEdit_tgt_epsg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"default 3857", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Elevation type", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Elevation File", None))
        self.toolButton_elev.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_elev_file.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_elev_file.setInputMask("")
        self.lineEdit_elev_file.setText(QCoreApplication.translate("MainWindow", u"H:/MNT/dted-2/DTED/E002/N48.DT2", None))
        self.lineEdit_elev_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DTED or TIFF for DEM , GRD for geoid", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"General", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"GDAL/OTB", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"GCPS generation method", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"RPCS generation method", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Orthorectification method", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Output Type", None))
        self.lineEdit_gdal_format.setPlaceholderText(QCoreApplication.translate("MainWindow", u"default GTiff", None))
        self.groupBox_3.setTitle("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Descriptors", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Matcher", None))
        self.comboBox_matchers.setItemText(0, QCoreApplication.translate("MainWindow", u"FLANN", None))
        self.comboBox_matchers.setItemText(1, QCoreApplication.translate("MainWindow", u"BRUTEFORCE", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Match distance", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Minimum matched features", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Log", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"geo\"></a><span style=\" font-size:8pt; font-weight:600;\">G</span><span style=\" font-size:8pt; font-weight:600;\">eo</span></h1>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This part of the application is used for orthorectification. Before going further be sure you have set your environment correctly (see requierements)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Note that it still very rough, some features aren't implemented (those with a '*').</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><a name=\"overview\"></a><span style=\" font-size:8pt; font-weight:600;\">O</span><span style=\" font-size:8pt; font-weight:600;\">verview</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This module is use to do the whole orthorectification from a non georeferenced image with GPS values at center to a orthorectified image (georeferenced or not)</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"functions\"></a><span style=\" font-size:8pt; font-weight:600;\">F</span><span style=\" font-size:8pt; font-weight"
                        ":600;\">unctions</span></h2>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\"><thead>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; font-style:italic;\">functions</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; font-style:italic;\">description</span></p></td></tr></thead>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">coords_distance</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span sty"
                        "le=\" font-size:8pt;\">Computes the distance between on earth's surface</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">cal_lat_lon</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Computes the longitude and latitude from a point with distance and angle</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">angle_from_coord</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Computes the angle between true north and a point</span></p><"
                        "/td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">load_gcps</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Loads </span><span style=\" font-size:8pt; font-style:italic;\">GCPs</span><span style=\" font-size:8pt;\"> from a file and parses them in a </span><span style=\" font-size:8pt; font-style:italic;\">numpy.array</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">generate_input_tif</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Genera"
                        "tes a georeferenced image from image, a list of </span><span style=\" font-size:8pt; font-style:italic;\">GCPs</span><span style=\" font-size:8pt;\"> and a elevation map</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">convert_save_gcps</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Converts the </span><span style=\" font-size:8pt; font-style:italic;\">GCPs</span><span style=\" font-size:8pt;\"> format for </span><span style=\" font-size:8pt; font-style:italic;\">GDAL</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">readgeom</span></p></td>\n"
"<td>\n"
"<p"
                        " style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Reads a </span><span style=\" font-size:8pt; font-style:italic;\">geom</span><span style=\" font-size:8pt;\"> file and parses it in </span><span style=\" font-size:8pt; font-style:italic;\">numpy.array</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">generate_rpc</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Generates </span><span style=\" font-size:8pt; font-style:italic;\">RPCs</span><span style=\" font-size:8pt;\"> with a list of points</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">projection_gdalcmd</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">gdalwarp</span><span style=\" font-size:8pt;\"> CLI function warpper in python</span></p></td></tr></table>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"classes\"></a><span style=\" font-size:8pt; font-weight:600;\">C</span><span style=\" font-size:8pt; font-weight:600;\">lasses</span></h2>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\"><thead>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600"
                        "; font-style:italic;\">classes</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; font-style:italic;\">description</span></p></td></tr></thead>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">StereoGCP</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Class that generates </span><span style=\" font-size:8pt; font-style:italic;\">GCPs</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">RpcGenerator</span></p></td>\n"
"<td>\n"
"<p style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Class that generates </span><span style=\" font-size:8pt; font-style:italic;\">RPCs</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">OrthoRectification</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Class for orthorectification calculation</span></p></td></tr>\n"
"<tr>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Georeferencer</span></p></td>\n"
"<td>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-blo"
                        "ck-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Main class for the whole process, <br />computes all images within the specified folder</span></p></td></tr></table>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"example\"></a><span style=\" font-size:8pt; font-weight:600;\">E</span><span style=\" font-size:8pt; font-weight:600;\">xample</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">from cosecam.geo import *</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fo"
                        "nt-family:'Courier New'; font-size:8pt;\"># digital elevation file</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">dem_file = &quot;/home/user/DTEDS/N40E01.dted&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\"># setting the images centers for Steregcp calculation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">center = dec.getResolution()/2</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin"
                        "-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\"># initialize all classes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">gcp_gen = StereoGCP(center)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">rpc_gen = RpcGenerator(dem_file)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">orthorect = OrthoRectification(projection_gdalcmd,dem_file)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-"
                        "indent:0; text-indent:0px; font-family:'Courier New'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\"># we create the main object, that compute the whole </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">geo = Georeferencer(gcp_gen,rpc_gen,orthorect)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">dec = Msfs_decoder(&quot;/home/user/datasets/&quot;,&quot;exemple&"
                        "quot;)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\"># when we setDataset, we set the dataset object and </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\"># the orthorectification folder output</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">geo.setDataset(dec,&quot;/home/user/datasets/example1_orthorectified/&quot;)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\"># it computes all images in the folder</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">geo.run()</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:8pt;\"><br /></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"data-structure\"></a><span style=\" font-size:8pt; font-weight:600;\">D</span><span style=\""
                        " font-size:8pt; font-weight:600;\">ata structure</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">See </span><a href=\"msfs_recorder.md\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">msfs_recorder</span></a><span style=\" font-size:8pt;\"> for input data structure.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The output structure is : </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">\u2514\u2500\u2500 datasets/</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-si"
                        "ze:8pt;\">    \u251c\u2500\u2500 example1/</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">    \u2502   \u251c\u2500\u2500 000.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">    \u2502   \u251c\u2500\u2500 001.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">    \u2502   \u251c\u2500\u2500 002.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">    \u2502   \u251c\u2500\u2500 003.png</span></p>\n"
"<p style=\" margin-top:0px;"
                        " margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">    \u2502   \u251c\u2500\u2500 004.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">    \u2502   \u251c\u2500\u2500 005.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">    \u2502   \u251c\u2500\u2500 values.txt</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">    \u2502   \u2514\u2500\u2500 images.txt</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">    \u2514\u2500\u2500 example1_orthorectified/</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">        \u251c\u2500\u2500 000.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">        \u251c\u2500\u2500 001.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">        \u251c\u2500\u2500 002.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">        \u251c\u2500"
                        "\u2500 003.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">        \u251c\u2500\u2500 004.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">        \u251c\u2500\u2500 005.png</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">        \u251c\u2500\u2500 values.txt</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">        \u2514\u2500\u2500 images.txt</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Output images are orthorectified, not georeferenced and homographied by pairs .</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Example : </span><span style=\" font-size:8pt; font-weight:600;\">000.png</span><span style=\" font-size:8pt;\"> is homographied with </span><span style=\" font-size:8pt; font-weight:600;\">001.png</span><span style=\" font-size:8pt;\">, and </span><span style=\" font-size:8pt; font-weight:600;\">002.png</span><span style=\" font-size:8pt;\"> is homographied with </span><span style=\" font-size:8pt; font-weight:600;\">003.png</span><span style=\" font-size:8pt;\"> but </span><span"
                        " style=\" font-size:8pt; font-weight:600;\">000.png</span><span style=\" font-size:8pt;\"> are not </span><span style=\" font-size:8pt; font-weight:600;\">002.png</span></p>\n"
"<h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"installation-issues\"></a><span style=\" font-size:8pt; font-weight:600;\">I</span><span style=\" font-size:8pt; font-weight:600;\">nstallation issues</span></h2>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">There is some issues with </span><span style=\" font-size:8pt; font-style:italic;\">GDAL/OTB</span><span style=\" font-size:8pt;\"> that we encounter during our setup.</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"on-windows-\"></a><span style=\" font-size:8pt; font-weight:600;\">O</span"
                        "><span style=\" font-size:8pt; font-weight:600;\">n windows :</span></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">There's issues with the different versions of </span><span style=\" font-size:8pt; font-style:italic;\">GDAL</span><span style=\" font-size:8pt;\"> in , a conflict can occur with </span><span style=\" font-size:8pt; font-style:italic;\">OTB/ANACONDA-PYTHON</span><span style=\" font-size:8pt;\"> version.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">We use the command line method because OTB's python warpper don't work with python versions above </span><span style=\" font-size:8pt; font-style:italic;\">3.5.x</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fo"
                        "nt-size:8pt;\">In that case you'll need to change the </span><span style=\" font-size:8pt; font-weight:600;\">projection_gdalcmd</span><span style=\" font-size:8pt;\"> function:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">cmd = 'E:/OTB-7.3.0-Win64/bin/gdalwarp.exe -rpc -to RPC_DEM={rpcPath} -of GTiff {srcPath}  {outPath} -overwrite -s_srs EPSG:4326 -t_srs EPSG:3857 '\\</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">.format(srcPath=in_image,outPath=out_image,rpcPath=dem)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; marg"
                        "in-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:8pt;\">print(f&quot;COMMAND:\\n{cmd}&quot;)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Replace </span><span style=\" font-size:8pt; font-weight:600;\">E:/OTB-7.3.0-Win64/bin/gdalwarp.exe</span><span style=\" font-size:8pt;\"> with your gdalwarp path.</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"on-linux-\"></a><span style=\" font-size:8pt; font-weight:600;\">O</span><span style=\" font-size:8pt; font-weight:600;\">n Linux:</span></h3>\n"
"<p sty"
                        "le=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">You can use </span><a href=\"https://www.orfeo-toolbox.org/CookBook/PythonAPI.html\"><span style=\" font-size:8pt; font-style:italic; text-decoration: underline; color:#0000ff;\">OTBApplication</span></a><span style=\" font-size:8pt;\"> instead, but for now it still uses </span><span style=\" font-size:8pt; font-style:italic;\">gdalwarp</span><span style=\" font-size:8pt;\"> on CLImode </span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Help", None))
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

