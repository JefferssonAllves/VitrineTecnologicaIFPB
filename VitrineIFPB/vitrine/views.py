from django.shortcuts import render
from .models import Projeto, Categoria

#TODO BUSCADOR DE PROJETOS
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Q


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

@csrf_exempt
def buscar_projetos(request):
  if request.method == 'POST':
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    termo = body['termo']

    if not termo:
      projetos = Projeto.objects.all()
    else:
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