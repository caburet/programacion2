from functools import reduce
import os
import datetime

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def Pedir_Entero_mayor1():
    num = 1
    while True and num>0:
        try:
            num = int(input())
            return num
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

def Pedir_Entero():
    while True:
        try:
            num = int(input())
            return num
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

def Pedir_Float():
    num = float(0.1)
    while True and num>0.0:
        try:
            num = float(input())
            return num
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")


def Ejercicio1():
    clear_console() 
    print("Ingrese un numero para devolver su cuadrado con lambda: ")
    numero = Pedir_Entero()
    cuadrado = lambda x: x**2
    print(cuadrado(numero))

    input("Presiona Enter para continuar...")

def Ejercicio2():
    clear_console()
    print("Crea una función lambda que tome dos números como argumentos y devuelva su suma.")
    print("Ingrese el primer número: ")
    numero1 = Pedir_Entero()
    print("Ingrese el segundo número: ")
    numero2 = Pedir_Entero()
    suma = lambda x,y: x+y

    print(suma(numero1,numero2))
    input("Presiona Enter para continuar...")

def Ejercicio3():
    clear_console()
    print("Crea una función lambda que devuelva el mayor de dos números.")
    print("Ingrese el primer número: ")
    numero1 = Pedir_Entero()
    numero2 = Pedir_Entero()
    numeromayor = lambda x,y: x if x>y else y

    print(numeromayor(numero1,numero2))

    input("Presiona Enter para continuar...")

def Ejercicio4():
    clear_console()
    print ("Ejercicio4 - A partir de una lista de números existente, crear una nueva lista incrementando en un 15% los valores originales usando map.")
    listanum = [40,66,100,100,200,1000]

    mas15porciento = list(map(lambda x:x+x*0.15, listanum))

    print(mas15porciento)

    input("Presiona Enter para continuar...")
    
def Ejercicio5():
    clear_console()
    print ("Ejercicio5 - ordenar por edad la suguiente lista de diccionarios:")

    personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]

    personas_ordenadas = sorted(personas, key=lambda x: x['edad'])
    print(personas_ordenadas)

    input("Presiona Enter para continuar...")
    
def Ejercicio6():
    clear_console()
    print ("Ejercicio 6 - Dada una lista con números, filtrar los números pares y devolverlos en una nueva lista.")
    listanum = [40,11,67,103,100,200,1000]
    print(listanum)
    filtrodepares = list(filter(lambda x: x%2==0,listanum))

    print(filtrodepares)

    input("Presiona Enter para continuar...")
    
def Ejercicio7():
    clear_console()
    print ("Ejercicio 7 - ada una lista de temperaturas en grados celsius generar una nueva lista con las temperaturas expresadas en grados fahrenheit, la fórmula para convertir la temperatura es `°F=(°C*(9/5))+32`.")
    listatemp = [25,17,39,45,60,35,27]
    print(listatemp)
    listafarenheit = list(map(lambda x: x*9/5 + 32, listatemp))

    print(listafarenheit)

    input("Presiona Enter para continuar...")
    
def Ejercicio8():
    clear_console()
    print ("Ejercicio 8 - Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar la lista de acuerdo a la longitud de las palabras.")
    listapalabras = ["hola","mundo","python","sorted","map","zxzzxczxcz"]
    print(listapalabras)
    palabras_ordenadas_long = sorted(listapalabras, key=lambda palabra:len(palabra))
    print(palabras_ordenadas_long)
    input("Presiona Enter para continuar...")
    
def Ejercicio9():
    clear_console()
    print ("Ejercicio 9 - Dada una lista de palabras, generar una lista con las iniciales de cada palabra.")


    listapalabras = ["hola","mundo","python","sorted","map","zxzzxczxcz"]

    lista_iniciales = list(map(lambda x: x[0], listapalabras))

    print(lista_iniciales)
    input("Presiona Enter para continuar...")
    
def Ejercicio10():
    clear_console()
    print ("Ejercicio10 - Dada una lista de diccionarios con los alumnos y notas de un curso, calcular el promedio del curso. Puede usar una lista como la siguiente: ")
    lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]

    suma = sum(map(lambda x: x['nota'], lista_dic))
    promedio = suma/len(lista_dic)

    print(promedio)
    input("Presiona Enter para continuar...")
    
