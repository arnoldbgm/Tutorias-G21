from db import db
from sqlalchemy import Column, String, Integer, Float

# Crearemos nuestra primera tabla
class Products(db.Model):
   #Colocamos un nombre la tabla
   __tablename__ = "product"

   #Column(Tipo)
   id = Column(Integer, primary_key=True)
   name = Column(String(100))
   price = Column(Float)
   stock = Column(Integer)
