from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Category, Thing, Basket
from django.core.paginator import Paginator


def index(request):
    context = {'title': 'Nigg'}
    return render(request, 'FSHL/index.html', context)


def products(request, category_id=None, page_num=1):
    things = Thing.objects.filter(category_id=category_id) if category_id else Thing.objects.all()
    per_page = 3
    paginator = Paginator(things, per_page)
    things_paginator = paginator.page(page_num)

    context = {
        'title': 'Store - Каталог',
        'categories': Category.objects.all(),
        'products': things_paginator,
    }
    return render(request, 'FSHL/products.html', context)


@login_required
def basket_add(request, thing_id):
    thing = Thing.objects.get(id=thing_id)
    baskets = Basket.objects.filter(user=request.user, thing=thing)

    if not baskets.exists():
        Basket.objects.create(user=request.user, thing=thing, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
