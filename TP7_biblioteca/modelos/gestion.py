# Importamos os
import os

# Iniciamos una variable global para los archivos libros.csv, prestamos.csv y socios.csv
# Asignamos las rutas a variables globales
ruta_libros = "modelos\\libros.csv"
ruta_socios = "modelos\\socios.csv"
ruta_prestamos = "modelos\\prestamos.csv"

#! Estructura del archivo prestamos.csv
# id,socio_dni,libro_id,fecha_retiro,fecha_devolucion
prestamos = []
#! Estructura del archivo socios.csv
# id, dni, nombre, apellido, teléfono, email
socios = []
#! Estructura del archivo libros.csv
# id, socio_dni, libro_id, fecha_retiro, fecha_devolucion
libros = []

# Función para cargar los datos en memoria
def cargar_datos_memoria():
    """
        Implementa la función para cargar los datos en memoria
    """
    # Cargamos los datos en memoria
    # Listas de diccionarios
    global prestamos, socios, libros
    #! Verificamos si existe los archivos
    # Si existe el archivo devuelve true
    if os.path.exists(ruta_prestamos) and os.path.exists(ruta_socios) and os.path.exists(ruta_libros):
        # Cargamos los datos en memoria desde los archivos
        cargar_desde_csv()
    else:
        # Si no existe el archivo creamos un archivo con la estructura del archivo
        crear_archivo()

#! Creamos el archivo
def crear_archivo():
    # Abrimos el archivo y creamos los archivos
    with open(ruta_libros, 'w') as crear:
        crear.write('id,titulo,autor,año_publicacion\n')
    with open(ruta_socios, 'w') as crear:
        crear.write('id,dni,nombre,apellido,telefono,email\n')
    with open(ruta_prestamos, 'w') as crear:
        crear.write('id,socio_dni,libro_id,fecha_retiro,fecha_devolucion\n')

#! Cargamos desde csv
def cargar_desde_csv():
    # Abrimos los archivos y cargamos los datos en memoria
    with open(ruta_prestamos, 'r') as archivo: #! Abrimos el archivo prestamos.csv
        lineas = archivo.readlines()[1:]
        for linea in archivo:
            id, socio_dni, libro_id, fecha_retiro, fecha_devolucion = linea.split(',')
            prestamos.append({
                'id': int(id),
               'socio_dni': socio_dni,
                'libro_id': libro_id,
                'fecha_retiro': fecha_retiro,
                'fecha_devolucion': fecha_devolucion
            })
    with open(ruta_socios, 'r') as archivo: #! Abrimos el archivo socios.csv
        lineas = archivo.readlines()[1:]
        for linea in lineas:
            id, dni, nombre, apellido, telefono, email = linea.split(',')
            socios.append({
                'id': int(id),
                'dni': dni,
                'nombre': nombre,
                'apellido': apellido,
                'telefono': telefono,
                'email': email
            })
    with open(ruta_libros, 'r') as archivo: #! Abrimos el archivo libros.csv
        lineas = archivo.readlines()[1:]
        for linea in lineas:
            #TODO
            id, titulo, autor, anio_publicacion = linea.split(',')
            libros.append({
                'id': int(id),
                'titulo': titulo,
                'autor': autor,
                'anio_publicacion': anio_publicacion
            })

#! Obtenemos los datos de las listas de diccionarios
# Obtenemos los datos de los socios
def obtener_socios():
    """
        Obtiene los datos de los socios,
        en forma de lista de diccionarios.
    """
    # Retornamos los datos de los socios
    return socios

# Obtenemos los datos de los libros
def obtener_libros():
    """
        Obtiene los datos de los libros,
        en forma de lista de diccionarios.
    """
    # Retornamos los datos de los libros
    return libros

# Obtenemos los datos de los prestamos
def obtener_prestamos():
    """
        Obtiene los datos de los prestamos,
        en forma de lista de diccionarios.
    """
    # Retornamos los datos de los prestamos
    return prestamos

