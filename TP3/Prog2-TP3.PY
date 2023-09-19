### PARTE DEL INICIO Y EL MENU
def Menu():
    repetir = True
    while repetir:
        print("************** Menu *****************")
        print("* 0. salir                          *")
        print("* 1. ejercicio 1                    *")
        print("* 2. ejercicio 2                    *")
        print("* 3. ejercicio 3                    *")
        print("* 4. ejercicio 4                    *")
        print("* 5. ejercicio 5                    *")
        print("* 6. ejercicio 6                    *")
        print("* 7. ejercicio 7                    *")
        print("* 8. ejercicio 8                    *")
        print("* 9. ejercicio 9                    *")
        print("* 9. ejercicio 9                    *")
        print("* 10. ejercicio 10                  *")
        print("* 11. ejercicio 11                  *")
        print("* => SELECCIONE UNA OPCION:      <= *")
        print("*************************************")
        opcion = Es_Entero()
        if (opcion<0 or opcion>11):
            print("la opcion ingresada debe estar entre 0 y 11, intente de nuevo...")
        else:
            repetir=False
            
    return opcion 



def Inicio():            ### INICIO DE ENTRADA, SELECION DE EJERCICIOS
    repetir=True
    while repetir:
        print("\tBIENVENIDO AL TRABAJO N°3 DE PROG2\n")
        opcion = Menu()
        if(opcion==0):
            print("\tNOS VEMOS :)")
            repetir = False
        elif (opcion==1):
            Ej1()
        elif (opcion==2):
            Ej2()
        elif opcion==3:
            Ej3()
        elif opcion==4:
            Ej4()
        elif opcion == 5:
            Ej5()
        elif opcion == 6:
            Ej6()
        elif opcion == 7:
            Ej7()
        elif opcion == 8:
            Ej8()
        elif opcion == 9:
            Ej9()
        elif opcion == 10:
            Ej10()
        else:
            Ej11() 


### funciones
def Es_Entero(): ## VALIDA NUMEROS ENTEROS
    while True:
        try:
            num=int(input("ingrese un numero entero: "))
            break
        except ValueError:
            print("ups!!!, acurrio un error, intentelo de nuevo...")
    return num   

def Es_real(): ## validacion de numeros reales
    while True:
        try:
            num=float(input("ingrese un numero: "))
            break
        except ValueError:
            print("ups!!!, acurrio un error, intentelo de nuevo...")
    return num 

def Lista_x2(lista_numeros): ### EJERCICIO 1
    # Devuelve una lista con sus elementos al cuadrado
    lista_nueva = [elementos**2 for elementos in lista_numeros]
    return lista_nueva

def Lista_Longitud_Caracteres(lista, CantidadCaracter): ### EJERCICIO 2
    # Devuelve una lista con los valores mayores o iguales a (CantidadCaracter)
    lista_nombres_MoI_a_cantidad_caracteres = [nombresMoI for nombresMoI in lista if nombresMoI == CantidadCaracter]
    return lista_nombres_MoI_a_cantidad_caracteres

def Es_Primo(num): ### ejercicio 5. funcion para buscar los primos
    # si el numero es menor a 2 no es primo
    if num < 2:
        return False
    else:
        # int elimina la parte decimal del num
        for i in range(2, int(num*0.5) + 1):
            # pruebo con los divisores desde 2 hasta la raiz cuadrada
            if num % i == 0:
                # si el numero es divicible x algun divisor no es primo
                return False
        return True # si no se encontro ningun divisor
    
def Contar_Vocales(palabra): ### ejercicio 7
    # defino una variable con las vocales
    vocales = "aeiou"
    # filtro las vocales
    vocales_en_palabra = filter(lambda letra: letra in vocales, palabra)
    # Usé len(list()) porque la función filter devuelve un objeto que es 
    # iterable, pero no tiene una longitud definida. Para obtener la 
    # cantidad de elementos que hay en ese objeto, hay que convertirlo en 
    # una lista y luego usar la función len
    return len(list(vocales_en_palabra))

def Lista_elementos_unicos(lista): ### ejercicio 8
    # inicializo una lista nueva
    # comparo elementos si no esta en la lista nueva lo agrego
    lista_elemUnicos = [elemento for elemento in lista if not(elemento in lista_elemUnicos)]
    return lista_elemUnicos


### EJERCICIOS:

### EJERCICIO 1
def Ej1():
    print("El ejercicio 1 es una funcion que devuelve una lista con sus elementos al cuadrado")

### EJERCICIO 2
def Ej2():
    print("2. Implemente una función que dada una lista de nombres, devuelva una nueva lista que contenga solo los nombres que tengan una longitud mayor o igual a una cantidad de caracteres pasada por parámetro, utilizando list comprehensions")

### EJERCICIO 3
def Ej3():
    print("3. Lee el contenido de un archivo de texto llamado 'datos.txt' y crea una lista con todas las líneas del archivo, utilizando list comprehensions.")
    # Abro el archivo en modo lectura
    archivo = open("datos.txt", "r")
    # Agrego las lineas del archivo a la lista "elijo creer XD"
    lista = [linea for linea in archivo]
    archivo.close()

