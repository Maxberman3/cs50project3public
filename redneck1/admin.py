from django.contrib import admin
from .models import Cruise, Passenger, ShoppingCartItem, Product

# Register your models here.
admin.site.register(Cruise)
admin.site.register(Passenger)
admin.site.register(ShoppingCartItem)
admin.site.register(Product)
