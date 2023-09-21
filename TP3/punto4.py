#Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que comienzan con una letra específica
# (por ejemplo, "a") indicada por el usuario, utilizando list comprehensions.


my_dict={'Accesorio': " Utensilio auxiliar para determinado trabajo o para el funcionamiento de una máquina",
        'Vasija': "Pieza cóncava y pequeña, de barro u otra materia y de forma común u ordinaria, que sirve para contener especialmente líquidos o cosas destinadas a la alimentación.",
        'Dogma': "Proposición tenida por cierta y como principio innegable."
        ,'Demagogia':"Práctica política consistente en ganarse con halagos el favor popular."
        ,'Amansar':'Domesticar, hacer manso a un animal'}

letra=input("Ingrese una letra para buscar en el diccionario: ")
    # Asignamos a la lista las palabras que empiecen con esa letra con list comprehension
lista = [palabra for palabra in my_dict.keys() if palabra.lower.startswith(letra)]

    # Mostramos la lista con las palabras que comiencen con la letra ingresada
print(lista)