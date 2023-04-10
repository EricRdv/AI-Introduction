""""Arbol parcial de Prim"""
#Eric Rodriguez Del Valle       20310419    6E

import heapq
import cv2

def prim(grafo):
    
    arbol = {}
    visitados = set()  #Nodos visitados
    costo_total = 0

    primer_nodo = list(grafo.keys())[0]  #Analisis prime nodo
    arbol[primer_nodo] = {}  #Añadimos al arbol
    visitados.add(primer_nodo)  #Lo marcamos como visitado

    # Usamos una cola de prioridad para almacenar las aristas
    aristas = [(distancia, primer_nodo, vecino) for vecino, distancia in grafo[primer_nodo].items()]
    heapq.heapify(aristas)

    while aristas and len(arbol) < len(grafo):
        peso, origen, destino = heapq.heappop(aristas)  #Seleccionamos la arista de menor peso

        # Si el destino ya fue visitado, ignoramos la arista
        if destino in visitados:
            continue

        costo_total += peso
        arbol[origen][destino] = peso

        # Agregamos el destino al árbol abarcador
        if destino not in arbol:
            arbol[destino] = {}

        visitados.add(destino)  #Lo marcamos como visitado

        # Agregamos las nuevas aristas a la cola de prioridad
        for vecino, distancia in grafo[destino].items():
            if vecino not in visitados:
                heapq.heappush(aristas, (distancia, destino, vecino))

    #Imprimimos el árbol final
    print("Arbol: {")
    for nodo, vecinos in arbol.items():
        print(f"  '{nodo}': {{", end="")
        for vecino, distancia in vecinos.items():
            print(f"'{vecino}': {distancia}, ", end="")
        print("},")
    print("}")

    #Costo total de la ruta
    print(f"Costo total de la ruta: {costo_total}")

    return arbol


grafo = {
    'A': {'B': 2, 'C': 6},
    'B': {'A': 2, 'D': 5},
    'C': {'A': 6, 'D': 8},
    'D': {'B': 5, 'C': 8, 'E': 15, 'F': 10},
    'E': {'D': 15, 'F': 6, 'Z': 6},
    'F': {'D': 10, 'E': 6, 'Z': 2},
    'Z': {'F': 2, 'E': 6}
}

prim(grafo)

graf_img = cv2.imread("Grafo.png")
cv2.imshow("Grafo", graf_img)

prim_img = cv2.imread("GrafoPrim.jpg")
cv2.imshow("Arbol", prim_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

