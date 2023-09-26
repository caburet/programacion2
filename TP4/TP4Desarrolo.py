# De la libreria functools importamos reduce
from functools import reduce
# Importamos la libreria datetime
import datetime

# Funcion para validar numeros enteros
def validar_entero(valor, min, max):
    try:
        # Asignamos el valor enetero a la variable
        entero = int(valor)

        # Si el entero es menor que el minimo o mayor que el maximo
        if entero < min or entero > max:
            # Controlo el error
            raise ValueError
        # Retorno el entero
        return entero
    except ValueError:
        # Manejo la excepcion y retorno None
        return None
    
def menu():
    # Mostramos las opciones del menu
    print("Menu de Ejercicios del TP4 de Programacion II.")
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
    print("12 - Ejercicio 12.")
    print("13 - Ejercicio 13.")
    print("14 - Ejercicio 14.")
    print("15 - Salir del programa.")

    # Pedimos al usuario que elija ina opcion
    op = input("Elija una opcion: ")

    # Validamos que la opcion ingresada sea correcta
    op = validar_entero(op, 1, 15)

    # Retornamos la opcion
    return op

# Funcion para validar real
def validar_real(num):
    try:
        # Asignamos el numero real a la variabla
        real = float(num)

        # Retonamos real
        return real
    except ValueError:
        # Manejo la excepcion y retorno None
        return None

# Funcio para ingressar un numero real
def ingresar_num_real():
    # Inicializamos la varibale
    num = None

    # Repetimos en caso de que no sea un numero
    while num is None:
        # Pedimos al usaurio que ingrese un numero
        num = input("Ingrese un numero: ")

        # Validamos el nume
        num = validar_real(num)

        print()

        # Si no es num
        if num is None:
            # Mostramos un mensaje de error
            print("Error: Debe introducir un numero valido.")
            print()

    # Retornamos el numero valido
    return num
        
def ejercicio1():
    # Mostramos un mensaje en pantalla
    print("En el siguiente renglon ingrese un numero real para calcular su cuadrado.")
    print()

    # Asignamos el numero que ingreso el usuario a la variable
    numero = ingresar_num_real()

    # Creamos la funcion lambda del cuadrado de un numero
    cuadrado_de_un_numero = lambda x: x ** 2

    # Mostramos el cuadrado del numero
    print(f"El cuadrado del numero {numero}, es {cuadrado_de_un_numero(numero)}")


def ejercicio2():
    # Mostramos un mensaje en pantalla
    print("En el siguiente renglon ingrese el primer numero.")
    print()

    # Pedimos al usuario que ingrese el primer numero
    num1 = ingresar_num_real()

    # Mostramos un mensaje en pantalla
    print("En el siguiente renglon ingrese el segundo numero.")
    print()

    # Pedimos al usuario que ingrese el segundo numero numero
    num2 = ingresar_num_real()

    # Creamos la funcion lambda de la suma de los dos numeros
    suma_de_los_num = lambda x,y : x + y

    # Mostramos la suma de los dos numeros
    print(f"La suma del numero {num1} y del numero {num2} es: {suma_de_los_num(num1,num2)}")

def ejercicio3():
    # Mostramos un mensaje en pantalla
    print("En el siguiente renglon ingrese el primer numero.")
    print()

    # Pedimos al usuario que ingrese el primer numero
    num1 = ingresar_num_real()

    # Mostramos un mensaje en pantalla
    print("En el siguiente renglon ingrese el segundo numero.")
    print()

    # Pedimos al usuario que ingrese el segundo numero numero
    num2 = ingresar_num_real()

    # Creamos la funcion lambda para saber cual es el numero mas grande
    num_mayor = lambda x,y : x if x > y else y

    # Mostramos cuales es el numero mas grande
    print(f"El numero mayor de los numeros ingresados es: {num_mayor(num1,num2)}")

def ejercicio4():
    # Inicializamos la lista
    lista = [1,2,3,4,5,6,7,8,9,10]

    # Creamos la lista con los aumentos de los numeros usando map y la funcion lambda
    lista_con_aumento = list(map(lambda x : x * 0.15, lista))

    # Mostramos las listas
    print(f"La lista incial es: {lista}")
    print()
    print(f"La lista con el aumento del 15% es: {lista_con_aumento}")

def ejercicio5():
    # Inicizalizamos el diccionario
    personas = [
        {'nombre': 'Hector', 'edad': 27}, 
        {'nombre': 'Juan', 'edad': 18}, 
        {'nombre': 'Maria', 'edad': 32}, 
        {'nombre': 'Pedro', 'edad': 21},
        {'nombre': 'Ana', 'edad': 20}
    ]

    # Creamos la lista ordenada por edad usando sorted y key pasandole la funcjon lambda
    lista_ord_por_edad = sorted(personas, key=lambda persona: persona['edad'])

    # Mostramos las listas
    print(f"La lista desordenada es: {personas}")
    print()
    print(f"La lista ordenada por edad es: {lista_ord_por_edad}")

