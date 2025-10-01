from django.shortcuts import render
from .models import Projeto, Categoria



def home(request):
  if request.method == 'GET':
    projetos = Projeto.objects.all()
    categorias = Categoria.objects.all()

  return render(request, 'home/home.html', {'projetos': projetos, 'categorias': categorias})

def patentes(request):
  if request.method == 'GET':
    projetos = Projeto.objects.all()
    categorias = Categoria.objects.all()
  return render(request, 'patentes/patentes.html', {'projetos': projetos, 'categorias': categorias})

def softwares(request):
  return render(request, 'softwares/softwares.html')