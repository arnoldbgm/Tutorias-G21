from django.db import models

# Create your models here.
class CategoriaModel(models.Model):
    nombre = models.CharField(max_length=255)
    class Meta:
        db_table = "categorias"
    
   #  Como se va a mostrar la informacion al cliente
   # Cuando creamos metodos magicos __str__
   # NO ES NECESARIO EJECUTAR UNA MIGRACION
    def __str__(self):
        return self.nombre


class PostsModel(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
   #  columna _id
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)

    class Meta:
        db_table = "posts"