from django.contrib import admin
from mi_admin.models import usuarios
from mi_admin.models import menus
from mi_admin.models import alimentos_menu
from mi_admin.models import planes_alimenticios
from mi_admin.models import reservas


 #Register your models here.
admin.site.register(usuarios)
admin.site.register(menus)
admin.site.register(alimentos_menu)
admin.site.register(planes_alimenticios)
admin.site.register(reservas)

