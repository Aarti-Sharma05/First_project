from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name 
    
    def get_absolute_url(self):
        return reverse('home')
    
class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField(max_length=255)
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profile/")
    facebook=models.CharField(max_length=255,null=True,blank=True)
    Instagram=models.CharField(max_length=255,null=True,blank=True)
    twitter=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):

    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=HTMLField()
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255,default='Technology')
    likes=models.ManyToManyField(User,related_name='blog_post')
    snippet=models.TextField()
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')