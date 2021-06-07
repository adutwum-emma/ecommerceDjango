from django.shortcuts import render, redirect
from home.models import Cart, Product
from django.contrib.auth.models import User
from django.contrib import messages

def my_carts(request, user_id):

    the_id = request.session['member_id']

    if the_id == user_id:

        user_obj = User.objects.get(pk=user_id)

        context = {
            'user_obj':user_obj,
        }

        return render(request, 'product_operation/myCartPage.html', context)
    else:
        messages.info(request, "Forbidden attempt")
        return redirect("/")

def add_to_cart(request):

    product_id = request.POST['product_id']
    user_id = request.POST['user_id']

    try:
        user = User.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)

        if Cart.objects.filter(
            user=user,
            product=product
        ).exists():
            messages.info(request, "Product already added on your cart")
            return redirect('/')
        else:
            cart = Cart.objects.create(
                user=user,
                product=product
            )
    except (ValueError):
        messages.info(request, "You need to login before you can perform such action !")
        return redirect('/')
    else:
        cart.save()
        messages.info(request, "Cart added successfully...")
        return redirect('/')

def delete_cart(request):

    cart_id = request.POST['cart_id']
    user_id = request.POST['user_id']

    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    messages.info(request, "Cart removed successfully")
    return redirect('/product_operation/' + str(user_id))
