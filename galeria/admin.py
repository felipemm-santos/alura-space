from django.contrib import admin

from galeria.models import Fotografias

# Register your models here.

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "titulo", "categoria", "data_publicacao", "publicada")
    list_display_links = ("id","titulo")
    search_fields = ("titulo", 'categoria')
    list_filter = ("categoria",)
    list_per_page = 4
    list_editable = ("publicada",)

admin.site.register(Fotografias, ListandoFotografias)