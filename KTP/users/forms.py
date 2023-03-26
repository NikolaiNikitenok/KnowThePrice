from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Sex


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nickname = forms.CharField()
    # sex = forms.ModelChoiceField(queryset=Sex.objects.all())
    date_of_birthday = forms.DateField()
    country = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nickname', 'date_of_birthday', 'country']
        
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    nickname = forms.CharField()
    # sex = forms.ModelChoiceField(queryset=Sex.objects.all())
    date_of_birthday = forms.DateField()
    country = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'nickname', 'date_of_birthday', 'country']
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

