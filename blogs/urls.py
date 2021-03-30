from django.urls import path

from . import views


app_name = 'blogs'
urlpatterns = [
    path('', views.blog_posts, name='blog_posts'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/', views.edit_post, name='edit_post'),
]
