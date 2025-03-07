from rest_framework import serializers
from .models import Comentarios

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'
