from django.db import models

# Create your models here.


class Autor(models.Model):
    autor = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.autor


class Noticia(models.Model):
    titulo = models.CharField(max_length= 100, null=False)
    texto = models.TextField(null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo