from django.shortcuts import get_object_or_404, redirect, render
from apps.galeria.models import Fotografia

def galeria_view(request):
    if not request.user.is_authenticated:
        return redirect('login')    
    
    fotos = Fotografia.objects.filter(
                publicada=True,
            ).order_by('-data_publicacao')
    return render(request, 'galeria/index.html', {'fotografias': fotos})

def imagem_view(request, foto_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    fotos = Fotografia.objects.filter(
                publicada=True,
            ).order_by('-data_publicacao')
    
    if 'buscar' in request.GET:
        termo = request.GET['buscar']   
        if termo:
            fotos = fotos.filter(titulo__icontains=termo)

    return render (request, "galeria/buscar.html", {'fotografias': fotos})
