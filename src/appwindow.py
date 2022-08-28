
import sys
from functools import partial
from zipfile import is_zipfile
from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon

from mesh_regionalization.qt_gui.mainwindow import MainWindow
from .config import REGIONS, REGION_COLORS
from .Model3D import Model3D
from .loadsave import save_data, load_data


class ToggleButton(QtWidgets.QPushButton):
    """ A subclass just to add a color, and make the button checkable by default """

    def __init__(self, title, color):
        super().__init__(title)

        self.color = color
        self.title = title
        self.setCheckable(True)  # Make it a toggle button

        self.setStyleSheet("QPushButton::checked"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             )


class AppWindow(MainWindow):
    """ Main window. This inherits from the GUI layout made with QT Editor """

    def __init__(self, region_colors = None):
        """ The gui can be initialized by passing a region_colors dictionnary, 
        where the keys are the names of the region, and "colors" are integers between 0 and 100 (excluded).
        For example:
            region_colors = {'Region 1': 20, 'Region 2': 40, 'Region 3': 60, 'Region 4': 80}
            
        """
    
    
        super().__init__()

        self.last_save_file = None
        self.Model3D = None
        
        self.setWindowTitle('Mesh regionalizer')
        self.setWindowIcon(QIcon("../images/icon.png"))

        # Impose control frame alignement
        self.ui.ControlsLayout = QtWidgets.QGridLayout(self.ui.main_widget)
        self.ui.ControlsLayout.addWidget(self.ui.frame_controls,0,0, Qt.AlignRight  | Qt.AlignTop )


        # Load regions
        if not region_colors:
            region_colors = REGION_COLORS

        # Create region buttons
        self.region_buttons = {}
        for region, color in region_colors.items():
            btn = ToggleButton(title = region, color = color)

            # Connect it to a callback gunction and pass the region name
            btn.clicked.connect(partial(self.region_button_callback, region))
            self.region_buttons[region] = btn
            self.ui.layout_regions.addWidget(btn)


        # Add actions to menus
        self.ui.mnOpen.triggered.connect(self.OpenFile)
        self.ui.mnSave_as.triggered.connect(self.mn_save_data_as)
        self.ui.mnSave.triggered.connect(self.mn_save_data)
        self.ui.mnQuit.triggered.connect(self.close_app)

        # Create statusbar messages
        status_label = QtWidgets.QLabel(self)
        status_label.setText('Ready...')
        instructions_label = QtWidgets.QLabel(self)
        instructions_label.setText('SHIFT to add to region. CTRL to remove from region.')

        self.ui.statusbar.addWidget(status_label)
        self.ui.statusbar.addPermanentWidget(instructions_label)

        # Slider init
        self.ui.radiusSlider.valueChanged.connect(self.radius_change)
        self.ui.labelRadius.setText('Selection radius: {}'.format(self.ui.radiusSlider.value()))


    def close_app(self):
        """ Exit program """

        sys.exit()

    def mn_save_data_as(self):
        """ Called from GUI menu when user wants to save by creating a new file """

        filename = QtWidgets.QFileDialog.getSaveFileName(self,
                                               "Save 3D data",
                                               "",
                                               "Save File (*.3D)")

        if not filename[0]:
            return

        self.save_data(filename[0])


    def mn_save_data(self):
        """ Called from GUI menu when user wants to save by overwriting an existing file """


        if not self.last_save_file:
            return

        self.save_data(self.last_save_file)


    def save_data(self, save_file):
        """ Saves the mesh and the regions. The save file is actually a zip file
        containing the STL and the regions. """

        data = {'mesh': self.Model3D.mesh,
                'regions': self.Model3D.mesh.cell_data['regions'],
                'region_data': REGION_COLORS
                }

        save_data(data, save_file)
        self.last_save_file = save_file

        txt = f'Data saved in: {save_file}'
        self.ui.statusbar.showMessage(txt, timeout = 2000)




    def radius_change(self, value):
        """ Called when the radius changes in the slider.
            It updates the GUI label and the brushes in the 3D model
        """

        self.ui.labelRadius.setText(f'Selection radius: {value}')

        if not self.Model3D:
            return

        self.Model3D.brush.radius = value
        if self.Model3D.picker:
            self.Model3D.picker.radius = value


    def OpenFile(self):
        """ Opens a save file (.3D) or 3D model mesh (.stl) """

        def WrongFile(text):
            """ Opens a message box showing "text" """

            msgbox = QtWidgets.QMessageBox()
            msgbox.setText(text)
            msgbox.exec()

        filename = QtWidgets.QFileDialog.getOpenFileName(self,
                                               "Open mesh or data",
                                               "",
                                               "Supported files (*.stl *.3D);;All files (*.*)")
        filename = filename[0]
        if not filename:
            WrongFile(filename)
            return


        # Check file extension
        if not (filename.lower().endswith('.3d') or filename.lower().endswith('.stl')):
            WrongFile(f'File format not recognized: {filename}')
            return

        if filename.lower().endswith('.3d'):
            # Check if valid zipfile
            if not is_zipfile(filename):
                WrongFile(f'Save file not recognized; it mgiht be corrupted: {filename}')

            try:# Load saved data
                data = load_data(filename)
            except Exception:
                WrongFile(f'Save file not recognized; it mght be corrupted: {filename}')

            self.delete_mesh()
            self.last_save_file = filename

            # Create a new Model3D
            self.Model3D = Model3D(parent = self, mesh = data['mesh'],
                                   plotter = self.ui.main_widget,
                                   regions = data['regions'])

        else:
            # Load new mesh
            self.delete_mesh()
            self.last_save_file = None

            # Create a new Model3D
            self.Model3D = Model3D(parent = self, mesh = filename,
                                   plotter = self.ui.main_widget)

        # Update radius values
        self.radius_change(self.ui.radiusSlider.value())


    def delete_mesh(self):
        """  Delete previous mesh """

        try:
            self.Model3D.plotter.clear()
            del self.Model3D.plotter
            del self.Model3D
        except Exception:
            pass


    def load_data(self):

        filename = QtWidgets.QFileDialog.getOpenFileName(self,
                                               "Open 3D data",
                                               "",
                                               "3D Files (*.3D)")
        if not filename[0]:
            return

        data = load_data(filename[0])
        self.last_save_file = filename[0]

        self.delete_mesh()

        # Create a new Model3D
        self.Model3D = Model3D(parent = self, mesh = data['mesh'],
                               plotter = self.ui.main_widget,
                               regions = data['regions'])

        # Update radius values
        self.radius_change(self.ui.radiusSlider.value())


    def region_button_callback(self, region):
        """ called when region buttons are pressed.

        Parameters:

            region (str): region name
        """

        # Change the state the other buttons
        for btn_name,_ in self.region_buttons.items():
            if not btn_name == region:
                self.region_buttons[btn_name].setChecked(False)

        if not self.Model3D:
            return

        # A button was pressed, so delete the region picker anyway
        self.Model3D.deletePicker()


        # Create or destroy picker
        if self.region_buttons[region].isChecked():
            self.Model3D.createPicker(region,
                                      color = self.region_buttons[region].color,
                                      radius = self.ui.radiusSlider.value())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    Window = AppWindow()
    Window.show()

    app.exec_()
