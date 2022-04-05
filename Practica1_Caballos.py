#!/usr/bin/env python 
# * coding: cp1252 *
# * coding: 850 *
# * coding: utf-8 *

#Usamos las lineas anteriores para codificar, y así poder utilizar caracteres especiales

#PRÁCTICA 1, CABALLOS;
# ¿Cuál es el MINIMO # de carreras se necesitan para obtener a los 2 caballos más rápidos? SI...
# Se tienen 25 caballos. y por carrera se pueden correr solamente 5 caballos, no más no menos.
              
import random
import numpy as np
from numpy.core.numeric import array_equiv

from networkx.utils.decorators import nodes_or_number
import matplotlib.pyplot as plt
import networkx as nx

#Asignamos los tiempos a nuestros 25 caballos que estarán separados en grupos de 5 por carrera, para obtener los caballos más rápidos de cada grupo.

#Caballos del PRIMER grupo de carreras
a1=  np.random.uniform(10,60)  #Tiempo aleatorio de 10s a 60 seg. (Float)
a2=  np.random.uniform(10,60)
a3=  np.random.uniform(10,60)
a4=  np.random.uniform(10,60)
a5=  np.random.uniform(10,60)

#Caballos del SEGUNDO grupo de carreras
b1=  random.uniform(10,60)  #Tiempo aleatorio de 10s a 60 seg. 
b2=  random.uniform(10,60)
b3=  random.uniform(10,60)
b4=  random.uniform(10,60)
b5=  random.uniform(10,60)

#Caballos del TERCER grupo de carreras
c1=  random.uniform(10,60)  #Tiempo aleatorio de 10s a 60 seg.
c2=  random.uniform(10,60)
c3=  random.uniform(10,60)
c4=  random.uniform(10,60)
c5=  random.uniform(10,60)

#Caballos del CUARTO grupo de carreras
d1=  random.uniform(10,60)  #Tiempo aleatorio de 10s a 60 seg.
d2=  random.uniform(10,60)
d3=  random.uniform(10,60)
d4=  random.uniform(10,60)
d5=  random.uniform(10,60)

#Caballos del QUINTO grupo de carreras
e1=  random.uniform(10,60)  #Tiempo aleatorio de 10s a 60 seg.
e2=  random.uniform(10,60)
e3=  random.uniform(10,60)
e4=  random.uniform(10,60)
e5=  random.uniform(10,60)

#GRUPOS DE LOS 25 CABALLOS con los tiempos
Caballos_A=[a1,a2,a3,a4,a5]  #caballoA=["Caballo 1: ", "Caballo 2: " , "Caballo 3: " , "Caballo 4: ", "Caballo 5: "]
Caballos_B=[b1,b2,b3,b4,b5]  #caballoB=["Caballo 6: ", "Caballo 7: " , "Caballo 8" , "Caballo 9", "Caballo 10"]
Caballos_C=[c1,c2,c3,c4,c5]
Caballos_D=[d1,d2,d3,d4,d5]
Caballos_E=[e1,e2,e3,e4,e5]

Poscaballos =np.array([Caballos_A,Caballos_B,Caballos_C,Caballos_D,Caballos_E]) #Creamos un array con las posciones de todos los caballos, según los tiempos

print(" \t\t \n ¿Cuál es el MINIMO # de carreras se necesitan para obtener a los 2 caballos más rápidos? ")
print(" \t\t  Los 25 caballos se separán en grupos de 5, para establecer los tiempos inciales. ")
print(" \t\t \n Mostrando los caballos y sus respectivos tiempos. ")

#print(caballoA[0]+ str(Caballos_A[0]))

Tcaballos =np.array([Caballos_A,Caballos_B,Caballos_C,Caballos_D,Caballos_E]) #Creamos un array con los tiempos de todos los caballos

#print(Tcaballos)

