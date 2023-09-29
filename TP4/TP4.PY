def menu():
    print("\n0. Salir.")
    print("\n1. Crea una función lambda que tome un número como argumento y devuelva su cuadrado.")
    print("\n2. Crea una función lambda que tome dos números como argumentos y devuelva su suma.")
    print("\n3. Crea una función lambda que devuelva el mayor de dos números.")
    print("\n4. A partir de una lista de números existente, cree una nueva lista incrementando en un 15% los valores originales usando map.")
    print("\n5. Ordenar una lista de diccionarios por un elemento del diccionario. ej: ordenar por edad la siguiente lista:")
    print("personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]")
    print("\n6. Dada una lista con números, filtra los números pares y devolverlos en una nueva lista.")
    print("\n7. Dada una lista de temperaturas en grados centígrados generar una nueva lista con las temperaturas expresadas en grados fahrenheit, la fórmula para convertir la temperatura es °F=(°C*(9/5))+32.")
    print("\n8. Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar la lista de acuerdo a la longitud de las palabras.")
    print("\n9. Dada una lista de palabras, genera una lista con las iniciales de cada palabra.")
    print("\n10. Dada una lista de diccionarios con los alumnos y notas de un curso, calcular el promedio del curso. Puede usar una lista como la siguiente:")
    print("lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]")
    print("\n11. Encuentra el número mayor de una lista utilizando reduce.")
    print("\n12. Utilice reducir para concatenar una lista de cadenas en una sola cadena.")
    print("\n13. Filtrar una lista de diccionarios por una condición. Ej: filtrar la lista del punto 10 para obtener notas de los alumnos aprobados.")
    print("\n14. Dada una lista de diccionarios con nombre, fecha de nacimiento, y teléfono, crear una nueva lista con los diccionarios de las personas que aún no cumplieron años respecto a la fecha actual del sistema, y ​​esa lista ordenarla por la fecha de nacimiento de menor a alcalde. Puede usar una lista como la siguiente:")
    print("import datetime")
    print("lista_alumnos = [{'nombre':'Joaquin', 'fecha_nacimiento':datetime.date(1990, 7, 2), 'telefono':'123456789'}, { 'nombre':'Maria', 'fecha_nacimiento':datetime.date(1995, 5, 16), 'telefono':'123456789'}, { nombre':'Pedro', 'fecha_nacimiento':datetime.date(1992, 9, 12), 'telefono':'123456789'}, { 'nombre':'Ana', 'fecha_nacimiento':datetime.date(1991, 9, 22), 'telefono':'123456789'}, { 'nombre':'Florencia', 'fecha_nacimiento':datetime.date(1994, 12, 8), 'telefono':'123456789'}, { 'nombre':'Hector'', 'fecha_nacimiento':datetime.date(1993, 4, 4), 'telefono':'123456789'}]")

def validar():
    numero_ejercio=-1
    while numero_ejercio<0 or numero_ejercio>14:
        numero_ejercio=int(input("Ingrese opcion a realizar: "))
        if numero_ejercio<0 or numero_ejercio>14:
            print("Opcion incorrecta, vuelva a intentar!")
    return numero_ejercio
    
def ejercicio_1():
    numero=int(input("Ingrese numero: "))
    cuadrado=lambda x: x**2
    resultado=cuadrado(numero)
    print(f"El resultado es: {resultado}")

def ejercicio_2():
    numero1=int(input("Ingrese numero 1: "))
    numero2=int(input("Ingrese numero 2: "))
    suma=lambda x,y: x+y
    resultado=suma(numero1,numero2)
    print(f"El resultado de la suma es: {resultado}")

def ejercicio_3():
    numero1=int(input("Ingrese numero 1: "))
    numero2=int(input("Ingrese numero 2: "))
    mayor=lambda x,y: x if x>y else y
    resultado=mayor(numero1,numero2)
    print(f"El mayor es: {resultado}")

def ejercicio_4():
    lista_original=[1,2,3,4,5,6,7,8,9]
    lista_nueva=[]
    lista_nueva=list(map(lambda x: (x*0.15)+x,lista_original))
    print(f"Muestro lista nueva:{lista_nueva}")
#SORTED ORDENA . SEGUN REVERSE
def ejercicio_5():
    personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]
    personas_ordenadas=sorted(personas, key=lambda x:x['edad'], reverse=True)
    print(personas_ordenadas)
