#8. Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los elementos únicos utilizando list comprehensions.

lista_duplicados = ['pepe','pepe','ignacio','maria','ignacio','pepe','pepe','roberto']

def sacar_duplicados(lista):
    nueva_lista = list(set(lista))
    return nueva_lista

print(sacar_duplicados(lista_duplicados))