id_caballo=0 #Contador para identificar el número del caballo 
for nombre in range(5):
	print("\t GRUPO DE CARRERA ", nombre+1)
	for pos in range(5):
		
		print("\t Caballo ", id_caballo+1,":", round(Tcaballos[nombre][pos], 5)) #Imprimimos el número del caballo, así como su tiempo marcado.
																				#Utilizando round(), tomaremos los primeros 5 decimales en caso de haberlos
		id_caballo+=1 #Contador que sumará 1 cada que se haga una vuelta

print("\t\t\t ---------------GANADOR DE CADA CARRERA------------------- ")

Tcaballos.sort() #Ordenamos nuestro array de menor a mayor, para así tener los mejores tiempos y las posiciones de las carreras de cada grupo. 

for x in range(5): #Creamos un for para buscar el número del caballo antes de ser acomodados por tiempos 

		print("\t GANADOR DE CARRERA ", x+1)
		posi= np.where( Poscaballos == Tcaballos [x][0]) #Asiganmos en posi, la posición dentro de la matriz de tiempos donde se encuentran los 5 más rápidos, ya que están ordenados por primeros de grupo
		#print(posi)
		lugar= (posi[0]*5) + (posi[1]+1)  #operación para asignarle la posición del caballo 
		print("\t Caballo ", lugar,":", round(Tcaballos[x][0], 5)) #Imprimimos el Top 5 de cada carrera

	

print(" \t\t \n Después de mostrar los tiempos de los caballos en las primeras 5 carreras, separaremos a los primeros de cada carrera ")
print(" \t\t Correrán nuevamente, mostrando así, el resultado de la carrera No. 6 \n ") 

#CARRERA 6 
topCarrera6= [Tcaballos[0][0], Tcaballos[1][0], Tcaballos[2][0], Tcaballos[3][0], Tcaballos[4][0]] #Tomamos el top 5, para determinar el caballo más rápido
topCarrera6.sort() #Ordenamos nuestra carrera 6 de acuerdo al caballo más rápido
#print(topCarrera6)

for y in range(5): #Creamos un for para buscar el número del caballo antes de ser acomodados por tiempos 

		#print("\t GANADOR DE CARRERA 6",)
		posi= np.where( topCarrera6 [y]== Poscaballos ) #Asiganmos en posi, la posición dentro de la matriz de tiempos donde se encuentran los 5 más rápidos, ya que están ordenados por primeros de grupo

		lugar= (posi[0]*5) + (posi[1]+1)  #operación para asignarle la posición del caballo  
		print("\t Caballo ", lugar,":", topCarrera6[y],) #Imprimimos el resultado de la carrera 6
		l=y #Almacenará la fila del caballo ganador

#CARRERA 7	

print(" \n\t\t\t\t Carrera No.7") 
#print(Tcaballos)

topCarrera7= [Tcaballos[l][1], topCarrera6[1], topCarrera6[2], topCarrera6[3], topCarrera6[4]] #Tomamos el top 5 anterior, quitando al lider de la carrera 6
topCarrera7.sort() #Ordenamos nuestra carrera 7 de acuerdo al caballo más rápido

for y in range(5): #Creamos un for para buscar el número del caballo antes de ser acomodados por tiempos 

		posi= np.where( topCarrera7 [y]== Poscaballos ) #Asiganmos en posi, la posición dentro de la matriz de tiempos donde se encuentran los 5 más rápidos, ya que están ordenados por primeros de grupo

		lugar= (posi[0]*5) + (posi[1]+1)  #operación para asignarle la posición del caballo 
		print("\t Caballo ", lugar,":", topCarrera7[y],) #Imprimimos el resultado de la carrera 6
		

print(" \n\t\t\t -------------CABALLO MÁS RÁPIDO--------------") 
posi= np.where( topCarrera6 [0]== Poscaballos ) #Asiganmos en posi, la posición dentro de la matriz de tiempos donde se encuentra la posición del caballo inicial
lugar= (posi[0]*5) + (posi[1]+1)  #operación para asignarle la posición del caballo 

print("\t Caballo ", lugar,":", topCarrera6[0],"segundos")

