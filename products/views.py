
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, Product_id):
    """ A view to show individual product details """

    products = get_objects_or_404(product, pk=Product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
