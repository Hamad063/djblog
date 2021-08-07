from django.db import models
from django.utils import timezone
# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    contenr = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='post/')
    email = models.EmailField(default='')
    published = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    


    def __str__(self):
        return self.title
