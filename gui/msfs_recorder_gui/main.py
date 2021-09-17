# This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtWidgets
from .main_window import Ui_MainWindow
from ...msfstools.msfs_rec import *
import traceback

VARS = [
    "PLANE_ALT_ABOVE_GROUND",
    "PLANE_LATITUDE",
    "PLANE_LONGITUDE",
    "TIME"
]

VARS_BEGIN_END = [
    "PLANE_ALTITUDE",
    "AIRSPEED_INDICATED",
    "HEADING_INDICATOR",
]

UNITS = ["FEETS", "DEGREES", "DEGREES", "SECONDS"]
UNITS_BEGIN_END = ["FEETS", "KNOTS", "RADIANS"]
list_Simvars = {
    "PLANE_ALT_ABOVE_GROUND":"FEETS",
    "PLANE_LATITUDE":"DEGREES",
    "PLANE_LONGITUDE":"DEGREES",
    "PLANE_ALTITUDE":"FEETS",
    "AIRSPEED_INDICATED": "KNOTS",
    "HEADING_INDICATOR":"RADIANS",
}
list_sim = np.array(list(list_Simvars.keys()))
list_units = np.array(list(list_Simvars.values()))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # Init
        image_formats = ['png','jpg','tiff','bmp']

        self.comboBox_format.addItems(image_formats)
        self.listWidget_simvars.addItems(list_Simvars)
        self.listWidget_simvars_endbegin.addItems(list_Simvars)
        self.d = d3dshot.create(capture_output="numpy")
        #
        for i in range(3):
            self.listWidget_simvars.item(i).setSelected(True)
            self.listWidget_simvars_endbegin.item(i+3).setSelected(True)
            self.listWidget_simvars.item(i).setToolTip("in "+list_units[i])
            self.listWidget_simvars.item(i+3).setToolTip("in "+list_units[i+3])
        #
        self.pushButton_run.clicked.connect(self.run_recording)
        self.toolButton_root.clicked.connect(self.select_rootfolder)

    
    # Signals
    def select_rootfolder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self)
        if len(directory) != 0 :
            self.lineEdit_root.setText(directory)
    def test(self):
        pass
    def getSelectedString(self,qlist):
        return list(map(lambda x : x.text(),qlist))
    def process_finished(self):
        self.pushButton_run.setDisabled(False)
        #self.progressBar.setValue(0)
    def run_recording(self):
        save_vars = self.getSelectedString(self.listWidget_simvars.selectedItems())
        save_vars_2 = self.getSelectedString(self.listWidget_simvars_endbegin.selectedItems())
        units = list_units[list(np.where(np.isin(list_sim,save_vars))[0])]
        units_be = list_units[list(np.where(np.isin(list_sim,save_vars_2))[0])]
        
        config = {
            'root':self.lineEdit_root.text(),
            'd':self.d,
            'dataset_name':self.lineEdit_dataset.text(),
            'nb_imgs':self.spinBox_nb_imgs.value(),
            'image_format':self.comboBox_format.currentText(),
            'fps':self.spinBox_fps.value(),
            'vars':save_vars,
            'units':units,
            'vars_be':save_vars_2,
            'units_be':units_be,


            
        }
        print(self.spinBox_fps.value())
        print(self.spinBox_fps.text())
        try :
            rec = Msfs_recorder(*config.values())
            rec.progress.connect(self.progressBar.setValue)
            rec.finished.connect(self.process_finished)
            self.pushButton_run.setDisabled(True)
            
            rec.run()
        except Exception as e:
            traceback.print_exc()
            dlg = QtWidgets.QMessageBox.warning(self,"Error","{0}".format(e))
            self.process_finished()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
