from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import ToDo
from django.forms import ModelForm

class ToDoCreateForm(forms.ModelForm):
    goal = forms.CharField()
    # title = forms.CharField()
    # deadline = forms.DateField()
    category = forms.CharField()
    
    class Meta:
        model = ToDo
        fields = ["category", "goal"]
    
