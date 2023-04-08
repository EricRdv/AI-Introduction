""""Ruta mas corta: Dijkstra"""
#Eric Rodriguez Del Valle       20310419    6E

import cv2
import heapq


def dijkstra(grafo, inicio, final):
    # Creamos un diccionario para almacenar la distancia más corta desde el nodo de inicio hasta cada nodo
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    # Creamos un diccionario para almacenar la ruta más corta desde el nodo de inicio hasta cada nodo
    ruta_mas_corta = {}

    # Creamos una cola de prioridad con la tupla (distancia, nodo)
    cola = [(0, inicio)]

    while cola:
        # Sacamos el nodo con la distancia más corta de la cola de prioridad
        (distancia_actual, nodo_actual) = heapq.heappop(cola)

        # Si hemos llegado al nodo final, devolvemos la ruta más corta hasta ese nodo
        if nodo_actual == final:
            ruta = []
            while nodo_actual in ruta_mas_corta:
                ruta.insert(0, nodo_actual)
                nodo_actual = ruta_mas_corta[nodo_actual]
            ruta.insert(0, nodo_actual)
            return ruta

        # Si no hemos llegado al nodo final, comprobamos sus vecinos
        for vecino in grafo[nodo_actual]:
            distancia = distancia_actual + grafo[nodo_actual][vecino]

            # Si hemos encontrado una distancia más corta, actualizamos las distancias y la ruta
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                ruta_mas_corta[vecino] = nodo_actual
                heapq.heappush(cola, (distancia, vecino))

    # Si no se encontró ninguna ruta, devolvemos None
    return None


grafo = {
    'A': {'B': 2, 'C': 6},
    'B': {'A': 2, 'D': 5},
    'C': {'A': 6, 'D': 8},
    'D': {'B': 5, 'C': 8, 'E': 15, 'F': 10},
    'E': {'D': 15, 'F': 6, 'Z': 6},
    'F': {'D': 10, 'E': 6, 'Z': 2},
    'Z': {'F': 2, 'E': 6}
}

ruta = dijkstra(grafo, 'A', 'Z')
print(ruta)


graf_img = cv2.imread("Grafo.png")
cv2.imshow("Grafo", graf_img)
cv2.waitKey(0)
cv2.destroyAllWindows()