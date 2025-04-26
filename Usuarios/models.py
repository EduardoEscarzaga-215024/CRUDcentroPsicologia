from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# Create your models here.
class RecepcionistaManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, telefono, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre, apellido=apellido, telefono=telefono, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

def create_superuser(self, email, nombre, apellido, telefono, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)  
    return self.create_user(email, nombre, apellido, telefono, password, **extra_fields)

class Recepcionista(AbstractUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    username = None  # Eliminar el campo username

    objects = RecepcionistaManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'telefono']

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


