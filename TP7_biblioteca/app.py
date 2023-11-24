# Importamos flask
from flask import Flask
# Importamos blueprint
from controladores.rutas import biblioteca_bp
#! Importo la funcion de carga de datos en memoria
from modelos.gestion import cargar_datos_memoria

app = Flask(__name__) #creamos una instancia de la clase Flask

# Iniciamos con la carga de datos
cargar_datos_memoria()

# Registramos blueprint
app.register_blueprint(biblioteca_bp)

# Iniciamos servidor
if __name__ == '__main__':
    app.run(debug=True, port=4000) #ejecutamos el servidor