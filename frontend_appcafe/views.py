from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Cafe

def incio(request):
    return HttpResponse("<h1> hola cafe</h1>")

def pagina_cafe(request):
    cafes = Cafe.objects.all()
    return render(request, 'cafe.html', {'cafes': cafes})