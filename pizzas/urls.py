#defines URL patterns for pizzas

from django.urls import path 
#import path() function which is needed when mapping URLs to views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
#import views.py module from same directory as the current urls.py module
#variable app_name helps django distinguish this urls.py file from the files of the same name in other apps within the project
#the variable urlpattern in this module is a list of individual pages that can be requested from the pizzas app



app_name = 'pizzas'
urlpatterns = [
    #home page
    path('', views.index, name='index'),
    #page that shows available pizzas
    path('availpizzas/', views.availpizzas, name = 'availpizzas'),
    #detailed page for a single pizza
    path('availpizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    #tells django to look for urls that have word availpizza after base url. Then <int:pizza_id matches an integer between two forward slashes and stores integer in pizza_id value argument
    path('new_toppings/<int:pizza_id>/',views.new_toppings, name='new_toppings'),
    #url pattern matches url where id is a number matching the pizza id, the code <int:pizza_id> captures numerical value and assigns it to variable pizza_id
    #when matching url this pattern requested, django send the request and the topic's ID to new_comment() view function
]
urlpatterns += staticfiles_urlpatterns()
#the actual url pattern is a call to the path() function, which takes 3 args: '' string that helps django route the current request. Django receives the requested URL and tries to route the request to a view
#routes reqeust to a view by searching all the URL patterns we've defined to find one that matches the current request, so empty string matches the base URL
#any other url won't match this pattern, and django will return an error page if the URL requested doesnt match any existing url patterns

#the second arg in path specifies which function to call in views.py
#when a requested URL matches the pattern we're defining, django calls the index() function from views.py

#the third argument provides the name index for this url pattern so we can refer to it in other code sections
#whenever we want to provide a link to the home page, we'll use this name instead of writing out a URL