import csv
import os
ruta_archivo_personas=''



def exportar_a_csv():
    """
    Exporta los datos de personas a un archivo CSV.
    """
    with open(ruta_archivo_personas, 'w', newline='') as csvfile:
        campo_nombres = ['id', 'nombre de persona', 'apellido','ciudad']
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for persona in personas:
            writer.writerow(persona)

def importar_datos_desde_csv():
    """
    Importa los datos de personas desde un archivo CSV.
    """
    global personas
    global id_persona
    personas = []  # Limpiamos la lista de personas antes de importar desde el archivo CSV
    with open(ruta_archivo_personas, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convertimos el ID de cadena a entero
            row['id'] = int(row['id'])
            personas.append(row) 
    if len(personas)>0:
        id_persona= personas[-1]["id"]+1
    else:
        id_persona = 1