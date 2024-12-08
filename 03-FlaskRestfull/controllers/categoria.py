# Importa mi instancia de SQLAlchemy
from db import db
# Importaremos mi tabla (model)
from models.categoria import  CategoriasModel
# Importamos flask restful
from flask_restful import Resource
# request => La solicitud del cliente (lo que el cliente pide)
# response => Lo que se le devuelve al cliente
from flask import request

# GET => Traer informacion
# POST => Crear o grabar 
# PUT - PATCH  => Actualizar informacion
# DELETE => Eliminar

# GET
# Este controlador se encargara de traer las categorias
class CategoriasList(Resource):
   # Creamos una funcion y ponemos el tipo de metodo
   def get(self):
      # SELECT * FROM TABLA
      # SELECT * FROM categorias;
      # SQLAlchemy => NombreDelModelo.query.accion()
      resultado_consulta = CategoriasModel.query.all()
      print(resultado_consulta)
      return [
         {
            "id": categoria.id,
            "nombre": categoria.nombre,
         } for categoria in resultado_consulta
      ], 200

class CategoriaPost(Resource):
   def post(self):
      # Siempre y siempre se hace el llamo al request
      # {
      #  "nombre": "Ciencia ficcion"
      # }
      data = request.get_json()
      # CategoriasModel(nombre=data['nombre'])
      # PeliculaModel(titulo=data['titulo'], anio=data['anio'], duracion=data['duracion'])
      # Es crear una instancia de mi nueva categoria
      nuevo_categoria = CategoriasModel(**data)
      # Ya estamos insertando la nueva categoria
      db.session.add(nuevo_categoria)
      # El commit es la confirmacion de la nueva categoria
      db.session.commit()
      return {
         "message": "Creacion exitosa"
      }, 201
