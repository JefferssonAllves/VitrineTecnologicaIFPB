from django.shortcuts import render
from .models import Projeto, Categoria



def home(request):
  if request.method == 'GET':
    projetos = Projeto.objects.all()
    categorias = Categoria.objects.all()

  return render(request, 'home/home.html', {'projetos': projetos, 'categorias': categorias})

def patentes(request):
  return render(request, 'patentes/patentes.html')

def softwares(request):
  return render(request, 'softwares/softwares.html')