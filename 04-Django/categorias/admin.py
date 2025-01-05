from django.contrib import admin
from .models import PostsModel, CategoriaModel

@admin.register(CategoriaModel)
class PostsAdmin(admin.ModelAdmin):
    list_display = ["nombre"]

@admin.register(PostsModel)
class PostsAdmin(admin.ModelAdmin):
    list_display = ["fecha", "titulo", "contenido","categoria_id"]