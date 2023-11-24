# Importamos jsonify, blueprint y request
from flask import jsonify, Blueprint, request
#! Importamos las funciones que sean necesarias desde modelos.gestion
from modelos.gestion import obtener_libros, obtener_libro, añadir_libro, modificar_libro
from modelos.gestion import obtener_socios, obtener_socio, añadir_socio, modificar_socio, eliminar_socio
from modelos.gestion import obtener_prestamos, obtener_prestamo, añadir_prestamo, modificar_prestamo

# Creamos blueprint
biblioteca_bp = Blueprint('biblioteca', __name__)

#! Obtener datos
# GET: Obtener todos los libros
@biblioteca_bp.route('/libros')
def obtener_libros_json():
    # Obtenemos los libros en un formato JSON
    return jsonify(obtener_libros()), 200

# GET: Obtener todos los socios
@biblioteca_bp.route('/socios')
def obtener_socios_json():
    # Obtenemos los socios en un formato JSON
    return jsonify(obtener_socios()), 200

# GET: Obtener todos los prestamos
@biblioteca_bp.route('/prestamos')
def obtener_prestamos_json():
    # Obtenemos los prestamos en un formato JSON
    return jsonify(obtener_prestamos()), 200

#! Obtener por id
# GET: Obtener un libro por id
@biblioteca_bp.route('/libros/<int:id>')
def obtener_libro_json(id):
    # Iniciamos el diccionario con el libro
    libro = obtener_libro(id)
    # Si no existe el libro, devolvemos un error
    print(libro)
    if libro == None:
        return jsonify({'error': 'Libro no encontrado'}), 404
    # Si existe el libro, devolvemos el libro en un formato JSON
    else:
        # Obtenemos el libro en un formato JSON, pasando el id como parámetro
        return jsonify(libro), 200

# GET: Obtener un socio por id
@biblioteca_bp.route('/socios/<int:id>')
def obtener_socio_json(id):
    # Iniciamos el diccionario con el socio
    socio = obtener_socio(id)
    # Si no existe el socio, devolvemos un error
    if socio == None:
        return jsonify({'error': 'Socio no encontrado'}), 404
    # Si existe el socio, devolvemos el socio en un formato JSON
    else:
        # Obtenemos el socio en un formato JSON, pasando el id como parámetro
        return jsonify(socio), 200

# GET: Obtener un prestamo por id
@biblioteca_bp.route('/prestamos/<int:id>')
def obtener_prestamo_json(id):
    # Iniciamos el diccionario con el prestamo
    prestamo = obtener_prestamo(id)
    # Si no existe el prestamo, devolvemos un error
    if prestamo == None:
        return jsonify({'error': 'Prestamo no encontrado'}), 404
    # Si existe el prestamo, devolvemos el prestamo en un formato JSON
    else:
        # Obtenemos el prestamo en un formato JSON, pasando el id como parámetro
        return jsonify(prestamo), 200

#! Añadir algo nuevo
# POST: Añadir un libro
@biblioteca_bp.route('/libros', methods=['POST'])
def añadir_libro_json():
    # Verificamos que se envie un JSON
    if request.is_json:
        # Verificamos que el JSON tenga los campos obligatorios
        if "titulo" in request.json and "autor" in request.json and "anio_publicacion" in request.json:
            # Obtenemos los datos del libro
            nuevo_libro = request.get_json()
            # Añadimos un libro nuevo a la lista de libros
            libro_creado = añadir_libro(nuevo_libro["titulo"], nuevo_libro["autor"], nuevo_libro["año_publicacion"])
            # Si el libro se ha añadido correctamente, devolvemos el libro en un formato JSON
            return jsonify(libro_creado), 201
        else: # Si no, devolvemos un error
            return jsonify({'error': 'Faltan datos'}), 400
    else: # Si no, devolvemos un error
        return jsonify({'error': 'JSON no válido'}), 400

# POST: Añadir un socio
@biblioteca_bp.route('/socios', methods=['POST'])
def añadir_socio_json():
    # Verificamos que se envie un JSON
    if request.is_json:
        # Verificamos que el JSON tenga los campos obligatorios
        if "nombre" and "dni" and "apellido" and "telefono" and "email" in request.json:
            # Obtenemos los datos del socio
            nuevo_socio = request.get_json()
            # Añadimos un socio nuevo a la lista de socios
            socio_creado = añadir_socio(nuevo_socio["dni"], nuevo_socio["nombre"], nuevo_socio["apellido"], nuevo_socio["telefono"], nuevo_socio["email"])
            # Si el socio se ha añadido correctamente, devolvemos el socio en un formato JSON
            return jsonify(socio_creado), 201
        else: # Si no, devolvemos un error
            return jsonify({'error': 'Faltan datos'}), 400
    else: # Si no, devolvemos un error
        return jsonify({'error': 'JSON no válido'}), 400

