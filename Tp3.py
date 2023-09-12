from os import system
from functools import reduce
import os 
global separador
separador = "------------------------"

#Funciones extras
def numero_valido(texto):
    while True: 
        try:
            numero = int(input(texto))
            
            print(separador)
            return numero
        except ValueError:
            print(separador)
            print("Eso no es un número entero válido. Inténtalo de nuevo.")
            print(separador)

def obtener_num_mayor_0(texto):

    while True: 
        try:
            numero = int(input(texto))
            if numero > 0:
                print(separador)
                return numero
            else:
                print(separador)
                print("El numero tiene que ser mayor a 0")
                print(separador)
        except ValueError:
            print(separador)
            print("Eso no es un número entero válido. Inténtalo de nuevo.")
            print(separador)

#Ejercicio 1

def Ej_1():
    #1. Implemente una función que dada una lista de números, devuelva una nueva lista que contenga 
    #   el cuadrado de cada número utilizando list comprehensions.
    print("En este ejericio tiene que agregar la cantidad de numeros que queres ")
    print("y todos los numeros ingresados va ser elevado por 2")
    print(separador)

    texto_repeticion = "Ingrese la cantidad de numeros que quiere ingresar: "
    
    repeticion = obtener_num_mayor_0(texto_repeticion)
    lista = []
    lista = [numero_valido(f"Ingrese numero {i + 1}°: ") for i in range(repeticion)]
    
    lista_elevada = [num**2 for num in lista]
    
    print(f"La lista es: {lista_elevada}")
    
#Ejercicio 2
def devolver_nombre_largo(lista, longitud):

    lista_larga = [ nombre for nombre in lista if len(nombre) >= longitud]

    return lista_larga

def Ej_2():
    #2. Implemente una función que dada una lista de nombres, devuelva una nueva lista que contenga 
    #   solo los nombres que tengan una longitud mayor o igual a una cantidad de caracteres pasada 
    #   por parámetro, utilizando list comprehensions.

    texto = "Ingrese la cantidad nombres que quiere ingresar: "
    texto_longitud = "Ahora ingrese la longitud de caracteres que desea: "
    
    #Usuario ingresa la cantidad de nombres que quiere ingresar
    repeticion = obtener_num_mayor_0(texto)
    #Usuario ingresa los nombres en la lista 'lista_nombres'
    lista_nombres = [input(f"Ingrese el nombre {i + 1}°: ") for i in range(repeticion)]

    print(separador)
    #Usuario ingresa la longitud de caracteres
    longitud = obtener_num_mayor_0(texto_longitud)

    #funcion para obtener nombre mas largo 
    lista_largos = devolver_nombre_largo(lista_nombres, longitud)

    if len(lista_largos) > 0:
        print(f"Estos son los nombres con mas de {longitud} caracteres: {lista_largos}")
    else:
        print(f"No hay una palabra con mas de {longitud} carcteres")
        
#Ejercicio 3
def Ej_3():
    #3. Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas las líneas 
    #   líneas del archivo, utilizando list comprehensions.
    
    ruta = "datos.txt"
    archivo = open(ruta, "r")

    lista = [linea.strip() for linea in archivo ]

    print("Las lineas del archivo son: ")
    contador = 1
    for linea in lista:    
        print(f"La linea Nroº {contador} es: {linea}")


#Ejercicio 4
def primera_letra():
    
    while True:
        letra = input("Escriba la LETRA que comienze su palabra deseada: ")
        
        if len(letra) == 1:
            return letra.upper()
        else:
            print("Tiene que escribir una letra")
        
def Ej_4():
    #4. Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que 
    #   comienzan con una letra específica (por ejemplo, "a") indicada por el usuario, utilizando list comprehensions.

    definiciones = {
        "Adulto" : "Persona con mas de 18 anios",
        "Perro" : "Animal de 4 patas domesticado por el humano",
        "Ciudad" : "Poblacion donde habita un gran conjunto de personas",
        "Aplicacion" : "Un programa de software diseñado para realizar una tarea específica o brindar una funcionalidad específica.",   
        "Algoritmo" : "Un conjunto de instrucciones lógicas y bien definidas que resuelven un problema o realizan una tarea.",    
    }
    #Usuario carga que letra quiere que comience
    letra = primera_letra()

    # guarda a la lista las palabnras que empiezen con la letra elegida por el usuario 
    palabras_con_a = [palabra for palabra in definiciones if letra == palabra[0]]

    print(separador)

    longitud = len(palabras_con_a)
    #Muestra de resultados
    if longitud > 1: 
        print(f"Estas son las palabras que empiezan con la {letra}: {palabras_con_a}")

    elif longitud == 1:
        print(f"Esta esta es la unica palabra que empieza con la letra {letra}: {palabras_con_a}")

    else:
        print(f"No existe palabras que empieza con la letra {letra}")

#Ejercicio 5
def es_primo(num):
    
    for i in range(2,num):
        if num % i == 0:
            return False
    
    return True
