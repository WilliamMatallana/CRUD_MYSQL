from django.db import models

from django.db import models

class Aprendiz(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    numero_documento = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=10)
    numero_ficha = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
