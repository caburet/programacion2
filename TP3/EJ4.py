#4. Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que comienzan
#   con una letra específica (por ejemplo, "a") indicada por el usuario, utilizando list comprehensions.

diccionario = {'nombre':'algo','apellido':'otra cosa','dni':'tercera cosa'}

def lista_dicc(caracter):
    lista = [elemento for elemento in diccionario if elemento[0] == caracter]
    return lista

car = input("ingrese caracter: ")

print(lista_dicc(car))