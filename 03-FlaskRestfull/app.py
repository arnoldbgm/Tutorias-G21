from flask import Flask
from db import db
# Esto me permite controlar las migraciones
from flask_migrate import Migrate
from models import *
# Debes importar flaskRESTful
from flask_restful import Api
from controllers.categoria import CategoriasList, CategoriaPost
from controllers.pelicula import PeliculasList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/db_pos'

db.init_app(app)
migrate = Migrate(app, db)
# Crear mi API (Es solo una vez)
api = Api(app)
# Ascociar mis controladores a unas rutas
# api.add_resource( El-nombre-controlador, ruta)
api.add_resource(CategoriasList, "/categorias")
api.add_resource(PeliculasList, "/pelicula")
api.add_resource(CategoriaPost, "/nueva-categoria")

# Este es mi archivo principal, estamos en modo de prueba
if __name__ == '__main__':
   app.run(debug=True)
