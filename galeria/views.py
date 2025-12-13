from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia

def galeria_view(request):
    fotos = Fotografia.objects.filter(publicada=True).order_by('-data_publicacao')
    return render(request, 'galeria/index.html', {'fotografias': fotos})    

def imagem_view(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})