#! Obtenemos por id
# Obtenemos los datos de un libro por id
def obtener_libro(id):
    """
        Obtiene los datos de un libro por id,
        en forma de diccionario.
    """
    # Recorremos la lista de libros
    for libro in libros:
        # Si el id del libro es igual al id pasado como parámetro
        if libro['id'] == id:
            # Retornamos los datos del libro
            return libro
    # Si no encontramos el libro retornamos None
    return None

# Obtenemos los datos de un socio por id
def obtener_socio(id):
    """
        Obtiene los datos de un socio por id,
        en forma de diccionario.
    """
    # Recorremos la lista de socios
    for socio in socios:
        # Si el id del socio es igual al id pasado como parámetro
        if socio['id'] == id:
            # Retornamos los datos del socio
            return socio
    # Si no encontramos el socio retornamos None
    return None

# Obtenemos los datos de un prestamo por id
def obtener_prestamo(id):
    """
        Obtiene los datos de un prestamo por id,
        en forma de diccionario.
    """
    # Recorremos la lista de prestamos
    for prestamo in prestamos:
        # Si el id del prestamo es igual al id pasado como parámetro
        if prestamo['id'] == id:
            # Retornamos los datos del prestamo
            return prestamo
    # Si no encontramos el prestamo retornamos None
    return None

#! Añadir algo nuevo
# Añadir un libro
def añadir_libro(titulo, autor, anio_publicacion):
    """
        Añade un libro a la lista de libros,
        retornando el libro.
    """
    # Creamos un diccionario con los datos del libro
    libro = {
        'id': libros[-1]['id'] + 1,
        'titulo': titulo,
        'autor': autor,
        'anio_publicacion': anio_publicacion
    }
    # Añadimos el libro a la lista de libros
    libros.append(libro)
    # Exportamos los nuevos datos al archivo libros.csv
    exportar_libros()
    # Retornamos el libro nuevo
    return libro

# Añadir un socio
def añadir_socio(dni, nombre, apellido, telefono, email):
    """
        Añade un socio a la lista de socios,
        retornando el socio.
    """
    # Creamos un diccionario con los datos del socio
    socio = {
        'id': socios[-1]['id'] + 1,
        'dni': dni,
        'nombre': nombre,
        'apellido': apellido,
        'telefono': telefono,
        'email': email
    }
    # Añadimos el socio a la lista de socios
    socios.append(socio)
    # Exportamos los nuevos datos al archivo socios.csv
    exportar_socios()
    # Retornamos el socio nuevo
    return socio

# Añadir un prestamo
def añadir_prestamo(socio_dni, libro_id, fecha_retiro, fecha_devolucion):
    """
        Añade un prestamo a la lista de prestamos,
        retornando el prestamo.
    """
    # Creamos un diccionario con los datos del prestamo
    prestamo = {
        'id': prestamos[-1]['id'] + 1,
       'socio_dni': socio_dni,
        'libro_id': libro_id,
        'fecha_retiro': fecha_retiro,
        'fecha_devolucion': fecha_devolucion
    }
    # Añadimos el prestamo a la lista de prestamos
    prestamos.append(prestamo)
    # Exportamos los nuevos datos al archivo prestamos.csv
    exportar_prestamos()
    # Retornamos el prestamo nuevo
    return prestamo

#! Exportamos las modificaciones de los datos
# Exportamos los libros a libreria.csv
def exportar_libros():
    """
        Exporta los libros a libreria.csv
    """
    # Abrimos el archivo libros.csv en modo escritura
    with open('libros.csv', 'w') as archivo:
        # Recorremos la lista de libros
        for libro in libros:
            # Escribimos los datos del libro en el archivo
            archivo.write(f"{libro['id']},{libro['titulo']},{libro['autor']},{libro['anio_publicacion']}\n")

