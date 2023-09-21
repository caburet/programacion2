# Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los elementos únicos utilizando list comprehensions.

list_1 = [1,2,3,3,3,2,5,6]

def eliminar_Dup(list_1):
    return list(set(list_1))

list_sinRepetidos = eliminar_Dup(list_1)
print(f"La lista sin items repetidos es: {list_sinRepetidos}")








