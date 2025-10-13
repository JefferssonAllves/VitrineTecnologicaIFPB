from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as django_login
from vitrine.models import Projeto, Categoria


# Create your views here.
def admin(request):
  return render(request, 'administrador/admin.html', {'projetos': Projeto.objects.all(), 'categorias' : Categoria.objects.all()})

#TODO CONTROLE DE LOGIN
def login(request):
  email = request.POST.get('email')
  senha = request.POST.get('senha')

  user = authenticate(request, username=email, password=senha)

  if user is not None:
    django_login(request, user)
    return redirect('projetos')
  return redirect('institucional')

def custom_logout(request):
  logout(request)
  return redirect('home')

def cadastrar_admin(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    User.objects.create_user(username=email, password=senha)

  return render(request, 'administrador/cadastrar_admin.html')

#TODO CONTROLE DE PROJETOS
def projetos(request):
  return render(request, 'projetos/projetos.html', {'projetos':Projeto.objects.all(), 'categorias':Categoria.objects.all()})

def cadastrar_projeto(request):
  if request.method == 'POST':
    imagem = request.FILES['projeto_imagem']
    titulo = request.POST.get('projeto_titulo')
    descricao = request.POST.get('projeto_descricao')
    autores = request.POST.get('projeto_autores')
    categoria = request.POST.get('projeto_categoria').lower()
    areas = request.POST.getlist('projeto_areas')

    projeto = Projeto(titulo=titulo, descricao=descricao, autores=autores, categoria=categoria, imagem=imagem)
    projeto.save()

    for area in areas:
      projeto.areas_conhecimento.add(Categoria.objects.get(id=int(area)))
  else:
    return render(request, 'projetos/cadastrar_projeto.html', {'categorias':Categoria.objects.all()})
  return redirect('projetos')

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
  return redirect('projetos')

def excluir_projeto(request):
  if request.method == "POST":
    projeto = request.POST.get('projeto_id')
    Projeto.objects.filter(id=projeto).delete()
  return redirect('projetos')

#TODO CONTROLE DE CATEGORIAS
def categorias(request):
  return render(request, 'categorias/categorias.html', {'categorias':Categoria.objects.all()})

def cadastrar_categoria(request):
  if request.method == 'POST':
    nome = request.POST.get('categoria_nome')
    descricao = request.POST.get('categoria_descricao')
    Categoria(nome=nome, descricao=descricao).save()
  else:
    return render(request, 'categorias/cadastrar_categoria.html')
  return redirect('categorias')

def editar_categoria(request):
  if request.method == 'POST':
    id = request.POST.get('categoria_id')
    nome = request.POST.get('categoria_nome')
    descricao = request.POST.get('categoria_descricao')

    Categoria.objects.filter(id=id).update(nome=nome, descricao=descricao)
  return redirect('categorias')

def excluir_categoria(request):
  if request.method == "POST":
    categoria = request.POST.get('categoria_id')
    Categoria.objects.filter(id=categoria).delete()
  return redirect('categorias')
