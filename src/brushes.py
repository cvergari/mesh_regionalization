# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:52:53 2022

@author: zep10
"""
import pyvista as pv
import pyvistaqt as pvqt
import numpy as np
from PySide2 import QtWidgets, QtCore


class RayTracer():

    def __init__(self, plotter, mesh, radius = 100):
        self.plotter = plotter
        self.mesh = mesh
        self.radius = radius
        self.current_point = None


    def FindPoint(self):
        """ Find a point on the mesh just below the mouse. uses ray tracing.
        
        Returns
        -------
        tuple
            point: 3D coordinates.
        int
            index: index of the closest mesh cell

        """
            
        
        if not self.mesh:
            return None, None

        self.current_point = self.plotter.pick_mouse_position()
        picked_pt = np.array(self.current_point)

        # Define a stabbing vector
        direction = picked_pt - self.plotter.camera_position[0]
        direction = direction / np.linalg.norm(direction)
        start = picked_pt - 10000 * direction
        end = picked_pt + 100000 * direction

        # Ray tracing to find the first point hit on the mesh
        # point is a 3-coordinate array. Not necessarily corresponding 
        # to a mesh point
        point, cell_index = self.mesh.ray_trace(start, end, first_point=True)

        return point, cell_index


    def FindCellRegion(self):
        """ Finds a region of the mesh within a certain radius below the mouse.
        The radius is self.radius.
        
        Returns
        -------
        list
            picked_cells_indexes: the indices of the cells below the mouse


        """
        if not self.mesh:
            return []

        point, center_cell_index = self.FindPoint()
        if len(point) == 0:
            # Mouse outside model
            return []
        
        center_cell_index = center_cell_index[0] # This is always a list, take 1st element

        #pts_indexes = self.mesh.find_closest_point(point, self.radius)  # "radius" is in number of cells

        # This is faster than using mesh.find_closest_point():
        _, pts_indexes = self.parent.tree.query(point.reshape(1,3), self.radius)

        if pts_indexes is None:
            return []
        
        # Function will return a list of lists
        pts_indexes = pts_indexes[0]
        

        # Get the cells attached  to points; this is a mesh with new cell numbering
        self.hovered_region = self.mesh.extract_points(pts_indexes)    
        # Get the original cell numbering
        picked_cells_indexes = self.hovered_region.cell_data['vtkOriginalCellIds']        
        
        
        # Check if multiple connected surfaces are seleccted; this means some 
        # cells are on the opposite side of the surface. It can occur if the 
        # surface is thin and the opposite surface is too close. We have to 
        # remove those spurious selections!
        connectivity = self.hovered_region.connectivity(largest=False)

        # If there are more than one region ids, there are unconnected surfaces...
        # deal with it
        regions_id_range = [np.min(connectivity.cell_data['RegionId']), 
                            np.max(connectivity.cell_data['RegionId'])]
        if not  regions_id_range[0] == regions_id_range[1]:
            picked_cells_indexes = keep_region_containing_cell(connectivity, 
                                                               regions_id_range, 
                                                               center_cell_index)


        return picked_cells_indexes



def keep_region_containing_cell(regions, regions_id_range, center_cell_index):
    """ keep_region_containing_cell(regions, regions_id_range, center_cell_index)
        
        *regions* is a mesh issuing from a manual selection. If the surface is thin,
        the selection could be partially on the other side of the mesh. These
        regions should have different ids (listed in *regions_id_range*).
        
        However, the central cell (*center_cell_index*) should be on the 
        correct side because it was selected with the ray tracing method.
        
        
        Attributes
        ----------
        mesh
           regions: a mesh issued from the connectiity() function. It should have 
                    a 'RegionId' cell_data property.
        list of ints
            regions_id_range: a list of possible region IDs, e.g. [0, 1] for two regions
        int
            center_cell_index: index of the center cell of the manual selection

        Returns
        ----------
        list
            indexes: list of indexes of retained cells (the group containing 
                     the central cell)
        
        
    """
    
    region_ids = regions.cell_data['RegionId']
    
    for region_id in regions_id_range:
        indexes = regions.cell_data['vtkOriginalCellIds'][region_ids == region_id]
        
        if center_cell_index in indexes:
            return indexes
    
    raise Exception('There was an error when brushing the surface; the '
                    'hovered surface was composed of unconnected surfaces, but'
                    'I could not determine which was the one to retain!')
    



class PickerBrush(RayTracer):
    """ Picks a region of contiguous cells and adds it to a named region """

    def __init__(self, parent, mesh, name = '_cell_picking_selection', color = 'pink', radius = 100):
        super().__init__(parent.plotter, mesh, radius)

        self.color = color
        self.name = name
        self.parent = parent

    
    def __call__(self, *args):
        """ This is called by the plotter on mouse move. It changes the color of the
            cells where the mouse is hovering over. The "color" identifies a 
            region, and it is a float value between 0 and 100 (excluded). 
            Cells are added to the selection if SHIFT is pressed, removed if CTRL. """
        
        # Return is SHIFT or CTRL are not pressed
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers not in [QtCore.Qt.ControlModifier, QtCore.Qt.ShiftModifier]:
            # if clicked without shift or CTRL, do nothing
            return
        
        # Avoid replotting if mouse did not move
        if self.current_point == self.plotter.pick_mouse_position():
            return
        
        # Find stabbing point and cells around it
        cell_indexes = self.FindCellRegion()
        
        # Check if user wants to add or remove points
        if modifiers == QtCore.Qt.ControlModifier:
            # Remove cells
            self.parent.regions[cell_indexes] = 0
        else:
            # Add cells
            self.parent.regions[cell_indexes] = self.color
    
        # Update colors
        self.plotter.update_scalars(self.parent.regions, mesh=self.mesh)



class LiveBrush(RayTracer):
    """ Plots a spot with specific radius on the 3D model below the mous pointer """
    

    def __init__(self, parent, mesh, radius = 100):
        super().__init__(parent.plotter, mesh, radius)

        self.parent = parent
        self.current_point = None

        self.hovered_region = pv.UnstructuredGrid()
        self.hovered_indexes = []
        self.actor = None  # This is the actual rendered mesh
 

    def __call__(self):
        """ Brushing the model below the mouse hovering regions uses the mesh's 
        scalars. mesh['regions'] is initialized in __init__() with zero values 
        for every cell. The values below the mouse are changed to one, and 
        back to zero when the mouse leaves.
        Values between zero and one codify the different regions.
        """
        
        # Avoid replotting if mouse did not move
        if self.current_point == self.plotter.pick_mouse_position():
            return

        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers in [QtCore.Qt.ControlModifier, QtCore.Qt.ShiftModifier]:
            # If user is pressing CTRL of SHIFt: save resources and do not show 
            # the hovering brush.
            # But first, remove the last cells where mouse was hovering
            data = self.mesh.cell_data['regions']
            data[data == 1] = 0  # Reset old hovering
            self.plotter.update_scalars(data, mesh=self.mesh)
            
            return
        

        # Find stabbing point and cells around it
        cell_indexes = self.FindCellRegion()
        
        # Retrieve already defined regions, and use values as colors
        coloring = np.copy(self.parent.regions)
        
        # Add cell coloring
        coloring[cell_indexes] = 100
        
        self.plotter.update_scalars(coloring, mesh=self.mesh)
