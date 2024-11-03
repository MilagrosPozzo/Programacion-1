import sys

class Grafo:
    def __init__(self):
        # Inicializa la matriz de adyacencia como una lista vacía y una lista para los nodos.
        self.nodos = []  # Lista para almacenar los nodos en el grafo
        self.matriz_adyacencia = []  # Lista de listas para la matriz de adyacencia, comenzando vacía

    def agregar_nodo(self, nodo):
        # Si el nodo no está en la lista, lo agregamos y ajustamos la matriz de adyacencia.
        if nodo not in self.nodos:
            self.nodos.append(nodo)
            # Añade una fila y una columna con 0's (sin conexión) para el nuevo nodo.
            for fila in self.matriz_adyacencia:
                fila.append(0)
            # Añade una nueva fila completa con ceros
            self.matriz_adyacencia.append([0] * len(self.nodos))
    
    def agregar_arista(self, nodo_origen, nodo_destino, peso=1):
        # Asegura que ambos nodos existen en el grafo; si no, los agrega.
        if nodo_origen not in self.nodos:
            self.agregar_nodo(nodo_origen)
        if nodo_destino not in self.nodos:
            self.agregar_nodo(nodo_destino)

        # Encuentra los índices de los nodos y actualiza el peso de la arista en la matriz de adyacencia.
        indice_origen = self.nodos.index(nodo_origen)
        indice_destino = self.nodos.index(nodo_destino)
        self.matriz_adyacencia[indice_origen][indice_destino] = peso

    def mostrar_matriz_adyacencia(self):
        # Imprime la matriz de adyacencia de forma legible
        print("Matriz de Adyacencia:")
        for fila in self.matriz_adyacencia:
            print(fila)

    def dijkstra(self, nodo_origen):
        # Inicializa las estructuras de distancia y visitación para Dijkstra
        distancias = {nodo: sys.maxsize for nodo in self.nodos}  # Todas las distancias se inicializan a infinito
        distancias[nodo_origen] = 0  # La distancia al nodo de origen es 0
        visitados = {nodo: False for nodo in self.nodos}  # Ningún nodo ha sido visitado al principio

        # Algoritmo de Dijkstra
        for _ in range(len(self.nodos)):
            # Selecciona el nodo no visitado con la menor distancia conocida
            nodo_actual = min((nodo for nodo in self.nodos if not visitados[nodo]), key=lambda nodo: distancias[nodo])
            visitados[nodo_actual] = True  # Marca el nodo actual como visitado
            indice_actual = self.nodos.index(nodo_actual)  # Índice en la matriz

            # Actualiza las distancias de los nodos vecinos
            for indice_vecino, peso in enumerate(self.matriz_adyacencia[indice_actual]):
                if peso > 0 and not visitados[self.nodos[indice_vecino]]:
                    nueva_distancia = distancias[nodo_actual] + peso
                    if nueva_distancia < distancias[self.nodos[indice_vecino]]:
                        distancias[self.nodos[indice_vecino]] = nueva_distancia

        # Imprime los resultados del camino más corto desde el nodo origen
        print(f"Distancias desde el nodo '{nodo_origen}':")
        for nodo, distancia in distancias.items():
            print(f"Distancia a {nodo}: {distancia if distancia < sys.maxsize else 'infinito'}")
            
            
