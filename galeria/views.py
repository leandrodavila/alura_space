from django.shortcuts import render, get_object_or_404, redirect 
from galeria.models import Fotografia
from django.contrib import messages
'''
dados = {
    1: {"nome": "Nebulosa de Carina",
        "legenda": "webbtelescope.org / NASA / James Webb"},
    2: {"nome": "Galaxia NGC 1079",
        "legenda": "nasa.org / NASA / James Webb / Hubble"}
}
'''

def index(request):
        
    #fotografias = Fotografia.objects.all()
    #fotografias = Fotografia.objects.filter(publicada=True)
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar autenticado!')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards":fotografias})

def imagem(request, foto_id):
    
    if not request.user.authenticated:
        messages.error(request, 'Usuário precisa estar autenticado!')
        return redirect('login')

    
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia" : fotografia})

def buscar(request):
    
    if not request.user.authenticated:
        messages.error(request, 'Usuário precisa estar autenticado!')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    if "buscar_input" in request.GET:
        termo_de_busca = request.GET["buscar_input"]
        
        if termo_de_busca:
            fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, nome__icontains=termo_de_busca )
            #fotografias = fotografias.filter(nome__icontains=termo_de_busca)
            
    return render(request, 'galeria/buscar.html', {"cards":fotografias})
    
