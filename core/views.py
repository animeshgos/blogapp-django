from django.shortcuts import render, redirect

from posts.models import *
from django.contrib.auth import logout

from .forms import SignupForm
# Create your views here.


def index(request):
    posts = Post.objects.filter()[0:6]
    tags = Tag.objects.all()
    return render(request, "core/index.html", {
        'tags': tags,
        'posts': posts
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_page(request):
    logout(request)
    return redirect('/login/')
