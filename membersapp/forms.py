from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class Signup(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput())
    First_name=forms.CharField(max_length=20,widget=forms.TextInput())
    Last_name=forms.CharField(max_length=50,widget=forms.TextInput())

    class Meta:
        model=User
        fields=('username','First_name','Last_name','email','password1','password2')

    
    def __init__(self, *args, **kwargs):
        super(Signup,self).__init__(*args, **kwargs)
        self.fields['username'].widget
        self.fields['password1'].widget
        self.fields['password2'].widget

class EditProfileForm(UserChangeForm):
    username=forms.CharField(max_length=100,widget=forms.TextInput())
    email=forms.EmailField(widget=forms.EmailInput())
    First_name=forms.CharField(max_length=20,widget=forms.TextInput())
    Last_name=forms.CharField(max_length=50,widget=forms.TextInput())
    
    class Meta:
        model=User
        fields=('username','First_name','Last_name','email','password')
    
