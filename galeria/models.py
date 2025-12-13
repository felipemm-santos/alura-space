from django.db import models

# Create your models here.

class Fotografias (models.Model):
    titulo = models.CharField(max_length=200,null=False, blank=False)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo