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
        MainWindow.resize(1114, 1088)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.toolButton_input = QToolButton(self.groupBox_5)
        self.toolButton_input.setObjectName(u"toolButton_input")

        self.horizontalLayout_4.addWidget(self.toolButton_input)

        self.lineEdit_input = QLineEdit(self.groupBox_5)
        self.lineEdit_input.setObjectName(u"lineEdit_input")

        self.horizontalLayout_4.addWidget(self.lineEdit_input)

        self.radioButton = QRadioButton(self.groupBox_5)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_5)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.radioButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.comboBox_detection = QComboBox(self.groupBox)
        self.comboBox_detection.setObjectName(u"comboBox_detection")

        self.verticalLayout_7.addWidget(self.comboBox_detection)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_7.addWidget(self.label_4)

        self.param_d_dpmean = QWidget(self.groupBox)
        self.param_d_dpmean.setObjectName(u"param_d_dpmean")
        self.param_d_dpmean.setEnabled(True)
        self.horizontalLayout_8 = QHBoxLayout(self.param_d_dpmean)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_16 = QLabel(self.param_d_dpmean)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_21.addWidget(self.label_16)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.param_d_dpmean)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")
        self.doubleSpinBox_14.setDecimals(7)
        self.doubleSpinBox_14.setValue(0.000001000000000)

        self.verticalLayout_21.addWidget(self.doubleSpinBox_14)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_21)

        self.line_9 = QFrame(self.param_d_dpmean)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_9)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_17 = QLabel(self.param_d_dpmean)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_23.addWidget(self.label_17)

        self.doubleSpinBox_15 = QDoubleSpinBox(self.param_d_dpmean)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")
        self.doubleSpinBox_15.setMaximum(100000.000000000000000)
        self.doubleSpinBox_15.setValue(2700.000000000000000)

        self.verticalLayout_23.addWidget(self.doubleSpinBox_15)

        self.label_19 = QLabel(self.param_d_dpmean)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_23.addWidget(self.label_19)

        self.doubleSpinBox_17 = QDoubleSpinBox(self.param_d_dpmean)
        self.doubleSpinBox_17.setObjectName(u"doubleSpinBox_17")
        self.doubleSpinBox_17.setMaximum(10000.000000000000000)
        self.doubleSpinBox_17.setValue(5400.000000000000000)

        self.verticalLayout_23.addWidget(self.doubleSpinBox_17)


        self.horizontalLayout_8.addLayout(self.verticalLayout_23)


        self.verticalLayout_7.addWidget(self.param_d_dpmean)

        self.param_d_weightedmean = QWidget(self.groupBox)
        self.param_d_weightedmean.setObjectName(u"param_d_weightedmean")
        self.horizontalLayout_3 = QHBoxLayout(self.param_d_weightedmean)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.param_d_weightedmean)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.param_d_weightedmean)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.verticalLayout_5.addWidget(self.doubleSpinBox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.line_2 = QFrame(self.param_d_weightedmean)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.param_d_weightedmean)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_8.addWidget(self.label_2)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.param_d_weightedmean)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setValue(0.700000000000000)

        self.verticalLayout_8.addWidget(self.doubleSpinBox_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.line = QFrame(self.param_d_weightedmean)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.param_d_weightedmean)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.param_d_weightedmean)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setValue(0.300000000000000)

        self.verticalLayout_6.addWidget(self.doubleSpinBox_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addWidget(self.param_d_weightedmean)

        self.param_d_none = QWidget(self.groupBox)
        self.param_d_none.setObjectName(u"param_d_none")
        self.horizontalLayout_5 = QHBoxLayout(self.param_d_none)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.param_d_none)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.comboBox_preprocess = QComboBox(self.groupBox_2)
        self.comboBox_preprocess.setObjectName(u"comboBox_preprocess")

        self.verticalLayout_9.addWidget(self.comboBox_preprocess)

        self.param_pr_median = QWidget(self.groupBox_2)
        self.param_pr_median.setObjectName(u"param_pr_median")
        self.verticalLayout_25 = QVBoxLayout(self.param_pr_median)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.param_pr_median)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_25.addWidget(self.label_20)

        self.spinBox_15 = QSpinBox(self.param_pr_median)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setMaximum(255)
        self.spinBox_15.setValue(11)

        self.verticalLayout_25.addWidget(self.spinBox_15)


        self.verticalLayout_9.addWidget(self.param_pr_median)

        self.param_pr_none = QWidget(self.groupBox_2)
        self.param_pr_none.setObjectName(u"param_pr_none")
        self.horizontalLayout_13 = QHBoxLayout(self.param_pr_none)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.param_pr_none)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.comboBox_postprocess = QComboBox(self.groupBox_3)
        self.comboBox_postprocess.setObjectName(u"comboBox_postprocess")

        self.verticalLayout_10.addWidget(self.comboBox_postprocess)

        self.param_po_none = QWidget(self.groupBox_3)
        self.param_po_none.setObjectName(u"param_po_none")
        self.horizontalLayout_14 = QHBoxLayout(self.param_po_none)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.param_po_none)

        self.param_po_median_sp = QWidget(self.groupBox_3)
        self.param_po_median_sp.setObjectName(u"param_po_median_sp")
        self.param_po_median_sp.setEnabled(True)
        self.horizontalLayout_11 = QHBoxLayout(self.param_po_median_sp)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_18 = QLabel(self.param_po_median_sp)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_24.addWidget(self.label_18)

        self.spinBox_21 = QSpinBox(self.param_po_median_sp)
        self.spinBox_21.setObjectName(u"spinBox_21")
        self.spinBox_21.setValue(12)

        self.verticalLayout_24.addWidget(self.spinBox_21)


        self.horizontalLayout_11.addLayout(self.verticalLayout_24)

        self.line_12 = QFrame(self.param_po_median_sp)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_12)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_28 = QLabel(self.param_po_median_sp)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_32.addWidget(self.label_28)

        self.spinBox_24 = QSpinBox(self.param_po_median_sp)
        self.spinBox_24.setObjectName(u"spinBox_24")
        self.spinBox_24.setValue(1)

        self.verticalLayout_32.addWidget(self.spinBox_24)


        self.horizontalLayout_11.addLayout(self.verticalLayout_32)


        self.verticalLayout_10.addWidget(self.param_po_median_sp)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_8)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.comboBox_threshold = QComboBox(self.groupBox_4)
        self.comboBox_threshold.setObjectName(u"comboBox_threshold")
        self.comboBox_threshold.setEditable(False)

        self.verticalLayout_3.addWidget(self.comboBox_threshold)

        self.param_t_value = QWidget(self.groupBox_4)
        self.param_t_value.setObjectName(u"param_t_value")
        self.verticalLayout_22 = QVBoxLayout(self.param_t_value)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.param_t_value)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_22.addWidget(self.label_15)

        self.spinBox_13 = QSpinBox(self.param_t_value)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setMaximum(255)
        self.spinBox_13.setValue(127)

        self.verticalLayout_22.addWidget(self.spinBox_13)


        self.verticalLayout_3.addWidget(self.param_t_value)

        self.param_t_pourcent = QWidget(self.groupBox_4)
        self.param_t_pourcent.setObjectName(u"param_t_pourcent")
        self.verticalLayout_26 = QVBoxLayout(self.param_t_pourcent)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.param_t_pourcent)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_26.addWidget(self.label_21)

        self.doubleSpinBox_19 = QDoubleSpinBox(self.param_t_pourcent)
        self.doubleSpinBox_19.setObjectName(u"doubleSpinBox_19")
        self.doubleSpinBox_19.setSingleStep(0.010000000000000)
        self.doubleSpinBox_19.setValue(0.700000000000000)

        self.verticalLayout_26.addWidget(self.doubleSpinBox_19)


        self.verticalLayout_3.addWidget(self.param_t_pourcent)

        self.param_kornia = QWidget(self.groupBox_4)
        self.param_kornia.setObjectName(u"param_kornia")
        self.horizontalLayout_9 = QHBoxLayout(self.param_kornia)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_22 = QLabel(self.param_kornia)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_27.addWidget(self.label_22)

        self.spinBox_20 = QSpinBox(self.param_kornia)
        self.spinBox_20.setObjectName(u"spinBox_20")
        self.spinBox_20.setValue(7)

        self.verticalLayout_27.addWidget(self.spinBox_20)


        self.horizontalLayout_9.addLayout(self.verticalLayout_27)

        self.line_10 = QFrame(self.param_kornia)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line_10)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_24 = QLabel(self.param_kornia)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_29.addWidget(self.label_24)

        self.doubleSpinBox_22 = QDoubleSpinBox(self.param_kornia)
        self.doubleSpinBox_22.setObjectName(u"doubleSpinBox_22")
        self.doubleSpinBox_22.setValue(5.000000000000000)

        self.verticalLayout_29.addWidget(self.doubleSpinBox_22)


        self.horizontalLayout_9.addLayout(self.verticalLayout_29)


        self.verticalLayout_3.addWidget(self.param_kornia)

        self.param_t_std = QWidget(self.groupBox_4)
        self.param_t_std.setObjectName(u"param_t_std")
        self.verticalLayout_28 = QVBoxLayout(self.param_t_std)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.param_t_std)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_28.addWidget(self.label_23)

        self.doubleSpinBox_20 = QDoubleSpinBox(self.param_t_std)
        self.doubleSpinBox_20.setObjectName(u"doubleSpinBox_20")
        self.doubleSpinBox_20.setDecimals(1)
        self.doubleSpinBox_20.setValue(3.000000000000000)

        self.verticalLayout_28.addWidget(self.doubleSpinBox_20)


        self.verticalLayout_3.addWidget(self.param_t_std)

        self.param_pourcent_sp = QWidget(self.groupBox_4)
        self.param_pourcent_sp.setObjectName(u"param_pourcent_sp")
        self.horizontalLayout_10 = QHBoxLayout(self.param_pourcent_sp)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_25 = QLabel(self.param_pourcent_sp)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_30.addWidget(self.label_25)

        self.doubleSpinBox_21 = QDoubleSpinBox(self.param_pourcent_sp)
        self.doubleSpinBox_21.setObjectName(u"doubleSpinBox_21")
        self.doubleSpinBox_21.setValue(0.950000000000000)

        self.verticalLayout_30.addWidget(self.doubleSpinBox_21)


        self.horizontalLayout_10.addLayout(self.verticalLayout_30)

        self.line_11 = QFrame(self.param_pourcent_sp)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_11)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_26 = QLabel(self.param_pourcent_sp)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_31.addWidget(self.label_26)

        self.doubleSpinBox_23 = QDoubleSpinBox(self.param_pourcent_sp)
        self.doubleSpinBox_23.setObjectName(u"doubleSpinBox_23")
        self.doubleSpinBox_23.setValue(1.300000000000000)

        self.verticalLayout_31.addWidget(self.doubleSpinBox_23)


        self.horizontalLayout_10.addLayout(self.verticalLayout_31)


        self.verticalLayout_3.addWidget(self.param_pourcent_sp)

        self.param_t_none = QWidget(self.groupBox_4)
        self.param_t_none.setObjectName(u"param_t_none")
        self.horizontalLayout_6 = QHBoxLayout(self.param_t_none)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.param_t_none)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.comboBox_thresh_postprocess = QComboBox(self.groupBox_6)
        self.comboBox_thresh_postprocess.setObjectName(u"comboBox_thresh_postprocess")

        self.verticalLayout_13.addWidget(self.comboBox_thresh_postprocess)

        self.param_po_none_3 = QWidget(self.groupBox_6)
        self.param_po_none_3.setObjectName(u"param_po_none_3")
        self.horizontalLayout_16 = QHBoxLayout(self.param_po_none_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_13.addWidget(self.param_po_none_3)

        self.param_tp_o = QWidget(self.groupBox_6)
        self.param_tp_o.setObjectName(u"param_tp_o")
        self.param_tp_o.setEnabled(True)
        self.horizontalLayout_17 = QHBoxLayout(self.param_tp_o)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_30 = QLabel(self.param_tp_o)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_35.addWidget(self.label_30)

        self.spinBox_23 = QSpinBox(self.param_tp_o)
        self.spinBox_23.setObjectName(u"spinBox_23")
        self.spinBox_23.setValue(3)

        self.verticalLayout_35.addWidget(self.spinBox_23)


        self.horizontalLayout_17.addLayout(self.verticalLayout_35)

        self.line_14 = QFrame(self.param_tp_o)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.line_14)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_31 = QLabel(self.param_tp_o)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_36.addWidget(self.label_31)

        self.spinBox_26 = QSpinBox(self.param_tp_o)
        self.spinBox_26.setObjectName(u"spinBox_26")
        self.spinBox_26.setValue(3)

        self.verticalLayout_36.addWidget(self.spinBox_26)


        self.horizontalLayout_17.addLayout(self.verticalLayout_36)


        self.verticalLayout_13.addWidget(self.param_tp_o)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_10)


        self.verticalLayout_4.addWidget(self.groupBox_6)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.image_container = QLabel(self.tab_2)
        self.image_container.setObjectName(u"image_container")
        self.image_container.setScaledContents(False)
        self.image_container.setAlignment(Qt.AlignCenter)
        self.image_container.setMargin(-6)

        self.verticalLayout_11.addWidget(self.image_container)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_stop = QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.pushButton_stop)

        self.pushButton_run = QPushButton(self.centralwidget)
        self.pushButton_run.setObjectName(u"pushButton_run")

        self.horizontalLayout_2.addWidget(self.pushButton_run)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1114, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.toolButton_input, self.lineEdit_input)
        QWidget.setTabOrder(self.lineEdit_input, self.comboBox_preprocess)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.toolButton_input.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_input.setText(QCoreApplication.translate("MainWindow", u"H:/images_database/wit_georef_124_paris_1", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Images", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Detection algorithm ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"alpha", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"low threshold", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"high threshold", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Pre-process", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Post-process", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"alpha", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"blur size", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"taille du kernel", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"temperature", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"factor", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"threshold pourcentage on histogram", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"factor", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Threshold Post-process", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"x size", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"y size", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Config", None))
        self.image_container.setText(QCoreApplication.translate("MainWindow", u"Run for output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Result", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"update parameters", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
    # retranslateUi

