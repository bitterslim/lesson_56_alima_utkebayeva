from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from webapp.form import ProductForm
from webapp.models import Product


def add_product(request: WSGIRequest):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_add.html', context={'form': form})

    form = ProductForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'product_add.html', context={'form': form})
    else:
        product = Product.objects.create(**form.cleaned_data)
        return redirect(f'/', pk=product.pk)

def detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context=context)
def update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'product_update.html', context={'form': form, 'product': product})

    form = ProductForm(instance=product)
    return render(request, 'product_update.html', context={'form': form, 'product': product})


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':

        return render(request, 'product_delete.html', context={'product': product})

    elif request.method == 'POST':
        product.delete()
        return redirect('index')