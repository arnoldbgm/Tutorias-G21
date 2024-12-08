# Para crear la tabla de mi base de datos
# Paso 01: Debo de importar
from db import db
from sqlalchemy import Column, Integer, String

# Paso 02: Crear la tabla
class CategoriasModel(db.Model):
   # Colocamos el nombre de la tabla
   __tablename__ = "categorias"

   # Creamos las columnas
   id = Column(Integer, primary_key=True)
   nombre = Column(String)