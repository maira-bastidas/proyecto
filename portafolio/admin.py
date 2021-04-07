from django.contrib import admin
# Register your models here.
from portafolio.models import Producto, Categoria
@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
    list_display = ('pk', 'nombre_gallo', 'padre', 'madre', 'categoria', )
    ordering = ('nombre_gallo',)

admin.site.register(Categoria)
