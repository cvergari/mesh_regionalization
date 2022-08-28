# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:45:52 2022

@author: adminibh
"""

import numpy as np

def generateColors(N):
    """ generate N colors.
    Source: https://stackoverflow.com/questions/876853/generating-color-ranges-in-python
    """
    colors = np.linspace(0,100,N+2, dtype=int)
    # Remove 0 and 1
    colors = np.delete(colors,[0, -1])

    return colors