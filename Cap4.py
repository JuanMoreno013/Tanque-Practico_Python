#!/usr/bin/env python 
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_
# _*_ coding: utf-8 _*_

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 4,  STRINGS 2 "CONCATENACIÓN

#P1 

men1 = "Do u wanna play? " + " Yes, bddy " #Le asignamos a la variable men1, un valor de tipo string
print("\n \t", men1) #Imprimimos el texto almacenado de la variable men1, que contiene una concatenación

#P2 

var1= "Seguimos con otra "  #Le asignamos a la variable men1, un valor de tipo string
var2= "concatenación de texto" #Le asignamos a la variable men1, un valor de tipo string

varConca2= var1 + var2 #Almacenamos los valores de texto de las variables var1 y var2, en una nueva variable
print("\n \n \t", varConca2) #imprimimos la variable VarConca2 que contiene la concatenación de texto de 2 variables distintas.

#P3 

palabra1= "La naturaleza es demasiado" #Le asignamos a la variable palabra1, un valor de tipo string

print( "\n\t", palabra1 + "hermosa, ¡hay que cuidarla!" ) #Imprimimos el texto de palabra1 concatenando texto directamente en un print.

#P4
nombre1 = "Juan" #Le asignamos a la variable un valor de tipo string, en este caso mi primer nombre
nombre2 = "Antonio"
apellido1 = "Moreno" #Asignos un valor de tipo string a la variable, en este mi primer apellido
apellido2 = "Bernardino"

nombre_completo = nombre1 + " " + nombre2 + " " + apellido1 + " " + apellido2  #Concatenamos los datos de las variables en una variable nueva

print( "\n\t", nombre_completo) #Imprimimos la variable como resultado de la concatenación de las variables y sus espacios.

#P5
# Solución 1

numero = "40" + "60" #Asignos un valor de tipo string a la variable, donde concatenaremos 2 numeros dentro de la misma

print("\n\t", numero) #Imprimos la variable anterior, mostrando la concatenación de 2 numeros