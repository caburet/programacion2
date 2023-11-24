from flask import Blueprint, jsonify, request
from modelo.estudio import crear_estudio, obtener_estudio_por_id, obtener_estudios,editar_estudio_por_id, eliminar_estudio_por_id


# Creamos el blueprint
estudios_bp = Blueprint('estudios', __name__)

@estudios_bp.route('/estudios/<int:id_estudio>', methods=["GET"])
def obtener_estudios_json():
    return jsonify(obtener_estudios())

@estudios_bp.route('/estudios/', methods=["POST"])
def crear_estudio_json():
    estudio = request.get_json()
    estudio_creado=crear_estudio(estudio["nombre_de_estudio"], estudio["descripcion"], estudio["precio"])
    return jsonify(estudio_creado),200
    
    
@estudios_bp.route('/estudios/<int:id_estudio>', methods=["PUT"])
def modificar_estudio_json(id_estudio):
    if request.is_json:
        if "nombre_de_estudio" in request.json and "descripcion" in request.json and "precio" in request.json:            
            estudio = request.get_json()
            estudio_modificado=editar_estudio_por_id(id_estudio,estudio["nombre_de_estudio"], estudio["descripcion"], estudio["precio"])
            return jsonify(estudio_modificado),200
        else:
            return jsonify({"error":"Faltan datos"}),400
    else:
        return jsonify({"error":"El formato de la solicitud no es JSON"}),400
    
@estudios_bp.route('/estudios/<int:id_estudio>', methods=["DELETE"])
def eliminar_estudio_json(id_estudio):
    return jsonify(eliminar_estudio_por_id(id_estudio)),200