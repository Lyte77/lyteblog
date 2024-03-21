from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts':posts})

def post_details(request,id):
    posts = get_object_or_404(Post, id=id)
    return render(request, 'post/post_details.html', {'posts':posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')

    form = PostForm()
    return render(request, 'post/create_post.html', {'form':form})

def update_post(request,id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()

            return redirect('blog:post_list')
    return render(request, 'post/create_post.html', {'form':form,
                                                     'post':post})
    
def delete_post(request,id):
    print("Deleting post with id:", id)
    post = get_object_or_404(Post,id=id)
    print("Retriving post: ",post)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')

    return render(request, 'post/delete_post.html',{"post":post})    
    
