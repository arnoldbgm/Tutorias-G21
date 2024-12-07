# Es la importacion para usar Flask
from flask import Flask
from db import db
# Esto me permite controlar las migraciones
from flask_migrate import Migrate
from controllers.products import ProductResource, ProductListResource
from flask_restful import Api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MDxoIeTSuZaluCghhiklXjAAPrjxBhbE@autorack.proxy.rlwy.net:53522/railway'

db.init_app(app)
migrate = Migrate(app, db)


api = Api(app)
api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<int:product_id>')


if __name__ == '__main__':
   app.run(debug=True)