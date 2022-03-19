#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#CAPITULO 31,  DICCIONARIOS 
              
teclado1 = { #inicializamos el diccionario, con "categoria","modelo" y "precio", con su respectivo valor
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {#inicializamos el diccionario, con "categoria","modelo" y "precio", con su respectivo valor
    "Categoria": "Teclados",
    "Modelo": "Corsair K55 RGB",
    "Precio": "59,99"
    }

consulta = teclado2["Modelo"]#obtenemos el valor en la posicion Modelo
consulta2 =teclado2["Precio"]#obtenemos el valor en la posicion Precio
print("El modelo",consulta,"cuesta",consulta2, "$")#luego imprimimos y concatenamos