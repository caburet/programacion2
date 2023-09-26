# 6. Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres
# de las personas cuya edad es mayor a una edad ingresada por el usuario, utilizando list comprehensions

def nombre_personas():
    dict = {
        "Camila": 26,
        "Rocio": 29,
        "Sofia": 4,
        "Valentin": 12,
        "Bautista": 8
        }
    
    edad_estipulada = int(input("Ingrese el minimo de edad que deseas ver en la lista: "))

    lista_edad = [nombre for nombre, edad in dict.items() if edad > edad_estipulada]
    print (lista_edad)

nombre_personas()