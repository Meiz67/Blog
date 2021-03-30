from django.urls import path

from . import views


app_name = 'blogs'
urlpatterns = [
    path('', views.summary, name='summary'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/', views.edit_post, name='edit_post'),
    path('users_posts/', views.users_posts, name='users_posts'),
]
