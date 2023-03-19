from django.shortcuts import render

def duvidas(request):
    return render(request, 'duvidas/duvidas.html')
