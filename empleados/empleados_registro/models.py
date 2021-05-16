from django.db import models

# Create your models here.


from django.db import models

# Create your models here.


class Posicion(models.Model):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo


class Empleados(models.Model):
    nombrecompleto = models.CharField(max_length=100)
    empleadocodigo = models.CharField(max_length=6)
    movil = models.CharField(max_length=20)
    posicion = models.ForeignKey(Posicion, on_delete=models.CASCADE)