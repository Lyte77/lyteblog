from django.urls import path
from .views import post_list,post_details,create_post, update_post, delete_post
app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:id>/<int:year>/<int:month>/<int:day>/<slug:posts>/', post_details, name='post_details'),
    path('create_post/', create_post, name='create_post'),
    path('update_post/<int:id>/', update_post, name='update_post'),
    path('delete_post/<int:id>', delete_post, name='delete_post'),
   
]