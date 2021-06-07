from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from datetime import datetime, date
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from home.models import Profile, Country, Region
from django.contrib.auth import hashers
from django.contrib.auth.models import User


def index(request):

    product = Product.objects.all()

    context = {
        'product': product,
    }

    return render(request, 'home/products.html', context)

def contact(request):

    username = request.POST['user_name']
    email = request.POST['user_email']
    subject = request.POST['subject']
    message = request.POST['message']

    send_mail(
        username + " - "+ email,
        message,
        email,
        ["emmanuelkyeiadutwum@gmail.com"],
        fail_silently = True,
    )

    messages.info(request, "Your message sent successfully")
    return redirect(url)

def profile(request, user_id):

    my_user = User.objects.all()
    country = Country.objects.all()
    region = Region.objects.all()

    context = {
        'profile':profile,
        'country':country,
        'region':region,
    }

    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        
        user = User.objects.get(id=user_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        messages.info(request, "Your settings have been saved successfully")
        return redirect("/" + str(user_id) + "/profile")
    else:
        if request.session['member_id'] == 0:
            return redirect('/')
        else:
            return render(request, 'home/profile_page.html', context)

def add_profile(request):

    gender = request.POST['gender']
    phone = request.POST['phone']
    address= request.POST['address']
    country = request.POST['country']
    region = request.POST['region']
    dob = request.POST['dob']
    city = request.POST['city']
    user_id = request.POST['user_id']

    my_user = User.objects.get(id=user_id)
    profile = Profile()

    profile.user = my_user
    profile.dob = dob
    profile.gender = gender
    profile.phone = phone
    profile.address = address
    profile.country = country
    profile.region = region
    profile.city = city
    profile.save()

    messages.info(request, "Profile updated successfully !")
    return redirect("/" + str(user_id) + "/profile")


def change_password(request):

    if request.method == "POST":
        user_id = request.POST["user_id"]
        old_pass = request.POST["old_pass"]
        new_pass = request.POST["new_pass"]
        conf_pass = request.POST["conf_pass"]

        user = User.objects.get(id=user_id)
        check = hashers.check_password(old_pass, user.password)

        if check:
            if new_pass == conf_pass:
                user.set_password(conf_pass)
                user.save()
                messages.info(request, "Password changed successfully !")
                request.session['member_id'] = 0
                return redirect("/")
            else:
                messages.info(request, "New passwords do not match !")
                return redirect("/change_password")
        else:
            messages.info(request, "Incorrect password")
            return redirect("/change_password")


    else:
        if request.session['member_id'] == 0:
            return redirect("/")
        else:
            return render(request, "home/change_pass.html")
