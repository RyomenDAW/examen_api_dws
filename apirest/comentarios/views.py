from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Comentario
from .serializers import ComentarioSerializer



def inicio(request):
    comentarios = Comentario.objects.all()
    return render(request, "comentarios/inicio.html", {"comentarios": comentarios})
