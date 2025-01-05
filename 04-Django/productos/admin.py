from django.contrib import admin
# Paso 01 => Debemos de llamar a nuestra TABLA que queremos que se muestre
from .models import Productos

# Para llamar a jazmmine ( Basta con registrar la tabla de la forma tradicional)

# FORMA 01 de registar mi modelo en el Admin
# admin.site.register(Productos)

# FORMA 02 de registar un modelo en el Admin
@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
   list_display = ["id","titulo", "precio"]