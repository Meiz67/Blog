from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import PostForm


# Create your views here.
def blog_posts(request):
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/blog_posts.html', context)


def new_post(request):
    if request.method != 'POST':
        form = PostForm
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_posts')
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
            return redirect('blogs:blog_posts')
    context = {'form': form, 'post_id': post_id}
    return render(request, 'blogs/edit_post.html', context)
    pass
