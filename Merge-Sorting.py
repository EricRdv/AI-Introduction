"""Sorting Algorithms:   Merge-Sort   """
# Eric Rodriguez Del Valle          20310419        6E2

list = [55, 66, 1111, 11, 22, 88]

def merge_sort(list):
    #Caso base: si la lista tiene 0 o 1 elementos, está ordenada
    if len(list) <= 1:
        return list

    #Dividimos la lista en dos mitades
    mid = len(list) // 2        #Division entera
    mitad_izq = list[:mid]
    mitad_der = list[mid:]

    #Ordenamos cada mitad
    orden_izq = merge_sort(mitad_izq)     #Utilizamos recursividad
    orden_der = merge_sort(mitad_der)

    #Combinamos las dos mitades ordenadas en una sola lista 
    list_ord = []
    i = j = 0
    while i < len(orden_izq) and j < len(orden_der):
        if orden_izq[i] < orden_der[j]:
            list_ord.append(orden_izq[i])
            i += 1
        else:
            list_ord.append(orden_der[j])
            j += 1
    list_ord += orden_izq[i:]
    list_ord += orden_der[j:]

    #Devolvemos la lista ordenada
    return list_ord

print(list)
print(merge_sort(list))