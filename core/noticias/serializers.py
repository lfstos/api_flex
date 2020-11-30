from rest_framework import serializers
from .models import Noticia
from .models import Autor


class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ('id', 'titulo', 'texto', 'autor')


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('autor')