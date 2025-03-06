from django.urls import path
from . import views

urlpatterns = [
    path('mi-vista/', views.mi_vista, name='mi_vista'),
    path('', views.mi_vista, name='home'),  
]

#En la carpeta "mi_admin" se crea una carpeta llamada "urls.py" para que Django pueda reconocer las urls.
