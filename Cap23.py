#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y as� poder utilizar caracteres especiales

#CAPITULO 23,  CONDICIONALES 3 , condicional IF ELIF ELSE
                                   
#Al siguiente c�digo a��dele un par de rangos de edad. Uno de 18 a�os hasta 45 y otro de m�s de 100 a�os hasta 120.


edad = int(input('�Cu�l es tu edad?\n')) #Pide la edad al usuario
if edad <= 0: #Incia la condici�n, si la edad es menor o igual que 0 se ejecuta lo siguiente
	print('Nadie puede tener esa edad.')

elif edad <= 1 and edad < 18: #si esta entre 1 y 18 a�os, ejecuta el elif e imprime que es menor de edad
	print('Eres menor de edad.')

elif edad == 18 and edad <= 45: #si tiene entre 18 y 45, imprime lo siguiente
	print('Eres mayor de edad.')

elif edad <= 100:  #si tiene menor a 100 a�os, imprime lo siguiente
	print('Eres mayor de edad.') 

elif edad > 100 and edad <= 120: #y si tiene entre 100 y 120, imprime lo siguiente
	print('Persona con edad muy avanzada.')
else: #de ser ninguno el caso, ya sea un numero negativo o mayor a 120, ejecuta lo siguiente
	print('Edad no v�lida.')