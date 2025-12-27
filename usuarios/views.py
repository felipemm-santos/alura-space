from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request, 'usuarios/login.html')

def cadastro_view(request):
    return render(request, 'usuarios/cadastro.html')

def logout_view(request):
    pass

