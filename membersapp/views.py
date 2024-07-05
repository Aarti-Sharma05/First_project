from django.db.models.base import Model as Model
from django.views import generic
from django.urls import reverse_lazy
from .forms import Signup
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import EditProfileForm,CreateProfileForm
from django.shortcuts import render
from Blogapp.models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from Blogapp.models import Post

class CustomLoginView(LoginView):
    template_name='registration/Login.html'
    
    def get_success_url(self):
        user = self.request.user
        if not Profile.objects.filter(user=user).exists():
            return reverse_lazy('create_profile')  
        return reverse_lazy('home') 

def change_password(request):
    if request.method =="POST":
        ob=PasswordChangeForm(user=request.user,data=request.POST)
        if ob.is_valid():
            ob.save()
            update_session_auth_hash(request,ob.user)
            messages.success(request,'Your password has successfully changed ...')
            return redirect('home')
    else:
        ob=PasswordChangeForm(user=request.user)    
    return render(request,'registration/change_password.html',{'ob':ob})

class Editprofilepage(generic.UpdateView):
    model=Profile
    template_name='registration/edit_profile.html'
    fields=['bio','profile_pic','facebook','Instagram','twitter']
    success_url=reverse_lazy('home')
            

class User_Register(generic.CreateView):
    form_class= Signup
    template_name='registration/register.html'

    def form_valid(self, form):
        form.save()
        return redirect(reverse_lazy('login_page'))

def logoutview(request):
    logout(request)
    return redirect('main_page')


class CreateProfile(LoginRequiredMixin,generic.CreateView):
    model = Profile
    form_class=CreateProfileForm
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('home')  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateProfile(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/Edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class ProfilePage(generic.DetailView):
    model=Profile
    template_name='registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)
        page_user = self.get_object() 
        user = page_user.user  
        posts = Post.objects.filter(author=user) 
        context["page_user"] = page_user
        context["date_joined"] = user.date_joined
        context["current_user"]=self.request.user
        context["posts"]=posts
        return context
    
