#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 14,  LISTAS 5, Eliminar elementos con POP() 
                                    #Pop() Elimina elementos y los almacena en una nueva variable


colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Lista inicializada con 10 elementos de tipo String
print("\n\t Lista Original", colores) #Imprimimos la lista 

color1 = colores.pop(1) #Eliminamos un elemento de la lista 'colores' en su posición 1, y lo alamacenaremos en una nueva variable
color2 = colores.pop(7)#Eliminamos un elemento de la lista 'colores' en su posición 7, y lo alamacenaremos en una nueva variable

colores_guardados = [color1, color2] #Guardamos en una nueva lista las variables de nuestros elementos borrados de la lilsta anterior
print("\n\t Colores eliminados: ",colores_guardados) #Imprimimos los colores eliminados
