from django.contrib import admin
from .models import libro, autor, editorial
# Register your models here.
admin.site.register(autor)
admin.site.register(libro)
admin.site.register(editorial)