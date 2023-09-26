# 9. Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar
# la lista de acuerdo a la longitud de las palabras.

def ordenar_palabras():
    lista_palabras = ["Alcohol", "Cerveza", "Vodka", "Fernet", "Gin", "Campari"]
    lista_ordenada = sorted(lista_palabras, key= lambda x: len(x))
    print(lista_ordenada)

ordenar_palabras()