from django.shortcuts import render
from blog.models import Categoria, Post
# Create your views here.

def blog(request):
    post = Post.objects.all()
    
    return render(request, 'blog/blog.html' , {"posts": post})

