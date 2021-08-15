from blog.forms import postform
from django.shortcuts import render , redirect
#from .forms import postform
from django.urls import reverse
#from typing import Reversible

# Create your views here.
from .models import itmes

def itmes1(request):
    all_itmes = itmes.objects.all()
    return render(request,'items/test.html',{'itmes':all_itmes})


def test_html(request):
    all_posts= itmes1.objects.all()
    return render(request,'itmes/post_list.html',{'posts':all_posts})


def post_edit(request , id):
    post= itmes.objects.get(id=id)
    return render(request,'itmes/post_edit.html',{'post':post})


def post_delete(request):
    all_posts = itmes1.objects.all()
    return render(request , 'itmes/post_delete',{'posts':all_posts})



def product_html(request):
    if request.method == 'POST':
        form =(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('/itmes')
    else:
        form =()

    return render(request, 'itmes/product.html',{'form':form})




def edit_post(request , id):
    post = itmes.objects.get(id=id)
    if request.method  == 'post':
        form = postform(request.post , request.FILES , instance=post )
        if form.is_valid():
            form.save()
            return redirect(reverse('itmes:post_edit' , args= [post.id]))

    else:
        form = postform( instance=post )
        
    return render(request,'blog/edit.html',{'form':form})





def delete_post(request , id):
    post = itmes.objects.get(id=id)
    post.delete()
    return redirect('/itmes')

