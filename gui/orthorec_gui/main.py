# This Python file uses the following encoding: utf-8
import os
import sys
from PySide2 import QtWidgets,QtGui
from PySide2.QtCore import QThread, Qt
from cv2 import AKAZE
from main_window import Ui_MainWindow
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from msfstools.msfs_dec import *
from osgeo import gdal, osr
import numpy as np
from geo.georef import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.fillUi()
        self.bindUI()
        # Init
    def fillUi(self):
        output_formats = ['png','jpg','tiff','bmp']
        output_mode = ['only homography','homography and georef*','only georef*']
        elevation_type = ['DEM','GEOID*','VALUE*']
        descriptors = ['SIFT','ORB','AKAZE','BRISK']
        ortho_methods = ['GDALWARP cmd','OTB python*']
        type_in = ['MSFS dataset folder','Files*']
        gcps_method = ['Stereo gcps']
        rpcs_method = ['OTB GenerateRPCModel']

        self.comboBox_format.addItems(output_formats)
        self.comboBox_mode.addItems(output_mode)
        self.comboBox_elevation_type.addItems(elevation_type)
        self.comboBox_descriptors.addItems(descriptors)
        self.comboBox_ortho_methods.addItems(ortho_methods)
        self.comboBox_type_in.addItems(type_in)
        self.comboBox_gcps_methods.addItems(gcps_method)
        self.comboBox_rpcs_methods.addItems(rpcs_method)
        self.horizontalWidget_input_points.setEnabled(False)

        self.lineEdit_srs_epsg.setValidator(QtGui.QIntValidator(0,10000,self.lineEdit_srs_epsg))
        self.lineEdit_tgt_epsg.setValidator(QtGui.QIntValidator(0,10000,self.lineEdit_srs_epsg))
    def bindUI(self):

        def select_folder(lineEdit):
            directory = QtWidgets.QFileDialog.getExistingDirectory(self)
            if len(directory) != 0 :
                lineEdit.setText(directory)

        def select_file(lineEdit):
            file_name,_ = QtWidgets.QFileDialog.getOpenFileName(
                self,
                "Open DEM",
                "",
                "DEM (*.dted *.dt2 *.tif *.tiff);;GEOID (*.grd);;All files (*)")
            if len(file_name) != 0 :
                lineEdit.setText(file_name)

        def fill_default_value(input,default):
            if len(str(input)) == 0:
                return default
            return input

        def get_values():
            in_epsg = fill_default_value(self.lineEdit_srs_epsg.text(),4326)
            out_epsg = fill_default_value(self.lineEdit_tgt_epsg.text(),3857)
            gdal_format = fill_default_value(self.lineEdit_gdal_format.text(),"GTiff")
            descriptor = "Descriptors."+self.comboBox_descriptors.currentText()
            matcher = "Matchers."+self.comboBox_matchers.currentText()
            config = {
                # Data parameters
                'root_folder':self.lineEdit_root.text(),
                'folder_name':self.lineEdit_dataset.text(),

                'only_images':False,
                'only_path':False,

                # Features parameters
                'mode': eval('['+descriptor+','+matcher+']'),
                'd' : self.doubleSpinBox_matchd.value(),

                # Gdal/OTB parameters
                'output':self.lineEdit_output_rasters.text(),
                'elev_mode':self.comboBox_elevation_type.currentText(),
                'dem':self.lineEdit_elev_file.text(),
                'in_epsg': in_epsg,
                'out_epsg': out_epsg,

                'gdal_format':gdal_format
            }
            return config

        def process_finished():
            self.pushButton_run.setDisabled(False) 
            self.pushButton_cancel.setDisabled(True) 
        def stop():
            # if self.thread != None and self.geo != None:
            self.geo.finished.emit()
        def run():
            values = get_values()
            geo=[]
            # try :
            dec = Msfs_decoder(
                values['root_folder'],
                values['folder_name'],
                values['only_path'],
                values['only_images'],
                )
            center = dec.getResolution()/2
            gcp_gen = StereoGCP(center)
            rpc_gen = RpcGenerator(values['dem'])
            orthorect = OrthoRectification(projection_gdalcmd,values['dem'])

            # Step 2: Create a QThread object
            self.thread = QThread()
            # Step 3: Create a worker object
            geo = Georeferencer(gcp_gen,rpc_gen,orthorect,mode=values['mode'],d=values['d'])
            self.geo = geo
            geo.setDataset(dec,values['output'])
            # Step 4: Move worker to the thread
            geo.moveToThread(self.thread)
            # Step 5: Connect signals and slots
            self.thread.started.connect(geo.run)
            geo.finished.connect(process_finished)
            geo.finished.connect(self.thread.quit)
            geo.finished.connect(geo.deleteLater)
            geo.progress.connect(self.progressBar.setValue)
            self.thread.finished.connect(self.thread.deleteLater)
            # Step 6: Start the thread
            self.thread.start()
            self.pushButton_run.setDisabled(True) 
            self.pushButton_cancel.setDisabled(False) 
        self.thread = None
        self.geo = None
        self.pushButton_cancel.setDisabled(True) 
        self.pushButton_run.clicked.connect(run)
        self.pushButton_cancel.clicked.connect(stop)
        self.toolButton_in_rasters.clicked.connect(lambda : select_folder(self.lineEdit_root))
        self.toolButton_out_rasters.clicked.connect(lambda : select_folder(self.lineEdit_output_rasters))
        self.toolButton_elev.clicked.connect(lambda : select_file(self.lineEdit_elev_file))
        self.checkBox_input_points.clicked.connect(lambda x : self.horizontalWidget_input_points.setEnabled(x))
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
