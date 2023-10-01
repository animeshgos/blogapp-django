from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from posts.models import Post


@login_required
def index(request):
    posts = Post.objects.filter(creator=request.user)

    return render(request, 'dashboard/index.html', {
        'posts': posts,
    })
