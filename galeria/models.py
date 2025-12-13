from django.db import models

# Create your models here.

class Fotografias (models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='fotos/')
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo