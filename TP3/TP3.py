import os #Importo libreria para hacer console clear y que quede mas prolija la navegacion entre ejercicios
def clear_console(): # llamo a la función cada vez que limpio la consola 
    os.system('cls' if os.name == 'nt' else 'clear')

def Pedir_Palabra():
    while True:
        palabra = input("Ingrese una palabra(escriba 'salir' para salir): ")
        if palabra.isalpha() and palabra.strip() != "":
            return palabra
        else:
            print("La palabra ingresada no es válida. Intente nuevamente.")

def Pedir_Char():
    caracter = ''
    while True:
        try:
            entrada = input("Ingrese un caracter: ")
            if len(entrada) == 1:
                caracter = entrada
                return caracter
            else:
                print("Debe ingresar exactamente un caracter. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

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

def Ejercicio1():
    clear_console() 
    print("Ejercicio 1 - Lista de números y devolver lista al cuadrado.")

    numeros = [5,8,2,4,8,9,2,4,12]
    print ("Lista original:", numeros)
    numeros2 = [elemento**2 for elemento in numeros]
    print ("Lista al cuadrado:", numeros2)

    input("Presiona Enter para continuar...")
def filtar_nombres(lista,longitud):
    listanueva = [nombre for nombre in lista if len(nombre)>=longitud]
    return listanueva

def Ejercicio2():
    clear_console()
    print("Ejercicio 2 - Función que devuelva lista nueva con nombres de long pasada por parametros.")

    lista = ["Juan", "Pedro", "Maria", "Cristina", "Jose", "Matias", "Fernando"]
    longitud = 5
    listanueva = filtar_nombres(lista,longitud)
    print("Lista original:", lista)
    print(f"Lista filtrada por longitud {longitud}:", listanueva)

    input("Presiona Enter para continuar...")

def Ejercicio3():
    clear_console()
    print("Ejercicio 3 - Leer datos de un txt y guardarlos en una lista")
    lista =[]
    try:
        with open("datos.txt", "r") as datos: #with abre en solo lectura y cierra el archivo automaticamente
            lista = [linea.strip() for linea in datos] #strip elimina los saltos de linea
        print("Lista:", lista)
    except FileNotFoundError:
        print("El archivo 'datos.txt' no se encuentra.")
    
    input("Presiona Enter para continuar...")

def Ejercicio4():
    clear_console()
    print ("Ejercicio 4 - Diccionario y definiciones, devolver palabras que contengan letra indicada por usuario")
    diccionario = {'azul': 'color', 'rojo': 'color', 'verde': 'color', 'mesa': 'mueble para apoyar elementos', 'silla': 'mueble con cuatro patas para sentarse', 'lampara': 'objeto que da luz','a': 'letra del abecedario','anis': 'planta aromatica'}
    letra = Pedir_Char()
    palabras_con_letra = [palabra for palabra in diccionario if letra in palabra[0]]
    print("Palabras que contienen la letra", letra, ":", palabras_con_letra)

    input("Presiona Enter para continuar...")
    
def esPrimo(numero):
    for num in range(2, numero):
        if numero % num == 0: #si el numero es divisible por otro que no sea uno o si mismo retorna falso
            return False
    return True #si no es divisible por ninguno retorna verdadero

def Ejercicio5():
    clear_console()
    print ("Ejercicio 5 - Lista de números y devolver lista de primos")
    numeros =[4,5,6,7,8,9,10,11,12,13]
    lista_primos = [numero for numero in numeros if esPrimo(numero)]
    print("Lista original:", numeros)
    print("Lista de números primos:", lista_primos)

    input("Presiona Enter para continuar...")
    
def Ejercicio6():
    clear_console()
    print ("Ejercicio 6 - Personas y edades, numero de usuario devolver edades mayores")
    dicc_personas = {'Juan':25, 'Javier':3, 'Gaston':18, 'Lucia':8, 'Jose':35, 'Ana':22, 'Maria':37}
    print ("Ingrese edad: ")
    edad = Pedir_Entero_mayor1()
    lista_personas = [nombre for nombre, edad_persona in dicc_personas.items() if edad_persona > edad]

    print (f"Lista de personas mayores a {edad}:", lista_personas)

    input("Presiona Enter para continuar...")
    
def Ejercicio7():
    clear_console()
    print ("Ejercicio 7 - Programa palabras y contar vocales")
    palabra = ""
    while palabra != "salir":
        palabra = Pedir_Palabra()
        palabra = palabra.lower()
        if palabra =='salir':
            break
        lista_vocales = [vocal for vocal in palabra if vocal=='a' or vocal=='e' or vocal=='i' or vocal=='o' or vocal=='u']
        print("Cantidad de vocales en su palabra: ", len(lista_vocales))

    input("Presiona Enter para continuar...")
    
def Ejercicio8():
    clear_console()
    print ("Ejercicio 8 - Lista con elementos duplicados, crear lista con elemtos únicos")
    lista_dupli = ['Riquelme','Palermo','Guillermo','Riquelme','Ibarra','Cordoba','Cordoba','Riquelme']
    lista_unica = []
    [lista_unica.append(jugador) for jugador in lista_dupli if jugador not in lista_unica]

    print("Lista origincal: ", lista_dupli)
    print("Lista única: ", lista_unica)

    input("Presiona Enter para continuar...")
    
def Ejercicio9():
    clear_console()
    print ("Ejercicio 9 - Multiplicar dos listas de numeros")
    lista_numeros = [6,8,5,9,3,6,0,12]
    lista_numeros2 = [9,5,8,3,5,8,9,66]

    lista_multiplicados = [lista_numeros[i]*lista_numeros2[i] for i in range(len(lista_numeros))]
    print("Lista de numeros 1: ", lista_numeros)
    print("Lista de numeros 2: ", lista_numeros2)
    print("Lista de multiplicados: ", lista_multiplicados)

    input("Presiona Enter para continuar...")
    
def Ejercicio10():
    clear_console()
    print ("Ejercicio 10 - Crear dos listas de acuerdo a si el número es par o no")

    lista_numeros = [2,5,8,3,6,9,11,20,12,100,7]
    lista_pares = []
    lista_impares = []
    [lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero) for numero in lista_numeros]
    print("Lista de numeros: ", lista_numeros)
    print("Lista de pares", lista_pares)
    print("Lista de impares", lista_impares)

    input("Presiona Enter para continuar...")
    
