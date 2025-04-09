from django.shortcuts import render, get_object_or_404
from .models import Libro

def index(request):
    return render(request, 'modulo/index.html')

def lista_libros(request):
    libros = Libro.objects.all()  # Obtén todos los libros
    return render(request, 'modulo/libros.html', {'libros': libros})

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)  # Obtiene el libro por su ID
    return render(request, 'modulo/detalle_libro.html', {'libro': libro})