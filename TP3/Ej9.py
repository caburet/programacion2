#9. Dadas dos listas de números del mismo tamaño, crea una nueva lista que contenga 
#   la multiplicación de los elementos correspondientes de ambas listas utilizando list comprehensions.

lista1 =[1,2,3,4,5,6,7,8,9]
lista2 =[9,8,7,6,5,4,3,2,1]

nueva_lista = [item1 * item2 for item1, item2 in zip(lista1, lista2)]

print(nueva_lista)