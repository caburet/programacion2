#Dadas dos listas de números del mismo tamaño, crea una nueva lista que contenga la multiplicación de los elementos correspondientes de ambas listas utilizando list comprehensions.

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

def Multi(list1, list2):
    list_multi = [a*b for a,b in zip(list1,list2)]
    return list_multi

lista_multiplicacion = Multi(list1, list2)
print(f"La lista de las multiplicaciones es: {lista_multiplicacion}")
