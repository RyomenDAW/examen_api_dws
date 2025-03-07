from django.contrib.auth.models import User
from django.db import models

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    texto = models.TextField()
    aplicacion = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Se refiere a User

    def __str__(self):
        return f"{self.usuario.username} - {self.aplicacion}"
