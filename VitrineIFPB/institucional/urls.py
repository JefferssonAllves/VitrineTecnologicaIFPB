from django.urls import path
from . import views
urlpatterns = [
  path('institucional/', views.institucional, name='institucional'),
]
