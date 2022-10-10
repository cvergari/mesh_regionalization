from PySide2 import QtWidgets

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from mesh_regionalization.src.appwindow import AppWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    Window = AppWindow()
    Window.show()

    app.exec_()
