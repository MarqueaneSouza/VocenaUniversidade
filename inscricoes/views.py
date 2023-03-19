from django.shortcuts import render
from . models import Post

def inscricoes(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'inscricoes/inscricoes.html', context)
