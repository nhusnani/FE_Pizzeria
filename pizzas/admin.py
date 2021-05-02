from django.contrib import admin

# Register your models here.
#register model to admin site
#want to register Pizza
from .models import Pizza, Toppings

admin.site.register(Pizza)
admin.site.register(Toppings)
#manage model Pizza through admin site