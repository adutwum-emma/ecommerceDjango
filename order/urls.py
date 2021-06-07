from django.urls import path
from . import views 

app_name = "order"

urlpatterns = [
    path('<int:product_id>', views.order_page, name="order_page"),
    path('<int:user_id>/order_history', views.order_history, name="order_history"),
    path('<int:order_id>/order_receipt', views.order_receipt, name="order_receipt"),
]