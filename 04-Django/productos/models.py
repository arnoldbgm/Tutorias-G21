from django.db import models

# models.Models => Por que vamos a herederar la capacidad
# de crear tablas usando Django


class Productos(models.Model):
    titulo = models.CharField(max_length=255)
    precio = models.FloatField()

    class Meta:
        db_table = 'productos'