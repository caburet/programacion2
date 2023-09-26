# 11. Dada una lista de diccionarios que contienen información de estudiantes de una materia 
# (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final), crea una lista que contenga
#  los nombres de todos los estudiantes que han obtenido una calificación superior a 90 en al menos un examen utilizando list comprehensions.

def estudiantes():
    estudiantes = [
        {"Nombre": "Camila", "Legajo": 21535, "Parcial1": 60, "Parcial2": 40, "Nota_final" :  50},
        {"Nombre": "Juan", "Perez": 21534, "Parcial1": 80, "Parcial2": 40, "Nota_final" :  60},
        {"Nombre": "Lucila", "Legajo": 21532, "Parcial1": 95, "Parcial2": 40, "Nota_final" : 75},
        {"Nombre": "Eros", "Legajo": 21531, "Parcial1": 92, "Parcial2": 90, "Nota_final" : 90}
    ]

    lista_estudiantes = [item["Nombre"] for item in estudiantes if (item["Parcial1"] >= 90 or item["Parcial2"] >= 90 ) ]

    print(lista_estudiantes)

estudiantes()
    