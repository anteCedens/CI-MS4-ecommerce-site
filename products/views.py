from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    if request.GET:
        """
        'q' is the value of the 'name' attribute
        assigned to the search bar in base.html
        """
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria...")
                return redirect(reverse('products'))

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)