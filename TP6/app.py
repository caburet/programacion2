from flask import Flask, jsonify, request # Importamos Flask y jsonify para crear la API, y jsonify para convertir los datos en JSON.
# request para obtener datos del formulario

app = Flask(__name__) # Creamos una nueva instancia de Flask llamada app.

# importar destinos
from destinos import destinos_argentina

@app.route("/destinos_argentina") # Metodo GET
def Get_destinos_argentina():
    # Devuelve la lista de destinos en formato JSON
    return jsonify(destinos_argentina)

# obtener viajes x id
@app.route("/destinos_argentina/<id>") # Metodo GET
def Get_destino_argentina(id):
    # Devuelve el destino con el id especificado en formato JSON
    for destino in destinos_argentina:
        if destino["id"] == id:
            return jsonify(destino)
    return jsonify({"message": "Destino no encontrado"})

# Agregar destino
@app.route("/destinos_argentina", methods=["POST"]) # Metodo POST
def Add_destino_argentina():
    # Validar que sea un JSON válido
    if request.is_json:
        if "id" and "ciudad" and "fecha_ida" and "fecha_vuelta" and "descripcion" and "tipo_viaje" and "precio" and "estrellas" and "pension" and "transporte" and "cupo_max" and "cupo_actual" in request.json:
            # Agrega un destino a la lista de destinos
            nuevo_destino = {
                # Obtenemos el id del destino
                "id": destinos_argentina[-1]["id"] + 1,
                # Obtenemos la ciudad del destino
                "ciudad": request.json["ciudad"],
                # Obtenemos la fecha_ida del destino
                "fecha_ida": request.json["fecha_ida"],
                # Obtenemos la fecha_vuelta del destino
                "fecha_vuelta": request.json["fecha_vuelta"],
                # Obtenemos la descripcion del destino
                "descripcion": request.json["descripcion"],
                # Obtenemos la tipo_viaje del destino
                "tipo_viaje": request.json["tipo_viaje"],
                # Obtenemos el precio del destino
                "precio": request.json["precio"],
                # Obtenemos las estrallas del destino
                "estrellas": request.json["estrellas"],
                # Obtenemos la pension del destino
                "pension": request.json["pension"],
                # Obtenemos transporte del destino
                "transporte": request.json["transporte"],
                # Obtenemos cupo_max del destino
                "cupo_max": request.json["cupo_max"],
                # Obtenemos cupo_actual del destino
                "cupo_actual": request.json["cupo_actual"]
            }
            destinos_argentina.append(nuevo_destino)
            # Retorno un mensaje de confirmación
            return jsonify({"message": "Destino agregado correctamente", "destino": nuevo_destino}), 201
        else:
            return jsonify({"error":"Faltan datos"}),400
    else:
        return jsonify({"error":"El formato de la solicitud no es JSON"}),400

# Actualizar destino
@app.route("/destinos_argentina/<id>", methods=["PUT"]) # Metodo PUT
def Actualizar_destino_argentina(id):
    # Validar que sea un JSON válido
    if request.is_json:
        if "id" and "ciudad" and "fecha_ida" and "fecha_vuelta" and "descripcion" and "tipo_viaje" and "precio" and "estrellas" and "pension" and "transporte" and "cupo_max" and "cupo_actual" in request.json:
            # Buscamos el destino con el id especificado
            destino_a_actualizar = [destino_buscado for destino_buscado in destinos_argentina if destino_buscado["id"] == id]
            # Si el destino no existe, retornamos un mensaje de error
            if len(destino_a_actualizar) == 0:
                return jsonify({"message": "Destino no encontrado"}), 404
            else: # Si el destino existe, actualizamos los datos del destino
                # Buscamos el destino con el id especificado
                for destino in destinos_argentina:
                    if destino["id"] == id:
                        # Actualizamos los datos del destino
                        destino_a_actualizar[0]["ciudad"] = request.json["ciudad"],
                        destino_a_actualizar[0]["fecha_ida"] = request.json["fecha_ida"],
                        destino_a_actualizar[0]["fecha_vuelta"] = request.json["fecha_vuelta"],
                        destino_a_actualizar[0]["descripcion"] = request.json["descripcion"],
                        destino_a_actualizar[0]["tipo_viaje"] = request.json["tipo_viaje"],
                        destino_a_actualizar[0]["precio"] = request.json["precio"],
                        destino_a_actualizar[0]["estrellas"] = request.json["estrellas"],
                        destino_a_actualizar[0]["pension"] = request.json["pension"],
                        destino_a_actualizar[0]["transporte"] = request.json["transporte"],
                        destino_a_actualizar[0]["cupo_max"] = request.json["cupo_max"],
                        destino_a_actualizar[0]["cupo_actual"] = request.json["cupo_actual"]
                        # Agregamos el destino actualizado a la lista de destinos
                        destinos_argentina.append(destino_a_actualizar[0])
                        # Retorno un mensaje de confirmación
                        return jsonify({"message": "Destino actualizado correctamente", "destinos": destinos_argentina}), 200
        else:
            return jsonify({"error":"Faltan datos"}),400
    else:
        return jsonify({"error":"El formato de la solicitud no es JSON"}),400

# Eliminar destino
@app.route("/destinos_argentina/<id>", methods=["DELETE"]) # Metodo DELETE
def Eliminar_destino_argentina(id):
    # Buscamos el destino con el id especificado
    destino_a_eliminar = [destino_buscado for destino_buscado in destinos_argentina if destino_buscado["id"] == id]
    # Si el destino no existe, retornamos un mensaje de error
    if len(destino_a_eliminar) == 0:
        return jsonify({"message": "Destino no encontrado"}), 404
    else: # Si el destino existe, lo eliminamos de la lista de destinos
       # Verificar si se a vendido el destino
       if destino_a_eliminar[0]["cupo_actual"] < destino_a_eliminar[0]["cupo_max"]:
           return jsonify({"message": "No se puede eliminar el destino, se a vendido"}), 400
       else:
            # Eliminamos el destino de la lista de destinos
            destinos_argentina.remove(destino_a_eliminar[0])
            # Retorno un mensaje de confirmación
            return jsonify({"message": "Destino eliminado correctamente", "destinos": destinos_argentina}), 200

# debug=True nos proporcionará información detallada sobre errores, restablecerá el servidor cada vez que se detecte un cambio en el código, etc.
# port = 4000 nos permite cambiar el puerto por defecto del servidor, en este caso se va a ejecutar en http://127.0.0.1:4000
# __name__ es una variable especial de Python que representa el nombre del módulo actual.
# Cuando un script es ejecutado, Python asigna el valor "__main__" a la variable __name__ si es el script principal que está siendo ejecutado.
# Si el script es importado como un módulo en otro script, entonces __name__ de ese script tomará el valor del nombre del módulo (nombre del archivo).
if __name__ == "__main__":
   app.run(debug=True, port=4000)