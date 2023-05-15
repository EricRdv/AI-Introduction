class Grafo:
    def __init__(self):
        self.aristas = []

    def agregar_arista(self, inicio, fin, peso):
        self.aristas.append((inicio, fin, peso))

def buscar_padre(padres, i):
    if padres[i] == i:
        return i
    return buscar_padre(padres, padres[i])

def union(padres, rango, x, y):
    raiz_x = buscar_padre(padres, x)
    raiz_y = buscar_padre(padres, y)

    if rango[raiz_x] < rango[raiz_y]:
        padres[raiz_x] = raiz_y
    elif rango[raiz_x] > rango[raiz_y]:
        padres[raiz_y] = raiz_x
    else:
        padres[raiz_y] = raiz_x
        rango[raiz_x] += 1

def kruskal_minimo(grafo):
    grafo.aristas.sort(key=lambda arista: arista[2])
    num_vertices = len(grafo.aristas)
    padres = [i for i in range(num_vertices)]
    rango = [0 for _ in range(num_vertices)]
    arbol_minimo = []

    i = 0
    while len(arbol_minimo) < num_vertices - 1:
        inicio, fin, peso = grafo.aristas[i]
        x = buscar_padre(padres, inicio)
        y = buscar_padre(padres, fin)

        if x != y:
            arbol_minimo.append((inicio, fin, peso))
            union(padres, rango, x, y)
        i += 1

    return arbol_minimo

def kruskal_maximo(grafo):
    grafo.aristas.sort(key=lambda arista: arista[2], reverse=True)
    return kruskal_minimo(grafo)

def calcular_peso(aristas):
    return sum(arista[2] for arista in aristas)

# Crear el grafo
g = Grafo()

# Agregar aristas al grafo
g.agregar_arista("A", "B", 2)
g.agregar_arista("A", "C", 6)
g.agregar_arista("B", "D", 5)
g.agregar_arista("C", "D", 8)
g.agregar_arista("D", "E", 15)
g.agregar_arista("D", "F", 10)
g.agregar_arista("E", "F", 6)
g.agregar_arista("E", "Z", 6)
g.agregar_arista("F", "Z", 2)

# Obtener los árboles mínimo y máximo usando Kruskal
min_arbol = kruskal_minimo(g)
max_arbol = kruskal_maximo(g)

# Imprimir las aristas del árbol mínimo y su peso total
print("Aristas del árbol mínimo:")
for arista in min_arbol:
    print(arista[0], "-", arista[1], ": Peso", arista[2])
print("Peso total del árbol mínimo:", calcular_peso(min_arbol))

# Imprimir las aristas del árbol máximo y su peso total
print("Aristas del árbol máximo:")
for arista in max_arbol:
        print(arista[0], "-", arista[1], ": Peso", arista[2])
print("Peso total del árbol máximo:", calcular_peso(max_arbol))
