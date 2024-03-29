from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
   name = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   
   def __str__(self):
       return self.name     

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(blank = False, null = True)

    def __str__(self):
        return self.name

    @property 
    def imageURl(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


    @property 
    def get_cart_total(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitem])
        return total

    @property 
    def get_cart_item(self):
        orderitem = self.orderitem_set.all()
        total = sum([item.quanatity for item in orderitem])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quanatity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.price * self.quanatity
        return total


class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    post_code = models.IntegerField(null=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

