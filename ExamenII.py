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

##Crear una funcion para mostrar el producto en una
def plotBand(product, band, vmin, vmax):
    band = product.getBand(band)
    w = band.getRasterWidth()
    h = band.getRasterHeight()
    print(w, h)
    band_data = np.zeros(w * h, np.float32)
    band.readPixels(0, 0, w, h, band_data)
    band_data.shape = h, w
    width = 12
    height = 12
    plt.figure(figsize=(width, height))
    imgplot = plt.imshow(band_data, cmap=plt.cm.binary, vmin=vmin, vmax=vmax)
    return imgplot

##PRE-PROCESAMIENTO

##Aplicar correccion orbital
parameters = HashMap()
GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
parameters.put('orbitType', 'Sentinel Precise (Auto Download)')
parameters.put('polyDegree', '3')
parameters.put('continueOnFail', 'false')
apply_orbit_file = GPF.createProduct('Apply-Orbit-File', parameters, product)

##Recortar la imagen
r = shapefile.Reader("C:/Users/Dell/Desktop/Desarrollo/san manuel/shape/San_Manuel_JC.shp")
g=[]
for s in r.shapes():
    g.append(pygeoif.geometry.as_shape(s))
m = pygeoif.MultiPoint(g)
wkt = str(m.wkt).replace("MULTIPOINT", "POLYGON(") + ")"
#Usar el shapefile para cortar la imagen
SubsetOp = snappy.jpy.get_type('org.esa.snap.core.gpf.common.SubsetOp')
bounding_wkt = wkt
geometry = WKTReader().read(bounding_wkt)
HashMap = snappy.jpy.get_type('java.util.HashMap')
GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
parameters = HashMap()
parameters.put('copyMetadata', True)
parameters.put('geoRegion', geometry)
product_subset = snappy.GPF.createProduct('Subset', parameters, apply_orbit_file)