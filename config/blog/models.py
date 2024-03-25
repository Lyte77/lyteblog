from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
      ordering = ['-created']
      indexes =[
         models.Index(fields=['created'])
      ]
        

