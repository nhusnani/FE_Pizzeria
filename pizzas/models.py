from django.db import models
from django import forms

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        return self.name

class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'toppings'
        
    def __str__(self):
        #return a string representation of the model
        return f"{self.name[:50]}"
        #tells django which info to show just 50 characters of text, and ... means not displaying entire entry

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.text[:50]}..."