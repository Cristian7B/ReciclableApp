from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "Reciclable/inicio.html/")

def tecnologias(request):
    return render(request, "Reciclable/tecnologias.html/")

def nosotros(request):
    return render(request, "Reciclable/nosotros.html/")