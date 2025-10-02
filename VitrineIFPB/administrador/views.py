from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as django_login
from vitrine.models import Projeto, AreaConhecimento


# Create your views here.
def admin(request):
  return render(request, 'administrador/admin.html', {'projetos': Projeto.objects.all(), 'categorias' : AreaConhecimento.objects.all()})

def login(request):
  email = request.POST.get('email')
  senha = request.POST.get('senha')
  user = authenticate(request, username=email, password=senha)

  print('veio pra ca')
  if user is not None:
    django_login(request, user)
    return redirect('administrador')
  return redirect('institucional')

def custom_logout(request):
  logout(request)
  return redirect('home')

#TODO CONTROLE DE PROJETOS
def cadastrar_projeto(request):
  if request.method == 'POST':
    imagem = request.FILES['projeto_imagem']
    titulo = request.POST.get('projeto_titulo')
    descricao = request.POST.get('projeto_descricao')
    autores = request.POST.get('projeto_autores')
    categoria = request.POST.get('projeto_categoria')

    Projeto(titulo=titulo, descricao=descricao, autores=autores, categoria=categoria, imagem=imagem).save()
  return redirect('administrador')

def editar_projeto(request):
  if request.method == 'POST':
    id = request.POST.get('projeto_id')
    titulo = request.POST.get('projeto_titulo')
    descricao = request.POST.get('projeto_descricao')
    autores = request.POST.get('projeto_autores')
    categoria = request.POST.get('projeto_categoria')

    if request.FILES.get('projeto_imagem') is not None:
      imagem = request.FILES['projeto_imagem']
    else:
      imagem = Projeto.objects.get(id=id).imagem

    Projeto.objects.filter(id=id).update(titulo=titulo, descricao=descricao, autores=autores, categoria=categoria, imagem=imagem)
  return redirect('administrador')

def excluir_projeto(request):
  if request.method == "POST":
    projeto = request.POST.get('projeto_id')
    Projeto.objects.filter(id=projeto).delete()
  return redirect('administrador')

#TODO CONTROLE DE CATEGORIAS
def cadastrar_categoria(request):
  if request.method == 'POST':
    nome = request.POST.get('categoria_nome')
    descricao = request.POST.get('categoria_descricao')
    AreaConhecimento(nome=nome, descricao=descricao).save()
  return redirect('administrador')

def editar_categoria(request):
  if request.method == 'POST':
    id = request.POST.get('categoria_id')
    nome = request.POST.get('categoria_nome')
    descricao = request.POST.get('categoria_descricao')

    AreaConhecimento.objects.filter(id=id).update(nome=nome, descricao=descricao)


  return redirect('administrador')
def excluir_categoria(request):
  if request.method == "POST":
    categoria = request.POST.get('categoria_id')
    AreaConhecimento.objects.filter(id=categoria).delete()
  return redirect('administrador')
