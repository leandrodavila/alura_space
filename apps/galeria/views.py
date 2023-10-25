from django.shortcuts import render, get_object_or_404, redirect 
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages
from framework.security import UrlSecutity

def index(request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar autenticado!')
        return redirect('login')
    
    #fotografias = Fotografia.objects.all()
    #fotografias = Fotografia.objects.filter(publicada=True)
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards":fotografias})

def imagem(request, foto_id):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar autenticado!')
        return redirect('login')
    
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia" : fotografia})

def buscar(request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar autenticado!')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    if "buscar_input" in request.GET:
        termo_de_busca = request.GET["buscar_input"]
        
        if termo_de_busca:
            fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, nome__icontains=termo_de_busca )
            #fotografias = fotografias.filter(nome__icontains=termo_de_busca)
            
    return render(request, 'galeria/index.html', {"cards":fotografias})
    
def nova_imagem(request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar autenticado!')
        return redirect('login')
        
    form = FotografiaForms()
    
    if request.method == 'POST':
        
        form = FotografiaForms(request.POST, request.FILES)
        
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Fotografia gravada com sucesso!')
            return redirect('index')
        
    return render(request, "galeria/nova_imagem.html", {'form': form})

def editar_imagem(request, foto_id):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar autenticado!')
        return redirect('login')
        
    if UrlSecutity.is_valid_url(request):
        messages.error(request, f'URL Inválida! {request.path}')
        return redirect('login')
        
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    
    if request.method == 'POST':
        #aqui tem o instance de diferença        
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Fotografia editada com sucesso!')
            #return redirect('index')
            return render(request, 'galeria/imagem.html', {"fotografia" : fotografia})
       
    return render(request, 'galeria/editar_imagem.html', {'form':form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar autenticado!')
        return redirect('login')
    
    #fotografia = get_object_or_404(Fotografia, pk=foto_id)
    fotografia = Fotografia.objects.get(id=foto_id)
    
    if fotografia:
        fotografia.delete()
        messages.success(request, 'Fotografia excluída com sucesso!')
        return redirect('index')

def filtro(request, categoria):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar autenticado!')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {"cards":fotografias})