from flask_restful import Resource
from flask import request
from models.products import Products  # Ajusta el import según tu estructura
from db import db

class ProductResource(Resource):
    def get(self, product_id):
        product = Products.query.get_or_404(product_id)
        return {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }, 200

    def put(self, product_id):
        product = Products.query.get_or_404(product_id)
        data = request.get_json()
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        db.session.commit()
        return {"message": "Product updated"}, 200

    def delete(self, product_id):
        product = Products.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return {"message": "Product deleted"}, 200

class ProductListResource(Resource):
    def get(self):
        products = Products.query.all()
        return [
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "stock": product.stock
            } for product in products
        ], 200

    def post(self):
        data = request.get_json()
        new_product = Products(
            name=data['name'],
            price=data['price'],
            stock=data['stock']
        )
        db.session.add(new_product)
        db.session.commit()
        return {"message": "Product created", "id": new_product.id}, 201
