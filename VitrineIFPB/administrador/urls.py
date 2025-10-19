from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
  path('', login_required(views.admin), name='administrador'),

  path('login/', views.login, name='login'),
  path('logout/', views.custom_logout, name='logout'),
  path('cadastrar_admin/', views.cadastrar_admin, name='cadastrar_admin'),


  path('projetos/', views.projetos, name='projetos'),
  path('cadastrar_projeto/', views.cadastrar_projeto, name='cadastrar_projeto'),
  path('editar_projeto/', views.editar_projeto, name='editar_projeto'),
  path('excluir_projeto/', views.excluir_projeto, name='excluir_projeto'),

  path('categorias/', views.categorias, name='categorias'),
  path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
  path('editar_categoria/', views.editar_categoria, name='editar_categoria'),
  path('excluir_categoria/', views.excluir_categoria, name='excluir_categoria'),

  path('campus/', views.campus, name='campus'),
  path('cadastrar_campus/', views.cadastrar_campus, name='cadastrar_campus'),
  path('editar_campus/', views.editar_campus, name='editar_campus'),
  path('excluir_campus/', views.excluir_campus, name='excluir_campus'),

]
