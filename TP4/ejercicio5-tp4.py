# 5. Ordenar una lista de diccionarios por un elemento del diccionario. ej: ordenar por edad la siguiente lista: 
#```python
#personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32},
# {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]

def ordenar_lista():
    personas = [
    {'nombre': 'Hector', 'edad': 27},
    {'nombre': 'Juan', 'edad': 18},
    {'nombre': 'Maria', 'edad': 32},
    {'nombre': 'Pedro', 'edad': 21},
    {'nombre': 'Ana', 'edad': 20}]

    lista_ordenada = sorted(personas, key=lambda x: x["edad"])
    print(lista_ordenada)

ordenar_lista()