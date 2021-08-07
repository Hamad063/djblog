from django.shortcuts import render

# Create your views here.

from .models import about

def about(request , about):
    all_abuot = about.objects.all()
    return render(request,'about/about_html')