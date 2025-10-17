from django.shortcuts import render
from .models import Projeto, Categoria

#TODO BUSCADOR DE PROJETOS
import json
from django.http import JsonResponse
from django.db.models import Q


def home(request):
  if request.method == 'GET':
    categoria_id = request.GET.get('categoria')
    if categoria_id:
      projetos = Projeto.objects.filter(areas_conhecimento__id=categoria_id)
    else:
      projetos = Projeto.objects.all()
  return render(request, 'home/home.html', {'projetos': projetos, 'categorias': Categoria.objects.all()})

def patentes(request):
  if request.method == 'GET':
    categoria_id = request.GET.get('categoria')
    if categoria_id:
      projetos = Projeto.objects.filter(categoria='patente', areas_conhecimento__id=categoria_id)
    else:
      projetos = Projeto.objects.filter(categoria='patente')
  return render(request, 'patentes/patentes.html', {'projetos': projetos, 'categorias': Categoria.objects.filter(projetos__categoria='patente').distinct()})

def softwares(request):
  if request.method == 'GET':
    projetos = Projeto.objects.filter(categoria='software')
  return render(request, 'softwares/softwares.html', {'projetos': projetos})

def institucional(request):
  return render(request, 'institucional/institucional.html')

def detalhes_projeto(request, projeto_id):
  projeto = Projeto.objects.get(id=projeto_id)
  return render(request, 'detalhes_projeto/detalhes_projeto.html', {'projeto': projeto})


#FUNCAO PARA BUSCAR PROJETOS ATRAVES DA BARRA DE PESQUISA
def buscar_projetos(request):
  if request.method == 'POST':
    body = json.loads(request.body)
    termo = body['termo']

    if not termo:
      projetos = Projeto.objects.all()
    else:
      #TODO Filtra usando Q objects para buscas complexas
      projetos = Projeto.objects.filter(
        Q(titulo__icontains=termo) |
        Q(descricao__icontains=termo) |
        Q(autores__icontains=termo) |
        Q(categoria__icontains=termo) |
        Q(areas_conhecimento__nome__icontains=termo)
      ).distinct()

    projetos_json = []
    for projeto in projetos:
      projetos_json.append({
        'id': projeto.id,
        'titulo': projeto.titulo,
        'descricao': projeto.descricao,
        'autores': projeto.autores,
        'categoria': projeto.categoria,
        'imagem_url': projeto.imagem.url if projeto.imagem else '',
        'areas_conhecimento': [area.nome for area in projeto.areas_conhecimento.all()]
      })
    return JsonResponse({'projetos': projetos_json})
  return JsonResponse({'error': 'Invalid request method'}, status=400)
