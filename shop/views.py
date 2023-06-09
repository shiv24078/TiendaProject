from django.shortcuts import get_object_or_404, render
from .models import Product, Category

def categories(request):
    return {
        "categories": Category.objects.all()
    }


def products_all(request):
    products = Product.products.all()
    order = request.GET.get('order', '')
    if order == 'price':
        products = products.order_by('price')
    return render(request, "shop/home.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/products/category.html', {'category': category, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, "shop/products/detail.html", {"product": product})

def sobrenosotros(request):
    return render(request,"shop/sobrenosotros.html")
