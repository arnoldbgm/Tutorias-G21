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

class CategoriaPut(Resource):
   def put(self, id):
      data = request.get_json()
      categoria = CategoriasModel.query.get(id)
      if not categoria:
         return {
            "message": "La categoria no existe"
         }, 404
      # La logica para poder actualizar un registro
      categoria.nombre = data.get("nombre", categoria.nombre)
      db.session.commit()
      return{
         "message": "Categoria actualizada",
         "data":{
            "id": categoria.id,
            "nombre": categoria.nombre
         }
      }, 200
   
class CategoriaDelete(Resource):
   def delete(self, id):
      # Siempre se debe de verificar si existe o no la categoria
      data = CategoriasModel.query.get(id)
      if not data:
         return {
            "message": "La categoria no existe"
         }, 404
      db.session.delete(data)
      db.session.commit()
      return {
         "message": "Categoria eliminada exitosamente"
      }, 200