#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y as� poder utilizar caracteres especiales

#CAPITULO 17,  LISTAS 8, Ordenar elementos con sort()
                                    #sort() Ordena una lista de manera alfabetica. (cambios permanentes en la lista)
                                    #sorted() Ordena de la misma manera, solo que los cambios son temporales


  #Ordena la siguiente lista en orden alfab�tico descendente (de la letra 'z' a la 'a').
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marr�n',
          'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Inicializamos nuestra lista con 10 elementos


print("\n Lista Original: ", colores) #Imprimimos la lista 

colores.sort(reverse=True) #Ordenaremos nuestra lista de manera alfab�tica, de la �ltima letra hasta la inicial del abecedario (z-a)

print("\n Nueva lista: ",colores) #Imprimos nuestra lista con el ordenamiento de z-a



