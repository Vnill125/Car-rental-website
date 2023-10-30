from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

# Create your models here.

class VehicleQuerySet(models.QuerySet):
    def is_available(self):
        return self.filter(is_available = True)
    
class VehiclesManager(models.Manager):
    def get_queryset(self):
        return VehicleQuerySet(self.model, using=self._db)
    
    def is_available(self):
        return self.get_queryset().is_available()


class Vehicles(models.Model):
    car_model = models.CharField(max_length = 200)
    car_brand = models.CharField(max_length=200)
    mileage = models.IntegerField(null=True, blank=True)
    transmission = models.CharField(max_length=50,null=True, blank=True)
    fuel = models.CharField(max_length=50,null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=7, null=True)
    is_available = models.BooleanField(default = True)
    image = models.ImageField(null=True, blank=True)
    
    objects = VehiclesManager()
    
    def __str__(self):
        return self.car_model
    
    

class Contact(models.Model):
    name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=30, blank=False)
    message = models.TextField(blank= False)



class Location(models.Model):
    pickUpPlace = models.CharField(max_length=105, null=True)
    def __str__(self):
        return self.pickUpPlace 



class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.PROTECT,max_length=70, null=True, blank=False)
    car = models.ForeignKey(Vehicles, on_delete=models.PROTECT, null=True)
    contact_phone = models.CharField(max_length=12, null=True)
    price_per_day = models.IntegerField(null=True, blank=False)
    startRent = models.DateField(auto_now_add=False, null=True)
    endRent = models.DateField(auto_now_add=False, null=True)
    orderDate = models.DateTimeField(auto_now_add=True, null=True)
    pickUp = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __int__(self):
        return self.id
