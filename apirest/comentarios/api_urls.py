from django.urls import path
from .api_views import ComentarioListCreate, ComentarioDetail, register_user, login_user

urlpatterns = [
    path('comentarios/', ComentarioListCreate.as_view(), name='comentario-list-create'),
    path('comentarios/<int:pk>/', ComentarioDetail.as_view(), name='comentario-detail'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]
