from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nickname = forms.CharField()
    sex = forms.ModelChoiceField()
    date_of_birthday = forms.DateField()
    country = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nickname', 'sex', 'date_of_birthday', 'country']
        
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    nickname = forms.CharField()
    sex = forms.ModelChoiceField()
    date_of_birthday = forms.DateField()
    country = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'nickname', 'sex', 'date_of_birthday', 'country']
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

