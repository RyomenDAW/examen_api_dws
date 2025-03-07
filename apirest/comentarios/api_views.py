from rest_framework import generics
from .models import Comentario
from .serializers import ComentarioSerializer


from django.contrib.auth.models import User, Group  # <-- grupo/roles
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status

class ComentarioListCreate(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer



@api_view(['POST'])
def register_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    grupo = request.data.get("grupo")  # Recibe el rol desde el cliente

    if not username or not password or not grupo:
        return Response({"error": "Faltan datos"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "El usuario ya existe"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    user.save()

    # Verificar que los grupos existen, si no, crearlos
    cliente_group, _ = Group.objects.get_or_create(name="ClienteAPP")
    creador_group, _ = Group.objects.get_or_create(name="CreadorDeAplicaciones")

    # Asignar usuario al grupo correcto
    if grupo == "ClienteAPP":
        user.groups.add(cliente_group)
    elif grupo == "CreadorDeAplicaciones":
        user.groups.add(creador_group)

    # Crear un token de autenticación para el usuario
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"message": "Usuario registrado con éxito", "token": token.key}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"message": "Login exitoso", "token": token.key}, status=status.HTTP_200_OK)
    return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)