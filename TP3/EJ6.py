#6. Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres
#   de las personas cuya edad es mayor a una edad ingresada por el usuario, utilizando list comprehensions.

diccionario = {'pepe': 35,'roberto':45,'alejandro':19,'maria':25}
lista_nueva=[]

def lista_mayores(dicc):
    lista_nueva =[nombre for nombre, edad in dicc.items() if edad >= 26]
    return lista_nueva


print(lista_mayores(diccionario))