import csv
import os
import random
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

#Funciones para colas

def encolar(cola,elemento):
    cola.append(elemento)

def desencolar(cola,elemento):
    if not estavaciacola():
        return cola.pop(0)
    else:
        return "La cola está vacía"
def longcola(cola):
    return len(cola)

def estavaciacola(cola):
    if len(cola)==0:
        return True
    else:
        return False

def Ejercicio1():
    clear_console() 
    input("Presiona Enter para continuar...")

# Funciones para pilas

def apilar(pila,elemento):
    pila.append(elemento)

def desapilar(pila,elemento):
    if not estavaciapila():
        return pila.pop()
    else:
        return "La pila está vacía"
def estavaciapila(pila):
    if len(pila)==0:
        return True
    else:
        return False

def Ejercicio2():
    clear_console()
    input("Presiona Enter para continuar...")

def doslistasrandom(lista1,lista2):
    longlista1 = random.randint(20,50)
    longlista2 = random.randint(20,50)
    for numero in range(0,longlista1):
        lista1.append(random.randint(200,5000))
    for numero in range(0,longlista2):
        lista2.append(random.randint(200,5000))


def Ejercicio3():
    clear_console()
    print("Ejercicio 3 - Dos listas random, con números random")
    lista_numeros1 = []
    lista_numeros2 = []
    doslistasrandom(lista_numeros1,lista_numeros2)
    print(lista_numeros1)
    print()
    print(lista_numeros2)


    input("Presiona Enter para continuar...")

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def Ejercicio4():
    clear_console()
    print ("Ejercicio 4 - ")
    lista_1 = []
    lista_2 = []
    doslistasrandom(lista_1,lista_2)

    lista1_impares_X_menorlista2 = list(filter(lambda x: x*min(lista_2) if x%2!=0 else None, lista_1))
    print(lista1_impares_X_menorlista2)
    print()
    print(lista_2)
    print()
    menor_primo = min(filter(lambda x: es_primo(x), lista_2), default=-1)

    print(menor_primo)
    input("Presiona Enter para continuar...")
    
def Cargar_Alumnos(ruta):
    alumnos = []
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            datos = linea.strip().split(';')
            alumno = {
                'alumno_dni' : int(datos[0]),
                'alumno_apellido' : datos[1],
                'alumno_nombre' : datos[2]
            }
            alumnos.append(alumno)

    return alumnos

def Cargar_eventos(ruta):
    eventos = []
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            datos = linea.strip().split(';')
            evento = {
                'evento_codigo': int(datos[0]),
                'deporte_codigo' : int(datos[1]),
                'evento_nombre' : datos[2],
                'evento_descripcion' : datos[3]
            }
            eventos.append(evento)
    
    return eventos

def Cargar_deportes(ruta):
    deportes = []
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            datos = linea.strip().split(';')
            deporte = {
                'deporte_codigo' : int(datos[0]),
                'deporte_nombre' : datos[1]
                }
            deportes.append(deporte)
   
    return deportes



def Cargar_alumnodeportes(ruta):
    alumnos_deportes = []
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            datos = linea.strip().split(';')
            alumno_deporte = {
                'alumno_dni': int(datos[0]),
                'deporte_codigo': int(datos[1])
                }
            alumnos_deportes.append(alumno_deporte)
    return alumnos_deportes

def Cargar_inscripciones(ruta):
    inscripciones = []
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:
            datos = linea.strip().split(';')
            inscripcion = {
                'alumno_dni': int(datos[0]),
                'evento_codigo': int(datos[1])
                }
            inscripciones.append(inscripcion)
    return inscripciones


def Ejercicio5():
    clear_console()
    print ("Ejercicio 5 - Alumnos deportes, encolar, estadisticas")
    rutaAlumnos = "alumnos.csv"
    rutaAlumnoDeportes = "alumnos_deportes.csv"
    rutaDeportes = "deportes.csv"
    rutaEventos = "eventos.csv"
    rutaInscripciones = "inscripciones.csv"
    rutaAlumnoEventos = "alumno_eventos.csv"

    ListaAlumnos = Cargar_Alumnos(rutaAlumnos)
    ListaAlumnoDeportes = Cargar_alumnodeportes(rutaAlumnoDeportes)
    ListaDeportes = Cargar_deportes(rutaDeportes)
    ListaEventos = Cargar_eventos(rutaEventos)
    ListaInscripciones = Cargar_inscripciones(rutaInscripciones)

    Alumno_Eventos = []
    contador = 1
    # Encolar Alumnos a Eventos
    for Inscripcion in ListaInscripciones:
        for Alumno in ListaAlumnos:
            if Alumno['alumno_dni'] == Inscripcion['alumno_dni']:
                        Alumno_Evento = {
                            'alumno_dni': Alumno['alumno_dni'],
                            'evento_codigo': Inscripcion['evento_codigo'],
                            'numero_inscripcion': contador
                        }
                        contador += 1
                        encolar(Alumno_Eventos, Alumno_Evento)

    # Escribir en el archivo
    with open(rutaAlumnoEventos, 'w', newline='') as csvfile:
        campos = ['alumno_dni', 'evento_codigo', 'numero_inscripcion']
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        for fila in Alumno_Eventos:
            writer.writerow(fila)


    

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


def Menu():
    clear_console()
    print("****************************************")
    print("*         TRABAJO PRÁCTICO X           *")    
    print("*Ingrese opción deseada:               *")
    print("*1- Ejercicio 1                        *")
    print("*2- Ejercicio 2                        *")
    print("*3- Ejercicio 3                        *")
    print("*4- Ejercicio 4                        *")
    print("*5- Ejercicio 5                        *")
    print("*0-  Salir                             *")
    print("****************************************")

n = int(1)
while int(n)>0 and int(n)<6:
    Menu()
    n = input("Ingrese opción de menú: ")
    if n.isdigit():
        n = int(n)
        switch(n)
    else:
        print("Ingrese un número válido")
        n = int(1)