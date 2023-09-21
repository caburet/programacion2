#Dada una lista de diccionarios que contienen información de estudiantes de una materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final), crea una lista que contenga los nombres de todos los estudiantes que han obtenido una calificación superior a 90 en al menos un examen utilizando list comprehensions.

list_Estudiantes = [
    {"Nombre": 'joaquin hernandez',"legajo":'1234',"nota_parcial1":10,"nota_parcial2":8,"nota_final":9},
    {"Nombre": 'Leo Messi',"legajo":'1235',"nota_parcial1":7,"nota_parcial2":7,"nota_final":7},
    {"Nombre": 'Rodrigo de Paul',"legajo":'1236',"nota_parcial1":10,"nota_parcial2":6,"nota_final":8},
    ]

list_Estudiantes_con10 = [estudiante["Nombre"] for estudiante in list_Estudiantes if estudiante["nota_parcial1"] > 9 or estudiante["nota_parcial2"] > 9]

print(f"los estudiantes que se sacaron mas de 9 son: {list_Estudiantes_con10}")

