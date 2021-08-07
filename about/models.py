from django.db import models

# Create your models here.
class about(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField(max_length=2000)
     image = models.ImageField(upload_to='post/')


    
def __str__(self):
    return self.title