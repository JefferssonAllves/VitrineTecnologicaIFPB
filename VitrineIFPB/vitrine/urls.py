from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name='home'),

  path('patentes/', views.patentes, name='patentes'),
  path('softwares/', views.softwares, name='softwares'),
  path('institucional/', views.institucional, name='institucional'),

  path('detalhes_projeto/id=<int:projeto_id>/', views.detalhes_projeto, name='detalhes_projeto'),
  path('buscar_projetos/', views.buscar_projetos, name='buscar_projetos'),

]
