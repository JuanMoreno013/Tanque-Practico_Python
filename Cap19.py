#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 19,  TUPLAS , Crear y manejar tuplas
                                   
#Imprime la segunda posición de esta tupla.
colores = ('rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja') #Tupla con 10 elementos
print("\n\t Color elegido: ", colores[1]) #Imprimimos la segunda posición de la dupla, que está en la posición 1 (azul)

#Utiliza los símbolos de suma y resta para obtener el resultado 25 a partir de los elementos de la siguiente tupla en una variable llamada operacion.

numeros = (10, 1, 5, 11) #Dupla con 4 elementos de tipo int

operacion = numeros[0] + numeros[2] + numeros[3] - numeros[1] #Almacenaremos en una variable la suma de los elementos de la dupla

print("\n\t Resultado es: ",operacion) #Imprimimos él resultado de la suma de los elementos de la dupla
