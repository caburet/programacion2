#Dadas dos listas de números del mismo tamaño, crea una nueva lista que contenga la multiplicación de los elementos correspondientes de ambas listas utilizando list comprehensions.

lista_uno=[1,2,3,4,5,6,7,8,9,10]
lista_dos=[10,9,8,7,6,5,4,3,2,1]

new_list=[lista_uno[i] * lista_dos[i] for i in range(len(lista_dos))]
print(new_list)