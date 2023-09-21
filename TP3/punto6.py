#Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres de las personas cuya edad es mayor a una edad ingresada por el usuario, utilizando list comprehensions.




personas_dict={'Eros':21,'Joaquin':22,'Daniela':48,'Marcelo':39,'Carlos':44}
edad=int(input("Ingrese la edad deseada para filtrar la lista"))
lista_filtrada=[nombre for nombre,edad_personas in personas_dict.items() if edad_personas>edad]
print(lista_filtrada)
