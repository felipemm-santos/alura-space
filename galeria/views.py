from django.shortcuts import render
from galeria.models import Fotografias

def galeria_view(request):
    fotos = Fotografias.objects.filter(publicada=True).order_by('-data_publicacao')
    return render(request, 'galeria/index.html', {'cards': fotos})    

def imagem_view(request):
    return render(request, 'galeria/imagem.html')