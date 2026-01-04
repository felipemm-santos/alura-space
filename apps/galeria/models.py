from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fotografia (models.Model):
    OPCOES_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]

    titulo = models.CharField(max_length=200,null=False, blank=False)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    legenda = models.CharField(max_length=300, blank=True, null=True)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA,blank=True, null=True)
    publicada = models.BooleanField(default=True)

    usuario = models.ForeignKey(
        to=User, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name='user'
        )

    def __str__(self):
        return self.titulo
    
    def __repr__(self):
        return self.titulo