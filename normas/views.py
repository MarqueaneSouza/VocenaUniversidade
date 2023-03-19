from django.shortcuts import render

def leis(request):
    return render(request, 'normas/leis.html')

def decretos(request):
    return render(request, 'normas/decretos.html')