### EJERCICIO 4
def Ej4():
    print("4. Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo las palabras que comienzan con una letra específica (por ejemplo, 'a') indicada por el usuario, utilizando list comprehensions.")
    # Inicializo un diccionario con valores ya cargado
    diccionario = {
    "python": "Lenguaje de programación interpretado, de alto nivel y propósito general",
    "diccionario": "Colección de palabras o términos con sus respectivos significados"
    }
    # Pido al usuario que ingrese una letra
    letra = input("Ingrese una letra: ")
    # recorro las llaves del diccionario y buco el que empiece con la letra ingresada
    # llave recorre las 'llaves' del diccionario, el if ve si llave[0](es la primera letra de la llave)
    # es igual a la letra
    lista_nombres = [llave for llave in diccionario if llave[0] == letra]
    # muestro la lista
    print(lista_nombres)

### EJERCICIO 5
def Ej5():
    print("5. Dado un rango de números, crea una lista que contenga todos los números primos dentro de ese rango utilizando list comprehensions.")
    # defino el inicio y el fin del rango
    inicio = 1
    fin = 50
    # recorro desde inicio hasta fin mas 1
    lista_rangos = [num for num in range(inicio, fin + 1) if Es_Primo(num)]
    print(lista_rangos)

### EJERCICIO 6
def Ej6():
    print("6. Dado un diccionario de personas y sus edades, crea una lista que contenga solo los nombres de las personas cuya edad es mayor a una edad ingresada por el usuario, utilizando list comprehensions. ")
    # Inicializo el diccionario con valores cargados
    personas = {
        "Miqueas": 19,
        "Gonzales": 2,
        "Pelon": 50
    }
    # Pido al usuario una edad
    print("Ingrese una edad:")
    # Valido q ingrese un numero entero
    edad_in = Es_Entero()
    # recorro el diccionario de forma q las llaves se guarden en nombres y las edades en edad y a este
    # la comparo con la edad ingresada
    lista_mayor_edadIN = [nombres for nombres, edad in personas.items() if edad > edad_in]
    print(lista_mayor_edadIN)

### EJERCICIO 7
def Ej7():
    print("7. Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra “salir”.")
    repetir = True
    while repetir:
        # inicio un bucle q se repetira hasta que el usuario ingrese la palabra "salir"
        palabra = input("ingrese una palabra, escriba salir para terminar el programa:")
        palabra = palabra.lower()# convierto la palabra en minuscula
        if palabra == "salir":
            repetir = False # termina el bucle
        else:
            # muestra la cantidad de vocales de la palabra ingresada
            print(f"la palabra {palabra} tiene {Contar_Vocales(palabra)} vocales")

### EJERCICIO 8
def Ej8():
    print("8. Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los elementos únicos utilizando list comprehensions.")
    lista_duplicada = ["hola", "hola", "no","no", "si", "si"]
    print(f"lista original: {lista_duplicada}, lista con elementos unicos: {Lista_elementos_unicos(lista_duplicada)}")
    

### EJERCICIO 9
def Ej9():
    print("9. Dadas dos listas de números del mismo tamaño, crea una nueva lista que contenga la multiplicación de los elementos correspondientes de ambas listas utilizando list comprehensions.")
    lista1 = [2, 3, 4, 5]
    lista2 = [2, 3, 4, 5]
    # genero una variable q contenga el rango da la lista
    rango = range(len(lista1))
    # ese rango va a ser mi tope en el for, y luego multiplico elementos
    lista_multiplicacion = [lista1[i]*lista2[i] for i in rango]
    print(lista_multiplicacion)

### EJERCICIO 10
def Ej10():
    print("10. Dada una lista de números, crea dos listas separadas: una que contenga los números pares y otra que contenga los números impares utilizando list comprehensions.")
    lista_numeros = [1, 2, 3, 4, 5, 6]
    # mi solucion para este ejercicio fue hacer dos list comprehensions
    lista_impar = [elem for elem in lista_numeros if elem % 2 == 0]
    lista_par = [elem for elem in lista_numeros if elem % 2 != 0]
    print(f"impares: {lista_impar}, pares: {lista_par}")

### EJERCICIO 11
def Ej11():
    print("11. Dada una lista de diccionarios que contienen información de estudiantes de una materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final), crea una lista que contenga los nombres de todos los estudiantes que han obtenido una calificación superior a 90 en al menos un examen utilizando list comprehensions.")
    # Supongamos que tenemos una lista de diccionarios llamada estudiantes
    estudiantes = [
        {"nombre_apellido": "Juan Perez", "legajo": 1234, "nota_parcial1": 85, "nota_parcial2": 92, "nota_final": 88},
        {"nombre_apellido": "María Garcia", "legajo": 5678, "nota_parcial1": 91, "nota_parcial2": 89, "nota_final": 90},
        {"nombre_apellido": "Pedro Lopez", "legajo": 9012, "nota_parcial1": 87, "nota_parcial2": 86, "nota_final": 93},
        {"nombre_apellido": "Ana Rodriguez", "legajo": 3456, "nota_parcial1": 94, "nota_parcial2": 95, "nota_final": 96}
    ]

    # Filtro los estudiantes que cumplen la condicion
    lista_estudiantes = [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] > 90 or estudiante["nota_parcial2"] > 90 or estudiante["nota_final"] > 90]

    print(lista_estudiantes)


#### INICIO DEL PROGRAMA:
Inicio()