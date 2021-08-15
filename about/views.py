from django.shortcuts import render

# Create your views here.

from .models import about

def about1(request):
    all_about = about.objects.all()
    return render(request,'about/about.html',{'about':all_about})