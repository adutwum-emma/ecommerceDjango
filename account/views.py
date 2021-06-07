from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def sign_up(request):

    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email= request.POST['email']
    password = request.POST['password']
    con_password = request.POST['con_password']

    if password == con_password:

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exist")
            return redirect('/')
        elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('/')
        else:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user.save()
            messages.info(request, "Account registered success...")
            send_mail(
                'TBS - Account registered successfully',
                'Hello, '+first_name + " " + 
                last_name + ", ToskyBrownShop (TBS) welcomes you." + "Your account has been registered successfully",
                'emmanuelkyeiadutwum@gmail.com',
                [email],
                fail_silently = True,
            )
            return redirect('/')
    else:
        messages.info(request, "Passwords do not match")
        return redirect('/')

def login(request):

    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        request.session['member_id'] = user.id
        messages.info(request, "Login success...")
        return redirect('/')
    else:
        messages.info(request, "Invalid login")
        return redirect('/')

def logout(request):
    if request.session.set_expiry(0):
        messages.info(request, "Session expired...login again")
        return redirect('/')
    else:
        auth.logout(request)
        request.session['member_id'] = 0
        messages.info(request, "Logout success..")
        return redirect('/')