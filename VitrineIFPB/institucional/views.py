from django.shortcuts import render
# Create your views here.
def institucional(request):
  return render(request, 'institucional/institucional.html')