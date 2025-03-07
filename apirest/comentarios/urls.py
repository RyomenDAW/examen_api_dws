from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('api/', include('comentarios.api_urls')),  # Ruta para la API REST
    
]

