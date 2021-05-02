from django.db import models
#anytime add app, do makemigrations which tells DJango to figure out how to modify database so it can store the data associated w any new models --> makes migration file
#manage.py migrate applies migration and has Django modify database
#whenever want to modify data that Pizzas manages, we do: modify models.py, call makemigrations on pizzas, and tell django to migrate the project

# Create your models here.
class Pizza(models.Model):
    #type of pizza
    #class called name inherits from Model, a parent class included in django taht defines a model's basic functionality
    #text attribute is CharFIeld, piece of data that's made up of characters
    #CharField when was to store a small amount of text such asa name, CharField attribute tells Django how much space it should reserve in the database
    name = models.CharField(max_length = 35)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Toppings'
        #nest a meta class inside the Toppings class
        #meta holds extra information for managing a model --> allows us to set a special attribute telling django to use Toppings when it needs to refer to more than one entry 
    
#Toppings class inherits from DJango's base Model class
#pizza is a foreign key instance, references another record in the database --> connects each entry to a specific topic
#when django needs to establish a connection between two pieces of data, it uses the key associated with each piece of info
#use connections to retrieve all the entries associated w a certain topic
#the on.delete=models.CASCADE argument tells Django that when a topic is deleted, all entries associated w that topic should be deleted as well, all entries associate w that topic shoul dbe deleted as well
#name is an instance of TextField, doesn't need size limit, because don't limit size of individual Toppings


    def __str__(self):
        #return a string representation of the model
        return f"{self.name[:50]}"
        #tells django which info to show just 50 characters of text, and ... means not displaying entire entry

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.text[:50]}..."

#yay pizza