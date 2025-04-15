#En la carpeta "mi_admin" se crea una carpeta llamada "urls.py" para que Django pueda reconocer las urls.
from django.urls import path
from . import views     
from .views import RegistroView  # Importa el registro que se hizo en la vista. 
from .views import ofertas_del_dia 
from .views import Nuestros_productos
from .views import canales_apoyo
from .views import perfil_usuario
from .views import HomeView
from .views import Login_usuario
from .views import Reservas
from .views import editar_perfil
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.inicio.as_view(), name='inicio'), 
    path('login/', Login_usuario.as_view(), name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('reservas/', Reservas.as_view(), name='reservas'),
    path('ofertas/', ofertas_del_dia, name='ofertas'), 
    path('productos/', Nuestros_productos.as_view(), name='productos'), 
    path('canales_de_apoyo/', canales_apoyo, name='canales_apoyo'),
    path('home/', HomeView.as_view(), name='home'), 
    path('perfil/', perfil_usuario, name='perfil'), 
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    
    
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




