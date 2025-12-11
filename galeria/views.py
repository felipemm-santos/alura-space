from django.shortcuts import render

def galeria_view(request):
    return render(request, 'galeria/index.html')

def imagem_view(request):
    return render(request, 'galeria/imagem.html')