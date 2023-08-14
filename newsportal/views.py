from django.http import HttpResponse
from django.shortcuts import render
from .models import *
def index(request):
    posts = Post.objects.all()
    context = {
        'title':'News Portal',
        'posts':posts

    }
    return render(request, 'newsportal/index.html', context)
