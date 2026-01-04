from django import forms
from apps.galeria.models import Fotografia

class FotografiaForm(forms.ModelForm):
    class Meta: 
        model = Fotografia
        exclude = ['data_publicacao', 'publicada', 'usuario']
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'imagem': 'Imagem',
            'legenda': 'Legenda',
            'categoria': 'Categoria',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }