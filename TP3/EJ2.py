#2. Implemente una función que dada una lista de nombres, devuelva una nueva lista que contenga solo los nombres que
# tengan una longitud mayor o igual a una cantidad de caracteres pasada por parámetro, utilizando list comprehensions.

lista_nombres = ["pepe","roberto","jose","ana","maria","lucrecia"]

def recortar_lista(lista,longitud):
    nueva_lista = [valor for valor in lista if len(valor) >= longitud]
    return nueva_lista

tamanio = int(input("ingrese longitud de las cadenas a conservar: "))

print(recortar_lista(lista_nombres,tamanio))
