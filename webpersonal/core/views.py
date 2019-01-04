# from django.shortcuts import render, HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about-me.html")


def contact(request):
    # return HttpResponse(http_header + "<H2>Contacto</H2>")
    return render(request, "core/contact.html")
