from django.urls import path
from .views import mostrar_libros, mostrar_editoriales_libros, mostrar_libros_con_editoriales

urlpatterns = [
    path('', mostrar_libros),
    path('', mostrar_editoriales_libros),
    path('', mostrar_libros_con_editoriales),
]

