from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor

# Create your views here.


def inicio(request):

    return render(request, "AppCoder/padre.html")


def curso(request):

    return render(request, "AppCoder/curso.html")


def estudiante(request):

    return render(request, "AppCoder/estudiante.html")


def entregable(request):

    return render(request, "AppCoder/entregable.html")


def profesor(request):

    profesor1 = Profesor(
        nombre="Fulano", apellido="Ramirez", email="a@a.com", profesion="Abogado"
    )
    context = {"profesor1": profesor1}
    return render(request, "AppCoder/profesores.html", context)
