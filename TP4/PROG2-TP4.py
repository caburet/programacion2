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
        print("* 12. ejercicio 12                  *")
        print("* 13. ejercicio 13                  *")
        print("* 14. ejercicio 14                  *")
        print("* 15. ejercicio 15                  *")
        print("* 16. ejercicio 16                  *")
        print("* => SELECCIONE UNA OPCION:      <= *")
        print("*************************************")
        opcion = Es_Entero()
        if (opcion<0 or opcion>16):
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
            print("\tNOS VEMOS :), gracias por usar el programa")
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
        elif opcion == 11:
            Ej11()
        elif opcion == 12:
            Ej12()
        elif opcion == 13:
            Ej13()
        elif opcion == 14:
            Ej14()
        elif opcion == 15:
            Ej15()
        else:
            Ej16()


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


### EJERCICIO 1
def Ej1():
    print("1. Crea una función lambda que tome un número como argumento y devuelva su cuadrado.")
    
    # Escribir la función lambda y la asigno a una variable
    func = lambda x: x**2

    # Imprimir el resultado de aplicar la función lambda a 5
    print(f"El cuadrado de 5 es: {func(5)}")

### EJERCICIO 2
def Ej2():
    print("2. Crea una función lambda que tome dos números como argumentos y devuelva su suma.")

    # Escribir la función lambda y la asigno a una variable
    func = lambda x,y: x+y

    # Imprimir el resultado de aplicar la función lambda a 5 y 10
    print(f"La suma de 5 y 10 es: {func(5,10)}")

### EJERCICIO 3
def Ej3():
    print("3. Crea una función lambda que devuelva el mayor de dos números.")

    # Escribir la función lambda y la asigno a una variable
    func = lambda x,y: x if x>y else y

    # Imprimir el resultado de aplicar la función lambda a 5 y 10
    print(f"El mayor de 5 y 10 es: {func(5,10)}")

### EJERCICIO 4
def Ej4():
    print("4. A partir de una lista de números existente, crear una nueva lista incrementando en un 15% los valores originales usando map.")
    
    # Crear una lista de números
    lista_numeros = [1,2,3,4,5,6,7,8,9,10]

    # Crear una función lambda que incremente en un 15%
    func = lambda x: x*1.15

    # Aplicar la función lambda a la lista de números
    lista_incrementada = list(map(func,lista_numeros))

### EJERCICIO 5
def Ej5():
    print("5. Ordenar una lista de diccionarios por un elemento del diccionario. ej: ordenar por edad la siguiente lista:")
    personas = [{'nombre': 'Hector', 'edad': 27}, {'nombre': 'Juan', 'edad': 18}, {'nombre': 'Maria', 'edad': 32}, {'nombre': 'Pedro', 'edad': 21}, {'nombre': 'Ana', 'edad': 20}]
    print(personas)

    # Crear una función lambda que tome un diccionario y devuelva el valor de la llave 'edad'
    func = lambda x: x['edad']

    # Ordenar la lista de diccionarios por el valor de la llave 'edad'
    lista_ordenada = sorted(personas, key=func)

    # Imprimir la lista ordenada
    print(lista_ordenada)

### EJERCICIO 6
def Ej6():
    print("No hay ejercicio 6")

### EJERCICIO 7
def Ej7():
    print("7. Dada una lista con números, filtrar los números pares y devolverlos en una nueva lista.")

    # Crear una lista de números
    lista_numeros = [1,2,3,4,5,6,7,8,9,10]

    # Crear una función lambda que devuelva True si el número es par
    func = lambda x: x%2==0

    # Filtrar los números pares de la lista
    lista_pares = list(filter(func,lista_numeros))

    # Imprimir la lista de pares
    print(lista_pares)

