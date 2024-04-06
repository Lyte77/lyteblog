from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm, CommentForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()

    
    return render(request, 'post/post_list.html', {'posts':posts,
                                                   })

def post_details(request,id,posts,year,month,day):
    posts = get_object_or_404(Post, id=id,slug=posts,created__year=year,
                              created__month=month,
                              created__day=day)
    

    comments = posts.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = posts
            new_comment.save()

    comment_form = CommentForm()
    
    


    return render(request, 'post/post_details.html', {'posts':posts,
                                                      'comments':comments,
                                                      'new_comment':new_comment,
                                                      'comment_form':comment_form})

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
    

# def comment_system(request):
    
#     if request.method == 'POST':
#         comment = CommentForm(request.POST)
#         if comment.is_valid():
#             comment.save()
#     comment = CommentForm()
#     return render(request, 'post/comment.html', {'comment':comment}) 
    