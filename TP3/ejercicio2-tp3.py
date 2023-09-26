#2. Implemente una función que dada una lista de nombres, devuelva una nueva lista que contenga solo los nombres que tengan 
#una longitud mayor o igual a una cantidad de caracteres pasada por parámetro, utilizando list comprehensions.

def lista_nombres(lista, longitud):
    return [nombre for nombre in lista if len(nombre) >= longitud]
    

lista = ["Camila", "Mariana", "Julieta", "Martina", "Sol", "Magdalena", "Francesca"]
nombre = lista_nombres(lista, 5)
print(nombre)

