from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import Product


def index_view(request: WSGIRequest):
    product = Product.objects.exclude(leftover = 0)
    context = {
        'product': product
    }
    return render(request, 'index.html', context=context)
