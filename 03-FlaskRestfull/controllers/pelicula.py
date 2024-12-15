from db import db
from models.pelicula import PeliculaModel
from flask_restful import Resource
from flask import request
import cloudinary.uploader


class PeliculasList(Resource):
    def get(self):
        resultado_consulta = PeliculaModel.query.all()
        return [
            {
                "id": titulo.id,
                "titulo": titulo.titulo,
                "anio": titulo.anio,
                "duracion": titulo.duracion,
                "imagen_url": titulo.imagen_url,
                "categoria_id": titulo.categoria_id
            } for titulo in resultado_consulta
        ], 200


class PeliculaPost(Resource):
    def post(self):
        data = request.form
        archivo = request.files['imagen_url']
        # PAra subir la imagen a Clodinary se debe hacer lo siguiente
        # Debes de importar el cloudinary.uploader
        imagen_url = None
        if archivo:
            try:
                # Esto me responde con diversas propiedades
                resultado = cloudinary.uploader.upload(
                    archivo, folder="peliculas/")
                # Es el secure_url => Es la ruta segura para que pueda consumir mi imagen de cloudinary
                imagen_url = resultado['secure_url']
            except Exception as err:
                return {
                    "error": f"Hubo un error al subir la imagen: {str(err)}"
                }, 500
        nueva_pelicula = PeliculaModel(
            titulo = data["titulo"],
            anio = data["anio"],
            duracion = data["duracion"],
            categoria_id = data["categoria_id"],
            imagen_url= imagen_url
        )
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
                "imagen_url": nueva_pelicula.imagen_url
            }
        }, 201


class PeliculaDelete(Resource):
    def delete(self, id):
        pelicula = PeliculaModel.query.get(id)
        if not pelicula:
            return {
                "message": "Pelicula no encontrada"
            }, 404

        # db.session.delete o add
        db.session.delete(pelicula)
        db.session.commit()

        return {
            "message": "Pelicula eliminada exitosamente"
        }, 200
