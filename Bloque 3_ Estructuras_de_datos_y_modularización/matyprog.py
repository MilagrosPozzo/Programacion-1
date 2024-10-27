# Creamos la clase Grafo para representar un grafo dirigido
class Grafo:
    def __init__(self, num_nodos):
        # Inicializamos el número de nodos y una matriz de adyacencia con "inf" en cada posición
        self.num_nodos = num_nodos
        self.matriz_adyacencia = [[float('inf') for _ in range(num_nodos)] for _ in range(num_nodos)]
        # Cada nodo hacia sí mismo tiene distancia 0
        for i in range(num_nodos):
            self.matriz_adyacencia[i][i] = 0

    # Método para agregar arista en la matriz de adyacencia
    def agregar_arista(self, desde, hacia, peso):
        # Agrega el peso en la posición desde->hacia
        self.matriz_adyacencia[desde][hacia] = peso

    # Método para visualizar la matriz de adyacencia
    def mostrar_matriz(self):
        for fila in self.matriz_adyacencia:
            print(fila)

    # Implementación del algoritmo de Dijkstra
    def dijkstra(self, inicio):
        # Inicializamos distancias con infinito, menos la posición de inicio que es 0
        distancias = [float('inf')] * self.num_nodos
        distancias[inicio] = 0  # Distancia del nodo inicial a sí mismo es 0
        visitados = [False] * self.num_nodos  # Lista de nodos visitados
        predecesores = [-1] * self.num_nodos  # Para guardar el camino

        for _ in range(self.num_nodos):
            # Selecciona el nodo con la menor distancia entre los no visitados
            min_dist = float('inf')
            min_nodo = -1
            for nodo in range(self.num_nodos):
                if not visitados[nodo] and distancias[nodo] < min_dist:
                    min_dist = distancias[nodo]
                    min_nodo = nodo

            # Marcar el nodo como visitado
            visitados[min_nodo] = True

            # Actualizar la distancia de los nodos adyacentes
            for vecino in range(self.num_nodos):
                if self.matriz_adyacencia[min_nodo][vecino] != float('inf') and not visitados[vecino]:
                    nueva_dist = distancias[min_nodo] + self.matriz_adyacencia[min_nodo][vecino]
                    if nueva_dist < distancias[vecino]:
                        distancias[vecino] = nueva_dist
                        predecesores[vecino] = min_nodo

        # Imprimir el resultado final
        print("Nodo\tDistancia\tCamino")
        for nodo in range(self.num_nodos):
            if distancias[nodo] == float('inf'):
                print(f"{nodo}\tNo accesible")
            else:
                # Recorremos los predecesores para mostrar el camino
                camino = []
                actual = nodo
                while actual != -1:
                    camino.insert(0, actual)
                    actual = predecesores[actual]
                print(f"{nodo}\t{distancias[nodo]}\t\t{' -> '.join(map(str, camino))}")