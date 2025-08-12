from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request,"contenido/principal.html")

def contacto(request):
    return render(request,"contenido/contacto.html")


