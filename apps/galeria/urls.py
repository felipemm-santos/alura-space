from django.urls import path

from apps.galeria.views import *

urlpatterns = [
    path('', galeria_view, name='galeria'),
    path('imagem/<int:foto_id>', imagem_view, name='imagem'),
    path('buscar/', buscar_view,name='buscar'),
    path('adicionar/', adicionar_imagem_view, name='adicionar_imagem'),
    path('editar/<int:foto_id>', editar_imagem_view, name='editar_imagem'),
    path('deletar/<int:foto_id>', deletar_imagem_view, name='deletar_imagem'),
    path('categoria/<str:categoria>/', filtrar_por_categoria_view, name='filtro_categoria'),
]