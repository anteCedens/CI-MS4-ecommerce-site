from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# 'Q' is used to generate a search query (mainly the 'OR' logic bit)
from django.db.models import Q
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

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

            """
            The pipe ('|') is what generates the OR statement/logic
            for the queries,
            and the 'i' in front of 'contains' makes
            the queries case insensitive
            """
            queries = Q(name__icontains=query) | Q(author__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)