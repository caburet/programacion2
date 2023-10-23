# MODULO JSON
import json

# RUTAS ARCHIVOS
ruta_alumnos = "programacion2-nuevo/TP5/alumnos.csv"
ruta_alumnos_deportes = "programacion2-nuevo/TP5/alumnos_deportes.csv"
ruta_deportes = "programacion2-nuevo/TP5/deportes.csv"
ruta_eventos = "programacion2-nuevo/TP5/eventos.csv"
ruta_inscripciones = "programacion2-nuevo/TP5/inscripciones.csv"


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
        print("* => SELECCIONE UNA OPCION:      <= *")
        print("*************************************")
        opcion = Es_Entero()
        if (opcion<0 or opcion>5):
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
        else:
            Ej5()

### FUNCIONES
def Es_Entero(): ## VALIDA NUMEROS ENTEROS
    while True:
        try:
            num=int(input("ingrese un numero entero: "))
            break
        except ValueError:
            print("ups!!!, acurrio un error, intentelo de nuevo...")
    return num   

### FUNCIONES PARA EL EJERCICIO 1
def Encolar(cola,elemento):
    # Agrega un elemento al final de la cola
    cola.append(elemento)

def Desencolar(cola): # SIRVE PARA EL EJERCICIO 5 ------------->
    # Devuelve el elemento al inicio de la cola y lo elimina de la cola
    if not Esta_bacia(cola):
        return cola.pop(0)
    else:
        return None

def Esta_bacia(cola):
    # Devuelve True si la cola está vacía, False en caso contrario
    return len(cola)==0

def Longitud(cola):
    # Devuelve la longitud de la cola
    return len(cola)

### FUNCIONES PARA EL EJERCICIO 2
def Apilar(pila,elemento):# SIRVE PARA EL EJERCICIO 5 ------------->
    # Agrega un elemento al final de la pila
    pila.append(elemento)

def Desapilar(pila,elemento):
    # Devuelve el elemento en la cima de la pila y lo elimina de la pila
    if not Esta_bacia_pila(pila):
        return pila.pop()
    else:
        return None
    
def Esta_bacia_pila(pila):
    # Devuelve True si la pila está vacía, False en caso contrario
    return len(pila)==0

def Longitud_pila(pila):
    # Devuelve la longitud de la pila
    return len(pila)

### FUNCIONES PARA EL EJERCICIO 3
def Listas_random():
    # Importamos el modulo random
    import random
    
    # Generamos dos listas con la longitud de 20-50, 
    # y cada lista con elementos de valores aleatorios entre 200 y 5000.
    # La función random.randint genera un número entero aleatorio dentro de un rango especificado.
    lista1 = [random.randint(200,5000) for i in range(random.randint(20,50))]
    lista2 = [random.randint(200,5000) for i in range(random.randint(20,50))]
    
    # Devolvemos las dos listas generadas
    return lista1,lista2

### FUNCIONES PARA EL EJERCICIO 5
# Definimos una función para crear una pila a partir de una lista
def crear_pila(lista):
    pila = []
    for elemento in lista:
        pila.append(elemento)
    return pila

# Definimos una función para crear una cola a partir de una lista
def crear_cola(lista):
    cola = []
    for elemento in lista:
        cola = Encolar(elemento)
    return cola

# Definimos una función para leer un archivo JSON y devolver un diccionario
def leer_json(nombre_archivo):
    with open(nombre_archivo) as archivo:
        diccionario = json.load(archivo)
    return diccionario

# Definimos una función para escribir un diccionario en un archivo JSON
def escribir_json(nombre_archivo, diccionario):
    with open(nombre_archivo, "w") as archivo:
        json.dump(diccionario, archivo)

### EJERCICIOS:

# ejercicio 1
def Ej1():
    print("1. crear las funciones genéricas que nos permitirán manejar una cola de datos.",
    "* encolar(cola,elemento) #agrega elemento al final de la cola",
    "* desencolar(cola,elemento) #devuelve el elemento al inicio de la cola y lo elimina de la cola",
    "* longitud(cola) #devuelve la longitud de la estructura",
    "* esta_vacia(cola) #devuelve True si la estructura está vacía")

# ejercicio 2
def Ej2():
    print("2. crear las funciones genéricas que nos permitirán manejar una pila de datos."
    "* apilar(pila,elemento) #agrega elemento encima de la pila"
    "* desapilar(pila,elemento) #devuelve el elemento en la cima de la pila y lo elimina de la pila"
    "* longitud(pila) #devuelve la longitud de la estructura (pueden reutilizar el del punto anterior)"
    "* esta_vacia(pila) #devuelve True si la estructura está vacía (pueden reutilizar el del punto anterior)")

