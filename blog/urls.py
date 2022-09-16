from django.urls import  path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post_detail/', post_detail, name='post_detail'),
    path('blogs/', blogs, name='blogs'),
    path('category_blogs/<str:slug>/', category_blogs, name='category_blogs'),
    path('tag_blogs/<str:slug>/', tag_blogs, name='tag_blogs'),
    path('blogs/<str:slug>/', blog_details, name='blog_details'),
    path('add_reply/<int:blog_id>/<int:comment_id>/', add_reply, name='add_reply'),
    path('like_blog/<int:pk>/', like_blog, name='like_blog'),
    path('search_blogs/', search_blogs, name='search_blogs'),
    path('add_blog/', add_blog, name='add_blog'),

]
