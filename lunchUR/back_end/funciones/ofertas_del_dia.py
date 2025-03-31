from django.shortcuts import render
from mi_admin.models import Oferta
from django.utils import timezone

def ofertas_del_dia(request):
    hoy = timezone.now().date()
    ofertas = Oferta.objects.filter(fecha_inicio__lte=hoy, fecha_fin__gte=hoy)
    return render(request, 'ofertas.html', {'ofertas': ofertas})
