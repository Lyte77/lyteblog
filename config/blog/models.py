from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=20)
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

