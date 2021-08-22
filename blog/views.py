from django.shortcuts import render , redirect
from .forms import PostForm
from django.urls import reverse

# Create your views here.
from . models import Post


def post_list(request):
    all_posts = Post.objects.all()
    return render(request ,'blog/post_list.html',{'posts':all_posts})


def post_detail(request , id):
    post = Post.objects.get(id=id)
    return render(request,'blog/post_detail.html',{'post':post})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    
    else:
        form = PostForm

    return render(request,'blog/new.html',{'form':form})



def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES , instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:post_detail', args=[post.id]))
    
    else:
        form = PostForm(instance=post)

    return render(request,'blog/edit.html',{'form':form})




def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/blog')