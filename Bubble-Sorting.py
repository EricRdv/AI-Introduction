"""Sorting Algorithms:   Bubble Sort   """
# Eric Rodriguez Del Valle          20310419        6E2

list = [55, 66, 1111, 11, 22, 88]

def bubble(list):
    cantidad = len(list) - 1            #Porque no podemos comparar la ultima posicion
    ordenada = False

    while not ordenada:
        ordenada = True
        for i in range(0, cantidad):
            if list[i]> list[i+1]:
                ordenada = False
                list[i], list[i+1] = list[i+1], list[i]     #Cambiamos las posiciones de los valores.
    return list

print(list)
print(bubble(list))