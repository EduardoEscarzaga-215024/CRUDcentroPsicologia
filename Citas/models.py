from django.db import models
from Usuarios.models import Recepcionista

# Create your models here.
class Cita(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    telefono_paciente = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField(blank = True, null = True)
    recepcionista = models.ForeignKey(Recepcionista, on_delete=models.CASCADE)

    def __str__(self):
        return f"{selk.nombre_paciente} - {self.fecha} - {self.hora}"