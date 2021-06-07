from django.urls import path
from . import views 

app_name = "home"

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('<int:user_id>/profile', views.profile, name="profile"),
    path('add_profile', views.add_profile, name="add_profile"),
    path('change_password', views.change_password, name="change_password"),
]