from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Aqui va el back

#En la carpeta "mi_admin" se crea una carpeta llamada "Templates" para que el front (html y css).

def mi_vista(request):
    return HttpResponse("¡Hola, LunchUR!")