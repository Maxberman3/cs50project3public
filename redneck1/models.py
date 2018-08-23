from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Cruise(models.Model):
    origin=models.CharField(max_length=300)
    destination=models.CharField(max_length=300)
    departure=models.CharField(max_length=300)
    arrival=models.CharField(max_length=300)
    tripback=models.CharField(max_length=300)
    craft=models.CharField(max_length=300)
    crew1=models.CharField(max_length=300,default="One Eye Mcgruffin", editable=False)
    crew2=models.CharField(max_length=300)
    crew3=models.CharField(max_length=300)

    def __str__(self):
        return "{} to {}".format(self.origin,self.destination)


class Passenger(models.Model):
    first_name=models.CharField(max_length=26)
    last_name=models.CharField(max_length=26)
    cruise=models.ForeignKey(Cruise,on_delete=models.CASCADE,related_name='passengers')

    def __str__(self):
        return self.first_name+" "+self.last_name

class Review(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
    submission_date=models.DateField(auto_now_add=True)
    cruise=models.ForeignKey(Cruise,on_delete=models.CASCADE,related_name='reviewsof')
    contents=models.CharField(max_length=3000)

class Product(models.Model):
    name=models.CharField(max_length=300)
    description=models.CharField(max_length=1000)
    price=models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.description

class ShoppingCartItem(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,related_name='shoppingcart')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='inshoppingcarts')
    quantity=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    price=models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return "{} x {} for a total of ${:,.2f}".format(self.product,self.quantity,self.price)
