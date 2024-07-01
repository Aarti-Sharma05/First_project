from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect,render,get_object_or_404
from django.http import HttpResponseRedirect
from  .models import Post

def Aboutview(request):
    return render(request,'About_us.html')

def Main(request):
    if request.user.is_authenticated:
        post=Post.objects.all()
        context={'post':post}
        return render(request,'home.html',context)
    else:
       return render(request,'Main.html')

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article_detail',args=[str(pk)]))

class Home(ListView):
    model=Post
    template_name="home.html"
    ordering=['-post_date']
    
    
    def get_context_data(self, *args,**kwargs):
        cat_menu=Category.objects.all()
        context= super(Home,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context


def Categoryview(request,cats):
    if request.method=="POST":
        searched=request.Post('searched')
        category=Category.objects.filter(name__contains=searched)
        return render(request,'categories.html',{'searched':searched,'category':category})
    else:
      Category_posts=Post.objects.filter(category=cats.replace('-',' '))
      return render(request,'categories.html',{'cats':cats.replace('-',' '),'Category_posts':Category_posts})


class ArticleDetail(DetailView):
    model=Post
    template_name="article_details.html"

    def get_context_data(self, *args,**kwargs):
        like=get_object_or_404(Post,id=self.kwargs['pk'])
        liked=False
        if like.likes.filter(id=self.request.user.id).exists():
            liked=True

        cat_menu=Category.objects.all()
        context= super(ArticleDetail,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        context['total_likes']=like.total_likes()
        context['liked']=liked
        return context

class Add_Post(CreateView):
    model=Post
    form_class =PostForm
    template_name="add_post.html"

class AddCategory(CreateView):
    model=Category
    template_name='add_category.html'
    fields='__all__'

class Update_Post(UpdateView):
    model=Post
    form_class=UpdateForm
    template_name="update_post.html"
    def post(self, request, *args, **kwargs):
        if request.POST.get('action') == 'cancel':
            return redirect('home')  
        return super().post(request, *args, **kwargs)

class Delete_Post(DeleteView):
    model=Post
    template_name="delete_post.html"
    success_url=reverse_lazy('home')
    def post(self, request, *args, **kwargs):
        if request.POST.get('action') == 'cancel':
            return redirect('home')  
        return super().post(request, *args, **kwargs)


def search(request):
    query=request.GET['search']
    allPosts=Post.objects.filter(title__icontains=query)
    params={'allPosts': allPosts}
    return render(request,'search_post.html',params)