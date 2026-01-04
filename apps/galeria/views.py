from django.shortcuts import get_object_or_404, redirect, render
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForm
from django.contrib import messages

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

    return render(request, "galeria/index.html", {'fotografias': fotos})

def adicionar_imagem_view(request):
    if not request.user.is_authenticated:        
        return redirect('login')   

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():            
            foto = form.save(commit=False)
            foto.usuario = request.user
            foto.save()
            messages.success(request, 'Imagem adicionada com sucesso!')
            return redirect('imagem', foto_id=foto.id)
        else:
            messages.error(request, 'Erro ao adicionar a imagem. Verifique os dados preenchidos.')      

    form = FotografiaForm()
    return render(request, 'galeria/adicionar_imagem.html', {'form': form})

def editar_imagem_view(request, foto_id):

    if not request.user.is_authenticated:
        return redirect('login')
    
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForm(instance=fotografia)

    if request.method == 'PUT':
        form = FotografiaForm(request.PUT, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso!')
        else:
            messages.error(request, 'Erro ao editar a imagem. Verifique os dados preenchidos.')

        return redirect('imagem', foto_id=fotografia.id)

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem_view(request, foto_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    fotografia.delete()
    return redirect('galeria')

def filtrar_por_categoria_view(request, categoria):
    if not request.user.is_authenticated:
        return redirect('login')

    fotos = Fotografia.objects.filter(
                publicada=True,
                categoria__iexact=categoria
            ).order_by('-data_publicacao')
    
    return render(request, "galeria/index.html", {'fotografias': fotos})