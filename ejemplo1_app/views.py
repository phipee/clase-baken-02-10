from django.shortcuts import render
from .models import libro
# Create your views here.
def mostrar_libros(request):
    lista = libro.objects.all()
    return render(request, "libros.html", {'libros': lista})
    
def mostrar_libros_con_editoriales(request):
    
    return render(request, "libros_con_editoriales.html")

def mostrar_editoriales_libros(request):
    return render(request, "editoriales_y_libros.html")