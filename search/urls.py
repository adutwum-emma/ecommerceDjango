from django.urls import path
from . import views 

app_name = "search"

urlpatterns = [
    path('product_search', views.product_search, name="product_search")
]