from django.shortcuts import render
from blog.forms import PostForm
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from django.conf import settings
from tuksimadventures import settings
from blog.models import Post

@login_required(login_url = "login")
def addpost(request):
    form = PostForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Post made successfully!")
        return redirect("blog")
    return render(request,"blog/post_form.html",{"form":form})
        


class BlogPageList(ListView):
  model = Post
  template_name = 'blog/page_list.html'
  paginate_by = 8
  context_object_name = 'posts'

  def get_queryset(self, *args, **kwargs):
    if self.kwargs:
      return Post.objects.filter(status='published').order_by('-created')
    else:
      query = Post.objects.all().order_by('-created')
      return query


def detail(request, slug):
    q = Post.objects.filter(slug__iexact = slug)
    if q.exists(): 
        q = q.first()
    else: 
       return render(request, 'blog/404.html', status=404)
  
    context = {
        'post': q,
        }
    return render(request, 'blog/post_detail.html', context) 


    

@login_required(login_url='login')
def dashboard(request):
    posts = Post.objects.filter(author=request.user)
    context = {'posts': posts}
    return render(request, "dashboard.html", context)

@login_required(login_url='login')
def updatepost(request, slug):
    post = get_object_or_404(Post, slug__iexact = slug)
    form = PostForm(request.POST or None,request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        form.save_m2m()
        messages.success(request, "You Have Successfully Updated Your Post")
        return redirect("dashboard")
    return render(request, 'blog/update.html', {'form': form})

@login_required(login_url='login')
def deletepost(request, slug):
    post = get_object_or_404(Post, slug__iexact = slug)
    post.delete()
    messages.success(request, "You Have Successfully deleted Your Post")
    return redirect("dashboard")
    return render(request, "blog/delete.html", {"post": post})


def handler404(request, exception):
    return render(request, 'blog/404.html', status=404)


def handler403(request, exception):
    return render(request, 'blog/403.html', status=403)


def handler400(request, exception):
    return render(request, 'blog/400.html', status=400)


def handler500(request):
    return render(request, 'blog/500.html', status=500)