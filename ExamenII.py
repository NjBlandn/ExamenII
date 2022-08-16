# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 19:03:39 2022

@author: Dell
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os
import snappy
from snappy import Product
from snappy import ProductIO
from snappy import ProductUtils
from snappy import WKTReader
from snappy import HashMap
from snappy import GPF
# Para leer shapefiles
import shapefile
import pygeoif

####LEER LOS DATOS DE LA IMAGEN
#Cargar imagenes
path_to_sentinel_data = "C:/Users/Dell/Desktop/Desarrollo/actividad7/S1B_IW_GRDH_1SDV_20201119T235742_20201119T235807_024341_02E47D_DCF6.zip"
product = ProductIO.readProduct(path_to_sentinel_data)
#Leer y mostrar la informaciónd de la imagen
width = product.getSceneRasterWidth()
print("Width: {} px".format(width))
height = product.getSceneRasterHeight()
print("Height: {} px".format(height))
name = product.getName()
print("Name: {}".format(name))
band_names = product.getBandNames()
print("Band names: {}".format(", ".join(band_names)))