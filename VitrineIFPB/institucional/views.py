from django.shortcuts import render, redirect

# Create your views here.
def institucional(request):
  return render(request, 'institucional/institucional.html')