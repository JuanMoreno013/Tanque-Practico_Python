#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 24,  CONDICIONALES 4 , Comprobar datos en listas y tuplas
                                   

entrada = input('Introduce el color:\n')#pedimos el color a buscar
tupla = ("rojo","azul","verde","negro")#declaramos la tupla

if entrada in tupla:#si el color buscado esta dentro, corre la tupla
    print('Color admitido en la tupla.')
else:#de ser lo contrario, se corre el else
    print('El color que buscas no está admitido.')