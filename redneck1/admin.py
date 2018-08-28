from django.contrib import admin
from .models import Cruise,Passenger,ShoppingCartItem,Product,OrderItem

# Register your models here.
admin.site.register(Cruise)
admin.site.register(Passenger)
admin.site.register(ShoppingCartItem)
admin.site.register(Product)
admin.site.register(OrderItem)