### EJERCICIO 8
def Ej8():
    print("8. Dada una lista de temperaturas en grados celsius generar una nueva lista con las temperaturas expresadas en grados fahrenheit, la fórmula para convertir la temperatura es `°F=(°C*(9/5))+32`.")

    # Crear una lista de temperaturas en grados celsius
    lista_celsius = [10,20,30,40,50,60,70,80,90,100]

    # Crear una función lambda que devuelva la temperatura en grados fahrenheit
    func = lambda x: (x*(9/5))+32

    # Convertir las temperaturas de celsius a fahrenheit
    lista_fahrenheit = list(map(func,lista_celsius))

    # Imprimir la lista de temperaturas en grados fahrenheit
    print(lista_fahrenheit)

### EJERCICIO 9
def Ej9():
    print("9. Dada una lista de palabras, utiliza la función sorted con una función lambda para ordenar la lista de acuerdo a la longitud de las palabras.")

    # Crear una lista de palabras
    lista_palabras = ['hola','como','estas','?']
    
    # Crear una función lambda que devuelva la longitud de la palabra
    func = lambda x: len(x)

    # Ordenar la lista de palabras por longitud
    lista_ordenada = sorted(lista_palabras, key=func)

    # Imprimir la lista de palabras ordenada
    print(lista_ordenada)

### EJERCICIO 10
def Ej10():
    print("10. Dada una lista de palabras, generar una lista con las iniciales de cada palabra.")

    # Crear una lista de palabras
    lista_palabras = ['hola','como','estas','?']

    # Crear una función lambda que devuelva la primera letra de la palabra
    func = lambda x: x[0]

    # Obtener las iniciales de las palabras
    lista_iniciales = list(map(func,lista_palabras))

    # Imprimir la lista de iniciales
    print(lista_iniciales)

### EJERCICIO 11
def Ej11():
    print("11. Dada una lista de diccionarios con los alumnos y notas de un curso, calcular el promedio del curso. Puede usar una lista como la siguiente:")
    lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]
    print(lista_dic)

    # Crear una función lambda que tome un diccionario y devuelva el valor de la llave 'nota'
    func = lambda x: x['nota']

    # Obtener la lista de notas
    lista_notas = list(map(func,lista_dic))

    # Crear una funcion lambda que que sume los valores de la lista
    func2 = lambda x,y: x+y

    # Importo la función reduce del modulo functools
    from functools import reduce

    # Aplicar la funcion reduce a la lista de notas y calcular el promedio
    promedio = reduce(func2, lista_notas)/len(lista_notas)

    # Imprimir el promedio
    print(f"El promedio del curso es: {promedio}")

### EJERCICIO 12
def Ej12():
    print("No hay ejercicio 12")

### EJERCICIO 13
def Ej13():
    print("13. Encuentra el número mayor de una lista utilizando reduce.")

    # Crear una lista de números
    lista_numeros = [1,2,3,4,5,6,7,8,9,10]

    # Crear una función lambda que devuelva el mayor de dos números
    func = lambda x,y: x if x>y else y

    # Aplicar la función reduce a la lista de números y obtener el mayor
    from functools import reduce
    mayor = reduce(func,lista_numeros)

    # Imprimir el mayor
    print(f"El mayor de la lista es: {mayor}")

### EJERCICIO 14
def Ej14():
    print("14. Utilice reduce para concatenar una lista de cadenas en una sola cadena.")

    # Crear una lista de cadenas
    lista_cadenas = ['hola','como','estas','?']

    # Crear una función lambda que concatene dos cadenas
    func = lambda x,y: x+y

    # Aplicar la función reduce a la lista de cadenas y obtener la cadena concatenada
    from functools import reduce
    cadena_concatenada = reduce(func,lista_cadenas)

    # Imprimir la cadena concatenada
    print(f"La cadena concatenada es: {cadena_concatenada}")

