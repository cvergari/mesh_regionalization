# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 09:28:01 2022

@author: zep10
"""


import pyvista as pv
import pyvistaqt as pvqt
import numpy as np

import sys

pelvis_mesh = pv.read('../data/Bassin.stl')
#pelvis_mesh['scalars'] = pelvis_mesh.points[:, 1] * 0



class RayTracer():

    def __init__(self, plotter, mesh):
        self.plotter = plotter
        self.mesh = mesh
        self.radius = 100

    def FindPoint(self):

        picked_pt = np.array(self.plotter.pick_mouse_position())

        # Define a stabbing vector
        direction = picked_pt - self.plotter.camera_position[0]
        direction = direction / np.linalg.norm(direction)
        start = picked_pt - 10000 * direction
        end = picked_pt + 100000 * direction

        # Ray tracing to find the first point hit
        point, index = self.mesh.ray_trace(start, end, first_point=True)

        return point, index

    def FindCellRegion(self):

        point, index = self.FindPoint()
        index = self.mesh.find_closest_point(point, self.radius)

        if len(index) == 0:
            # Mouse outside model
            return None

        picked_cells = self.mesh.extract_points(index)

        return picked_cells



class Picker(RayTracer):
    def __init__(self, plotter, mesh):
        super().__init__(plotter,mesh)

        self._points = []
        self.picked = pv.UnstructuredGrid()

        self.enabled = False

    @property
    def points(self):
        """To access all the points when done."""
        return self._points

    def __call__(self, *args):
        # Find the point picked
        picked_cells = self.FindCellRegion()

        if not picked_cells:
            # Mouse outside model
            return

        self.picked.merge(picked_cells, inplace=True)

        #print(self.picked)

        self.display()

        return

    def key_press(self):
        self.enabled = not self.enabled
        print(self.enabled)


    def display(self):
        """ Plots the selected mesh """
        self.plotter.add_mesh(self.picked,
              style='wireframe',
              line_width=5, color='pink',
              name='_cell_picking_selection')
        return


class LiveBrush(RayTracer):

    def __init__(self, plotter):
        self.plotter = plotter

    def brush(self):

        picked_pt = np.array(self.plotter.pick_mouse_position())
        print('Mouse position: ', picked_pt)

class Selector3D():
    
    def init(self):

        self.plotter = pvqt.BackgroundPlotter(notebook=0)

        self.plotter.add_mesh(pelvis_mesh, show_edges=False, opacity=1, lighting=True, label="Test Mesh")

        self.picker = Picker(self.plotter, pelvis_mesh)
        self.brush = LiveBrush(self.plotter)

        self.plotter.track_click_position(picker, side='right')
        self.plotter.add_key_event('a', picker.key_press)

        self.plotter.track_mouse_position()
        self.plotter.add_callback(brush.brush, 500)

#p.app.exec_()
