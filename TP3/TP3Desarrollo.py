import os.path
import math

# Función para validar que un valor sea un número entero dentro de un rango
def validar_entero(valor, minimo, maximo):
    try:
        entero = int(valor)
        if entero < minimo or entero > maximo:
            raise ValueError
        return entero
    except ValueError:
        return None

def Menu():
    print("Menu de Ejercicios del TP1 de programacion II:")
    print("1 - Ejercicio 1.")
    print("2 - Ejercicio 2.")
    print("3 - Ejercicio 3.")
    print("4 - Ejercicio 4.")
    print("5 - Ejercicio 5.")
    print("6 - Ejercicio 6.")
    print("7 - Ejercicio 7.")
    print("8 - Ejercicio 8.")
    print("9 - Ejercicio 9.")
    print("10 - Ejercicio 10.")
    print("11 - Ejercicio 11.")
    print("12 - Salir del programa.")

    # Pedir al usuario que elija una opción
    opcion = input("Elija una opcion: ")

    # Validar la opcion elegida
    opcion = validar_entero(opcion, 1, 12)

    # Retornamos la opcion
    return opcion

def ejercicio1():
    # Inicializamos las lista con los numeros
    lista_oroginal = [1,2,3,4,5,6,7,8,9,10]

    # Utilizamos list comprenhensions
    lista_nueva = [elem**2 for elem in lista_oroginal]

    # Mostrar las listas
    print(f"Esta es la lista original: {lista_oroginal}")
    print()
    print(f"Esta es la lista nueva: {lista_nueva}")

def calcular_longitud(cadena):
    return len(cadena)

def añadir_nombres_largos(parametro,longitudes,lista_nombres_longitud_mayor__parametro):
    lista_nombres_longitud_mayor__parametro =[longitud for longitud in longitudes if longitud >= parametro]

    return lista_nombres_longitud_mayor__parametro

def diccionario_nombres_longitudes(lista_nombres_longitudes, lista_nombres, longitudes):
    for i in range(0, len(lista_nombres)):
        lista_nombres_longitudes[lista_nombres[i]] = longitudes[i]


def ejercicio2():
    parametro = 7

    global lista_nombres_longitud_mayor__parametro

    lista_nombres_longitud_mayor__parametro = []

    lista_nombres = ["Matias", "Eamanuel", "Coronel", "Dittler"]

    longitudes = list(map(calcular_longitud, lista_nombres))

    lista_nombres_longitud_mayor__parametro = añadir_nombres_largos(parametro,longitudes, lista_nombres_longitud_mayor__parametro)

    lista_nombres_longitudes = {}

    diccionario_nombres_longitudes(lista_nombres_longitudes, lista_nombres, longitudes)

    for nombre, longitud in lista_nombres_longitudes.items():
        if longitud in lista_nombres_longitud_mayor__parametro:
            print(f"Los nombres mayores al parametro 7 son: {nombre} : {longitud}")

def leer_archivo_con_strip():
    # Inicializamos la ruta del archivo
    ruta= r"C:/Users/matia/OneDrive/Documentos/datos.txt"

    try:
        # Intenta abrir el archivo en modo de lectura
        archivo = open(ruta, 'r')

        #Leemos las líneas y creamos una lista
        lineas = archivo.readlines()
        lista =[linea.strip() for linea in lineas]

        # Mostramos la lista
        print(lista)

        # Cerramos el archivo
        archivo.close()
    except FileNotFoundError:
        # Si el archivo no existe, imprime un mensaje de error
        print(f"El archivo con la ruta: {ruta} no existe")
    except IOError:
        # Si hay algún otro problema al abrir el archivo, imprime un mensaje de error
        print(f"No se pudo abrir el archivo con la ruta {ruta}")

def leer_archivo_con_split():
    # Inicializamos la ruta del archivo
    ruta= r"C:/Users/matia/OneDrive/Documentos/datos1.txt"

    try:
        # Intenta abrir el archivo en modo de lectura
        archivo = open(ruta, 'r')

        # Leemos las lineas
        lineas = archivo.readlines()

        # Usa list comprehension para crear una nueva lista con los nombres
        # Usa el método split para dividir cada línea por el salto de línea y obtener el nombre
        lista =[nombre for linea in lineas for nombre in linea.split(",")]

        # Mostramos la lista
        print(lista)

        # Cerramos el archivo
        archivo.close()
    except FileNotFoundError:
        # Si el archivo no existe, imprime un mensaje de error
        print(f"El archivo con la ruta: {ruta} no existe")
    except IOError:
        # Si hay algún otro problema al abrir el archivo, imprime un mensaje de error
        print(f"No se pudo abrir el archivo con la ruta {ruta}")

def ejercicio3():
    # Llammamos a las funciones
    leer_archivo_con_strip()
    print()
    leer_archivo_con_split()

