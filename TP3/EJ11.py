#11. Dada una lista de diccionarios que contienen información de estudiantes de una materia 
#   (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final), crea una lista que contenga
#   los nombres de todos los estudiantes que han obtenido una calificación superior a 90 en al menos 
#   un examen utilizando list comprehensions. 

archivo_alumnos =open('G:/Mi unidad/UTN/Programacion2/TP-3/programacion2/TP3/alumnos.txt','r')

def leer_archivo(archivo):
    lista =[]
    for linea in archivo:
        campos = linea.strip().split(';')
        nombre, legajo,nota1,nota2,notaf = campos
        alumno ={'nombre':nombre,'legajo':legajo,'nota1':nota1,'nota2':nota2,'notaf':notaf}
        lista.append(alumno)

    return lista

def main():
    lista_alumnos = leer_archivo(archivo_alumnos)

    for alumno in lista_alumnos:
        promedio = 0
        suma = 0
        suma = int(alumno['nota1']) + int(alumno['nota2']) + int(alumno['notaf'])
        promedio = suma / 3
        if promedio >= 9:
            lista_aprobados = [alumno['nombre']]  

    lista_aprobados_l = [alumno['nombre'] for alumno in lista_alumnos if (int(alumno['nota1']) + int(alumno['nota2']) + int(alumno['notaf']))/3 >= 9]

    print(lista_aprobados)
    print(lista_aprobados_l)
main()

