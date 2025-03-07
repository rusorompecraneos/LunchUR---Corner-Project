#En la carpeta "mi_admin" se crea una carpeta llamada "urls.py" para que Django pueda reconocer las urls.
from django.urls import path
from . import views     
from .views import LoginUsuario     # Importa el login del html
from .views import RegistroUsuario  # Importa el registro que se hizo en la vista. 



urlpatterns = [
    path('mi-vista/', views.mi_vista, name='mi_vista'),
    path('', views.mi_vista, name='home'), 
    path('login/', LoginUsuario.as_view(), name='login'),
    path('registro/', RegistroUsuario.as_view(), name='registro')
]

