from django.shortcuts import render
from .models import Post


def community(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'community.html', context)
