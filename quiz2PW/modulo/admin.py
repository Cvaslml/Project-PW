from django.contrib import admin
from .models import Categoria, Libro

# Clase administradora personalizada para Categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # Muestra nombre y descripción
    search_fields = ['nombre']  # Permite buscar por nombre
    list_filter = ('nombre',)  # Filtro por nombre de categoría

# Clase administradora personalizada para Libro
class LibroAdmin(admin.ModelAdmin):
    # Personaliza las columnas que se mostrarán en la lista de administración
    list_display = ('titulo', 'autor', 'categoria', 'fecha_publicacion')  # Solo se mostrarán estos campos
    
    # Permite la búsqueda por título o autor
    search_fields = ['titulo', 'autor']
    
    # Añade filtros laterales por categoría y fecha de publicación
    list_filter = ('categoria', 'fecha_publicacion')

# Registrar ambos modelos con sus respectivas configuraciones
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Libro, LibroAdmin)
