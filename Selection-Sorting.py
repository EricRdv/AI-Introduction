"""Sorting Algorithms:   Selection Sort   """
# Eric Rodriguez Del Valle          20310419        6E2

list = [55, 66, 1111, 11, 22, 88]


def selection(list):
    n = len(list)   #Longitud lista

    for i in range(n):
        min_idx = i     #Valor mínimo actualizable
        for j in range(i+1, n):
            if list[j] < list[min_idx]:
                min_idx = j     #Actualizamos el valor mínimo
        # Intercambiamos el valor mínimo con el valor actual
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

print(list)
print(selection(list))