### EJERCICIO 15
def Ej15():
    print("15. Filtrar una lista de diccionarios por una condición. Ej: filtrar la lista del punto 10 para obtener notas de los alumnos aprobados.")
    lista_dic = [{'nombre': 'Hector', 'nota': 70}, {'nombre': 'Juan', 'nota': 45}, {'nombre': 'Maria', 'nota': 75}, {'nombre': 'Pedro', 'nota': 80}, {'nombre': 'Ana', 'nota': 60},  {'nombre': 'Florencia', 'nota': 95}]

    # Crear una funcion lambda que tome el diccionario y devuelva el alumno aprobado
    func = lambda x: x['nota'] if x['nota']>=60 else None

    # Obtener la lista de los alumnos aprobados
    lista_aprobados = list(filter(func,lista_dic))

    # Imprimir la lista de alumnos aprobados
    print(lista_aprobados)

### EJERCICIO 16
def Ej16():
    print("16. Dada una lista de diccionarios con nombre, fecha de nacimiento, y teléfono, crear una nueva lista con los diccionarios de las personas que aún no cumplieron años respecto a la fecha actual del sistema, y esa lista ordenarla por la fecha de nacimiento de menor a mayor. Puede usar una lista como la siguiente:")
    # Importar datetime en Python significa importar un módulo llamado datetime 
    # que proporciona clases y funciones para trabajar con fechas y horas como 
    # objetos. Por ejemplo, se puede usar la clase datetime para obtener la fecha 
    # y hora actuales, o para crear objetos de fecha y hora a partir de cadenas 
    # de texto. También se puede usar la clase timedelta para representar diferencias 
    # entre objetos de fecha y hora, o para realizar operaciones aritméticas con 
    # ellos. El módulo datetime es parte de la biblioteca estándar de Python, por 
    # lo que no se necesita instalar nada adicional para usarlo. Para importar el 
    # módulo datetime, se puede usar la siguiente sintaxis: "import datetime"
    import datetime
    lista_alumnos = [{"nombre":"Joaquin", "fecha_nacimiento":datetime.date(1990, 7, 2), "telefono":"123456789"}, { "nombre":"Maria", "fecha_nacimiento":datetime.date(1995, 5, 16), "telefono":"123456789"}, { "nombre":"Pedro", "fecha_nacimiento":datetime.date(1992, 9, 12), "telefono":"123456789"}, { "nombre":"Ana", "fecha_nacimiento":datetime.date(1991, 9, 22), "telefono":"123456789"}, { "nombre":"Florencia", "fecha_nacimiento":datetime.date(1994, 12, 8), "telefono":"123456789"}, { "nombre":"Hector", "fecha_nacimiento":datetime.date(1993, 4, 4), "telefono":"123456789"}]

    # l método datetime.date.today () devuelve un objeto de tipo date que contiene 
    # el valor de la fecha actual. Por ejemplo, si hoy es el 24 de septiembre de 
    # 2023, el método devolvería un objeto que representa la fecha 2023-09-24. Se 
    # puede usar este método para obtener la fecha actual sin la hora, o para crear 
    # objetos de tipo date a partir de otros objetos de tipo datetime.
    fecha_actual = datetime.date.today() # Creando un objeto tipo date con la fecha actual
    print(fecha_actual) # Imprimiendo el objeto tipo date

    # Crear una list comprehension que filtre la lista de alumnos que no cumplieron años
    lista_alumnos_nueva = [alumno for alumno in lista_alumnos 
    # La condicion debe ir (variable.month y variable.day) y no (variable.day y variable.month)
    # Porque sino devolvera una lista vacia y no cuplira lo que queremos.
    if (fecha_actual.month, fecha_actual.day) < (alumno['fecha_nacimiento'].month, alumno['fecha_nacimiento'].day)]

    # Crear una funcion lambda que tome el diccionario y devuelva el menor de los alumnos
    func = lambda x: x["fecha_nacimiento"]

    # Ordenar la lista por la fecha de nacimiento de menor a mayor
    lista_ordenada = sorted(lista_alumnos_nueva, key=func)

    # Imprimir la lista ordenada
    print(lista_ordenada)

#### INICIO DEL PROGRAMA:
Inicio()