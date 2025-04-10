from django.contrib import admin
from mi_admin.models import usuarios
from mi_admin.models import menus
from mi_admin.models import alimentos_menu
from mi_admin.models import planes_alimenticios
from mi_admin.models import Reserva
from mi_admin.models import PerfilUsuario
from mi_admin.models import CanalDeApoyo
from mi_admin.models import Oferta


 #Register your models here.
admin.site.register(usuarios)
admin.site.register(menus)
admin.site.register(alimentos_menu)
admin.site.register(planes_alimenticios)
admin.site.register(Reserva)
admin.site.register(PerfilUsuario)
admin.site.register(CanalDeApoyo)
admin.site.register(Oferta)



