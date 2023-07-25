from django.shortcuts import render
from .models import Produtos


def home(request):
    produtos = Produtos.objects.all().select_related('categoria')
    print(produtos)
    return render(request, 'home.html', {'produtos': produtos})
