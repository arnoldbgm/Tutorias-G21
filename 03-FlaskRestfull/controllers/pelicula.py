from db import db
from models.pelicula import PeliculaModel
from flask_restful import Resource
from flask import request


class PeliculasList(Resource):
    def get(self):
        resultado_consulta = PeliculaModel.query.all()
        return [
            {
                "id": titulo.id,
                "titulo": titulo.titulo,
                "anio": titulo.anio,
                "duracion": titulo.duracion
            } for titulo in resultado_consulta
        ], 200


class PeliculaPost(Resource):
    def post(self):
        data = request.get_json()
        nueva_pelicula = PeliculaModel(**data)
        db.session.add(nueva_pelicula)
        db.session.commit()
        return {
            "message": "Creacion exitosa",
            "pelicula": {
                "id": nueva_pelicula.id,
                "titulo": nueva_pelicula.titulo,
                "anio": nueva_pelicula.anio,
                "duracion": nueva_pelicula.duracion,
                "categoria_id": nueva_pelicula.categoria_id,
            }
        }, 201
