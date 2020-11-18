from django.shortcuts import render
from .models import Product, Category, SubCategory


def all_products(request):
    """ A view to return the product page """
    products = Product.objects.all()
    categories= None
    sub_categories= None

    if request.GET:
        if sub_category in request.GET:
            sub_categories = request.GET['sub_category'].split[',']
            products = products.filter(sub_category__name__in=sub_categories)
            sub_categories = SubCategory.objects.filter(name__in=sub_categories)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)
