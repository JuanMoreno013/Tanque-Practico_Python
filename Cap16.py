#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 16,  LISTAS 6, Insertar elementos con insert()
                                    #insert() Añade elementos a una lista en cualquier posición asignada.

#Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert().
# Tendrás que posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición. 
# Deberás hacer esto utilizando posiciones de lista negativas.


colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Lista inicializada con 10 elementos de tipo String
print("\n Lista Original: ", colores) #Imprimimos la lista 

colores.insert(6, 'magenta') #Añadimos este elemento a nuestra lista en la posición 6, ára que esté después de lila
colores.insert(-1, 'turquesa') #Añadimos este elemento a nuestra lista en la posición -1 (penultima)


print("\n Nueva lista: ",colores) #Imprimos nuestra lista con los nuevos colores añadidos


