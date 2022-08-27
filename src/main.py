
import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QGridLayout
from pyvistaqt import QtInteractor

from appwindow import AppWindow
from Model3D import Model3D


pelvis_mesh_path = '../data/Bassin.stl'



#selector.plotter.app.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    Window = AppWindow()

    # Window.Model3D = Model3D(parent = Window, mesh = pelvis_mesh_path,
    #                          plotter = Window.ui.main_widget)
    #selector.plotter.app.exec_()
    Window.show()

    app.exec_()
