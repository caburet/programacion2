# 10. Dada una lista de palabras, generar una lista con las iniciales de cada palabra.

def iniciales():
    lista_palabras = ["Alcohol", "Cerveza", "Vodka", "Fernet", "Gin", "Campari"]

    lista_iniciales = list(map(lambda x: x[0], lista_palabras))

    print(lista_iniciales)

iniciales()

def iniciales2():
    lista_palabras = ["Alcohol", "Cerveza", "Vodka", "Fernet", "Gin", "Campari"]
    lista_iniciales = []

    for linea in lista_palabras:
        inicial = linea[0]
        lista_iniciales.append(inicial)
    
    print(lista_iniciales)

iniciales2()