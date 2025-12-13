from django.urls import path

from galeria.views import galeria_view, imagem_view

urlpatterns = [
    path('', galeria_view, name='galeria'),
    path('imagem/<int:foto_id>', imagem_view, name='imagem'),
]