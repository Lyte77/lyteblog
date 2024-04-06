from django.forms import ModelForm, forms
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']

    