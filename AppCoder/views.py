from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def inicio(request):

    return render(request, "AppCoder/padre.html")


def curso(request):

    return render(request, "AppCoder/curso.html")


def estudiante(request):

    return render(request, "AppCoder/estudiante.html")
