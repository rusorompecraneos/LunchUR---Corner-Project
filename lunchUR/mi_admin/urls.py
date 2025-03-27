#En la carpeta "mi_admin" se crea una carpeta llamada "urls.py" para que Django pueda reconocer las urls.
from django.urls import path
from . import views     
from .views import LoginUsuario     # Importa el login del html
from .views import RegistroView  # Importa el registro que se hizo en la vista. 



urlpatterns = [
    path('', views.inicio.as_view(), name='inicio'), 
    path('login/', LoginUsuario.as_view(), name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('lista_productos', views.Lista_de_precios.as_view(), name='lista_productos')

]

