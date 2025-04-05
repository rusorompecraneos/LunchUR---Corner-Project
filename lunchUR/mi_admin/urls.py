#En la carpeta "mi_admin" se crea una carpeta llamada "urls.py" para que Django pueda reconocer las urls.
from django.urls import path
from . import views     
from .views import LoginUsuario     # Importa el login del html
from .views import RegistroView  # Importa el registro que se hizo en la vista. 
from .views import ofertas_del_dia 
from .views import Nuestros_productos
from .views import canales_apoyo
from .views import perfil_usuario


urlpatterns = [
    path('', views.inicio.as_view(), name='inicio'), 
    path('login/', LoginUsuario.as_view(), name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
    # path('reservas/' , views.id_reservas.as_view(), name='')  #Hay que modificar esta direccion luego. HAY QUE HACERLA. 
     path('ofertas/', ofertas_del_dia, name='ofertas'),
    # path('inicio_home', inicio_home.as_view(), name='inicio_home'), #Editar dependiendo de lo que mande Paola. 
    path('productos/', Nuestros_productos.as_view(), name='productos'), 
    path('canales_de_apoyo/', canales_apoyo, name='canales_apoyo'),
    path('perfil/', perfil_usuario, name='perfil'), #DEBE ESTAR EN EL HOME, IMPLEMENTALO. 
]   



