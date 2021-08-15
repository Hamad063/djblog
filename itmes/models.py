from django.db import models

# Create your models here.

class itmes(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    image = models.ImageField(upload_to='models/')
    price = models.IntegerField()


    def __str__(self):
      return self.name