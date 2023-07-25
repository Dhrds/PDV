from django.db import models


class Categoria(models.Model):
    nome = models.TextField(max_length=255)
    subtitulo = models.TextField(max_length=255, null=True, blank=True,
                                 default=None)
    titulo = models.TextField(max_length=255, null=True, blank=True,
                              default=None)
    class_html = models.TextField(max_length=255, null=True, blank=True,
                                  default=None)

    def __str__(self):
        return self.nome


class Produtos(models.Model):
    cover = models.ImageField(
        upload_to='covers/%Y/%m/%d/', blank=True, default='')
    nome = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    preco = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,
                                  null=True, blank=True, default=None)

    def __str__(self):
        return self.nome
