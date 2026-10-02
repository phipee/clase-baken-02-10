from django.urls import path
from .views import mostrar_libros,  mostrar_libros_con_editoriales

urlpatterns = [
    path('', mostrar_libros),
    path('libro/<int:id>', mostrar_libros_con_editoriales),
]

