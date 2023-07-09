from django.db import models


class Tarjeta(models.Model):
    titulo = models.CharField(max_length=100, verbose_name = 'Titulo', unique=True)
    imagen = models.ImageField(upload_to='media/', null=True, blank=True)
    descripcion = models.TextField(verbose_name = 'Descripción')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
