from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import NewPostForm, EditPostForm
from posts.models import *


def browse(request):
    query = request.GET.get('query', '')
    tag_id = request.GET.get('tag', 0)
    tags = Tag.objects.all()
    posts = Post.objects.filter()

    if tag_id:
        posts = posts.filter(tag_id=tag_id)

    if query:
        posts = posts.filter(Q(name__icontains=query) |
                             Q(content__icontains=query))

    return render(request, 'posts/browse.html', {
        'posts': posts,
        'tags': tags,
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    related_posts = Post.objects.filter(
        tag=post.tag).exclude(pk=pk)[0:3]
    return render(request, 'posts/detail.html', {
        'post': post,
        'related': related_posts,
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.save()

            return redirect('post:detail', pk=post.id)
    else:
        form = NewPostForm()

    return render(request, 'posts/form.html', {
        'form': form,
        'title': 'New Post'
    })


@login_required
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk, creator=request.user)

    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()

            return redirect('post:detail', pk=post.id)
    else:
        form = EditPostForm(instance=post)

    return render(request, 'posts/form.html', {
        'form': form,
        'title': 'Edit Post',
    })


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk, creator=request.user)
    post.delete()

    return redirect('dashboard:index')
