#Dada una lista de diccionarios que contienen información de estudiantes de una materia 
#(nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final), 
#crea una lista que contenga los nombres de todos los estudiantes que han obtenido una calificación 
#superior a 90 en al menos un examen utilizando list comprehensions.

lista_alumnos=[
             {'nombre_apellido':'Eros Marziani','legajo':21987,'nota_parcial1':91,'nota_parcial_2':89,'nota_parcial3':87},
             {'nombre_apellido':'Matias Martinez','legajo':78945,'nota_parcial1':55,'nota_parcial_2':47,'nota_parcial3':80},
             {'nombre_apellido':'Gabriela Garcia','legajo':74858,'nota_parcial1':12,'nota_parcial_2':23,'nota_parcial3':99},
             {'nombre_apellido':'John Rockefeller ','legajo':66666,'nota_parcial1':90,'nota_parcial_2':83,'nota_parcial3':100},
             {'nombre_apellido':'Juan Travolta','legajo':78931,'nota_parcial1':44,'nota_parcial_2':45,'nota_parcial3':23}
             ]

lista_noventa=[alumno['nombre_apellido']for alumno in lista_alumnos if alumno['nota_parcial1']>90 or alumno['nota_parcial_2']  or alumno["nota_parcial3"]>90]

print(f"Los alumnos con notas superiores a 90 son {lista_noventa}")

