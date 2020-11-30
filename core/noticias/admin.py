from django.contrib import admin

# Register your models here.

from .models import Noticia, Autor

admin.site.register(Noticia)
admin.site.register(Autor)