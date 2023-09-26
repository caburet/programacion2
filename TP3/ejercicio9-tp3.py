# 9. Dadas dos listas de números del mismo tamaño, crea una nueva lista que contenga la multiplicación
# de los elementos correspondientes de ambas listas utilizando list comprehensions.

def dos_lista():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    lista_concatenada = [x *y for x, y in zip(list1, list2)]
    print(lista_concatenada)

dos_lista()