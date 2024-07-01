from django.urls import path
from .views import Home,ArticleDetail,Add_Post,Update_Post,Delete_Post,AddCategory
from .views import Categoryview,LikeView,Main,Aboutview,search

urlpatterns = [
   path('search/',search,name='search'),
   path('about_us/',Aboutview,name='about_us'),
   path('',Main,name='main_page'),
   path('Categories_of_/<str:cats>',Categoryview,name='category'),
   path('article/<int:pk>',ArticleDetail.as_view(),name='article_detail'),
   path('home/',Home.as_view(),name='home'),
   path('add_category/',AddCategory.as_view(),name='AddCategory'),
   path('post/',Add_Post.as_view(),name='Add_Post'),
   path('update/<int:pk>',Update_Post.as_view(),name='Update_Post'),
   path('delete/<int:pk>/remove',Delete_Post.as_view(),name='delete_post'),
   path('like/<int:pk>',LikeView,name='postlike'),
]