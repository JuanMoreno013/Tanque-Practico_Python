#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y as� poder utilizar caracteres especiales

#CAPITULO 16,  LISTAS 6, Insertar elementos con insert()
                                    #insert() A�ade elementos a una lista en cualquier posici�n asignada.

#A�ade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert().
# Tendr�s que posicionar 'magenta' en la posici�n siguiente a la de 'lila' y 'turquesa' en la pen�ltima posici�n. 
# Deber�s hacer esto utilizando posiciones de lista negativas.


colores = ['rojo', 'azul', 'verde', 'amarillo', 'marr�n', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Lista inicializada con 10 elementos de tipo String
print("\n Lista Original: ", colores) #Imprimimos la lista 

colores.insert(6, 'magenta') #A�adimos este elemento a nuestra lista en la posici�n 6, �ra que est� despu�s de lila
colores.insert(-1, 'turquesa') #A�adimos este elemento a nuestra lista en la posici�n -1 (penultima)


print("\n Nueva lista: ",colores) #Imprimos nuestra lista con los nuevos colores a�adidos


