from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name='home'),
  path('patentes/', views.patentes, name='patentes'),
  path('softwares/', views.softwares, name='softwares'),
]
