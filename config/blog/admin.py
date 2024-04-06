from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','updated','created')
    search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'commented','email')
    list_filter = ('commented','email')
    search_fields = ('name','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment, CommentAdmin)
