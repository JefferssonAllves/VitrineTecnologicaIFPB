from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
  path('', login_required(views.admin), name='administrador'),

  path('login/', views.login, name='login'),
  path('logout/', views.custom_logout, name='logout'),

  path('cadastrar_projeto/', views.cadastrar_projeto, name='cadastrar_projeto'),
  path('editar_projeto/', views.editar_projeto, name='editar_projeto'),
  path('excluir_projeto/', views.excluir_projeto, name='excluir_projeto'),

  path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
  path('editar_categoria/', views.editar_categoria, name='editar_categoria'),
  path('excluir_categoria/', views.excluir_categoria, name='excluir_categoria'),

]
