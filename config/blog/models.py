from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255,default="", unique_for_date='created')
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
        
    def get_absolute_url(self):
       return  reverse('blog:post_details', args=[self.id,
                                                  self.created.year,
                                                  self.created.month,
                                                  self.created.day,
                                                  self.slug])

class Comment(models.Model):
   post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
   name = models.CharField(max_length=20)
   email = models.EmailField()
   comment = models.TextField()
   commented = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return f"{self.name} commented on {self.post.title}"
   
   class Meta:
      ordering = ['-commented']
      indexes =[
         models.Index(fields=['commented'])
      ]
   
