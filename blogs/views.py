from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import BlogPost
from .forms import PostForm


# Create your views here.
def summary(request):
    posts = []
    for user in User.objects.all():
        posts += BlogPost.objects.filter(owner=user).order_by('-date_added')[:1]
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def new_post(request):
    if request.method != 'POST':
        form = PostForm
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:summary')
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


def edit_post(request):
    if request.method != 'POST':
        post_id = request.GET['post_id']
        post = BlogPost.objects.get(id=post_id)
        form = PostForm(instance=post)
    else:
        data = request.POST
        post = BlogPost.objects.get(id=data['submit'])
        form = PostForm(instance=post, data=data)
        if form.is_valid():
            form.save()
            return redirect('blogs:summary')
    context = {'form': form, 'post_id': post_id}
    return render(request, 'blogs/edit_post.html', context)
    pass
