from rest_framework import viewsets
from .serializers import AutorSerializer, NoticiaSerializer
from .models import Autor, Noticia


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer