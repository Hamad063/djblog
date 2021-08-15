from .models import itmes
from django import forms 

class postform(forms.ModelForm):
    class Meta:
        model = itmes
        fields = ['name','desc','price' ,'image' ,'email']
