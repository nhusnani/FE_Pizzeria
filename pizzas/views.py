from django.shortcuts import render, redirect
from .models import Pizza, Toppings
from .forms import CommentForm

def index(request):
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
  
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.order_by('-date_added')
    comments=pizza.comment_set.order_by('-date_added')
    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments}
    return render(request,'pizzas/pizza.html', context)
   
def comment(request, pizza_id):
    if request.method != 'POST':
        form=CommentForm()
    else:
        pizza = Pizza.objects.get(id = pizza_id)
        form=CommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.pizza=pizza
            comment.save()
            return redirect('pizzas:pizzas')
    context={'form':form, 'pizza_id': pizza_id}
    return render(request,'pizzas/comment.html',context)