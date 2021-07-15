from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    contenr = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='post/')

    


    def _str_(self):
        return self.title