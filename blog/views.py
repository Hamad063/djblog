from about.models import about
from django.shortcuts import render
from .forms import postform

# Create your views here.
from . models import blog


def post_list(request):
    all_posts = blog.objects.all()
    return render(request,'blog/post_list.html',{'posts':all_posts})



def post_detail(request , id):
    post = blog.objects.get(id=id)
    return render(request,'blog/post_detail.html',{'post':post})



def new_post(request):
    if request.method == 'POST':
        form = postform(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = postform()

    return render(request, 'blog/new.html',{'form':form})



def about_html(request):
    all_posts = about.objects.all()
    return render(request,'blog/about_html',{'posts':all_posts})