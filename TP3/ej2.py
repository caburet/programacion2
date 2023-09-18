##2. Implemente una función que dada una lista de nombres, devuelva una nueva lista que contenga solo los nombres que tengan una longitud mayor o igual a una cantidad de caracteres pasada por parámetro, utilizando list comprehensions.

list_names = ["dibu","cuti","otamendi","molina","tagliafico","de paul"]
longitud = int(input("Ingrese la longitud que desea: "))
new_list = []

new_list = [nombre for nombre in list_names if len(nombre) >= longitud]
print(new_list)