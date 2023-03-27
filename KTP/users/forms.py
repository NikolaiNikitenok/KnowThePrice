from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # nickname = forms.CharField()
    # sex = forms.ChoiceField(choices=[Profile.SEX], required=False)
    # date_of_birthday = forms.DateField()
    # country = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
# class ProfileRegisterForm(forms.ModelForm):
#     nickname = forms.CharField()
    
#     class Meta:
#         model = User
#         fields = ['nickname']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    # nickname = forms.CharField()
    # sex = forms.CharField()
    # date_of_birthday = forms.DateField()
    # country = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nickname", "image"]
