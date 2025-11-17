from django.shortcuts import render
from .models import Projeto, Categoria, Campus

#TODO BUSCADOR DE PROJETOS
import json
from django.http import JsonResponse
from django.db.models import Q


def home(request):
  print(Projeto.objects.all().count())
  return render(request, 'home/home.html', {'projetos': filtrar_projetos(request), 'categorias': Categoria.objects.all(), 'campus': Campus.objects.all()})

def patentes(request):
  return render(request, 'patentes/patentes.html', {'projetos': filtrar_projetos(request), 'categorias': Categoria.objects.all(), 'campus': Campus.objects.all()})

def softwares(request):
  return render(request, 'softwares/softwares.html', {'projetos': filtrar_projetos(request), 'categorias': Categoria.objects.all(), 'campus': Campus.objects.all()})

def institucional(request):
  return render(request, 'institucional/institucional.html')

def detalhes_projeto(request, projeto_id):
  projeto = Projeto.objects.get(id=projeto_id)
  return render(request, 'detalhes_projeto/detalhes_projeto.html', {'projeto': projeto})

def filtrar_projetos(request):
  categoria_id = request.GET.get('categoria')
  campus_id = request.GET.get('campus')
  if categoria_id:
    return Projeto.objects.filter(categorias__id=categoria_id)
  elif campus_id:
    return Projeto.objects.filter(campus__id=campus_id)
  return Projeto.objects.all()

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
        Q(servidor_solicitante__icontains=termo) |
        Q(descricao__icontains=termo) |
        Q(setor_lotacao__icontains=termo)
      ).distinct()

    projetos_json = []
    for projeto in projetos:
      projetos_json.append({
        'id': projeto.id,
        'imagem_url': projeto.imagem.url if projeto.imagem else '',
        'titulo': projeto.titulo,
        'descricao': projeto.descricao,
        'setor_lotacao': projeto.setor_lotacao,
        'ano_deposito': projeto.ano_deposito,
        'status': projeto.status,
        'observacoes': projeto.observacoes,
        'categorias': [categoria.nome for categoria in projeto.categorias.all()],
      })
    return JsonResponse({'projetos': projetos_json})
  return JsonResponse({'error': 'Invalid request method'}, status=400)

#FUNCAO PARA BUSCAR CATEGORIAS ATRAVES DA BARRA DE PESQUISA
def buscar_categorias(request):
  if request.method == 'POST':
    body = json.loads(request.body)
    termo = body['termo']

    if not termo:
      categorias = Categoria.objects.all()
    else:
      categorias = Categoria.objects.filter(nome__icontains=termo)

    categorias_json = []
    for categoria in categorias:
      categorias_json.append({
        'id': categoria.id,
        'nome': categoria.nome,
      })
    return JsonResponse({'categorias': categorias_json})
  return JsonResponse({'error': 'Invalid request method'}, status=400)
