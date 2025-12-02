from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as django_login
from vitrine.models import Projeto, Categoria, Campus


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
  return render(request, 'projetos/projetos.html', {'Projeto': Projeto, 'projetos':Projeto.objects.all(), 'categorias':Categoria.objects.all()})

def cadastrar_projeto(request):
  if request.method == 'POST':
    imagem = request.FILES['projeto_imagem']
    titulo = request.POST.get('projeto_titulo')
    campus = request.POST.get('projeto_campus')
    servidor = request.POST.get('projeto_servidor')
    descricao = request.POST.get('projeto_descricao')
    setor_lotacao = request.POST.get('projeto_setor')
    ano_deposito = request.POST.get('projeto_ano')
    categorias = request.POST.getlist('projeto_categorias')
    link_suap = request.POST.get('projeto_link')
    certificado = request.FILES['projeto_certificado']
    status = request.POST.get('projeto_status')
    observacoes = request.POST.get('projeto_observacoes')

    projeto = Projeto(
                      imagem=imagem,
                      titulo=titulo,
                      campus=Campus.objects.get(id=int(campus)),
                      descricao=descricao,
                      servidor_solicitante=servidor,
                      setor_lotacao=setor_lotacao,
                      ano_deposito=ano_deposito,
                      link=link_suap,
                      certificado=certificado,
                      status=status,
                      observacoes=observacoes
                    )
    projeto.save()
    print(categorias)
    for categoria in categorias:
      projeto.categorias.add(Categoria.objects.get(id=int(categoria)))
  else:
    return render(request, 'projetos/cadastrar_projeto.html', {'categorias':Categoria.objects.all(), 'campus': Campus.objects.all(), 'projeto_status': Projeto.STATUS_CHOICES})
  return redirect('projetos')

def editar_projeto(request, projeto_id):
  if request.method == 'POST':
    imagem = request.FILES.get('projeto_imagem')
    titulo = request.POST.get('projeto_titulo')
    campus = request.POST.get('projeto_campus')
    servidor = request.POST.get('projeto_servidor')
    descricao = request.POST.get('projeto_descricao')
    setor_lotacao = request.POST.get('projeto_setor')
    ano_deposito = request.POST.get('projeto_ano')
    categorias = request.POST.getlist('projeto_categorias')
    link_suap = request.POST.get('projeto_link')
    certificado = request.FILES.get('projeto_certificado')
    status = request.POST.get('projeto_status')
    observacoes = request.POST.get('projeto_observacoes')

    projeto = Projeto.objects.get(id=projeto_id)
    if imagem:
      projeto.imagem = imagem

    projeto.titulo = titulo
    projeto.campus = Campus.objects.get(id=int(campus))
    projeto.servidor_solicitante = servidor
    projeto.descricao = descricao
    projeto.setor_lotacao = setor_lotacao
    projeto.ano_deposito = ano_deposito
    projeto.link = link_suap

    if certificado:
      projeto.certificado = certificado

    projeto.status = status
    projeto.observacoes = observacoes
    projeto.save()

    projeto.categorias.clear()
    for categoria in categorias:
      projeto.categorias.add(Categoria.objects.get(id=int(categoria)))

    return redirect('projetos')
  return render(request, 'projetos/editar_projeto.html', {'projeto': Projeto.objects.get(id=projeto_id), 'categorias':Categoria.objects.all(), 'campus': Campus.objects.all(), 'projeto_status': Projeto.STATUS_CHOICES})

def excluir_projeto(request, projeto_id):
  Projeto.objects.filter(id=projeto_id).delete()
  return redirect('projetos')


#TODO CONTROLE DE CATEGORIAS
def categorias(request):

  return render(request, 'categorias/categorias.html', {'categorias':Categoria.objects.all()})

def cadastrar_categoria(request):
  if request.method == 'POST':
    nome = request.POST.get('categoria_nome')
    Categoria(nome=nome).save()
  return redirect('categorias')

def editar_categoria(request):
  if request.method == 'POST':
    id = request.POST.get('categoria_id')
    nome = request.POST.get('categoria_nome')

    Categoria.objects.filter(id=id).update(nome=nome)
  return redirect('categorias')

def excluir_categoria(request):
  if request.method == "POST":
    categoria = request.POST.get('categoria_id')
    Categoria.objects.filter(id=categoria).delete()
  return redirect('categorias')



#TODO CONTROLE DE CAMPUS
def campus(request):
  return render(request, 'campus/campus.html', {'campus':Campus.objects.all()})

def cadastrar_campus(request):
  if request.method == 'POST':
    nome = request.POST.get('campus_nome')
    Campus(nome=nome).save()
  return redirect('campus')

def editar_campus(request):
  if request.method == 'POST':
    id = request.POST.get('campus_id')
    nome = request.POST.get('campus_nome')

    Campus.objects.filter(id=id).update(nome=nome)
  return redirect('campus')

def excluir_campus(request):
  if request.method == "POST":
    campus = request.POST.get('campus_id')
    Campus.objects.filter(id=campus).delete()
  return redirect('campus')