def Ejercicio11():
    clear_console()
    print ("Ejercicio 11 - Lista de diccionarios de estudiantes y notas mas altas")
    lista_estudiantes = [
        {"nombre_apellido": "Juan Chaparro","legajo": 21737,"notaparcial1":100,"notaparcial2":100,"notafinal": 100},
        {"nombre_apellido": "Ariel Sanchez","legajo": 22222,"notaparcial1":88,"notaparcial2":70,"notafinal": 70},
        {"nombre_apellido": "Carlos Gonzalez","legajo": 23456,"notaparcial1":91,"notaparcial2":30,"notafinal": 80},
        {"nombre_apellido": "Maria Correa","legajo": 28999,"notaparcial1":95,"notaparcial2":100,"notafinal": 10},
        {"nombre_apellido": "Lucas Fernando","legajo": 20333,"notaparcial1":88,"notaparcial2":90,"notafinal": 100},
        {"nombre_apellido": "Luna Ledesma","legajo": 22012,"notaparcial1":60,"notaparcial2":80,"notafinal": 70},
        {"nombre_apellido": "Angel Clemente","legajo": 22332,"notaparcial1":88,"notaparcial2":79,"notafinal": 80},
        {"nombre_apellido": "Salvador Liniers","legajo": 21734,"notaparcial1":70,"notaparcial2":88,"notafinal": 89},
    ]
    lista_nombres_mas90 = [alumno["nombre_apellido"] for alumno in lista_estudiantes if alumno["notaparcial1"]>90 or alumno["notaparcial2"]>90 or alumno["notafinal"]>90]

    print("Lista de alumnos completa: ")
    for alumno in lista_estudiantes:
        print(alumno,"\n")

    print("Nombres de alumndos con notas mayores a 90: ", lista_nombres_mas90)

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

def Menu():
    clear_console()
    print("**************************************************")
    print("*               TRABAJO PRÁCTICO 3               *")    
    print("*Ingrese opción deseada:                         *")
    print("*1- Ejercicio 1                                  *")
    print("*2- Ejercicio 2                                  *")
    print("*3- Ejercicio 3                                  *")
    print("*4- Ejercicio 4                                  *")
    print("*5- Ejercicio 5                                  *")
    print("*6- Ejercicio 6                                  *")
    print("*7- Ejercicio 7                                  *")
    print("*8- Ejercicio 8                                  *")
    print("*9- Ejercicio 9                                  *")
    print("*10- Ejercicio 10                                *")
    print("*11- Ejercicio 11                                *")
    print("*Otro número- Salir                              *")
    print("**************************************************")

n = int(1)
while int(n)>0 and int(n)<12:
    Menu()
    n = input("Ingrese opción de menú: ")
    if n.isdigit():
        n = int(n)
        switch(n)
    else:
        print("Ingrese un número válido")
        n = int(1)