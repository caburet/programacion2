# Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que comienzan con 
# una letra específica (por ejemplo, "a") indicada por el usuario, utilizando list comprehensions.

def diccionario():
    dict = {
        "anana": "fruta amarilla",
        "manzana": "fruta roja",
        "naranja": "fruta naranja",
        "banana": "fruta amarilla",
        "durazno": "la fruta mas rica"
        }
    
    letra_inicio = input("Ingrese la inicial de la fruta que desea ver: ")
    lista = [fruta for fruta in dict.keys() if fruta.startswith(letra_inicio)]
    print(lista)

diccionario()