from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views import generic
from django.urls import reverse_lazy
from .forms import Signup
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import EditProfileForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from Blogapp.models import Profile,Post
from django.shortcuts import get_object_or_404,HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

class Editprofilepage(generic.UpdateView):
    model=Profile
    template_name='registration/edit_profile.html'
    fields=['bio','profile_pic','facebook','Instagram','twitter']
    success_url=reverse_lazy('home')

        
class CustomLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()
        if not hasattr(user, 'profile'):
            return redirect('create_profile')
        else:
            return super().form_valid(form)
    

class User_Register(generic.CreateView):
    form_class= Signup
    template_name='registration/register.html'
    success_url=reverse_lazy('login_page')

def logoutview(request):
    logout(request)
    return redirect('main_page')

class CreateProfile(generic.CreateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    success_url = reverse_lazy('home')  # Adjust 'home' to your actual home page URL
    fields = ['bio', 'profile_pic', 'facebook', 'Instagram', 'twitter']

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and not hasattr(request.user, 'profile'):
            return super().dispatch(request, *args, **kwargs)
        elif(request.user.is_authenticated):
            return redirect('home')  # Redirect if user is not authenticated or already has a profile
        else:
            return HttpResponse("you're not authenticated")
        
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
    
    def get_context_data(self, *args,**kwargs):
        context= super(ProfilePage,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        date_joined=get_object_or_404(User,id=self.kwargs['pk'])
        context["page_user"]=page_user
        context["date_joined"]=date_joined
        return context
    
