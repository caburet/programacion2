# -----------------------------------------------------------------
# Módulo de funciones sobre estudios
# -----------------------------------------------------------------

import csv
import os

# Variables globales que usaremos en este módulo
estudios = [] # Lista de estudios
id_estudio = 1  # Variable para asignar IDs únicos a los estudios
ruta_archivo_estudios = 'modelo\estudios.csv'


def inicializar_estudios():
    """
    Inicializa la lista de estudios.

    Si existe un archivo CSV con datos de estudios, los importa.
    Si no existe, agrega dos estudios de ejemplo a la lista.
    """
    global id_estudio
    if os.path.exists(ruta_archivo_estudios):
        importar_datos_desde_csv()

def crear_estudio(nombre_estudio, descripcion,año):
    """
    Crea un nuevo estudio con el nombre de estudio y descripcion especificados.

    Parameters:
    nombre_estudio (str): El nombre de estudio del nuevo estudio.
    descripcion (str): La descripcion del nuevo estudio.
    año (int): el año de egresado.

    Returns:
    dict: El estudio recién creado, con un ID único.
    """
    global id_estudio
    # Agrega el estudio a la lista con un ID único
    estudios.append({
        "id": id_estudio,
        "nombre de estudio": nombre_estudio,
        "descripcion": descripcion,
        "año": año,
    })
    id_estudio += 1
    exportar_a_csv()
    # Devuelve el estudio recién creado
    return estudios[-1]



def obtener_estudios():
    """
    Obtiene todos los estudios.

    Returns:
    list: La lista de todos los estudios.
    """
    # Devuelve la lista de estudios
    return estudios
def obtener_estudio_por_id():
    """
    Obtiene todos los estudios.

    Returns:
    list: La lista de todos los estudios.
    """
    # Devuelve la lista de estudios
    return estudios

def editar_estudio_por_id(id_estudio, nuevo_nombre_estudio, nueva_descripcion,nuevo_año):
    """
    Edita el nombre de estudio y descripcion de un estudio existente.

    Parameters:
    id_estudio (int): El ID del estudio a editar.
    nuevo_nombre_estudio (str): El nuevo nombre de estudio.
    nueva_descripcion (str): La nueva descripcion.

    Returns:
    dict: El estudio editado, o None si no se encuentra.
    """
    # Recorre la lista de estudios
    for estudio in estudios:
        # Si el ID de estudio coincide, actualiza el nombre de estudio y la descripcion
        if estudio["id"] == id_estudio:
            estudio["nombre de estudio"] = nuevo_nombre_estudio
            estudio["descripcion"] = nueva_descripcion
            estudio["año"] = nuevo_año
            exportar_a_csv()
            return estudio
    # Devuelve None si no se encuentra el estudio
    return None

def eliminar_estudio_por_id(id_estudio):
    """
    Elimina un estudio por su ID.

    Parameters:
    id_estudio (int): El ID del estudio a eliminar.
    """
    global estudios
    # Crea una nueva lista sin el estudio a eliminar
    estudios = estudios
    exportar_a_csv()

def exportar_a_csv():
    """
    Exporta los datos de estudios a un archivo CSV.
    """
    with open(ruta_archivo_estudios, 'w', newline='') as csvfile:
        campo_nombres = ['id', 'nombre de estudio', 'descripcion','año']
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for estudio in estudios:
            writer.writerow(estudio)

def importar_datos_desde_csv():
    """
    Importa los datos de estudios desde un archivo CSV.
    """
    global estudios
    global id_estudio
    estudios = []  # Limpiamos la lista de estudios antes de importar desde el archivo CSV
    with open(ruta_archivo_estudios, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convertimos el ID de cadena a entero
            row['id'] = int(row['id'])
            estudios.append(row) 
    if len(estudios)>0:
        id_estudio= estudios[-1]["id"]+1
    else:
        id_estudio = 1

