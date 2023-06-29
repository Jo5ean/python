from django.shortcuts import render, redirect
from .forms  import ProductForm, SearchForm
from .models import Product

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def search_products(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            products = Product.objects.filter(name__icontains=keyword)
            return render(request, 'search_results.html', {'products': products})
    else:
        form = SearchForm()
    return render(request, 'search_products.html', {'form': form})
