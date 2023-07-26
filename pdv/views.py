from django.shortcuts import render
from .models import Produtos, Categoria


def home(request):
    categoria = Categoria.objects.all()
    produtos = Produtos.objects.all().select_related('categoria')
    return render(request, 'home.html', {'produtos': produtos,
                                         'categorias': categoria})


def about(request):
    return render(request, 'about.html')


def service(request):
    categoria = Categoria.objects.all()
    produtos = Produtos.objects.all().select_related('categoria')
    return render(request, 'service.html', {'produtos': produtos,
                                            'categorias': categoria})


def menu(request):
    categoria = Categoria.objects.all()
    produtos = Produtos.objects.all().select_related('categoria')
    return render(request, 'menu.html', {'produtos': produtos,
                                         'categorias': categoria})


def booking(request):

    return render(request, 'booking.html',)


def team(request):
    categoria = Categoria.objects.all()
    produtos = Produtos.objects.all().select_related('categoria')
    return render(request, 'team.html', {'produtos': produtos,
                                         'categorias': categoria})


def testimonial(request):
    categoria = Categoria.objects.all()
    produtos = Produtos.objects.all().select_related('categoria')
    return render(request, 'testimonial.html', {'produtos': produtos,
                                                'categorias': categoria})


def contact(request):
    categoria = Categoria.objects.all()
    produtos = Produtos.objects.all().select_related('categoria')
    return render(request, 'contact.html', {'produtos': produtos,
                                            'categorias': categoria})
