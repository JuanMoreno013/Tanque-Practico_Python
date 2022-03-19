#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 27,  BUCLES 1 , BUCLE WHILE 1
                                   

#Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.
x = 0 #Inicializamos variable
print("\n\t Primer bucle")
while x <= 15:  #Se establece nuestra condición en la que el bucle continuará hasta que nuestra variable alcance el valor de 15
	print("\n\t ",x) #Se imprime el valor de x, en el momento del bucle
	x += 5 #Se establece el incremento de 5

#Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
x = 0
print("\n\t Segundo bucle")
while x >= -100: #Se establece nuestra condición en la que el bucle continuará hasta que nuestra variable alcance el valor de -100
	print("\n\t ", x) #Se imprime el valor de x, en el momento del bucle
	x -= 20  #Se establece un decremento de 20

#Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'...
x = 10 #Se inicializa nuestra variable con 10
print("\n\t Tercer bucle")
while x >= 0:
	print(' \n\t El valor de x es: ', x) #Se imprime el valor de x, en el momento del bucle
	x -= 1 #Se establece un decremento de 1