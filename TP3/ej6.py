# Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres de las personas cuya edad es mayor a una edad ingresada por el usuario, utilizando list comprehensions.

dict_Edades = {"joaquin": 22,"messi": 35,"ramon": 10,"sebastian":12}

def Personas(dict_Edades):
    lista_edades = []
    edad_min = int(input("Ingrese la edad minima: "))
    for persona, edad in dict_Edades.items():
        if edad >= edad_min:
            lista_edades.append(persona)
    return lista_edades

edades = Personas(dict_Edades)
print("normal:")
print(f"Personas con edad igual o mayor a la edad mínima: {edades}")


edad_minima = int(input("Ingrese la edad minima: "))

lista_edades_mayores = [nombre for nombre, edad in dict_Edades.items() if edad > edad_minima]

print(f"list comprehension: {lista_edades_mayores}")
