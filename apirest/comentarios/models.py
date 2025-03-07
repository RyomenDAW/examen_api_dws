from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    ADMINISTRADOR = 1
    CREADORDEAPLICACIONES = 2
    CLIENTE = 3
    
    ROLES=(
        (ADMINISTRADOR, 'administrador'),
        (CREADORDEAPLICACIONES, 'creadoraplicacinones'),
        (CLIENTE, 'clientes'),
    )
    
    rol = models.PositiveSmallIntegerField(
        choices=ROLES, default=3
    )    
    
class AplicacionMovil(models.Model):
    nombre = models.CharField(max_length=100)
    fechaCreacion = models.DateField()

    def __str__(self):
        return self.nombre


class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    texto = models.TextField()
    aplicacion = models.ForeignKey(AplicacionMovil, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Se refiere a User
    puntuacioncomentario = models.IntegerField(default=1, choices=((i,i) for i in range(1, 6)))   #Aparecera como desplegable del 1 al 5 
    fecha_comentario = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.usuario.username} - {self.aplicacion}"



