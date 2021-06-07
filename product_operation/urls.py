from django.urls import path
from . import views

app_name = "product_operation"

urlpatterns = [
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path('<int:user_id>', views.my_carts, name="my_carts"),
    path('delete_cart', views.delete_cart, name="delete_cart"),
]