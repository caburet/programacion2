##1. Implemente una función que dada una lista de números, devuelva una nueva lista que contenga el cuadrado de cada número utilizando list comprehensions.

lista1 = [1,2,3,4,5,6,7]
nueva_lista = []
nueva_lista = [elem**2 for elem in lista1]

print(f"La lista original es: {lista1}")
print(f"La lista elevada al cuadrado es: {nueva_lista}")