print(" \n\t\t\t ------------SEGUNDO CABALLO MÁS RÁPIDO-----------") 
posi= np.where( topCarrera7 [0]== Poscaballos ) #Asiganmos en posi, la posición dentro de la matriz de tiempos donde se encuentra la posición del caballo inicial
lugar= (posi[0]*5) + (posi[1]+1)  #operación para asignarle la posición del caballo 

print("\t Caballo ", lugar,":", topCarrera7[0],"segundos")
print(" \n\t\t\t 7 CARRERAS MÍNIMAS PARA ENCONTRAR A LOS 2 CABALLOS MÁS RÁPIDOS")

#------------------------------------------------------GRÁFICOS--------------------------------------------------------------------

#Grafo
Grafo = nx.Graph() # creamos un grafo

#Añadir nodos
Grafo.add_node("Caballo #1") #Caballo más rápido
Grafo.add_node("Caballo #2") #Segundo caballo más rapido
Grafo.add_node("Caballo #3")
Grafo.add_node("Caballo #4")
Grafo.add_node("Caballo #5")


Grafo.add_node("Caballo 2 C1") #Caballo del grupo del ganador por carrera 1
Grafo.add_node("Caballo 2 C2") #Carrera 2, segundo caballo
Grafo.add_node("Caballo 2 C3")
Grafo.add_node("Caballo 2 C4")
Grafo.add_node("Caballo 2 C5") #Caballo 2do veloz de la carrera 5

Grafo.add_nodes_from(["C1.3", "C1.4", "C1.5"])  #Nodos de los caballos, siguientes del Caballo #1, en orden de carrera 
Grafo.add_nodes_from(["C2.3", "C2.4", "C2.5"])
Grafo.add_nodes_from(["C3.3", "C3.4", "C3.5"])
Grafo.add_nodes_from(["C4.3", "C4.4", "C4.5"]) #Nodos de los caballos, siguientes del Caballo #4, en orden de carrera 
Grafo.add_nodes_from(["C5.3", "C5.4", "C5.5"]) #Nodo de caballos, siguientes del caballo #5, en orden de su carrera


#Añadir aristas
Grafo.add_edge("Caballo #1", "Caballo #2") #Caballo 1, raiz (Arista de la raiz al nodo del segundo caballo veloz)

Grafo.add_edge("Caballo #1", "Caballo #3") #Arista del caballo 1, hasta el tercer más rápido
Grafo.add_edge("Caballo #3", "Caballo #4") #Arista del caballo 3, hasta el #4
Grafo.add_edge("Caballo #2", "Caballo #5")


Grafo.add_edge("Caballo #1", "Caballo 2 C1") #Arista que se conecta al nodo raiz con un nodo interno del #1
Grafo.add_edge("Caballo #2", "Caballo 2 C2")
Grafo.add_edge("Caballo #3", "Caballo 2 C3")
Grafo.add_edge("Caballo #4", "Caballo 2 C4")
Grafo.add_edge("Caballo #5", "Caballo 2 C5")

Grafo.add_edges_from([("Caballo 2 C1", "C1.3"),("C1.3", "C1.4"), ("C1.4", "C1.5")]) #Aristas que comunican los nodos internos con la hoja, conformando C1.5 como frontera
Grafo.add_edges_from([("Caballo 2 C2", "C2.3"),("C2.3", "C2.4"), ("C2.4", "C2.5")])
Grafo.add_edges_from([("Caballo 2 C3", "C3.3"),("C3.3", "C3.4"), ("C3.4", "C3.5")])
Grafo.add_edges_from([("Caballo 2 C4", "C4.3"),("C4.3", "C4.4"), ("C4.4", "C4.5")])
Grafo.add_edges_from([("Caballo 2 C5", "C5.3"),("C5.3", "C5.4"), ("C5.4", "C5.5")]) #Aristas que comunican los nodos internos con la hoja, conformando C5.5 como frontera


print(len(Grafo.nodes))
print(len(Grafo.edges))
#graficar gafo
nx.draw(Grafo, node_size = 50, width = 1.2, with_labels=True)
plt.show() #mostramos grafo