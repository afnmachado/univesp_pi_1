from django.core.files.utils import FileProxyMixin
from django.http.response import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Funcionario
import hashlib
    
def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/home/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})
    
def login(request):
    if request.session.get('usuario'):
        return redirect('/home/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    cpf = request.POST.get('cpf')
    ponto = request.POST.get('ponto')

    
    usuario = Funcionario.objects.filter(cpf = cpf)

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=1')
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=2')
    
    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = hashlib.sha256(senha.encode()).hexdigest()
        usuario = Funcionario(nome = nome,
                          email = email,
                          senha = senha,
                          cpf = cpf,
                          ponto = ponto)
        usuario.save()
        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')

def valida_login(request):
    cpf = request.POST.get('cpf')
    senha = request.POST.get('senha')
    senha = hashlib.sha256(senha.encode()).hexdigest() 
    usuarios = Funcionario.objects.filter(cpf = cpf).filter(senha = senha)
    if usuarios[0].tipo == 'motorista':
        request.session['usuario'] = usuarios[0].id
        return redirect('/home/itinerario/')
    if len(usuarios) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuarios) > 0:
        request.session['usuario'] = usuarios[0].id
        return redirect('/home/')

def sair(request):
    request.session.flush()
    return redirect('/auth/login/')