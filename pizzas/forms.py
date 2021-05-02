from django import forms 

from .models import Toppings


class ToppingsForm(forms.ModelForm):
    class Meta:
        model = Toppings
        fields = ["name"]
        label = {"Name:": ""}
        widgets = {"name": forms.Textarea(attrs={"cols": 80})}


#adding a comment
#new class called commentform that inherits from forms.ModelForm which uses info from models to automatically build a form
#the commentform class has a nested meta class lsitign the model its based on and the field to include in the form
#give label a blank 'text' blank label
#widget is html form element such as sinlge line text box, limit text area to 60 columns wide