# ejercicio 3
def Ej3():
    print("3. Usando el módulo random, cree una función que retorne dos listas de longitud aleatoria entre 20 y 50, y cada lista con elementos de valores aleatorios entre 200 y 5000.")

# ejercicio 4
def Ej4():
    print("4. Utilizando la función anterior genere dos listas de datos. Con la lista1 se debe generar una sublista con los elementos impares de lista1 multiplicados por el valor menor de la lista2.")

    # Generamos las dos listas llamando a la función Listas_random()
    lista1, lista2 = Listas_random()

    # Imprimimos las dos listas para ver su contenido
    print(lista1)
    print(lista2)

    # Crear una funcion lambda que devuelva el menor de los elementos de la lista2
    func = lambda x, y: x if x<y else y

    # Agregar una variable que almacene el valor menor de la lista2, usando reduce
    from functools import reduce
    menor = reduce(func,lista2)

    # Crear una funcion lambda que multiplique los elementos de la lista1 por el valor menor de la lista2
    func2 = lambda x: x*menor

    # Generar una sublista con los elementos de la lista1 que sean impares y multiplicarlos por el valor menor de la lista2
    lista_impares = [x for x in lista1 if x%2!=0]
    lista_impares_multiplicados = list(map(func2,lista_impares))

    # Imprimir la sublista con los elementos de la lista1 que sean impares y multiplicarlos por el valor menor de la lista2
    print(lista_impares_multiplicados)

