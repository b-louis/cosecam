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
        MainWindow.resize(1227, 1000)
        MainWindow.setMinimumSize(QSize(1000, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_run = QPushButton(self.centralwidget)
        self.pushButton_run.setObjectName(u"pushButton_run")

        self.gridLayout.addWidget(self.pushButton_run, 7, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout.addWidget(self.progressBar, 6, 0, 1, 1)

        self.groupBox_simvars = QGroupBox(self.centralwidget)
        self.groupBox_simvars.setObjectName(u"groupBox_simvars")
        self.gridLayout_2 = QGridLayout(self.groupBox_simvars)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget_simvars = QListWidget(self.groupBox_simvars)
        self.listWidget_simvars.setObjectName(u"listWidget_simvars")
        self.listWidget_simvars.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_2.addWidget(self.listWidget_simvars, 2, 1, 1, 1)

        self.label_simvars = QLabel(self.groupBox_simvars)
        self.label_simvars.setObjectName(u"label_simvars")

        self.gridLayout_2.addWidget(self.label_simvars, 0, 1, 1, 1)

        self.listWidget_simvars_endbegin = QListWidget(self.groupBox_simvars)
        self.listWidget_simvars_endbegin.setObjectName(u"listWidget_simvars_endbegin")
        self.listWidget_simvars_endbegin.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_2.addWidget(self.listWidget_simvars_endbegin, 2, 2, 1, 1)

        self.label_simvars_endbegin = QLabel(self.groupBox_simvars)
        self.label_simvars_endbegin.setObjectName(u"label_simvars_endbegin")

        self.gridLayout_2.addWidget(self.label_simvars_endbegin, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_simvars, 1, 0, 1, 1)

        self.groupBox_options = QGroupBox(self.centralwidget)
        self.groupBox_options.setObjectName(u"groupBox_options")
        self.groupBox_options.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_options)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_fps = QLabel(self.groupBox_options)
        self.label_fps.setObjectName(u"label_fps")

        self.verticalLayout_4.addWidget(self.label_fps)

        self.spinBox_fps = QSpinBox(self.groupBox_options)
        self.spinBox_fps.setObjectName(u"spinBox_fps")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_fps.sizePolicy().hasHeightForWidth())
        self.spinBox_fps.setSizePolicy(sizePolicy)
        self.spinBox_fps.setValue(1)

        self.verticalLayout_4.addWidget(self.spinBox_fps)

        self.label_nb_imgs = QLabel(self.groupBox_options)
        self.label_nb_imgs.setObjectName(u"label_nb_imgs")

        self.verticalLayout_4.addWidget(self.label_nb_imgs)

        self.spinBox_nb_imgs = QSpinBox(self.groupBox_options)
        self.spinBox_nb_imgs.setObjectName(u"spinBox_nb_imgs")
        self.spinBox_nb_imgs.setValue(50)

        self.verticalLayout_4.addWidget(self.spinBox_nb_imgs)

        self.label_format = QLabel(self.groupBox_options)
        self.label_format.setObjectName(u"label_format")

        self.verticalLayout_4.addWidget(self.label_format)

        self.comboBox_format = QComboBox(self.groupBox_options)
        self.comboBox_format.setObjectName(u"comboBox_format")

        self.verticalLayout_4.addWidget(self.comboBox_format)

        self.label_display = QLabel(self.groupBox_options)
        self.label_display.setObjectName(u"label_display")

        self.verticalLayout_4.addWidget(self.label_display)

        self.comboBox_display = QComboBox(self.groupBox_options)
        self.comboBox_display.setObjectName(u"comboBox_display")

        self.verticalLayout_4.addWidget(self.comboBox_display)

        self.label_modes = QLabel(self.groupBox_options)
        self.label_modes.setObjectName(u"label_modes")

        self.verticalLayout_4.addWidget(self.label_modes)

        self.checkBox_modes = QCheckBox(self.groupBox_options)
        self.checkBox_modes.setObjectName(u"checkBox_modes")

        self.verticalLayout_4.addWidget(self.checkBox_modes)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.groupBox_options, 4, 0, 1, 1)

        self.verticalGroupBox_main = QGroupBox(self.centralwidget)
        self.verticalGroupBox_main.setObjectName(u"verticalGroupBox_main")
        self.verticalLayout = QVBoxLayout(self.verticalGroupBox_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.label_root = QLabel(self.verticalGroupBox_main)
        self.label_root.setObjectName(u"label_root")

        self.verticalLayout.addWidget(self.label_root)

        self.horizontalLayout_root = QHBoxLayout()
        self.horizontalLayout_root.setSpacing(0)
        self.horizontalLayout_root.setObjectName(u"horizontalLayout_root")
        self.horizontalLayout_root.setContentsMargins(-1, 0, 0, -1)
        self.toolButton_root = QToolButton(self.verticalGroupBox_main)
        self.toolButton_root.setObjectName(u"toolButton_root")
        self.toolButton_root.setCheckable(False)
        self.toolButton_root.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_root.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_root.setAutoRaise(False)
        self.toolButton_root.setArrowType(Qt.NoArrow)

        self.horizontalLayout_root.addWidget(self.toolButton_root)

        self.lineEdit_root = QLineEdit(self.verticalGroupBox_main)
        self.lineEdit_root.setObjectName(u"lineEdit_root")

        self.horizontalLayout_root.addWidget(self.lineEdit_root)


        self.verticalLayout.addLayout(self.horizontalLayout_root)

        self.label_dataset = QLabel(self.verticalGroupBox_main)
        self.label_dataset.setObjectName(u"label_dataset")

        self.verticalLayout.addWidget(self.label_dataset)

        self.lineEdit_dataset = QLineEdit(self.verticalGroupBox_main)
        self.lineEdit_dataset.setObjectName(u"lineEdit_dataset")
        self.lineEdit_dataset.setEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_dataset)


        self.gridLayout.addWidget(self.verticalGroupBox_main, 0, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 5, 0, 1, 1)

        self.textBrowser_tuto = QTextBrowser(self.centralwidget)
        self.textBrowser_tuto.setObjectName(u"textBrowser_tuto")
        self.textBrowser_tuto.setOpenExternalLinks(True)
        self.textBrowser_tuto.setOpenLinks(True)

        self.gridLayout.addWidget(self.textBrowser_tuto, 0, 2, 8, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1227, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MSFS2020 recorder", None))
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.groupBox_simvars.setTitle(QCoreApplication.translate("MainWindow", u"Simvars", None))
        self.label_simvars.setText(QCoreApplication.translate("MainWindow", u"Captured Values during the whole recordings", None))
        self.label_simvars_endbegin.setText(QCoreApplication.translate("MainWindow", u"Captured values at the end and begining", None))
        self.groupBox_options.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.label_fps.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.label_nb_imgs.setText(QCoreApplication.translate("MainWindow", u"Number of images", None))
        self.label_format.setText(QCoreApplication.translate("MainWindow", u"Format", None))
        self.comboBox_format.setCurrentText("")
        self.label_display.setText(QCoreApplication.translate("MainWindow", u"Recording Display", None))
        self.comboBox_display.setCurrentText("")
        self.label_modes.setText(QCoreApplication.translate("MainWindow", u"Modes", None))
#if QT_CONFIG(tooltip)
        self.checkBox_modes.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Only records the images, <span style=\" font-weight:600;\">plane's values are ignored</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_modes.setText(QCoreApplication.translate("MainWindow", u"Only images", None))
        self.verticalGroupBox_main.setTitle(QCoreApplication.translate("MainWindow", u"Process", None))
        self.label_root.setText(QCoreApplication.translate("MainWindow", u"Root folder", None))
        self.toolButton_root.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lineEdit_root.setText("")
        self.lineEdit_root.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set root folder for all recordings", None))
        self.label_dataset.setText(QCoreApplication.translate("MainWindow", u"Dataset name", None))
        self.lineEdit_dataset.setText(QCoreApplication.translate("MainWindow", u"dataset", None))
        self.lineEdit_dataset.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set the dataset name", None))
        self.textBrowser_tuto.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"steps\"></a><span style=\" font-size:8pt; font-weight:600;\">S</span><span style=\" font-size:8pt; font-weight:600;\">TEPS</span></h1>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">After you launch the game, you have to :</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0"
                        "px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Chose 'Flight'</li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To chose a route, there's multiple ways</li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can do a <span style=\" font-style:italic;\">right click</span> on and select your departure position and your arrival </li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You also can <span style=\" font-style:italic;\">click</span> on the existing points of interest, </li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-bl"
                        "ock-indent:2; text-indent:0px;\"><span style=\" font-size:8pt;\">Be careful by selecting a existing point, you can end up in a position with no speed etc (\u00e0 revoir !)</span></p>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Or You can select them from the search bar</li></ul>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Chose your flight attitude in <span style=\" font-style:italic;\">navigation journal</span></li>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:8pt;\">Be careful (as 27/07/2021) the attitude doesn't account landforms, you can end up too close to the ground.</span></p>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\">Select weather condition (can be changed via dev panel)</li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select your plane (<span style=\" font-weight:600;\">the cruising speed is different from one another</span>)</li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Launch your flight, at the end of the loading, the game doesn't start directly it's paused. Press 'Resume??' <span style=\" font-weight:600;\">The plane is on your control at the beginning, you have to set AI pilot first</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Menus are hidden unless you move your mouse, press <span style=\" font-weight:600;\">'Pause'</span> butto"
                        "n.</li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Then select the <span style=\" font-weight:600;\">Control</span> section and check <span style=\" font-weight:600;\">AI pilot</span></li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Now you have to unpause the game until the plane is on a stable speed, attitude and heading.<br />Unfortunatly sometime, the simulation starts at the opposite direction.</li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When everything is stable enough, <span style=\" font-weight:600;\">you can set your camera</span> </li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px;\">Go to <span style=\" font-weight:600;\">Camera</span> section and set <span style=\" font-weight:600;\">Drone camera</span> (you'll see the camera pointing to the ground)</li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Close all ingame windows (Camera, AI pilot ...) and unpause the game.<br /><span style=\" font-weight:600;\">Becareful,</span> during the recording, you have to stand still and not move anything on your computer otherwise <br />your recording will be affected by theses changes.<br />Also <span style=\" font-weight:600;\">remove all windows overlaying your window game</span> for the same reasons above. </li>\n"
"<li style=\" font-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Now on the recorder gui, start your recording or if you use a python script, launch it. </li>\n"
"<li style=\" fo"
                        "nt-size:8pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">We recording is finished, you'll have all your images and the planes values on the folder you specified .</li></ol>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:40px; margin-right:40px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Written with </span><a href=\"https://stackedit.io/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">StackEdit</span></a><span style=\" font-size:8pt;\">. </span></p></body></html>", None))
    # retranslateUi

