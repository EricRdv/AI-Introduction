""""Ruta mas corta: Dijkstra"""
#Eric Rodriguez Del Valle       20310419    6E

import cv2
import heapq

def dijkstra(grafo, inicio, final):
    distancias = {nodo: float('inf') for nodo in grafo}     #Diccionario de distancias
    distancias[inicio] = 0
    ruta_mas_corta = {}

    cola = [(0, inicio)]        #Tupla Distancia y nodo inicio

    while cola:
        (distancia_actual, nodo_actual) = heapq.heappop(cola)   #Sacamos el nodo con la distancia más corta

        if nodo_actual == final:        #Checamos si llegamos al final para indicar la ruta creada
            ruta = []
            while nodo_actual in ruta_mas_corta:
                ruta.insert(0, nodo_actual)
                nodo_actual = ruta_mas_corta[nodo_actual]
            ruta.insert(0, nodo_actual)

            #Tabla
            print(f"{'Nodo actual':<15}{'Dist. desde ini.':<18}{'Nodo previo':<15}{'Dist. total':<15}")
            distancia_total = 0
            for i in range(len(ruta)):
                if i == 0:
                    print(f"{ruta[i]:<15}{str(distancias[ruta[i]]):<18}{'-':<15}{str(distancias[ruta[i]]):<15}")
                else:
                    print(f"{ruta[i]:<15}{str(distancias[ruta[i]]):<18}{str(ruta_mas_corta[ruta[i]]):<15}{str(distancia_total + grafo[ruta_mas_corta[ruta[i]]][ruta[i]]):<15}")
                    distancia_total += grafo[ruta_mas_corta[ruta[i]]][ruta[i]]

            return ruta

        for vecino in grafo[nodo_actual]:       #Comparamos nodos vecinos
            distancia = distancia_actual + grafo[nodo_actual][vecino]

            if distancia < distancias[vecino]:     #Actualizamos distancia más corta
                distancias[vecino] = distancia
                ruta_mas_corta[vecino] = nodo_actual
                heapq.heappush(cola, (distancia, vecino))

    return None #En caso de no haber ruta



#Diccionario simulando el grafo, sus nodos y distancias.
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