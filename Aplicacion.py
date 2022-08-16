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
vent.config(bg= 'gray')

# Widget 1 #

# Agregar etiqueta 1
etiq1 = tk.Label(vent, text='1. Seleciona la imagen a utilizar.', bg='silver',  fg='black', font = 'Calibri 10')
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
etiq2 = tk.Label(vent, text='2. Seleciona el Shapefile de la zona de estudio.', font = 'Calibri 10', bg='silver', fg='black')
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