from django.urls import path
from .views import User_Register,logoutview,UpdateProfile,ProfilePage,Editprofilepage,CreateProfile,CustomLoginView
from django.contrib.auth import views as auth_views
urlpatterns=  [
    #password change pending 
    path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),name='passwordchange'),
    path('register/',User_Register.as_view(),name='register'),
    path('login/',CustomLoginView.as_view(),name='login_page'),
    path('create-profile/', CreateProfile.as_view(), name='create_profile'),
    path('logout_user/',logoutview,name='Logout'),
    path('Edit_Profile/',UpdateProfile.as_view(),name='update_profile'),
    path('<int:pk>/edit_profile_page',Editprofilepage.as_view(),name='edit_profile_page'),
    path('<int:pk>/profile/',ProfilePage.as_view(),name='Profile_page'),
]