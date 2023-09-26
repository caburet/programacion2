# 8. Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los elementos
# únicos utilizando list comprehensions.

def duplicados():
    lista = [2, 3, 4, 5, 2, 2, 2, 3, 4, 5]
    lista_sin_repetir = [num for num in lista if lista.count(lista[num])== 1]
    print (lista_sin_repetir)

duplicados()

def duplicados2():
    lista2 = ["camila", "camila", "joaquin", "martina", "sol", "sol"]

    lista_nueva = sin_repetidos(lista2)
    print (lista_nueva)


def sin_repetidos(lista2):
    return list(set(lista2))

duplicados2()