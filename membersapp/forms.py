from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from Blogapp.models import Profile

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
        fields=('username','First_name','Last_name','email')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        if 'password' in self.fields:
            del self.fields['password']
    
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('bio','profile_pic','facebook','Instagram','twitter')
        widget={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'profile_pic':forms.TextInput(attrs={'class':'form-control'}),
            'facebook':forms.TextInput(attrs={'class':'form-control'}),
            'Instagram':forms.TextInput(attrs={'class':'form-control'}),
            'twitter':forms.TextInput(attrs={'class':'form-control'}),
        }