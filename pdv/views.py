from django.shortcuts import render
from .models import Produtos, Categoria


def home(request):
    categoria = Categoria.objects.all()
    produtos = Produtos.objects.all().select_related('categoria')
    print(produtos)
    return render(request, 'home.html', {'produtos': produtos,
                                         'categorias': categoria})