# Exportamos los socios a socios.csv
def exportar_socios():
    """
        Exporta los socios a socios.csv
    """
    # Abrimos el archivo socios.csv en modo escritura
    with open('socios.csv', 'w') as archivo:
        # Recorremos la lista de socios
        for socio in socios:
            # Escribimos los datos del socio en el archivo
            archivo.write(f"{socio['id']},{socio['dni']},{socio['nombre']},{socio['apellido']},{socio['telefono']},{socio['email']}\n")

# Exportamos los prestamos a prestamos.csv
def exportar_prestamos():
    """
        Exporta los prestamos a prestamos.csv
    """
    # Abrimos el archivo prestamos.csv en modo escritura
    with open('prestamos.csv', 'w') as archivo:
        # Recorremos la lista de prestamos
        for prestamo in prestamos:
            # Escribimos los datos del prestamo en el archivo
            archivo.write(f"{prestamo['id']},{prestamo['socio_dni']},{prestamo['libro_id']},{prestamo['fecha_retiro']},{prestamo['fecha_devolucion']}\n")

#! Modificamos algo
# Modificar un libro
def modificar_libro(id, titulo, autor, anio_publicacion):
    """
        Modifica un libro,
        retornando el libro.
    """
    # Recorremos la lista de libros
    for libro in libros:
        # Si el id del libro es igual al id pasado como parámetro
        if libro['id'] == id:
            # Cambiamos los datos del libro
            libro['titulo'] = titulo
            libro['autor'] = autor
            libro['anio_publicacion'] = anio_publicacion
            # Exportamos los nuevos datos al archivo libros.csv
            exportar_libros()
            # Retornamos el libro modificado
            return libro
    # Si no encontramos el libro retornamos None
    return None

# Modificar un socio
def modificar_socio(id, dni, nombre, apellido, telefono, email):
    """
        Modifica un socio,
        retornando el id del socio.
    """
    # Recorremos la lista de socios
    for socio in socios:
        # Si el id del socio es igual al id pasado como parámetro
        if socio['id'] == id:
            # Cambiamos los datos del socio
            socio['dni'] = dni
            socio['nombre'] = nombre
            socio['apellido'] = apellido
            socio['telefono'] = telefono
            socio['email'] = email
            # Exportamos los nuevos datos al archivo socios.csv
            exportar_socios()
            # Retornamos el socio modificado
            return socio
    # Si no encontramos el socio retornamos None
    return None

# Modificar un prestamo
def modificar_prestamo(id, socio_dni, libro_id, fecha_retiro, fecha_devolucion):
    # Recorremos la lista de prestamos
    for prestamo in prestamos:
        if prestamo['id'] == id:
            # Cambiamos los datos del prestamo
            prestamo['socio_dni'] = socio_dni
            prestamo['libro_id'] = libro_id
            prestamo['fecha_retiro'] = fecha_retiro
            prestamo['fecha_devolucion'] = fecha_devolucion
            # Exportamos los nuevos datos al archivo prestamos.csv
            exportar_prestamos()
            # Retornamos el prestamo modificado
            return prestamo
    # Si no encontramos el prestamo retornamos None
    return None

#! Zona de eliminar
# Elimino un socio
def eliminar_socio(id):
    """
        Elimina un socio
    """
    # Buscamos el socio por su id
    socio = obtener_socio(id)
    # Si encontramos el socio
    if socio!= None:
        # Verificamos si el socio tiene prestamos
        prestamo = buscar_prestamo_por_socio_id(id)
        # Si el socio no tiene prestamos
        if prestamo != None:
            # Eliminamos el socio de la lista de socios
            socios.remove(socio)
            # Exportamos los nuevos datos al archivo socios.csv
            exportar_socios()
            # Retornamos el id del socio eliminado
            return socio
    # Si no encontramos el socio retornamos None o tiene un prestamo
    return None

# Funcion de busqueda de un prestamo por socio_id
def buscar_prestamo_por_socio_id(socio_id):
    """
        Busca un prestamo por socio_id
    """
    # Recorremos la lista de prestamos
    for prestamo in prestamos:
        if prestamo['socio_id'] == socio_id:
            return prestamo
    # Si no encontramos el prestamo retornamos None
    return None