def Ejercicio11():
    clear_console()
    print ("Ejercicio11 - Encuentra el número mayor de una lista utilizando reduce.")
    listanum = [1,2,3,4,5,1000,2,5,1212]

    num_mayor = reduce(lambda x,y: x if x>y else y, listanum)

    print(num_mayor)

    input("Presiona Enter para continuar...")
    
def Ejercicio12():
    clear_console()
    print ("Ejercicio 12 - Utilice reduce para concatenar una lista de cadenas en una sola cadena")
    lista_cadenas = ["hola","mundo","python", "lambda"]
    print(lista_cadenas)
    unir_cadena_texto = reduce(lambda x,y:x + " " + y, lista_cadenas)

    print(unir_cadena_texto)

    input("Presiona Enter para continuar...")
    
def Ejercicio13():
    clear_console()
    print ("Ejercicio 13 - iltrar una lista de diccionarios por una condición. Ej: filtrar la lista del punto 10 para obtener notas de los alumnos aprobados.")
    lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]
    print(lista_dic)

    lista_aprobados = list(filter(lambda x: x['nota']>=60,lista_dic))

    print(lista_aprobados)

    input("Presiona Enter para continuar...")
    
def Ejercicio14():
    clear_console()
    print ("Ejercicio 14 - ")
    lista_alumnos = [{"nombre":"Joaquin", "fecha_nacimiento":datetime.date(1990, 7, 2), "telefono":"123456789"}, { "nombre":"Maria", "fecha_nacimiento":datetime.date(1995, 5, 16), "telefono":"123456789"}, { "nombre":"Pedro", "fecha_nacimiento":datetime.date(1992, 9, 12), "telefono":"123456789"}, { "nombre":"Ana", "fecha_nacimiento":datetime.date(1991, 9, 22), "telefono":"123456789"}, { "nombre":"Florencia", "fecha_nacimiento":datetime.date(1994, 12, 8), "telefono":"123456789"}, { "nombre":"Hector", "fecha_nacimiento":datetime.date(1993, 4, 4), "telefono":"123456789"}]
    fechasistema = datetime.date.today()  
    print("Fecha del sistema:", fechasistema)
    print(lista_alumnos)
    lista_sin_cumpleanios = list(filter(lambda x: x['fecha_nacimiento'].month < fechasistema.month or (x['fecha_nacimiento'].month == fechasistema.month and x['fecha_nacimiento'].day <= fechasistema.day), lista_alumnos))
    print()
    print(lista_sin_cumpleanios)


    input("Presiona Enter para continuar...")
    

def switch(opcion):

    if opcion == 1:
        Ejercicio1()
    elif opcion == 2:
        Ejercicio2()
    elif opcion == 3:
        Ejercicio3()
    elif opcion == 4:
        Ejercicio4()
    elif opcion == 5:
        Ejercicio5()
    elif opcion == 6:
        Ejercicio6()
    elif opcion == 7:
        Ejercicio7()
    elif opcion == 8:
        Ejercicio8()
    elif opcion == 9:
        Ejercicio9()
    elif opcion == 10:
        Ejercicio10()
    elif opcion == 11:
        Ejercicio11()
    elif opcion == 12:
        Ejercicio12()
    elif opcion == 13:
        Ejercicio13()
    elif opcion == 14:
        Ejercicio14()


def Menu():
    clear_console()
    print("****************************************")
    print("*         TRABAJO PRÁCTICO 4           *")    
    print("*Ingrese opción deseada:               *")
    print("*1- Ejercicio 1                        *")
    print("*2- Ejercicio 2                        *")
    print("*3- Ejercicio 3                        *")
    print("*4- Ejercicio 4                        *")
    print("*5- Ejercicio 5                        *")
    print("*6- Ejercicio 6                        *")
    print("*7- Ejercicio 7                        *")
    print("*8- Ejercicio 8                        *")
    print("*9- Ejercicio 9                        *")
    print("*10- Ejercicio 10                      *")
    print("*11- Ejercicio 11                      *")
    print("*12- Ejercicio 12                      *")
    print("*13- Ejercicio 13                      *")
    print("*14- Ejercicio 14                      *")
    print("*0-  Salir                             *")
    print("****************************************")

n = int(1)
while int(n)>0 and int(n)<15:
    Menu()
    n = input("Ingrese opción de menú: ")
    if n.isdigit():
        n = int(n)
        switch(n)
    else:
        print("Ingrese un número válido")
        n = int(1)