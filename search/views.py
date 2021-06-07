from django.shortcuts import render
from home.models import Product
from django.db.models import Q

def product_search(request):

    search = request.GET['search']

    product = Product.objects.filter(
        Q(name__icontains=search)
    )

    context = {
        'product':product,
        'search_key':search,
    }

    return render(request, "search/search_result.html", context)
