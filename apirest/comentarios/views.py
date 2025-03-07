from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Comentarios
from .serializers import ComentarioSerializer



def inicio(request):
    comentarios = Comentarios.objects.all()
    return render(request, "comentarios/inicio.html", {"comentarios": comentarios})
