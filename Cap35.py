#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 35,  FUNCIONES 2 , Argumentos arbitrarios
              

def colores(*args):#definimos la funcion con args para que pueda variar de acuerdo a lo que vayamos pidiendo
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')#imprimimos los valores que se mandaron

colores('rojo', 'azul', 'verde', 'amarillo')#mandamos los diferentes valores
colores('lila', 'negro', 'rojo')
colores('rosa','negro')
colores('marrón', 'naranja')

#Crea una función que realice la suma de cinco números utilizando solo *args. Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

def suma(*args): #Definimos la función 
	resultado = args[0] + args[1] + args[2] + args[3] + args[4] #Realizamos la suma de acuerdo a la posición 
	print('El resultado de sumar estos cinco números es:', resultado) #Imprimos el resultado

suma(5, 7, 45, 8657, 3, 4)