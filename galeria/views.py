from django.shortcuts import render

def index(request):
    #return HttpResponse('<h1> Alura space </h1><p> Bem vindo ao espaço</p>')
    return render(request, 'galeria/index.html')
