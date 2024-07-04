from django import forms
from .models import Post
from .models import Category

cat=Category.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','author','header_image','snippet','body')
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Enter the title '}),
            'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title tag'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            'body':forms.Textarea(attrs={'id':'classic','class':'form-control','placeholder':'Enter the content'}),
            'snippet':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your snippet'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','header_image','body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Edit your title'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder':'Edit your content'}),
        }