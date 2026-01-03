from django.shortcuts import render, redirect
from apps.usuarios.forms import CadastroForms, LoginForms  
from django.contrib import messages, auth   
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():          
            nome_login = form.cleaned_data['nome_login']
            senha = form.cleaned_data['senha']

            # autenticação do usuário
            user = auth.authenticate(username=nome_login, password=senha)

            if user is None:
                messages.error(request, 'Nome de usuário ou senha inválidos.')
                return redirect('login')
                
            auth.login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('galeria')

    return render(request, 'usuarios/login.html', {'form': LoginForms()})

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        # validação do formulário
        if form.is_valid():            
            
            nome_cadastro = form.cleaned_data['nome_cadastro']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            # verificação de existência de usuário
            if User.objects.filter(username=nome_cadastro).exists():
                messages.error(request, 'Nome de usuário já existe.')
                return redirect('cadastro')
            
            # verificação de existência de e-mail
            if User.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já cadastrado.')
                return redirect('cadastro')
            
            # Criação do usuário
            user = User.objects.create_user(
                username=nome_cadastro, 
                email=email, 
                password=senha
                )
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça o login.')

            return redirect('login')
    return render(request, 'usuarios/cadastro.html', {'form': CadastroForms()})

def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

