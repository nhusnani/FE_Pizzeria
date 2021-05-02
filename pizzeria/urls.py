"""pizzeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#urls.py file represents project as a whole
#urlpatterns variable includes sets of URLs from the apps in the project
#the path ('admin/', admin.site.urls) defines all the urls that can be requested from the admin site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizzas.urls')), 
]
#added a line to include module pizzas, then created another urls.py file in pizzas