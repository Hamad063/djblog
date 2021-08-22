from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='posts/'   , default='')
    email = models.EmailField(default='')
    published = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
      return self.title
