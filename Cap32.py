#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 32,  DICCIONARIOS  con el bucle for
              
teclado1 = { #inicializamos el diccionario, con "categoria","modelo" y "precio", con su respectivo valor
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado1 ={#declaramos el diccionario
    "Categoria": "Teclados",
    "Modelo": "HyperX Alloy FPS Pro",
    "Precio": "89,99"
}

for x,y in teclado1.items():#aqui definimos X y Y, X va a momstrar las definiciones, el lado "Izquierdo", y Y va a mostrar sus atributos, y usando la funcion items, obtenemos los valores del diccionario
    print(x," = ",y,".")#imprimimos