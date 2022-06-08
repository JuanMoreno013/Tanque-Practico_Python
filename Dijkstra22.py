import networkx as nx
import matplotlib.pyplot as plt
import random

#Creamos nuestra variable random para asignar el tiempo de coste al azar
n=[m for m in range (1,100)]
random.shuffle(n)


graph = {

    'Guadalajara': [{'v': 'Tlaque','tiempo': n[0]}, {'v': 'Tlajomulco','tiempo': n[1]}],
    'Tlaque': [{'v': 'Guadalajara','tiempo': n[2]}, {'v': 'Calera','tiempo':n[3]}],
    'Calera': [{'v': 'Tlaque','tiempo': n[4]}, {'v': 'Santa Rosa','tiempo': n[5]}],

    'Santa Rosa': [{'v': 'Calera','tiempo': n[6]}, {'v': 'Santa Cecilia','tiempo': n[7]}, {'v': 'Chapala','tiempo': n[8]}],
    'Santa Cecilia': [{'v': 'Santa Rosa','tiempo': n[9]}, {'v': 'Tuxcueca','tiempo': n[10]}],
    'Tuxcueca': [{'v': 'Santa Cecilia','tiempo': n[11]}, {'v': 'Mazamitla','tiempo': n[12]}],
    'Mazamitla': [{'v': 'Tuxcueca','tiempo': n[13]}, {'v': 'Tamazula','tiempo': n[14]}],
    'Tamazula': [{'v': 'Mazamitla','tiempo': n[15]}, {'v': 'Ciudad Guzman','tiempo': n[16]}],

    'Ciudad Guzman': [{'v': 'Tamazula','tiempo': n[17]}, {'v': 'San Sebastian','tiempo': n[18]}],
    'San Sebastian': [{'v': 'Ciudad Guzman','tiempo': n[19]}, {'v': 'Andres','tiempo': n[20]}],
    'Andres': [{'v': 'San Sebastian','tiempo': n[21]}, {'v': 'Sayula','tiempo': n[22]}],
    'Sayula': [{'v': 'Andres','tiempo': n[23]}, {'v': 'Zacoalco','tiempo': n[24]}],
    'Zacoalco': [{'v': 'Sayula','tiempo': n[25]}, {'v': 'Acatlan','tiempo': n[26]}],
    'Acatlan': [{'v': 'Zacoalco','tiempo': n[27]}, {'v': 'Tlajomulco','tiempo': n[28]}],

    'Tlajomulco': [{'v': 'Acatlan','tiempo': n[29]}, {'v': 'Guadalajara','tiempo': n[30]},{'v': 'Miguel','tiempo': n[31]}],
    'Miguel': [{'v': 'Tlajomulco','tiempo': n[32]}, {'v': 'Ajic','tiempo': n[33]}],
    'Ajic': [{'v': 'Miguel','tiempo': n[34]}, {'v': 'Chapala','tiempo': n[35]}],
    'Chapala': [{'v': 'Ajic','tiempo': n[36]}, {'v': 'Santa Rosa','tiempo': n[37]}]
}

# Crando el grafo
class Grafo:
  def __init__(self, graph):
    self.G = nx.Graph()
    self.graph = graph
    self.nodes = list(graph.keys())

  #Creando los bordes
  def bordes(self, a, b, weight):
    self.G.add_edge(a, b, weight=weight)
  
  # Mostrar el grafo
  def mostrar(self):
    pos = nx.spring_layout(self.G)
    weights = nx.get_edge_attributes(self.G, "weight")
    self.G.add_nodes_from(self.nodes)

    plt.figure()
    #Esto es simplemente para darle un poco de estilo al codigo
    nx.draw(
      self.G, pos, edge_color='red', width=1, linewidths=1,
      node_size=500, node_color='blue', alpha=0.9,
      labels={node: node for node in self.G.nodes()}
    )
    nx.draw_networkx_edge_labels(self.G, pos, edge_labels=weights)
    plt.axis('off')
    plt.show()

  
  def Mostrar_grafo(self):
    for i in self.graph:
      for j in self.graph[i]:
        self.bordes(i, j['v'], j['tiempo'])

    self.mostrar()

    # Asignamos nuestros datos


# Mostramos nuestro primer grafo
G = Grafo(graph=graph)
G.Mostrar_grafo()

# Con esta funcion nos da el costo de la ruta que en su caso son el tiempo
def costo(path):
  path_weight = 0

  for index, value in enumerate(path):
    try:
      for j in graph[value]:
        if j['v'] == path[index + 1]:
            path_weight += j['tiempo']
    except:
      break

  return path_weight

# Con esta funcion empleamos el algoritmo de dijkstra para encontrar 
# el camino con menor costo
def encontrar_ruta_corta(graph, start, end, path =[]):
  path = path + [start]
  shortest = None
  weights = None

  if start == end: return path

  for node in graph[start]:
      if node['v'] not in path:
          newpath = encontrar_ruta_corta(graph, node['v'], end, path)
          if newpath:
            new_wexight = costo(newpath)
            if not weights or new_wexight < weights:
              shortest = newpath
              weights = new_wexight

  return shortest

ruta_corta = encontrar_ruta_corta(graph, 'Guadalajara', 'Ciudad Guzman')
costo_de_ruta_corta = costo(ruta_corta)

print('Ruta con menor tiempo :', ruta_corta)
print('Minutos :', costo_de_ruta_corta,'min')


grafo_final = {}

# Aqui generamos nuestro grafo final 
for index, value in enumerate(ruta_corta):
  try:
    for j in graph[value]:
      if j['v'] == ruta_corta[index + 1]:
        grafo_final.update({value: [j]})
  except:
    break

# Mostramos nuestro grafo final
Fuga = Grafo(grafo_final)

for i in grafo_final:
  for j in grafo_final[i]:
        Fuga.bordes(i, j['v'], j['tiempo'])

Fuga.mostrar()
