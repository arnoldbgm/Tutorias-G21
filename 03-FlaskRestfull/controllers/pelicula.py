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
