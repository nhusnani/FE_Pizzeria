import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Pizzeria.settings")

import django 
django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()

p = Pizza.objects.get(id=1)
print()

toppings = p.topping_set.all()
for topping in toppings:
    print(topping)