
#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 12,  LISTAS 3, Eliminar elementos con del()

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Lista inicializada con 10 elementos
print("\n\t Lista Original: ", colores) #Imprimimos nuestra lista de colores

colores1= colores # Asginamos nuestra lista a otra lista para posterior eliminar elementos de la misma
del colores1[1] #Eliminamos un elemento, en su posición 1, de nuestra nueva lista
del colores1[3] #Eliminamos un elemento, en su posición 3, de nuestra nueva lista
del colores1[4] #Eliminamos un elemento, en su posición 4, de nuestra nueva lista
del colores1[-3] #Eliminamos un elemento, en su posición -3, de nuestra nueva lista

print("\n\t Nueva lista : ", colores1) #Imprimimos nuestra nueva lista con los elementos eliminados