def ejercicio6():
    # Inicializamos la lista
    lista = [1,2,3,4,5,6,7,8,9,10]

    # Creamos la lista de numeros pares usando filter y la funcion lambda
    num_pares = list(filter(lambda x: x % 2 == 0, lista))

    # Mostarmos las listas
    print(f"La lista inicial es: {lista}")
    print()
    print(f"La lista de numeros pares es: {num_pares}")

def ejercicio7():
    # Inicializamos la lista en celsius
    lista_celsius = [-273.15,-50,0,22,37,100,537.78]

    # Creamos la lista utilizando map y la funcion lambda
    lista_farenheit = list(map(lambda x : round((x*(9/5) + 32),2), lista_celsius))

    # Mostramos las listas
    print(f"La lista en grados celsius es: {lista_celsius}")
    print()
    print(f"La lista en grados farenheit es: {lista_farenheit}")

def ejercicio8():
    # Inicializamos la lista 
    lista_palabras = ['casa', 'perro', 'flor', 'libro', 'luna', 'sol', 'agua', 'pan', 'queso', 'vino']

    # Creamos la lista ordenada por la longitud de las palabras usando sorted y la funcion lambda
    lista_palabras_ord_por_long = sorted(lista_palabras, key = lambda palabra : len(palabra))

    # Mostramos las listas
    print(f"La lista de palabras es: {lista_palabras}")
    print()
    print(f"La lista ordenada por longitud de las palbaras es: {lista_palabras_ord_por_long}")

def ejercicio9():
    # Inicializamos la lista 
    lista_palabras = ['casa', 'perro', 'flor', 'libro', 'luna', 'sol', 'agua', 'pan', 'queso', 'vino']

    # Creamos la lista de letras con la inicial de las palbras usando map y la funcion lambda
    lista_letra_inic_palabra = list(map(lambda palabra : palabra[0], lista_palabras))

    # Mostramos las listas
    print(f"La lista de palabras es: {lista_palabras}")
    print()
    print(f"La lista de las letras iniciales de cada palbra es: {lista_letra_inic_palabra}")

def ejercicio10():
    # Inicializamos la lista de diccionarios
    lista_dic = [
        {'nombre': 'Hector', 'nota': 70}, 
        {'nombre': 'Juan', 'nota': 45}, 
        {'nombre': 'Maria', 'nota': 75}, 
        {'nombre': 'Pedro', 'nota': 80}, 
        {'nombre': 'Ana', 'nota': 60},  
        {'nombre': 'Florencia', 'nota': 95}
    ]

    # Obtenemos la suma de promedios usando map y la funcion lambda y sum() para sumar los numeros y len para obtener la longitud de la lista y round para redondear el resultado a 2 decimales
    promedio = round(sum(list(map(lambda dic : dic['nota'], lista_dic))) / len(lista_dic), 2)

    # Mostramos la suma de los promedios, los promedios y la lista
    print(f"La lista_dic es: {lista_dic}")
    print()
    print(f"La suma de los promedios es: {promedio}")

def encontrar_maximo(x, y):
    if x > y:
        return x
    else:
        return y

def ejercicio11():
    # Inicializamos la lista
    lista = [2,4,1,3,5,8,6,10,7,9]

    # Asignamos el valor obtenido de la funcion usando reduce
    maximo = reduce(encontrar_maximo, lista)

    # Mostramos la lista y el maximo
    print(f"La lista es: {lista}")
    print()
    print(f"El maximo elemento de la lista es: {maximo}")

def ejercicio12():
    # Inicializamos la lista 
    lista_palabras = ['casa', 'perro', 'flor', 'libro', 'luna', 'sol', 'agua', 'pan', 'queso', 'vino']

    # Creamos la concatenacion de la cadena usando reduce y la funcion lambda
    cadena_concatenada = reduce(lambda x, y : x + "," + y, lista_palabras)

    # Mostramos la lista y la concatenacion de la cadena
    print(f"La lista de cadena es: {lista_palabras}")
    print()
    print(f"La cadena concatenada es: {cadena_concatenada}")

def ejercicio13():
    # Inicializamos la lista
    lista_dic = [
        {'nombre': 'Hector', 'nota': 70}, 
        {'nombre': 'Juan', 'nota': 45}, 
        {'nombre': 'Maria', 'nota': 75}, 
        {'nombre': 'Pedro', 'nota': 80}, 
        {'nombre': 'Ana', 'nota': 60},  
        {'nombre': 'Florencia', 'nota': 95}
    ]

    # Creamos la lista de notas de alumnos aprobados usando filter y la funcion lambda
    notas_alumnos_aprobados = list(filter(lambda dic : dic['nota'] >= 60, lista_dic))

    # Mostramos las listas
    print(f"La lista es: {lista_dic}")
    print()
    print(f"La lista de las notas de los alumnos aprobados es: {notas_alumnos_aprobados}")

