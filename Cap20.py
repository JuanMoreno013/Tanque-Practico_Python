#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 20,  TUPLAS , convertir tuplas a listas y viceversa  tuple() o list()
                                   
#Convierte la siguiente lista en una tupla y asegúrate que se haya convertido en tupla correctamente
# imprimiendo en la consola el tipo de elemento que es.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Lista con 10 elementos



colores_tupla = tuple(colores) #Tuple() crea una tupla a partir de una lista
#List() Crea una lista a partir de una tupla

print(type(colores_tupla))  #Imprimimos el tipo de elemento que es



