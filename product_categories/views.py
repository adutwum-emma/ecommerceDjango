from django.shortcuts import render
from home.models import Category, Product

def categories(request):

    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'category':category,
        'my_pro':product,
    }

    return render(request, "product_categories/categoriesPage.html", context)
