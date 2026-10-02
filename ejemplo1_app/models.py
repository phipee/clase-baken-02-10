from django.db import models


class autor(models.Model):
    nombre = models.CharField(max_length=250)
    def __str__(self):
        return self.nombre 

class editorial(models.Model):
    nombre_editorial = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre_editorial
    
class libro(models.Model):
    titulo = models.CharField(max_length=250)
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    editorial = models.ManyToManyField(editorial )
    def __str__(self):
        return self.titulo
       