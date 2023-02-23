#LÓGICA DE NEGÓCIO
from django.shortcuts import render
from . models import Post

def home(request): #Carregar a home com todos os posts catalogados no banco de dados.
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'pagina/home.html', context)
