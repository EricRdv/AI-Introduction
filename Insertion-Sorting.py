"""Sorting Algorithms:   Insertion Sort   """
# Eric Rodriguez Del Valle          20310419        6E2

list = [55, 66, 1111, 11, 22, 88]


def insertion(list):
    for i in range(1, len(list)):       # Empezamos desde el 2do valor
        value = list[i]         #Valor con el que se esta trabajando
        j = i - 1               #Valor anterior
        while j >= 0 and list[j] > value:       #Recorremos la lista comparando y moviendo los elementos
            list[j+1] = list[j]
            j -= 1
        list[j+1] = value   #Insertamos el valor en la posicion correcta.
    return list

print(list)
print(insertion(list))