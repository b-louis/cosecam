# This Python file uses the following encoding: utf-8
import os
import sys
from PySide2 import QtWidgets,QtGui
from PySide2 import QtCore
from PySide2.QtCore import QThread, Qt
from main_window import Ui_MainWindow
from msfstools.msfs_dec import *
from osgeo import gdal, osr
import numpy as np
from ...geo.georef import *
from .controller import *
import choices
from imutils import paths, resize
from PIL.ImageQt import ImageQt 
from PIL import Image

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.fillUi()
        self.bindUi()
        # Init
        self.image_pairs = []
        self.current = -1
        self.detectionApp = DetectionWorker()



    def fillUi(self):

        self.comboBox_detection.addItems(choices.detection_list)
        self.comboBox_postprocess.addItems(choices.postprocess_list)
        self.comboBox_preprocess.addItems(choices.preprocess_list)
        self.comboBox_threshold.addItems(choices.threshold_list)
        self.comboBox_thresh_postprocess.addItems(choices.threshold_postprocess_list)
        self.param_d_dpmean.setHidden(True)
        pixmap = QtGui.QPixmap("../../dataset/000.png")
        pixmap = pixmap.scaled(max(pixmap.width() //2,1920),max(pixmap.height() //2,1200))
        self.image_container.setPixmap(pixmap)
        # self.image_container.resize(max(pixmap.width() //2,1920),max(pixmap.height() //2,1200))
        # self.image_container.resize(200,200)
    def bindUi(self):

        def hider_params_detection():
            [x.setHidden(True) for x in self.button_detection.values()]
            self.button_detection[self.comboBox_detection.currentText()].setHidden(False)
        def hider_params_threshold():
            [x.setHidden(True) for x in self.button_threshold.values()]
            self.button_threshold[self.comboBox_threshold.currentText()].setHidden(False)
        def hider_params_postprocess():
            [x.setHidden(True) for x in self.button_postprocess.values()]
            self.button_postprocess[self.comboBox_postprocess.currentText()].setHidden(False)
        def hider_params_preprocess():
            [x.setHidden(True) for x in self.button_preprocess.values()]
            self.button_preprocess[self.comboBox_preprocess.currentText()].setHidden(False)
        def hider_params_threshold_postprocess():
            [x.setHidden(True) for x in self.button_threshold_postprocess.values()]
            self.button_threshold_postprocess[self.comboBox_thresh_postprocess.currentText()].setHidden(False)
        def select_folder(lineEdit):
            directory = QtWidgets.QFileDialog.getExistingDirectory(self)
            if len(directory) != 0 :
                lineEdit.setText(directory)
        def setButtonsLists():
            self.button_detection = [
                self.param_d_weightedmean,
                self.param_d_none,
                self.param_d_dpmean,
                self.param_d_none
            ]
            self.button_threshold = [
                self.param_t_value,
                self.param_pourcent_sp,
                self.param_t_pourcent,
                self.param_t_std,
                self.param_kornia,
                self.param_t_none

            ]
            self.button_preprocess = [
                self.param_pr_median,
                self.param_pr_median,
                self.param_pr_none,
            ]
            self.button_postprocess = [
                self.param_po_median_sp,
                self.param_po_none,
            ]
            self.button_threshold_postprocess = [
                self.param_tp_o,
                self.param_po_none,
            ]
            self.button_detection = dict(zip(
                list(choices.detection_list.keys()),
                self.button_detection
                ))
            self.button_threshold = dict(zip(
                list(choices.threshold_list.keys()),
                self.button_threshold
                ))
            self.button_postprocess = dict(zip(
                list(choices.postprocess_list.keys()),
                self.button_postprocess
                ))
            self.button_preprocess = dict(zip(
                list(choices.preprocess_list.keys()),
                self.button_preprocess
                ))
            self.button_threshold_postprocess = dict(zip(
                list(choices.threshold_postprocess_list.keys()),
                self.button_threshold_postprocess
                ))

        def fill_default_value(input,default):
            if len(str(input)) == 0:
                return default
            return input

        def get_values():
            # in_epsg = fill_default_value(self.lineEdit_srs_epsg.text(),4326)
            # out_epsg = fill_default_value(self.lineEdit_tgt_epsg.text(),3857)
            # gdal_format = fill_default_value(self.lineEdit_gdal_format.text(),"GTiff")
            
            ###### tres sale !
            ###### detect
            choices.detection_selected["Weighted Mean"] = choices.detection_list["Weighted Mean"](
                self.param_d_weightedmean.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox").value(),
                self.param_d_weightedmean.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox_2").value(),
                self.param_d_weightedmean.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox_3").value()
            )
            choices.detection_selected["DPMean"] = choices.detection_list["DPMean"](
                self.param_d_dpmean.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox_14").value(),
                self.param_d_dpmean.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox_15").value(),
                self.param_d_dpmean.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox_17").value()
            )
            ######
            ###### thresh
            choices.threshold_selected["Value"] = choices.threshold_list["Value"](
                self.param_t_value.findChild(QtWidgets.QSpinBox,"spinBox_13").value()
            )
            choices.threshold_selected["Standard deviation"] = choices.threshold_list["Standard deviation"](
                self.param_t_std.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox_20").value()
            )
            choices.threshold_selected["Pourcentage of maximum"] = choices.threshold_list["Pourcentage of maximum"](
                self.param_t_pourcent.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox_19").value()
            )
            choices.threshold_selected["Cumsum"] = choices.threshold_list["Cumsum"](
                self.param_pourcent_sp.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox_21").value(),
                self.param_pourcent_sp.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox_23").value(),
            )
            ker_size= self.param_kornia.findChild(QtWidgets.QSpinBox,"spinBox_20").value()
            choices.threshold_selected["Kornia custom"] = choices.threshold_list["Kornia custom"](
                (ker_size,ker_size),
                self.param_kornia.findChild(QtWidgets.QDoubleSpinBox,"doubleSpinBox_22").value(),
            )
            ######
            ###### pre
            choices.preprocess_selected["Median Filter"] = choices.preprocess_list["Median Filter"](
                self.param_pr_median.findChild(QtWidgets.QSpinBox,"spinBox_15").value()
            )
            choices.preprocess_selected["Gauss Filter"] = choices.preprocess_list["Gauss Filter"](
                self.param_pr_median.findChild(QtWidgets.QSpinBox,"spinBox_15").value()
            )
            ######
            ###### post
            ker_size= self.param_po_median_sp.findChild(QtWidgets.QSpinBox,"spinBox_21").value()
            choices.postprocess_selected["Median and Dilate"] = choices.postprocess_list["Median and Dilate"](
                np.ones((ker_size,ker_size)),
                self.param_po_median_sp.findChild(QtWidgets.QSpinBox,"spinBox_24").value(),
            )
            ######
            ###### thresh post
            ker_sizex= self.param_tp_o.findChild(QtWidgets.QSpinBox,"spinBox_23").value()
            ker_sizey= self.param_tp_o.findChild(QtWidgets.QSpinBox,"spinBox_26").value()
            choices.threshold_postprocess_selected["Opening"] = choices.threshold_postprocess_list["Opening"](
                (ker_sizex,ker_sizey)
            )
            values = {

                'detection':choices.detection_selected[self.comboBox_detection.currentText()],
                'preprocess':choices.preprocess_selected[self.comboBox_preprocess.currentText()],
                'postprocess':choices.postprocess_selected[self.comboBox_postprocess.currentText()],
                'threshold':choices.threshold_selected[self.comboBox_threshold.currentText()],
                'threshold_postprocess':choices.threshold_postprocess_selected[self.comboBox_thresh_postprocess.currentText()],
                'input':self.lineEdit_input.text(),
            }
            return values

        def sendStop():
            self.thread.terminate()
            self.thread.quit()
            self.thread.exit()
        def setParameters():
            values = get_values()
            if self.current < 0:
                list_images = sorted(paths.list_images(values['input']))
                self.image_pairs= np.array(list_images).reshape((len(list_images)//2,2))
            self.detectionApp.setConfig(
                values['detection'],
                values['preprocess'],
                values['postprocess'],
                values['threshold'],
                values['threshold_postprocess']
                )
        def setImageFrame(image):
            pixmap = QtGui.QPixmap("tmp_imgs/result.png")
            pixmap = pixmap.scaled(pixmap.width() //4,pixmap.height() //4)
            self.image_container.setPixmap(pixmap)
        def run():
            # Step 2: Create a QThread object
            self.thread = QtCore.QThread()
            # Step 3: Create a worker object
            self.worker = self.detectionApp
            # Step 4: Move worker to the thread
            self.worker.moveToThread(self.thread)
            # Step 5: Connect signals and slots
            self.thread.setTerminationEnabled(True)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.nextstep.connect(setImageFrame)
            self.worker.finished.connect(self.worker.deleteLater)
            self.pushButton_stop.clicked.connect(self.worker.setStop)
            self.thread.finished.connect(self.thread.deleteLater)
            # self.worker.progress.connect(self.reportProgress)
            # Step 6: Start the thread
            
            self.detectionApp.set_image(self.image_pairs)
            self.thread.start()


        self.pushButton_run.clicked.connect(setParameters)
        self.pushButton_run.clicked.connect(run)
        self.pushButton_stop.clicked.connect(sendStop)

        self.comboBox_detection.currentTextChanged.connect(hider_params_detection)
        self.comboBox_threshold.currentTextChanged.connect(hider_params_threshold)
        self.comboBox_preprocess.currentTextChanged.connect(hider_params_preprocess)
        self.comboBox_postprocess.currentTextChanged.connect(hider_params_postprocess)
        self.comboBox_thresh_postprocess.currentTextChanged.connect(hider_params_threshold_postprocess)
        self.toolButton_input.clicked.connect(lambda : select_folder(self.lineEdit_input))

        setButtonsLists()
        hider_params_detection()
        hider_params_threshold()
        hider_params_preprocess()
        hider_params_postprocess()
        hider_params_threshold_postprocess()
        self.comboBox_detection.removeItem(0) # remove Weight Mean
        self.comboBox_postprocess.setCurrentIndex(1) # Median dilate is bad
        self.comboBox_preprocess.setCurrentIndex(1) # Median is bad too
        self.comboBox_threshold.setCurrentIndex(3)
        self.pushButton_stop.hide()
        self.pushButton_stop.setDisabled(True) # Doesnt work !
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())