#Filter Filtra la lista segun condicion que se quiera
def ejercicio_6():
    lista_original=[1,2,3,4,5,6,7,8,9,10]
    lista_pares=[]
    lista_impares=[]
    lista_pares=list(filter(lambda x: x% 2==0,lista_original))
    lista_impares=list(filter(lambda x: x% 2!=0,lista_original))
    print("Lista impares")
    print(lista_impares)
    print("Lista pares")
    print(lista_pares)

def ejercicio_7():
    lista_original=[1,2,3,4,5,6,7,8,9,10]
    lista_nueva=[]
    lista_nueva=[(elemento*(9/5)+32) for elemento in lista_original]
    print("Lista en F")
    print(lista_nueva)

def ejercicio_8():
    lista_original=['hola','mundo','jonatan','bruno','lenguaje','ana']
    lista_nueva=sorted(lista_original, key=lambda x: len(x),reverse=False )
    print("Lista nueva")
    print(lista_nueva)

def ejercicio_9():
    lista_original=['hola','mundo','jonatan','bruno','lenguaje','ana']
    lista_nueva=[elemento[0] for elemento in lista_original]
    print("Lista nueva")
    print(lista_nueva)

from functools import reduce

def ejercicio_10():
    suma=0
    lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]
    cantidad_alumnos=len(lista_dic)
    for elemento in lista_dic:
        suma=suma+int(elemento['nota'])
    promedio=suma/cantidad_alumnos
    print(f"El promedio de los alumnos es: {promedio}")

def ejercicio_11():
    lista_original=[1,2,3,4,90,6,7,8,9,10]
    numero_mayor=reduce(lambda x,y: x if x>y else y,lista_original)
    print(f"El mayor numero es: {numero_mayor}")

def ejercicio_12():
    lista_original=['hola','mundo','jonatan','bruno','lenguaje','ana']
    cadena=reduce(lambda x,y: x+y,lista_original)
    print(f"La cadena quedaria: {cadena}")

def ejercicio_13():
    lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]
    lista_nueva=list(filter(lambda x: x['nota']>=60 ,lista_dic))
    print("Lista de alumnos aprobados: ")
    print(lista_nueva)

import datetime
def ejercicio_14():
    fecha_actual=datetime.date.today()
    lista_alumnos = [{'nombre':'Joaquin', 'fecha_nacimiento':datetime.date(1990, 7, 2), 'telefono':'123456789'}, { 'nombre':'Maria', 'fecha_nacimiento':datetime.date(1995, 5, 16), 'telefono':'123456789'}, {'nombre':'Pedro', 'fecha_nacimiento':datetime.date(1992, 9, 12), 'telefono':'123456789'}, { 'nombre':'Ana', 'fecha_nacimiento':datetime.date(1991, 9, 22), 'telefono':'123456789'}, { 'nombre':'Florencia', 'fecha_nacimiento':datetime.date(1994, 12, 8), 'telefono':'123456789'}, { 'nombre':'Hector', 'fecha_nacimiento':datetime.date(1993, 4, 4), 'telefono':'123456789'}]
    personas_sin_cumpleanos = [alumno for alumno in lista_alumnos if (alumno["fecha_nacimiento"].month, alumno["fecha_nacimiento"].day) > (fecha_actual.month, fecha_actual.day)]
    personas_sin_cumpleanos.sort(key=lambda x: x["fecha_nacimiento"])
    for alumno in personas_sin_cumpleanos:
        print(f"Nombre: {alumno['nombre']}, Fecha de Nacimiento: {alumno['fecha_nacimiento']}, Teléfono: {alumno['telefono']}")

#Aca comienza el programa


sigue=True
while sigue==True:
    menu()
    n_ejercicio=validar()
    if n_ejercicio==1:
        ejercicio_1()
    elif n_ejercicio==2:
        ejercicio_2()
    elif n_ejercicio==3:
        ejercicio_3()
    elif n_ejercicio==4:
        ejercicio_4()
    elif n_ejercicio==5:
        ejercicio_5()
    elif n_ejercicio==6:
        ejercicio_6()
    elif n_ejercicio==7:
        ejercicio_7()
    elif n_ejercicio==8:
        ejercicio_8()
    elif n_ejercicio==9:
        ejercicio_9()
    elif n_ejercicio==10:
        ejercicio_10()
    elif n_ejercicio==11:
        ejercicio_11()
    elif n_ejercicio==12:
        ejercicio_12()
    elif n_ejercicio==13:
        ejercicio_13()
    elif n_ejercicio==14:
        ejercicio_14()

