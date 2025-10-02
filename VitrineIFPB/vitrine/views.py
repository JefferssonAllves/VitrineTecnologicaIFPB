from django.shortcuts import render
from .models import Projeto, AreaConhecimento



def home(request):
  if request.method == 'GET':
    projetos = Projeto.objects.all()
  return render(request, 'home/home.html', {'projetos': projetos, 'areas': AreaConhecimento.objects.all()})

def patentes(request):
  if request.method == 'GET':
    projetos = Projeto.objects.all()
  return render(request, 'patentes/patentes.html', {'projetos': projetos, 'areas': AreaConhecimento.objects.all()})

def softwares(request):
  return render(request, 'softwares/softwares.html')