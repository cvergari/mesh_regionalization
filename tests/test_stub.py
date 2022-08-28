""" Tests will be implemented. This is just a stub...gotta start somewhere.

"""
import pytest
import os
import sys
import pyvista as pv

sys.path.append('../src')
from Model3D import Model3D

def test_Model3D():

    mesh = pv.Sphere()
    M = Model3D(parent = None, mesh = mesh)
    assert M


if __name__ == '__main__':
    pytest.main(["-x", os.path.abspath(__file__)])

