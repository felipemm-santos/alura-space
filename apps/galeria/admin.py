from django.contrib import admin

from apps.galeria.models import Fotografia

# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "titulo", "categoria","usuario", "data_publicacao", "publicada")
    list_display_links = ("id","titulo")
    search_fields = ("titulo", 'categoria', 'usuario')
    list_filter = ("categoria","usuario","publicada")
    list_per_page = 4
    list_editable = ("publicada",)

admin.site.register(Fotografia, ListandoFotografias)