from django.forms import fields
from .models import blog
from django import forms 

class postform(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title','contenr','published']

