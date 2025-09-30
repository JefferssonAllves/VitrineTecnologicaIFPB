from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home/home.html')

def patentes(request):
  return render(request, 'patentes/patentes.html')

def softwares(request):
  return render(request, 'softwares/softwares.html')