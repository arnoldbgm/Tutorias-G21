from db import db
from sqlalchemy import Column, Integer, String, ForeignKey

class PeliculaModel(db.Model):
   __tablename__ = "peliculas"

   id = Column(Integer, primary_key=True)
   titulo = Column(String(100))
   anio = Column(Integer)
   duracion = Column(Integer)
   # ForeingKey ( 'nombre_tabla.id ' )
   # NO EL NOMBRE DE LA CLASE
   categoria_id = Column(Integer, ForeignKey('categorias.id'))
