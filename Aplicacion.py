# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 19:21:50 2022

@author: Dell
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os
from tkinter.messagebox import showinfo

#Establecer ventana
vent = tk.Tk()
vent.geometry('1400x700')

vent.title('Calculo de Zonas Inundadas')    #Titulo
vent.config(bg= 'ivory2')

# Widget 1 #

# Agregar etiqueta 1
etiq1 = tk.Label(vent, text='1. Seleciona la imagen a utilizar.', bg='gray85',  fg='black', font = 'Calibri 11')
etiq1.grid(row = 0, column = 1, pady = (3))

# caja de texo 1
textResult1 = tk.Text(vent, height = 1, font = 'Calibri 10', bg = 'white', fg = 'black', highlightthickness = 3)                                
textResult1.grid(row = 2, column = 1, padx = (50,50))
#funcion para abrir imagen
def abrir_imagen():
    imagen_abierta=filedialog.askopenfilename(initialdir = "/", title = "Seleccione la imagen.",filetypes = (("zip files","*.zip"),("all files","*.*")))
    print (imagen_abierta)
    textResult1.insert(tk.END, imagen_abierta)
    
#Agregar boton 1
boton1 = tk.Button(text="Seleccionar imagen", font = 'Calibri 10',  bg="white",command=abrir_imagen)
boton1.grid(row = 1, column = 1, padx = (10,10))

# Widget 2 #

#Agregar etiqueta 2
etiq2 = tk.Label(vent, text='2. Seleciona el Shapefile de la zona de estudio.', font = 'Calibri 10', bg='gray85', fg='black')
etiq2.grid(row = 3, column = 1)

#caja de texo 1
textResult2 = tk.Text(vent, height = 1, font = 'Calibri 10', bg = 'white', fg = 'black', highlightthickness = 3)                                     
textResult2.grid(row = 5, column = 1, padx = (100,100))

#funcion para abrir imagen
def abrir_shape():
    shape_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione shapefile",filetypes = (("shapefile files","*.shp"),
                ("all files","*.*")))
    print (shape_abierto)
    textResult2.insert(tk.END, shape_abierto)
    
#Agregar boton 2
boton2 = tk.Button(text="Seleccione el shapefile ", font = 'Helvetica 10', bg="white", command = abrir_shape)
boton2.grid(row = 4, column = 1)
# Widget 3 #

#Agregar etiqueta 3
etiq3 = tk.Label(vent, text='3. Proceda a pre-procesar la imagen.', font = 'Calibri 11', bg='gray85',  fg='black')
etiq3.grid(row = 6, column = 1)


#Agregar boton 3
boton3 = tk.Button(text="Preprocesar la imagen", font = 'Calibri 10', bg="white")
boton3.grid(row = 7, column = 1)

# Widget 4 #

#Agregar etiqueta 4
etiq4 = tk.Label(vent, text='4. Defina el umbral de la mascara de agua.', font = 'Calibri 11', bg='gray85',  fg='black')
etiq4.grid(row = 9, column = 1)

#Agregar caja de texto
umbral = tk.Entry(vent, font= 'Calibri 10', justify = 'center', highlightthickness = 3)
umbral.grid(row = 10, column = 1, pady = (3))
#Agregar boton 4
boton4 = tk.Button(text="Aplicar la mascara", font = 'Calibri 10', bg="white")
boton4.grid(row = 11, column = 1, pady =(3))

# Widget 5 #

#Agregar etiqueta 5
etiq5 = tk.Label(vent, text='5. Crea la imagen GeoTIFF a partir del umbral seleccionado.', font = 'Calibri 11', bg='gray88', fg='black')
etiq5.grid(row = 12, column = 1)

mapa = tk.Canvas(vent, width = 500, height = 600, bg = 'white', highlightthickness = 10)
mapa.grid(row = 0, column = 2, rowspan = 14, pady =(30))

#Agregar boton 5
boton5 = tk.Button(text="Crear el archivo", font = 'Calibri 10', bg="white")
boton5.grid(row = 13, column = 1)

vent.mainloop()