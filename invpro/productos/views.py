from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'productos/index.html')

def perfil(request):
    return render(request, 'productos/perfil.html')