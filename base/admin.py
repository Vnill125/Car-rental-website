from django.contrib import admin
from .models import Vehicles, Location, Order, Contact

# Register your models here.

admin.site.register(Vehicles)
admin.site.register(Location)
admin.site.register(Order)
admin.site.register(Contact)


