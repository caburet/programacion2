#1. Implemente una función que dada una lista de números, devuelva una nueva lista que contenga
# el cuadrado de cada número utilizando list comprehensions.

lista_numeros = [1,2,3,4,5,6,7,8,9]

def lista_al_cuadrado(lista):
    nueva_lista =[valor**2 for valor in lista]
    return nueva_lista

print(lista_al_cuadrado(lista_numeros))