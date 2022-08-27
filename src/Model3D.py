# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:28:01 2022

@author: zep10
"""


import pyvista as pv
import pyvistaqt as pvqt
import numpy as np

import os
os.environ["QT_API"] = "pyside2"
from qtpy.QtCore import QTimer

from brushes import PickerBrush, LiveBrush
from loadsave import save_data, load_data



class Model3D():
    """  A 3d model, linked to a pyvista plotter.  """

    def __init__(self, parent, mesh, plotter = None, regions = None):
        """ mesh_path is loaded at startup OR, if an object is passed,
            it is used as is.

        """

        self.parent = parent

        if plotter:
            self.plotter = plotter
        else:
            self.plotter = pvqt.BackgroundPlotter(notebook=0)


        # load mesh
        if isinstance(mesh, str):
            self.mesh_path = mesh
            self.mesh = pv.read(mesh)
        else:
            self.mesh_path = ''
            self.mesh = mesh

        # Initialize regions with float64 0 values
        #self.mesh.cell_data['regions'] = np.zeros(self.mesh.n_cells)
        if regions is None:
            self.mesh.cell_data['regions'] = np.zeros(self.mesh.n_cells)
        else:
            self.mesh.cell_data['regions'] = regions


        self.plotter.add_mesh(self.mesh, clim = [0,1], show_edges=False,
                              opacity=1, lighting=True, label="Main Mesh")

        self.plotter.remove_scalar_bar()

        # Brushes
        self.picker = None  # Picker(self.plotter, self.mesh, self.name, self.color)
        self.brush = LiveBrush(self.plotter, self.mesh)  # highlights the region below the mouse

        self.plotter.track_mouse_position()  #  Starts tracking mouse
        self.add_callback(self.brush, 100)  # Mouse hovering updated every 100 ms


    def createPicker(self, name, color, radius = 100):
        """ A picker is created with a specific name and color"""

        self.picker = PickerBrush(self, self.mesh, name, color, radius)
        #self.plotter.add_key_event('a', self.picker.key_press)
        #self.plotter.track_click_position(self.picker, side='left')
        self.plotter.track_mouse_position()
        self.add_callback(self.picker, 25)  # Mouse hovering updated every 100 ms


    def deletePicker(self):
        """ The picker is deleted (if it exists), and clicks are not tracked anymore """
        self.plotter.untrack_click_position()

        if self.picker:
            self.stop_callback()
            del self.picker
            self.picker = None


    def stop_callback(self):
        """ Stops and deletes the timed callback """

        self._callback_timer.stop()
        del self._callback_timer



    def add_callback(self, func, interval: int = 500) -> None:
        """Add a function that can update the scene in the background.
        Parameters
        ----------
        func :
            Function to be called with no arguments.
        interval :
            Time interval between calls to `func` in milliseconds.
        """
        self._callback_timer = QTimer(parent=self.parent)
        self._callback_timer.timeout.connect(func)
        self._callback_timer.start(interval)
        if self.parent:
            self.parent.signal_close.connect(self._callback_timer.stop)



if __name__ == "__main__":

    pelvis_mesh_path = '../data/Bassin.stl'

    selector = Model3D(parent = None, mesh = pelvis_mesh_path)
    selector.plotter.app.exec_()
