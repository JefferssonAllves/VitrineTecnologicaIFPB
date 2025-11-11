from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
  path('', login_required(views.admin), name='administrador'),

  path('login/', views.login, name='login'),
  path('logout/', views.custom_logout, name='logout'),
  path('cadastrar_admin/', login_required(views.cadastrar_admin), name='cadastrar_admin'),


  path('projetos/', login_required(views.projetos), name='projetos'),
  path('cadastrar_projeto/', login_required(views.cadastrar_projeto), name='cadastrar_projeto'),
  path('editar_projeto/', login_required(views.editar_projeto), name='editar_projeto'),
  path('excluir_projeto/', login_required(views.excluir_projeto), name='excluir_projeto'),

  path('categorias/', login_required(views.categorias), name='categorias'),
  path('cadastrar_categoria/', login_required(views.cadastrar_categoria), name='cadastrar_categoria'),
  path('editar_categoria/', login_required(views.editar_categoria), name='editar_categoria'),
  path('excluir_categoria/', login_required(views.excluir_categoria), name='excluir_categoria'),

  path('campus/', login_required(views.campus), name='campus'),
  path('cadastrar_campus/', login_required(views.cadastrar_campus), name='cadastrar_campus'),
  path('editar_campus/', login_required(views.editar_campus), name='editar_campus'),
  path('excluir_campus/', login_required(views.excluir_campus), name='excluir_campus'),

]