def filtrar_y_ordenar(lista_alumnos):
    # Obtener la fecha actual
    hoy = datetime.date.today()

    # Crear una lista vacia
    lista_filtrada = []

    # Recorrer cada diccionario de la lista original
    for alumno in lista_alumnos:
        # Obtener la fecha de nacimiento del diccionario
        fecha_nacimiento = alumno['fecha_nacimiento']

        # Comparar el mes y el dia de la fecha de nacimiento con el mes y el dia de hoy
        if fecha_nacimiento.month > hoy.month or (fecha_nacimiento.month == hoy.month and fecha_nacimiento.day > hoy.day):
            # agrregar el diccionario a la lista vacia
            lista_filtrada.append(alumno)

    # Ordenar la lista por la fecha de nacimiento
    lista_ordenada = sorted(lista_filtrada, key = lambda d: d['fecha_nacimiento'])

    # Retornar la lista ordenada
    return lista_ordenada

def ejercicio14():
    # Inicalizamos la lista de diccionarios
    lista_alumnos = [
        {"nombre":"Joaquin", "fecha_nacimiento":datetime.date(1990, 7, 2), "telefono":"123456789"}, 
        { "nombre":"Maria", "fecha_nacimiento":datetime.date(1995, 5, 16), "telefono":"123456789"},
        { "nombre":"Pedro", "fecha_nacimiento":datetime.date(1992, 9, 12), "telefono":"123456789"}, 
        { "nombre":"Ana", "fecha_nacimiento":datetime.date(1991, 9, 22), "telefono":"123456789"}, 
        { "nombre":"Florencia", "fecha_nacimiento":datetime.date(1994, 12, 8), "telefono":"123456789"}, 
        { "nombre":"Hector", "fecha_nacimiento":datetime.date(1993, 4, 4), "telefono":"123456789"}
    ]

    # Asiganamos el resultado a la lista
    lista_resultado = filtrar_y_ordenar(lista_alumnos)

    # Mostramos las listas
    print(f"La lista inicial de alumnos es: {lista_alumnos}")
    print()
    print(f"La lista resultado de alumnos es: {lista_resultado}")

# Asignamos el valor a op
op = menu()

# Repetimos mientras op != 16 o op sea None
while op is None or op != 15:
    # Si op es None
    if op is None:
        # Imprimimos un mensaje de error
        print()
        print("Error: Debes intoducir un numero entero entre 1 y 15.")
        print()
    # Si op es 1
    elif op == 1:
        # Llamamos a la funcion del ejercicio 1
        print()
        ejercicio1()
        print()
    # Si op es 2
    elif op == 2:
        # Llamamos a la funcion del ejercicio 2
        print()
        ejercicio2()
        print()
    # Si op es 3
    elif op == 3:
        # Llamamos a la funcion del ejercicio 3
        print()
        ejercicio3()
        print()
    # Si op es 4
    elif op == 4:
        # Llamamos a la funcion del ejercicio 4
        print()
        ejercicio4()
        print()
    # Si op es 5
    elif op == 5:
        # Llamamos a la funcion del ejercicio 5
        print()
        ejercicio5()
        print()
    # Si op es 6
    elif op == 6:
        # Llamamos a la funcion del ejercicio 6
        print()
        ejercicio6()
        print()
    # Si op es 7
    elif op == 7:
        # Llamamos a la funcion del ejercicio 7
        print()
        ejercicio7()
        print()
    # Si op es 8
    elif op == 8:
        # Llamamos a la funcion del ejercicio 8
        print()
        ejercicio8()
        print()
     # Si op es 9
    elif op == 9:
        # Llamamos a la funcion del ejercicio 9
        print()
        ejercicio9()
        print()
    # Si op es 10
    elif op == 10:
        # Llamamos a la funcion del ejercicio 10
        print()
        ejercicio10()
        print()
    # Si op es 11
    elif op == 11:
        # Llamamos a la funcion del ejercicio 11
        print()
        ejercicio11()
        print()
    # Si op es 12
    elif op == 12:
        # Llamamos a la funcion del ejercicio 12
        print()
        ejercicio12()
        print()
    # Si op es 13
    elif op == 13:
        # Llamamos a la funcion del ejercicio 13
        print()
        ejercicio13()
        print()
    # Si op es 14
    elif op == 14:
        # Llamamos a la funcion del ejercicio 14
        print()
        ejercicio14()
        print()

    # Volver a mostrar el menu de opciones
    op = menu()

# Si op es la de salir
# Mostramos un mensaje de despedida
print()
print("Gracias por usar el programa. Hasta pronto.")