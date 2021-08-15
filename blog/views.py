from itmes.views import itmes1
from typing import Reversible
from itmes.models import itmes
from about.models import about
from django.shortcuts import redirect, render
from .forms import postform
from django.urls import reverse

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
        form = postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('/blog')
    else:
        form = postform()

    return render(request, 'blog/new.html',{'form':form})



def edit_post(request , id):
    post = blog.objects.get(id=id)
    if request.method  == 'post':
        form = postform(request.post , request.FILES , instance=post )
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:post_detail' , args= [post.id]))

    else:
        form = postform( instance=post )
        
    return render(request,'blog/edit.html',{'form':form})



def delete_post(request , id):
    post = blog.objects.get(id=id)
    post.delete()
    return redirect('/blog')



def about_html(request):
    all_posts = about.objects.all()
    return render(request,'blog/about_html',{'posts':all_posts})


 
def test_html(request):
    all_posts = itmes.objects.all()
    return render(request,'itmes/test_html',{'posts':all_posts})


def post_delete(request):
    all_posts = itmes1.objects.all()
    return render(request , 'itmes/post_delete',{'posts':all_posts})


def post_edit(request , id):
    all_Posts = itmes.objects.all()
    return render(request , 'itmes/post_edit',{'posts':all_Posts})


def product_html(request):
    all_posts = itmes.objects.all()
    return render(request , 'itmes/product_html',{'posts':all_posts})