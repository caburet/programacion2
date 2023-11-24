from flask import Flask
from modelo.estudio import inicializar_estudios

from controlador.rutas_estudio import estudios_bp

app = Flask(__name__) #creamos una instancia de la clase Flask

inicializar_estudios()

# registramos el blueprint

app.register_blueprint(estudios_bp)

if __name__ == '__main__':
    app.run(debug=True) #iniciamos la aplicación