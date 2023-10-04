# 5. Un club deportivo que organiza para sus alumnos una serie de competencias para el fin de semana 
#    cerró las inscripciones a los eventos y se desea a procesarlas. Dada la siguiente estructura de datos simplificada:
#     
#    - eventos.csv (con datos en el formato 'evento_codigo;deporte_codigo;evento_nombre;evento_descripción')
#    - deportes.csv (con datos en el formato 'deporte_codigo;deporte_nombre')
#    - alumnos_deportes (con datos en el formato 'alumno_dni;deporte_codigo')
#    - alumnos.csv (con datos en el formato 'alumno_dni;alumno_apellido;alumno_nombre')
#    - inscripciones.csv (con datos en el formato 'alumno_dni;evento_codigo')

#    se pide:
#    cargar los datos en memoria usando las estructuras adecuadas, y procesar la cola de inscripciones a 
#    los eventos deportivos registrando los datos en un nuevo archivo "alumnos_eventos.csv" con el formato 
#    'alumno_dni;evento_codigo;numero_inscripcion'.

#    Se debe verificar que los datos cargados en la cola sean válidos 
#    (es decir que el dni exista en alumnos, que el código de deporte exista en deportes, 
#    que el código de evento exista en eventos, y que el evento en el que se inscribe el alumno sea de un 
#    deporte que el alumno realiza en el club *(un alumno puede realizar mas de un deporte)*). 
#    Si hay un registro en inscripciones que no es correcto no se debe procesar y se debe almacenar 
#    en una pila con los datos 'dni_alumno; evento_nombre'.
#     
#    luego al finalizar las inscripciones imprimir por pantalla el orden inverso al que se 
#    ejecutaron las inscripciones válidas (utilizando la pila del inciso anterior).
#    de las inscripciones válidas se pueden calcular estadísticas: mostrar cuantos inscriptos tiene cada evento, 
#    cual es el evento con mayor inscriptos, cual es el que tiene menor inscriptos, 
#    cual es el que su cantidad de inscriptos se aproxima más al promedio de 'inscriptos/eventos'.

def encolar(lista, elemento):
    return lista.append(elemento)

#Funcion generica para leer todos los archivos CSV
def leer_archivos(ruta):
    
    archivo = open(ruta,'r', encoding="utf-8")

    #Leo la primera linea que va contener las claves del archivo
    primera_cadena = archivo.readline()
    claves = primera_cadena.split(";")
    
    lista = []
    #Leo linea por linea y voy guardando en una diccionario con su respetiva clave,
    #Luego la agrego a una lista que es lo que devuelve la funcion
    #(La longitud de las claves va ser igual que la longitud de los valores datito)

    for linea in archivo:
        dict = {}
        valores = linea.split(";")
        for i in range(len(claves)):
            dict[claves[i]] = valores[i]
        encolar(lista, dict)
        
    archivo.close()
    
    return lista, claves


ruta_alumnos = r"C:\Users\weyla\Escritorio\Practico_3\programacion2\TP5\alumnos.csv"
ruta_inscripciones = r"C:\Users\weyla\Escritorio\Practico_3\programacion2\TP5\inscripciones.csv"
ruta_eventos = r"C:\Users\weyla\Escritorio\Practico_3\programacion2\TP5\eventos.csv"

lista_alumnos, claves_alumnos = leer_archivos(ruta_alumnos)
lista_inscripciones, claves_inscripciones = leer_archivos(ruta_inscripciones)
lista_eventos, claves_eventos = leer_archivos(ruta_eventos)

for i in enumerate(claves_alumnos):
    print(i)
    