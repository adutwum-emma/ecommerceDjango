from django.contrib import admin
from .models import Profile, Category, Product, Order, Cart, Country, Region

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Country)
admin.site.register(Region)
