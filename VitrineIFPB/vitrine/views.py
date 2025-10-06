from django.shortcuts import render
from .models import Projeto, Categoria



def home(request):
  if request.method == 'GET':
    projetos = Projeto.objects.all()
  return render(request, 'home/home.html', {'projetos': projetos, 'categorias': Categoria.objects.all()})

def patentes(request):
  if request.method == 'GET':
    projetos = Projeto.objects.filter(categoria='patente')
  return render(request, 'patentes/patentes.html', {'projetos': projetos, 'categorias': Categoria.objects.all()})

def softwares(request):
  if request.method == 'GET':
    projetos = Projeto.objects.filter(categoria='software')
  return render(request, 'softwares/softwares.html', {'projetos': projetos})

def detalhes_projeto(request, projeto_id):
  projeto = Projeto.objects.get(id=projeto_id)
  return render(request, 'detalhes_projeto/detalhes_projeto.html', {'projeto': projeto})