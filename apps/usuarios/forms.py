from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o seu nome de login',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        )
    )

    def clean_nome_login(self):
        nome_login=self.cleaned_data.get('nome_login')

        if nome_login:
            nome_login=nome_login.strip()
            if ' ' in nome_login:
                raise forms.ValidationError('Nome de login não pode conter espaços em branco.'
                )
        return nome_login

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o seu nome de cadastro',
            }
        )
    )
    email=forms.EmailField(
        label='E-mail', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o seu e-mail',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        )
    )
    confirma_senha=forms.CharField(
        label='Confirmação de Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme a sua senha',
            }
        )
    )

    def clean_nome_cadastro(self):
        nome_cadastro=self.cleaned_data.get('nome_cadastro')

        if nome_cadastro:
            nome_cadastro=nome_cadastro.strip()
            if ' ' in nome_cadastro:
                raise forms.ValidationError('Nome de cadastro não pode conter espaços em branco.'
                )
        return nome_cadastro
    
    def clean_email(self):
        email=self.cleaned_data.get('email')

        if email:
            email=email.strip()
            if ' ' in email:
                raise forms.ValidationError('E-mail não pode conter espaços em branco.'
                )
            if '@' not in email:
                raise forms.ValidationError('E-mail inválido.'
                )
        return email
    
    def clean_confirma_senha(self):
        senha=self.cleaned_data.get('senha')
        confirma_senha=self.cleaned_data.get('confirma_senha')

        if senha and confirma_senha and senha != confirma_senha:
            raise forms.ValidationError('As senhas não coincidem.'
            )
        return confirma_senha

