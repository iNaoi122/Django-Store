from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "digital")
    list_filter = ("price", "digital")

admin.site.register(Product, ProductAdmin)

admin.site.register(Customer)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)
