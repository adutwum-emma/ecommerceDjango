from django.db import models
from django.contrib.auth.models import auth, User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=200, verbose_name="Phone Number")
    country = models.CharField(max_length=200, verbose_name="Country/National")
    region = models.CharField(max_length=200, verbose_name="Region")
    city = models.CharField(max_length=200, verbose_name="City/Town")
    address = models.CharField(max_length=200, verbose_name="Adress")
    date_edited = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.phone + "_" + self.address
    
    class Meta:

        verbose_name_plural = "Profiles"

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Categories")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = "Categories"



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Names")
    description = models.TextField()
    price = models.FloatField()
    old_price = models.FloatField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="product_pics")
    buy = models.ManyToManyField(User, through="Order")
    on_promotion = models.BooleanField(default=False)

    def __str__(self):
        
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Products"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_orderd = models.DateTimeField(auto_now_add=True)
    number_of_item = models.IntegerField()
    address = models.CharField(max_length=200)
    momo = models.CharField(max_length=20)
    total_amount = models.FloatField()
    is_delivered = models.BooleanField(default=False)
    is_processing = models.BooleanField(default=True)


    def __str__(self):

        return self.product.name + " _" + self.user.username

    class Meta:

        verbose_name_plural = "Orders"


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " " + self.product.name

    class Meta:

        verbose_name_plural = "Carts"

class Country(models.Model):
    country_name = models.CharField(max_length=200)


    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ["country_name"]

class Region(models.Model):
    region_name = models.CharField(max_length=200)


    def __str__(self):
        return self.region_name



