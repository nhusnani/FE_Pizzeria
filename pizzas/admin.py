from django.contrib import admin


from .models import Pizza, Toppings, Comment

admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Comment)
