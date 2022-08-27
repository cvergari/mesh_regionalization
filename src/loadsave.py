# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:17:12 2022

@author: zep10
"""

import tempfile
import zipfile
import json
import numpy as np
import pyvista as pv
from os import path

import os


def save_data(data, out_file):

    # Dump files in a temporary directory
    tmp_dir, files_list = dump_file(data)

    # Save them in a zip file
    with zipfile.ZipFile(out_file, mode="w") as archive:
        for filepath in files_list:
            # Must retrieve the file name, otherwise the file is stored
            # in ZIP with full path
            filename = path.split(filepath)
            filename = filename[-1]
            # Write
            archive.write(filepath, arcname = filename)


def load_data(filepath):

    data = {}
    tmp_dir = tempfile.TemporaryDirectory()

    with zipfile.ZipFile(filepath, mode="r") as archive:
        for file in archive.namelist():

            archive.extract(file, tmp_dir.name)

            if file.lower().endswith('.stl'):
                # it is a 3D model
                var_name = file[:-len('.stl')]  # remove extension
                filename = os.path.join(tmp_dir.name, file)
                data[var_name] = pv.read(filename)

            elif file.lower().endswith('.dict'):
                var_name = file[:-len('.dict')]  # remove extension
                filename = os.path.join(tmp_dir.name, file)
                data[var_name]  = json.load( open(filename, encoding="utf8") )
                #data[var_name] = json.load(open(filename, 'r'), encoding="utf8")

            elif file.lower().endswith('.array'):
                var_name = file[:-len('.array')]  # remove extension
                filename = os.path.join(tmp_dir.name, file)
                data[var_name]  = np.loadtxt(filename)
                #data[var_name] = json.load(open(filename, 'r'), encoding="utf8")





    return data



def dump_file(data):

    tmp_dir = tempfile.TemporaryDirectory()

    files_list = []
    for key, value in data.items():
        tmp_file = os.path.join(tmp_dir.name, key)

        if isinstance(value, str):
            pass

        elif isinstance(value, dict):
            # Write dictionnary as JSON
            tmp_file = tmp_file + '.dict'
            #with open(tmp_file, 'w', encoding='utf8') as file:
            json.dump(value, open(tmp_file, 'w', encoding='utf8'))

        elif isinstance(value, pv.pyvista_ndarray):
            tmp_file = tmp_file + '.array'
            value = np.array(value)
            np.savetxt(tmp_file, value)

        else:
            # Write a mesh file
            tmp_file = tmp_file + '.stl'
            value.save(tmp_file)

        files_list.append(tmp_file)


    return tmp_dir, files_list


if __name__ == '__main__':
    import pyvista as pv
    from config import REGIONS, REGION_COLORS

    pelvis_mesh_path = '../data/Bassin.stl'

    mesh = pv.read(pelvis_mesh_path)
    mesh.cell_data['regions'] = np.zeros(mesh.n_cells)

    # data = {'mesh': mesh,
    #         'regions': {},
    #         }
    data = {'mesh': mesh,
            'regions': mesh.cell_data['regions'],
            'region_data': REGION_COLORS
            }


    out_file = 'C:\\temp\\save.zip'

    save_data(data, out_file)

    data_out = load_data(out_file)
