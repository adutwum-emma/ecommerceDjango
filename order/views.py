from django.shortcuts import render, redirect
from home.models import Product, Order
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def order_page(request, product_id):

    user_id = request.session['member_id']

    now = datetime.datetime.now()

    if request.method == "POST":
        user_id = request.POST['user_id']
        phone = request.POST['phoneNumber']
        address = request.POST['address']
        no_items = request.POST['num_of_items']

        try:
            
            user = User.objects.get(pk=user_id)
            product = Product.objects.get(pk=product_id)
            amount = float(product.price) * float(no_items)
            order = Order.objects.create(
                user=user,
                product=product,
                momo=phone,
                number_of_item=no_items,
                address=address,
                total_amount=amount,
            )
            
        except (KeyError):
            messages.info(request, "Invalid action !")
            return redirect("/order/" + str(product_id))
        else:
            order.save()
            messages.info(request, "Order done successfully...")

            #Html message to the user
            #html_content = render_to_string("order/email_receipt.html", {'user':user, 'product':product, 'now':now, 'amount':amount, 'items':no_items})
            #text_content = strip_tags(html_content)

            #email = EmailMultiAlternatives(
                #" TBS - Your order report",
                #text_content,
                #"emmanuelkyeiadutwum@gmail.com",
                #[user.email],
            #)
            #email.attach_alternative(html_content, "text/html")
            #email.send()


            return redirect("/order/" + str(product_id))

    else:
        if request.session['member_id'] == 0:
            messages.info(request, "You cannot access page until you login")
            return redirect('/')
        else:
            product = Product.objects.get(pk=product_id)
            context={
                'product':product,
            }
            return render(request, "order/orderPage.html", context)

def order_history(request, user_id):

    user = User.objects.get(pk=user_id)

    try:
        if request.session['member_id'] != user_id:
            messages.info(request, "You were not permitted to access that page")
            return redirect("/")

        else:
            context = {
                'user':user,
            }

            return render(request, "order/order_history.html", context)

    except(KeyError):
        messages.info(request, "You were not permitted to access that page")
        return redirect("/")


def order_receipt(request, order_id):

    template_path = 'order/order_receipt.html'
    now = datetime.datetime.now()
    order = Order.objects.get(pk=order_id)
    context = {
        'product': 'Your order',
        'now': now,
        'order': order,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #if want to download 
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    #if you want to display in the browser get rid of the attatchment
    response['Content-Disposition'] = 'filename="TBS_order_receipt.pdf"'


    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
