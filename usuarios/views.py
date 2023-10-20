from django.shortcuts import render, redirect 
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

def login(request):
    
    login_form = LoginForms()
    return render(request, 'usuarios/login.html', {"form": login_form})

def cadastro(request):
    
    cadastro_form = CadastroForms()
    
    if (request.method == 'POST'):
        
        cadastro_form = CadastroForms(request.POST)
            
        if cadastro_form.is_valid():
            
            if ( cadastro_form['senha_1'].value() != cadastro_form['senha_2'].value() ):
                return redirect('cadastro') #nome da rota
            
            nome = cadastro_form['nome_cadastro'].value()
            email = cadastro_form['email'].value()
            senha = cadastro_form['senha_1'].value()
                        
            #if User.objects.filter(username=nome).exists():
            #    return redirect('cadastro') #nome da rota
            
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            
            usuario.save()
            
            return redirect('login')
        else:
            
            for field in cadastro_form:
                print("Field Error:", field.name,  field.errors)
            return render(request, 'usuarios/cadastro.html', {"form": cadastro_form})
