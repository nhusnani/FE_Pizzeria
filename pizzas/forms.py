from django import forms 

from .models import Pizza, Comment

'''
class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["name"]
        label = {"Name:": ""}
        widgets = {"name": forms.Textarea(attrs={"cols": 80})}
'''

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':''}