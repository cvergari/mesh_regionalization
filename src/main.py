import sys
from PySide2 import QtWidgets

from mesh_regionalization.src.appwindow import AppWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    Window = AppWindow()
    Window.show()

    app.exec_()