def leer_letra(letra):
    # Pedimos al usuario que ingrese una letra
    letra = input("Ingrese una letra para guardar las palabras que comiencen con esa letra: ")

    # Convertimos la letra a minúscula
    letra = letra.lower()

    # Repetimos en caso de que sea una letra y sea un solo caracter
    while not (letra.isalpha() and len(letra) == 1):
        # Imprime un mensaje de error
        print()
        print("El dato ingresado no es una letra, vuelva a ingresar un dato correcto.")
        print()
        # Pide al usuario que ingrese otra letra
        letra = input("Ingrese una letra para guardar las palabras que comiencen con esa letra: ")
        
        # Convertimos la letra a minúscula
        letra = letra.lower()

    # Retornamos una letra en caso de que el dato sea correcto
    return letra


def ejercicio4():
    # Inicializamos el diccionario y las variables
    diccionario = {"algoritmo":"Conjunto ordenado y finito de operaciones que permite hallar la solución de un problema.", "bit":"Unidad mínima de información que puede tomar dos valores: 0 o 1.","codigo":"Conjunto de símbolos y reglas que se utilizan para representar datos o instrucciones.","dato":"Representación simbólica de un hecho, concepto o entidad.","estructura":"Forma de organizar y relacionar los datos en un programa."}
    letra = None

    # Llamamos a la funcion
    letra = leer_letra(letra)

    # Asignamos a la lista las palabras que empiecen con esa letra con list comprehension
    lista = [palabra for palabra, definicion in diccionario.items() if palabra.startswith(letra)]

    # Mostramos la lista con las palabras que comiencen con la letra ingresada
    print(lista)

def es_primo(num):
    # Si num es menor o igual que 1, no es primo
    if num <= 1:
        return False
    
    # Si el num es 2, es primo
    if num == 2:
        return True
    
    # Si el número es par, no es primo
    if num % 2 == 0:
        return False
    
    # Comprueba si hay algún divisor desde 3 hasta la raíz cuadrada del número
    limite = int(math.sqrt(num)) + 1

    for i in range(3, limite, 2):
        if num % i == 0:
            return False
        
    # Si no se encuentra ningún divisor, el número es primo
    return True

def validar_ent(valor):
    # Validamos que sea un entero
    try:
        entero = int(valor)

        if entero <= 0:
            raise ValueError
        
        return entero
    except ValueError:
        return None
    
def leer_inicio(num):
    # Pedimos al usuario que ingrese un numero
    while num is None:
        num = input("Ingrese el inicio del rango: ")

        num = validar_ent(num)

        print()

        if num is None:
            print("Error: Debe introducir un numero valido.")
            print()

    return num

def leer_fin(num):
    # Pedimos al usuario que ingrese un numero
    while num is None:
        num = input("Ingrese el fin del rango: ")

        num = validar_ent(num)

        print()

        if num is None:
            print("Error: Debe introducir un numero valido.")
            print()

    return num

def ejercicio5():
    # Inicializamos las variables
    inicio = None
    fin = None

    # Llamamos a las funciones
    inicio = leer_inicio(inicio)
    fin = leer_fin(fin)

    # Asignamos los numeros a la lista con list comprehension
    lista = [num for num in range(inicio, fin + 1) if es_primo(num)]

    # Mostramos la lista
    print(lista)

def ingrese_edad_minima(edad_minima):
     # Pedimos al usuario que ingrese un numero
    while edad_minima is None:
        edad_minima = input("Ingrese la edad minima: ")

        edad_minima = validar_ent(edad_minima)

        print()

        if edad_minima is None:
            print("Error: Debe introducir un numero valido.")
            print()

    return edad_minima

def ejercicio6():
    # Inicializamos el diccionario y la variable
    diccionario = {"Matias": 23, "Uma": 13, "Matina": 12, "Nora": 69}
    edad_minima = None

    # Llamamos a la funcion
    edad_minima = ingrese_edad_minima(edad_minima)

    # Asignamos las edades a la lista usando list comprehension
    lista = [nombre for nombre, edad in diccionario.items() if edad > edad_minima]

    # Mostramos la lista
    print(lista)

def leer_palabra(palabra):
    # Pedimos al usuario que ingrese una palabra
    palabra = input("Ingrese una palabra para contar la cantidad de vocales (ingrese salir para salir del programa): ")

    # Convertimos la palabra a minúscula
    palabra = palabra.lower()

    # Repetimos en caso de que sea una palabra y sea un solo caracter
    while not palabra.isalpha():
        # Imprime un mensaje de error
        print()
        print("El dato ingresado no es una palabra, vuelva a ingresar un dato correcto.")
        print()
        # Pide al usuario que ingrese otra palabra
        palabra = input("Ingrese una palabra para contar la cantidad de vocales: ")
        
        # Convertimos la palabra a minúscula
        palabra = palabra.lower()

    # Retornamos una palabra en caso de que el dato sea correcto
    return palabra

