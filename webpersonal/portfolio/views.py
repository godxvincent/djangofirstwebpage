from django.shortcuts import render
from .models import Project

# Create your views here.


def portfolio(request):
    projects = Project.objects.all()
    # Para pasar datos desde el controlador de la vista se crea un diccionario
    # con el nombre de la variable que reconocera el template.
    return render(request, "portfolio/portfolio.html", {'projects': projects})