# POST: Añadir un prestamo
@biblioteca_bp.route('/prestamos', methods=['POST'])
def añadir_prestamo_json():
    # Verificamos que se envie un JSON
    if request.is_json:
        # Verificamos que el JSON tenga los campos obligatorios
        if "socio_id" and "libro_id" and "fecha_retiro" and "fecha_devolucion" in request.json:
            # Obtenemos los datos del prestamo
            nuevo_prestamo = request.get_json()
            # Añadimos un prestamo nuevo a la lista de prestamos
            prestamo_creado = añadir_prestamo(nuevo_prestamo["socio_id"], nuevo_prestamo["libro_id"], nuevo_prestamo["fecha_retiro"], nuevo_prestamo["fecha_devolucion"])
            # Si el prestamo se ha añadido correctamente, devolvemos el prestamo en un formato JSON
            return jsonify(prestamo_creado), 201
        else: # Si no, devolvemos un error
            return jsonify({'error': 'Faltan datos'}), 400
    else: # Si no, devolvemos un error
        return jsonify({'error': 'JSON no válido'}), 400

#! Modificar algo existente
# PUT: Modificar un libro
@biblioteca_bp.route('/libros/<int:id>', methods=['PUT'])
def modificar_libro_json(id):
    # Verificamos que se envíe un JSON
    if request.is_json:
        # Verificamos que el JSON tenga los campos obligatorios
        if "titulo" and "autor" and "año_publicacion" in request.json:
            # Obtenemos los datos del libro
            libro = request.get_json()
            # Obtenemos el libro por id
            libro_a_modificar = modificar_libro(id, libro["titulo"], libro["autor"], libro["año_publicacion"])
            # Si el libro existe
            if libro_a_modificar!= None:
                # Devolvemos el libro en un formato JSON
                return jsonify(libro_a_modificar), 200
            else: # Si no, devolvemos un error
                return jsonify({'error': 'Libro no encontrado'}), 404
        else: # Si no, devolvemos un error
            return jsonify({'error': 'Faltan datos'}), 400
    else: # Si no, devolvemos un error
        return jsonify({'error': 'JSON no válido'}), 400

# PUT: Modificar un socio
@biblioteca_bp.route('/socios/<int:id>', methods=['PUT'])
def modificar_socio_json(id):
    # Verificamos que se envíe un JSON
    if request.is_json:
        # Verificamos que el JSON tenga los campos obligatorios
        if "nombre" and "dni" and "apellido" and "telefono" and "email" in request.json:
            # Obtenemos los datos del socio
            socio = request.get_json()
            # Obtenemos el socio por id
            socio_a_modificar = modificar_socio(id, socio["dni"], socio["nombre"], socio["apellido"], socio["telefono"], socio["email"])
            # Si el socio existe
            if socio_a_modificar!= None:
                # Devolvemos el socio en un formato JSON
                return jsonify(socio_a_modificar), 200
            else: # Si no, devolvemos un error
                return jsonify({'error': 'Socio no encontrado'}), 404
        else: # Si no, devolvemos un error
            return jsonify({'error': 'Faltan datos'}), 400
    else: # Si no, devolvemos un error
        return jsonify({'error': 'JSON no válido'}), 400

# PUT: Modificar un prestamo
@biblioteca_bp.route('/prestamos/<int:id>', methods=['PUT'])
def modificar_prestamo_json(id):
    # Verificamos que se envíe un JSON
    if request.is_json:
        # Verificamos que el JSON tenga los campos obligatorios
        if "socio_id" and "libro_id" and "fecha_retiro" and "fecha_devolucion" in request.json:
            # Obtenemos los datos del prestamo
            prestamo = request.get_json()
            # Obtenemos el prestamo por id
            prestamo_a_modificar = modificar_prestamo(id, prestamo["socio_id"], "Devuelto", prestamo["fecha_retiro"], prestamo["fecha_devolucion"])
            # Si el prestamo existe
            if prestamo_a_modificar!= None:
                # Devolvemos el prestamo en un formato JSON
                return jsonify(prestamo_a_modificar), 200
            else: # Si no, devolvemos un error
                return jsonify({'error': 'Prestamo no encontrado'}), 404
        else: # Si no, devolvemos un error
            return jsonify({'error': 'Faltan datos'}), 4

#! Eliminar algo existente
# DELETE: Eliminar un socio
@biblioteca_bp.route('/socios/<int:id>', methods=['DELETE'])
def eliminar_socio_json(id):
    # Dabmos de baja un socio y verificamos que no tenga un libro prestado
    # Verificamos que se envie un JSON
    if request.is_json:
        # Obtenemos el socio eliminado si no tiene un prestamo,
        socio = eliminar_socio(id)
        # si lo tiene notificamos el problema
        if socio!= None:
            # Devolvemos el socio que se elimino
            return jsonify(socio), 200
        else: # Si no se encontro o tiene un prestamo
            return({'error': 'Socio no encontrado o tiene un prestamo'}), 404
    else: # Si no devolvemos un error
        return({'error': 'JSON no válido'}), 400