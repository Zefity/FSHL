from django.shortcuts import render

from .models import Category, Thing


def index(request):
    context = {'title': 'Nigg'}
    return render(request, 'FSHL/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Thing.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'FSHL/products.html', context)
