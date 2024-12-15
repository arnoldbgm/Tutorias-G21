from flask import Flask
from flask_cors import CORS
from db import db
# Esto me permite controlar las migraciones
from flask_migrate import Migrate
from models import *
# Debes importar flaskRESTful
from flask_restful import Api

# Podamos trabajar con Cloudinary para la subida de imagenes
import cloudinary
import cloudinary.uploader
import cloudinary.api

from controllers.categoria import CategoriasList, CategoriaPost, CategoriaPut, CategoriaDelete
from controllers.pelicula import PeliculasList, PeliculaDelete, PeliculaPost

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/db_pos'
CORS(app)

cloudinary.config(
    cloud_name="", #Aqui va tu cloud name
    api_key="", # Aqui va tu api_key
    api_secret="" # Aqui va tu api_secret
)

db.init_app(app)
migrate = Migrate(app, db)
# Crear mi API (Es solo una vez)
api = Api(app)
# Ascociar mis controladores a unas rutas
# api.add_resource( El-nombre-controlador, ruta)
api.add_resource(CategoriasList, "/categorias")
api.add_resource(PeliculasList, "/peliculas")
api.add_resource(PeliculaPost, "/nueva-pelicula")
api.add_resource(CategoriaPost, "/nueva-categoria")
api.add_resource(CategoriaPut, "/categorias/<int:id>")
api.add_resource(CategoriaDelete, "/categorias/<int:id>")
api.add_resource(PeliculaDelete, "/peliculas/<int:id>")

# Este es mi archivo principal, estamos en modo de prueba
if __name__ == '__main__':
    app.run(debug=True)