def contar_vocales(palabra, total):
    # Obetenemos la longitud de la palabra
    longitud = len(palabra)

    # Iteramos letra por letra en la palabra
    for letra in palabra:
        # Si la letra es igual a la vocal, asignamos 1 a total
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            total += 1

    # Retornamos el total
    return total

def ejercicio7():
    # Inicializamos las variables
    palabra = None
    total = 0

    # Repetimos hasta que palabra sea igual salir
    while palabra != 'salir':
            # Asignamos la palabra ingresada a la variable
            palabra = leer_palabra(palabra)

            print()

            # Convertimos la palabra en minusculas
            palabra = palabra.lower()

            # Si la palabra es distinta a salir
            if palabra != 'salir':
                # Asignamos la cantidad de vocales que tiene
                total = contar_vocales(palabra, total)

                # Mostramaos la cantidad de vocales que tiene la palabra ingresada
                print(f"La palabra: {palabra}, tiene un total de {total} vocales.")
                print()

            # Si la palabra es igual a salir, frenamamos la ejecucion del bucle
            else:
                break

def ejercicio8():
    # Inicializamos la lista con los numeros repetidos
    lista_num = [1,2,3,4,5,1,2,3,4,5]

    #Utilizamos list comprehensions para obtener una nueva lista con elementos sin repetir con set()
    lista_num_sin_repetidos = [elemento for elemento in set(lista_num)]

    # Mostramos las dos listas
    print(lista_num)
    print()
    print(lista_num_sin_repetidos)

def ejercicio9():
    # Inicializamos las listas
    lista1 = [1,2,3,4,5]
    lista2 = [6,7,8,9,10]

    # Creamos la lista con el resultado de la multiplicacion de los numeros de las dos listas con list comprehensions
    lista_multiplicada = [elemento1 * elemento2 for elemento1 in lista1 for elemento2 in lista2 if lista1.index(elemento1) == lista2.index(elemento2)]

    # Mostramos las listas
    print(lista1)
    print()
    print(lista2)
    print()
    print(lista_multiplicada)


def ejercicio10():
    # Inicilizamos la lista
    lista = [1,2,3,4,5,6,7,8,9,10]

    # Creamos las dos listas de numeros pares e impares con list comprehensions 
    lista_num_pares = [elemento for elemento in lista if elemento % 2 == 0]
    lista_num_impares = [elemento for elemento in lista if elemento % 2 != 0]

    # Mostramos las listas 
    print(lista)
    print()
    print(lista_num_pares)
    print()
    print(lista_num_impares)

def ejercicio11():
    # Inicalizamos la lista de diccionarios
    # Supongamos que tenemos una lista de diccionarios llamada estudiantes
    estudiantes = [
        {"nombre_apellido": "Juan Pérez", "legajo": 1234, "nota_parcial1": 85, "nota_parcial2": 92, "nota_final": 88},
        {"nombre_apellido": "María García", "legajo": 2345, "nota_parcial1": 91, "nota_parcial2": 89, "nota_final": 90},
        {"nombre_apellido": "Pedro López", "legajo": 3456, "nota_parcial1": 87, "nota_parcial2": 86, "nota_final": 93},
        {"nombre_apellido": "Ana Rodríguez", "legajo": 4567, "nota_parcial1": 95, "nota_parcial2": 94, "nota_final": 96}
    ]
    
    # Usamos una list comprehension para filtrar los nombres de los estudiantes que cumplen la condición
    nombres = [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] > 90 or estudiante["nota_parcial2"] > 90 or estudiante["nota_final"] > 90]

    # Imprimimos el diccionario y la lista
    print(estudiantes)
    print()
    print(nombres)

# Asignamos el valor a la opcion
op = Menu()

# Mientras op no sea valida o no sea la de salir
while op is None or op != 12:
    if op is None:
        # Mostrar mensaje de error
        print()
        print("Error: Debes introducir un numero entero entre 1 y 10")
        print()
    elif op == 1:
        print()
        ejercicio1()
        print()
    elif op == 2:
        print()
        ejercicio2()
        print()
    elif op == 3:
        print()
        ejercicio3()
        print()
    elif op == 4:
        print()
        ejercicio4()
        print()
    elif op == 5:
        print()
        ejercicio5()
        print()
    elif op == 6:
        print()
        ejercicio6()
        print()
    elif op == 7:
        print()
        ejercicio7()
        print()
    elif op == 8:
        print()
        ejercicio8()
        print()
    elif op == 9:
        print()
        ejercicio9()
        print()
    elif op == 10:
        print()
        ejercicio10()
        print()
    elif op == 11:
        print()
        ejercicio11()
        print()

    # Volver a mostar el menu de opciones
    op = Menu()

# Si la opcion es la de salir
# Mostrar un mensaje de despedida
print()
print("Gracias por usar el programa. Hasta pronto.")