# ejercicio 5
def Ej5():
    print("5. Un club deportivo que organiza para sus alumnos una serie de competencias para el fin de semana cerró las inscripciones a los eventos y se desea a procesarlas. Dada la siguiente estructura de datos simplificada:"
    "* **alumnos.csv** (con datos en el formato `alumno_dni;alumno_apellido;alumno_nombre`)"
    "* **eventos.csv** (con datos en el formato `evento_codigo;deporte_codigo;evento_nombre;evento_descripción`)"
    "* **deportes.csv** (con datos en el formato `deporte_codigo;deporte_nombre`)"
    "* **alumnos_deportes** (con datos en el formato `alumno_dni;deporte_codigo`)"
    "* **inscripciones.csv** (con datos en el formato `alumno_dni;evento_codigo`)"
    
    "se pide:"
    "* cargar los datos en memoria usando las estructuras adecuadas, y procesar la cola de inscripciones a los eventos deportivos registrando los datos en un nuevo archivo ***alumnos_eventos.csv*** con el formato `alumno_dni;evento_codigo;numero_inscripcion`."
    "Se debe verificar que los datos cargados en la cola sean válidos (es decir que el dni exista en alumnos, que el código de deporte exista en deportes, que el código de evento exista en eventos, y que el evento en el que se inscribe el alumno sea de un deporte que el alumno realiza en el club *(un alumno puede realizar mas de un deporte)*). Si hay un registro en inscripciones que no es correcto no se debe procesar y se debe almacenar en una pila con los datos `dni_alumno; evento_nombre`."
    "* luego al finalizar las inscripciones imprimir por pantalla el orden inverso al que se ejecutaron las inscripciones válidas (utilizando la pila del inciso anterior)."
    "* de las inscripciones válidas se pueden calcular estadísticas: mostrar cuantos inscriptos tiene cada evento, cual es el evento con mayor inscriptos, cual es el que tiene menor inscriptos, cual es el que su cantidad de inscriptos se aproxima más al promedio de `inscriptos/eventos`.")
   


    # Leemos los archivos JSON y los guardamos en diccionarios
    alumnos = leer_json("alumnos.json")
    eventos = leer_json("eventos.json")
    deportes = leer_json("deportes.json")
    alumnos_deportes = leer_json("alumnos_deportes.json")
    inscripciones = leer_json("inscripciones.json")

    # Creamos una cola con las inscripciones
    cola_inscripciones = crear_cola(inscripciones)

    # Creamos una pila vacía para los errores
    pila_errores = crear_pila([])

    # Creamos una lista vacía para los alumnos_eventos
    alumnos_eventos = []

    # Creamos un contador para el número de inscripción
    numero_inscripcion = 0

    # Procesamos la cola de inscripciones hasta que esté vacía
    while len(cola_inscripciones) > 0:
        # Desencolamos una inscripción
        inscripcion = Desencolar(cola_inscripciones)

        # Obtenemos el dni del alumno y el código del evento
        dni_alumno = inscripcion["alumno_dni"]
        codigo_evento = inscripcion["evento_codigo"]

        # Buscamos al alumno en el diccionario de alumnos
        alumno = alumnos.get(dni_alumno)
        
        # Buscamos el evento en el diccionario de eventos
        evento = eventos.get(codigo_evento)
        
        # Si el alumno o el evento no existen, apilamos un error con el dni y el nombre del evento
        if alumno is None or evento is None:
            error = dni_alumno + ";" + evento["evento_nombre"]
            Apilar(pila_errores, error)
        
        # Si el alumno y el evento existen, verificamos que el alumno practique el deporte del evento
        else:
            # Obtenemos el código del deporte del evento
            codigo_deporte = evento["deporte_codigo"]

            # Buscamos al alumno en la lista de alumnos_deportes con ese código de deporte
            practica_deporte = False
            for ad in alumnos_deportes:
                if ad["alumno_dni"] == dni_alumno and ad["deporte_codigo"] == codigo_deporte:
                    practica_deporte = True
                    break
            
            # Si el alumno practica el deporte del evento, creamos un diccionario con el dni, el código del evento y el número de inscripción
            if practica_deporte:
                numero_inscripcion += 1
                alumno_evento = {"alumno_dni": dni_alumno, "evento_codigo": codigo_evento, "numero_inscripcion": str(numero_inscripcion)}
                alumnos_eventos.append(alumno_evento)
            # Si el alumno no practica el deporte del evento, apilamos un error con el dni y el nombre del evento
            else:
                error = dni_alumno + ";" + evento["evento_nombre"]
                Apilar(pila_errores, error)

    # Escribimos la lista de alumnos_eventos en un archivo JSON
    escribir_json("alumnos_eventos.json", alumnos_eventos)

    # Imprimimos por pantalla el orden inverso al que se ejecutaron las inscripciones válidas
    print("El orden inverso al que se ejecutaron las inscripciones válidas es:")
    while len(pila_errores) > 0:
        # Desapilamos un error
        error = Desapilar(pila_errores)

        # Imprimimos el error
        print(error)

    # Calculamos estadísticas de las inscripciones válidas

    # Creamos un diccionario vacío para contar los inscriptos por evento
    inscriptos_por_evento = {}

    # Recorremos la lista de alumnos_eventos
    for ae in alumnos_eventos:
        # Obtenemos el código del evento
        codigo_evento = ae["evento_codigo"]

        # Si el código del evento está en el diccionario, le sumamos uno al contador
        if codigo_evento in inscriptos_por_evento:
            inscriptos_por_evento[codigo_evento] += 1
        
        # Si no está, lo agregamos al diccionario con valor uno
        else:
            inscriptos_por_evento[codigo_evento] = 1

    # Creamos variables para guardar el evento con mayor y menor inscriptos y sus respectivos valores
    evento_mayor_inscriptos = None
    mayor_inscriptos = 0
    evento_menor_inscriptos = None
    menor_inscriptos = float("inf")

    # Creamos una variable para guardar la suma total de inscriptos
    total_inscriptos = 0

    # Recorremos el diccionario de inscriptos por evento
    for codigo_evento, cantidad in inscriptos_por_evento.items():
        # Sumamos la cantidad al total de inscriptos
        total_inscriptos += cantidad

        # Si la cantidad es mayor que el mayor valor actual, actualizamos el evento con mayor inscriptos y su valor
        if cantidad > mayor_inscriptos:
            evento_mayor_inscriptos = codigo_evento
            mayor_inscriptos = cantidad
        
        # Si la cantidad es menor que el menor valor actual, actualizamos el evento con menor inscriptos y su valor
        if cantidad < menor_inscriptos:
            evento_menor_inscriptos = codigo_evento
            menor_inscriptos = cantidad

    # Calculamos el promedio de inscriptos por evento
    promedio_inscriptos = total_inscriptos / len(inscriptos_por_evento)

    # Creamos una variable para guardar la diferencia mínima entre la cantidad de inscriptos y el promedio
    diferencia_minima = float("inf")

    # Creamos una variable para guardar el evento que se aproxima más al promedio
    evento_mas_cercano_al_promedio = None

    # Recorremos nuevamente el diccionario de inscriptos por evento
    for codigo_evento, cantidad in inscriptos_por_evento.items():
        # Calculamos la diferencia absoluta entre la cantidad y el promedio
        diferencia = abs(cantidad - promedio_inscriptos)

        # Si la diferencia es menor que la diferencia mínima actual, actualizamos el evento más cercano al promedio y su diferencia
        if diferencia < diferencia_minima:
            evento_mas_cercano_al_promedio = codigo_evento
            diferencia_minima = diferencia

    # Imprimimos las estadísticas por pantalla

    print("Estadísticas de las inscripciones válidas:")

    print("Cantidad de inscriptos por evento:")
    for codigo_evento, cantidad in inscriptos_por_evento.items():
        print(codigo_evento + ": " + str(cantidad))

    print("Evento con mayor inscriptos: " + evento_mayor_inscriptos + " (" + str(mayor_inscriptos) + ")")

    print("Evento con

#### INICIO DEL PROGRAMA:
Inicio()