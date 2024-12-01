# Es la importacion para usar Flask
from flask import Flask
from db import db
# Esto me permite controlar las migraciones
from flask_migrate import Migrate

from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/db_pos'

db.init_app(app)
migrate = Migrate(app, db)


# Crearemos nuestra primera tabla
class Products(db.Model):
   #Colocamos un nombre la tabla
   __tablename__ = "product"

   #Column(Tipo)
   id = Column(Integer, primary_key=True)
   name = Column(String(100))
   price = Column(Float)
   stock = Column(Integer)

class Purchanse(db.Model):
   __tablename__ = "purchanse"
   id = Column(Integer, primary_key=True)
   quantity = Column(Integer)
   price = Column(Float)
   time = Column(TIMESTAMP)
   # ForeingKey('NOMBRE_TABLA.atributo')
   producto_id = Column(Integer, ForeignKey('product.id'))

class Sale(db.Model):
   __tablename__ = "sale"
   id = Column(Integer, primary_key=True)
   quantity = Column(Integer)
   price = Column(Float)
   time = Column(TIMESTAMP)
   producto_id = Column(Integer, ForeignKey('product.id'))

# Este es mi archivo principal, estamos en modo de prueba
if __name__ == '__main__':
   app.run(debug=True)