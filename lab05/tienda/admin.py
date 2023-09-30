from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto, Cliente

class Personalizacion(admin.ModelAdmin):
    list_display=('id','nombres', 'apellidos', 'correo','telefono', 'fecha_pub')
    search_fields=('apellidos', 'nombres')

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente, Personalizacion)