from django.shortcuts import render

def como_funciona(request):
    return render(request, 'como_funciona/diretrizes.html')
