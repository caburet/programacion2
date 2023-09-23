from os import system
from functools import reduce
import os 
import datetime
global separador
separador = "------------------------"

#Funciones extras

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
    print("** 12 - Ejercicio **")   
    print("** 13 - Ejercicio **")   
    print("** 14 - Ejercicio **")   
    print("**  0 - Salir     **")
    print("********************")

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

def Ej_1():
    #1. Crea una función lambda que tome un número como argumento y devuelva su cuadrado. 
    texto = "Escriba el numero que quiere elevar al cuadrado: "
    
    cuadrado = lambda x: x**2

    print("Bienvenido al ejercicio 1, donde calcularemos el cuadrado de un numero usando funciones lambda")
    print(separador)

    numero = numero_valido(texto)

    print(f"El numero {numero} al cuadrado es: {cuadrado(numero)}")

def Ej_2():
    #2. Crea una función lambda que tome dos números como argumentos y devuelva su suma.
    
    texto_1 = "Escriba el primer numero: "
    texto_2 = "Escriba el segundo numero: "

    suma = lambda x, y: x + y

    print("Bienvenido al ejercicio 2, donde calcularemos la suma de dos numeros usando funciones lambda")
    print(separador)

    numero_1 = numero_valido(texto_1)
    numero_2 = numero_valido(texto_2)

    print(f"La suma de los dos numeros es de {suma(numero_1,numero_2)}")

def Ej_3():
    #3. Crea una función lambda que devuelva el mayor de dos números.

    texto_1 = "Escriba el primer numero: "
    texto_2 = "Escriba el segundo numero: "

    mayor = lambda num1,num2: num1 if num1 > num2 else num2
    
    print("Bienvenido al ejercicio 3, donde calcularemos el mayor de dos numeros usando funciones lambda")
    print(separador)

    numero_1 = numero_valido(texto_1)
    numero_2 = numero_valido(texto_2)

    print(f"El mayor entre {numero_1} y {numero_2} es: {mayor(numero_1,numero_2)}")

def Ej_4():
    #4. A partir de una lista de números existente, crear una nueva lista incrementando en un 15% los valores originales usando map.

    lista = [2, 4, 1, 2, 62, 45, 10]

    lista_aux = list(map(lambda x: x * 1.15, lista))

    lista_incrementada = list(map(lambda x: round(x, 2), lista_aux))

    print("Bienvenido al ejercicio 4, donde incrementaremos los valores de una lista en un 15% usando map y lambda")
    print(separador)

    print(f"La lista original es: {lista}")

    print(f"La lista con un incremento del 15% es: {lista_incrementada}")

def Ej_5():
    #5. Ordenar una lista de diccionarios por un elemento del diccionario. ej: ordenar por edad la siguiente lista: 

    personas = [
        {'nombre': 'Hector', 'edad': 27}, 
        {'nombre': 'Juan', 'edad': 18}, 
        {'nombre': 'Maria', 'edad': 32}, 
        {'nombre': 'Pedro', 'edad': 21}, 
        {'nombre': 'Ana', 'edad': 20}
    ]
    print("Bienvenido al ejercicio 5, donde ordenaremos una lista de diccionarios por el elemento 'edad'")
    print(separador)

    print(f"La lista orignial es: {personas}")
    print()
    print(f"La lista ordenada por edad es: {sorted(personas, key=lambda x: x['edad'])}")

def Ej_6():
    #6. Dada una lista con números, filtrar los números pares y devolverlos en una nueva lista.
    print("Bienvenido al ejercicio 6, donde filtraré los numeros pares ingresados en una lista")
    print(separador)

    cantidad = obtener_num_mayor_0("Escribe la cantidad de numero que quiere ingresar: ")

    lista = []
    for i in range(cantidad):
        lista.append(numero_valido(f"Ingrese el numero {i + 1}: "))


    lista_pares = list(filter(lambda x: x % 2 == 0, lista))

    print(f"La lista que ingresaste es de: {lista}")
    print(f"La lista de numeros pares es: {lista_pares}")

def Ej_7():
    #7. Dada una lista de temperaturas en grados celsius generar una nueva lista con las temperaturas 
    #   expresadas en grados fahrenheit, la fórmula para convertir la temperatura es `°F=(°C*(9/5))+32`.
    #68, 72, 75, 80, 62, 70, 78
    print("Bienvenidos al ejercicio 7, comvertiremos grados Celsius a grados Fahrenheit usando map y lambda")
    print(separador)
    grados_celsius = [20, 22, 24, 27, 17, 21, 26]
    
    grados_fahrenheit = list(map(lambda x: (x*9/5) + 32, grados_celsius))

    print(f"Los grados celsius serian: {grados_celsius}")
    print(f"Los grados fajrenjeit seria: {grados_fahrenheit}")


def Ej_8():
    #8. Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar 
    #   la lista de acuerdo a la longitud de las palabras.
    print("Bienvenidos al ejercicio 8, donde ordenaremos una lista de palabras por la longitud de cada palabra que esta en la lista")
    print(separador)
    lista = ["hola" , "carlitos" , "JA" , "jajajaja" , "weyland" , "boca"]

    lista_ordenada = sorted(lista, key= lambda palabra: len(palabra))

    print(f"La lista original es: {lista}")
    print(f"La lista ordenada es: {lista_ordenada}")

