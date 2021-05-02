from django.shortcuts import render, redirect
from .models import Pizza, Toppings
from .forms import ToppingsForm

#a view function takes in info from a request, prepares the data needed to generate a page, and then sends the data back to the browser, often by using a template that defines what the page will look like
#render() functionr enders the response based on the data provided by views
# Create your views here.

def index(request):
    #the home page for the pizzas
    return render(request, 'pizzas/index.html')
    #when url request matches pattern, django looks for function called index (this is in the urls file) but urls looks into this file views
    #django passes the request object ot this view function
    #in this case, we don't need to process any data for the page, so only code in function is call to render()
    #the render() function passes two arguments --> the original request object and template it cna use to build the page

def availpizzas(request):
    #show all available pizzas
    availpizzas = Pizza.objects.order_by('date_added')
    #query database by asking for the Pizza objects, sorted by the datte time added attribute
    context = {'availpizzas':availpizzas}
    return render(request, 'pizzas/availpizzas.html', context)
    #the availpizzas() function needs one parameter - the request object django received from the server
    #define the context we'll sen ot template. Context is a dictionary in which keys are names we'll use in template to access data, and values are the data we need to send to the template
    #this case contains set of pizzas we'll display on page
    #pass the the context variable to render() as well as the request object and the path to the template

def pizza(request, pizza_id):
    #show a single pizza and all its toppings
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request,'pizzas/pizza.html', context)
    #function accepts the value capture by <int:pizza_id> from urls and stores in pizza_id. Retrieve pizza and get toppings associated with the topic, order according to date added

def new_toppings(request, pizza_id):
    #add a new comment for a particular topic
    pizza = Pizza.objects.get(id=pizza_id)
    #we'll need the pizza to render the page and process the forms data, so we use pizza_id to get the correct pizza object

    #check whether the request method is POST or GET
    if request.method != 'POST':
        #no data submitted; create a blank form
        form = ToppingsForm()
    else:
        #POST data submitted; process data
        #if request method is POST, process the data by making an isntance of CommentForm, populated with POST data from the request object
        #then check if form is valid, if it is need to set the entry's object pizza attribute before saving it to database
        #when call save(), include arg commit=False to tell django to create a new comment oject and assign it to new_comment without saving it to database yet
        #set pizza attribute of new_comment to pizza we pulled from database at beginning of function
        #then we calll save() with no arguments, saving the entry to database with correct associate topic
        form = ToppingsForm(data=request.POST) #form has data user entered
        if form.is_valid():
            new_toppings = form.save(commit=False)
            new_toppings.pizza = pizza
            new_toppings.save() #writes data from form to database
            return redirect('pizzas:pizza', pizza_id=pizza_id) #after saving takes us back to available pizza page
            #redirect call requires two arguments, name of view we want to redirect to and arg that view function requires. Here redirectiong to pizza() which needs arg pizza_id
            #view then renders the pizza page that user made an entry for, and they should see their new comment in list of comments
    #display a blank or invalid form 
    context = {'pizza': pizza, 'form': form}
    #create a context dictionary and rendor the page using new_comment.html template. This code wille xecute for a blank form or for a submitted form that is evaluated as invalid
    return render(request, 'pizzas/new_toppings.html', context)
