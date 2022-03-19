#!/usr/bin/env python 
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_
# _*_ coding: utf-8 _*_

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 4,  STRINGS 3 "métodos upper(), lower() y title()"

#P1 

nombre = "enrique barros fernández".title() #Le asignamos a la variable un valor de tipo string y aplicamos el método title() 
print("\n \t", nombre) #Imprimimos el texto almacenado con el método ya aplicado para poner la primera letra de cada palabra en mayúscula

#P2 

nombre2 = "Esta Es Una Frase Para Ser Formateada.".lower() #Almacenamos un valor de tipo string y aplicamos el método lower()
print("\n \t", nombre2) #Imprimimos el valor de la variable donde el todas las letras del texto serán minúsculas

#P3 

nombre3 = "Esta Es Una Frase Para Ser Formateada.".upper() #Almacenamos un valor de tipo string y aplicamos el método upper()
print("\n \t", nombre3) #Imprimimos el valor de la variable donde el todas las letras del texto serán mayúsculas
