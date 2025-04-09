from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('libros/', views.lista_libros, name='lista_libros'),  # Vista de lista de libros
    path('libro/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),  # Vista de detalles de un libro
]