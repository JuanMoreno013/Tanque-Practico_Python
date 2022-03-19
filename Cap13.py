
#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 13,  LISTAS 4, Eliminar elementos con REMOVE()

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Lista inicializada con 10 elementos
print("\n\t Lista Original: ", colores) #Imprimimos nuestra lista de colores

colores1= colores # Asginamos nuestra lista a otra lista para posterior eliminar elementos de la misma

colores1.remove('amarillo') #Eliminamos un elemento de nuestra lista con el método remove, utilizando el valor de nuestro elemento
colores1.remove('rojo')

print("\n\t Nueva lista : ", colores1) #Imprimimos nuestra nueva lista con los elementos eliminados