def Ej_9():
    #9. Dada una lista de palabras, generar una lista con las iniciales de cada palabra.
    print("Bienvenido al ejericio 9, donde guardaremos en una lista con las iniciales de las palabras que hay en una lista")
    print(separador)
    lista = ["hola" , "carlitos" , "JA" , "jajajaja" , "weyland" , "boca"]

    lista_iniciales = list(map(lambda x: x[0], lista))

    print(f"La lista con las palabras es: {lista}")
    print(f"La lista con las iniciales es: {lista_iniciales}")

def Ej_10():
    #10. Dada una lista de diccionarios con los alumnos y notas de un curso, calcular el 
    #    promedio del curso. Puede usar una lista como la siguiente: 
    lista_dic = [
        {'nombre': 'Hector', 'nota': 70}, 
        {'nombre': 'Juan', 'nota': 45}, 
        {'nombre': 'Pedro', 'nota': 80}, 
        {'nombre': 'Ana', 'nota': 60},  
        {'nombre': 'Florencia', 'nota': 95}
    ]
    print("Bienvenido al ejercicio 10, donde calcularemos el promedio de notas de un curso usando reduce")
    print(separador)
    #La x es donde se va ir sumando (x empieza valor cero dado por el tercer argumento)
    #y la 'y' es la nota que va iterando de la lista

    suma = reduce(lambda x, y: x + y["nota"], lista_dic,0)
    
    promedio = suma / len(lista_dic)

    print(f"El promdio del curso es de {promedio}")

def Ej_11():
    #11. Encuentra el número mayor de una lista utilizando reduce.

    print("Bienvendio al ejercicio 11, donde encontraremos el numero mayor de una lista utilizando reduce")
    print(separador)
    lista = [1, 4, 2, 1, 2, 5, 7, 4]

    num_mayor = reduce(lambda x, y: x if x > y else y, lista)

    print(f"La lista es: {lista}")
    print(f"El numero mas grande de la lista es: {num_mayor}")

def Ej_12():
    #12. Utilice reduce para concatenar una lista de cadenas en una sola cadena
    lista = ["Hola,", "soy,", "Pedro,", "Weyland,", "y,", "tengo,", "19,", "años" ]
    

    print("Bienvenido al ejercicio 12, donde concatenaremos las cadenas de una lista usando reduce ")
    print(separador)

    aux = reduce(lambda x,y: x + y, lista)
    palabra = aux.replace(",", " ")

    print(f"La lista completa seria {lista}")
    print(f"Y esta seria la cadena completa: '{palabra}'")

def Ej_13():
    #13. Filtrar una lista de diccionarios por una condición. 
    #    Ej: filtrar la lista del punto 10 para obtener notas de los alumnos aprobados.
    
    
    lista_dic = [
            {'nombre': 'Hector', 'nota': 70}, 
            {'nombre': 'Juan', 'nota': 45}, 
            {'nombre': 'Pedro', 'nota': 80}, 
            {'nombre': 'Ana', 'nota': 60},  
            {'nombre': 'Florencia', 'nota': 95}
        ]
    
    aprobados = list(filter(lambda x: x["nota"] >= 60, lista_dic))

    print(f"Estas son las notas aprobadas {aprobados} ")

def Ej_14():
    #14. Dada una lista de diccionarios con nombre, fecha de nacimiento, y teléfono, 
    #    crear una nueva lista con los diccionarios de las personas que aún no cumplieron años 
    #    respecto a la fecha actual del sistema, y esa lista ordenarla por la fecha de nacimiento de menor a mayor. 
    #    Puede usar una lista como la siguiente:
    lista_alumnos = [
        {"nombre":"Joaquin", "fecha_nacimiento":datetime.date(1990, 7, 2), "telefono":"123456789"}, 
        { "nombre":"Maria", "fecha_nacimiento":datetime.date(1995, 5, 16), "telefono":"123456789"}, 
        { "nombre":"Pedro", "fecha_nacimiento":datetime.date(1992, 9, 12), "telefono":"123456789"}, 
        { "nombre":"Ana", "fecha_nacimiento":datetime.date(1991, 9, 22), "telefono":"123456789"}, 
        { "nombre":"Florencia", "fecha_nacimiento":datetime.date(1994, 12, 8), "telefono":"123456789"}, 
        { "nombre":"Hector", "fecha_nacimiento":datetime.date(1993, 4, 4), "telefono":"123456789"}
    ]

    



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
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "5":
        print("5 - Ejercicio")
        print(separador)
        Ej_5()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "6":
        print("6 - Ejercicio")
        print(separador)
        Ej_6()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "7":
        print("7 - Ejercicio")
        print(separador)
        Ej_7()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "8":
        print("8 - Ejercicio")
        print(separador)
        Ej_8()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    elif opcion == "9":
        print("9 - Ejercicio")
        print(separador)
        Ej_9()
        print(separador)
        #system("pause")
        #system("cls")
        input("Presione Enter para continuar")
        os.system("clear")
    elif opcion == "10":
        print("10 - Ejercicio")
        print(separador)
        Ej_10()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "11":
        print("11 - Ejercicio")
        print(separador)
        Ej_11()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "12":
        print("12 - Ejercicio")
        print(separador)
        Ej_12()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "13":
        print("13 - Ejercicio")
        print(separador)
        Ej_13()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")
    elif opcion == "14":
        print("14 - Ejercicio")
        print(separador)
        #Ej_14()
        print(separador)
        system("pause")
        system("cls")
        #input("Presione Enter para continuar")
        #os.system("clear")

    else:
        print("Opcion incorrecta, pruebe de vuelta")
