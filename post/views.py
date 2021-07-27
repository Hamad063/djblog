from django.shortcuts import render

# Create your views here.
from . models import Post


def post_list(request):
    all_posts = Post.objects.all()
    return render(request,'post/post_list.html',{'posts':all_posts})