def Ej_5():
    #5. Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango utilizando list comprehensions.
    texto = "Escriba un numero para saber si existe numeros primos entre el 2 hasta el numero deseado: "
    
    maximo = obtener_num_mayor_0(texto)
    
    #Creacion de lista con el rango de numeros dado por el usuario
    lista = list(range(2,maximo + 1))

    #Suma a la 'lista_primos' todo numero primo
    
    lista_primos = [numero for numero in lista if es_primo(numero)]
    
    #opcion usando 'filter
    #lista_primos = list(filter(es_primo, lista))
    
    #Resultado
    longitud = len(lista_primos)
    if longitud > 1:
        print(f"Estos son los numeros primos que hay entre el cero y el {maximo}: {lista_primos}")
    elif longitud == 1:
        print(f"Este es el unico numero primero que hay entre el cero y el {maximo}: {lista_primos}")

#Ejercicio 6


def Ej_6():
    #6. Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres de las personas 
    #   personas cuya edad es mayor a unaedad ingresada por el usuario, utilizando list comprehensions.
    personas = {
        "Carlos" : 10,
        "Pedro" : 65,
        "Juan" : 40,
        "Tevez" : 20,
        "Riquelme" : 25,
        "Gustavo" : 30,
    }

    edad = obtener_num_mayor_0("Escriba la edad minima de las personas que quiere visualizar: ")

    lista_mayores = [clave for clave in personas if edad < personas[clave] ]

    longitud = len(lista_mayores)
    if longitud > 1:
        print(f"Estas son las personas cuya edad es mayor a {edad}: {lista_mayores}")
    elif longitud ==1:
        print(f"Esta es la unica persona con la edad mayo a {edad}: {lista_mayores}")
    else:
        print("No existe una persona que tenga mayor edad que esa")

#Ejercicio 7

#Contar vocales forma basica
def contador_vocales(palabra):
    contador = 0
    for letra in palabra:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            contador += 1
    return contador

def Ej_7():
    #7. Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella. 
    #   El programa deberá pedirle palabras  al usuario hasta que éste introduzca la palabra “salir”.

    seguir = True
    
    while seguir:
        
        palabra = input("Escriba una palabra para ver cuantas vocales tiene, si quiere salir escriba 'salir': ").lower()
        print(separador)
        if palabra != "salir":
            
            #cant_vocales = contador_vocales(palabra)
            
            #funcion para saber si la letra es vocal
            es_vocal = lambda letra: letra in "aeiou"
            
            #filter para recorrer letra por letra y ver si es vocal, filter vuelve true o false, si es true se suma a la lista
            lista_vocales = list(filter(es_vocal, palabra))

            cant_vocales = len(lista_vocales)

            print(f"La cantidad de vocales que tiene la palabra es de: {cant_vocales}")
            print(separador)

        else:
            print("Saliendo...")
            seguir = False    
        
#Ejercicio 8 

def Ej_8():
    #8. Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los elementos únicos utilizando list comprehensions.

    lista = [2 ,1 ,4 ,2 ,2 , 5, 4, 1, 2, 3, 6, 3]

    #lista_unicos = list(set(lista))
    lista_unicos = []
    [lista_unicos.append(elem) for elem in lista if elem not in lista_unicos]
    
    print(lista_unicos)



def MainMenu():
    print("********************") 
    print("**  1 - Ejercicio **")
    print("**  2 - Ejercicio **")
    print("**  3 - Ejercicio **")
    print("**  4 - Ejercicio **")
    print("**  5 - Ejercicio **")
    print("**  6 - Ejercicio **")
    print("**  7 - Ejercicio **")
    print("**  8 - Ejercicio **")
    print("**  9 - Ejercicio **")
    print("** 10 - Ejercicio **")
    print("** 11 - Ejercicio **")   
    print("**  0 - Salir     **")
    print("********************")

#Main
sigue = True

while (sigue):

    MainMenu()
    opcion = input("Ingrese una opcion: ")
    print(separador)
    if opcion == "0":
        print("Saliendo...")
        sigue = False  

    elif opcion == "1":
        print("1 - Ejercicio")
        print(separador)
        Ej_1()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "2":
        print("2 - Ejercicio")
        print(separador)
        Ej_2()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "3":
        print("3 - Ejercicio")
        print(separador)
        Ej_3()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "4":
        print("4 - Ejercicio")
        print(separador)
        Ej_4()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    elif opcion == "5":
        print("5 - Ejercicio")
        print(separador)
        Ej_5()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    elif opcion == "6":
        print("6 - Ejercicio")
        print(separador)
        Ej_6()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    elif opcion == "7":
        print("7 - Ejercicio")
        print(separador)
        Ej_7()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    elif opcion == "8":
        print("8 - Ejercicio")
        print(separador)
        Ej_8()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")

    elif opcion == "9":
        print("9 - Ejercicio")
        print(separador)
        #Ej_9()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    else:
        print("Opcion incorrecta, pruebe de vuelta")
