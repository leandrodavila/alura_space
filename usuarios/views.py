from django.shortcuts import render, redirect 
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    
    login_form = LoginForms()
    
    if request.method == 'POST':
        
        login_form = LoginForms(request.POST)
        
        if login_form.is_valid():
            
            user  = login_form['nome_login'].value()    
            senha = login_form['senha'].value()    
            
            usuario = auth.authenticate(
                request=request,
                username = user,
                password=senha
            )
            
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request,f'{user} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request,'Erro ao efetuar login')
                return redirect('login')
        else:
            for field in login_form:
                messages.error(request, f'{field.name}: {field.errors}')
            return redirect('login')
                
    #GET        
    return render(request, 'usuarios/login.html', {"form": login_form})

def cadastro(request):
    
    cadastro_form = CadastroForms()
    
    if (request.method == 'POST'):
        
        cadastro_form = CadastroForms(request.POST)
            
        if cadastro_form.is_valid():
            
            if ( cadastro_form['senha_1'].value() != cadastro_form['senha_2'].value() ):
                
                messages.error(request, 'Senhas devem ser iguais!')
                return redirect('cadastro') #nome da rota
            
            nome = cadastro_form['nome_cadastro'].value()
            email = cadastro_form['email'].value()
            senha = cadastro_form['senha_1'].value()
                        
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existe')
                return redirect('cadastro') #nome da rota
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            
            usuario.save()
            
            messages.success(request,'Cadastro efetuado com sucesso!')
            
            return redirect('login')
        else:
            
            for field in cadastro_form:
                if field.errors:
                    messages.error(request, field.errors)
            return redirect('cadastro') #nome da rota
                
    return render(request, 'usuarios/cadastro.html', {"form": cadastro_form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efeutado com sucesso!")
    return redirect('login')