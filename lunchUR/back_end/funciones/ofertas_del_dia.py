from django.shortcuts import render
from mi_admin.models import Oferta
from django.utils import timezone

def ofertas_del_dia(request):
    
    ofertas = [
    {
        "titulo": "Combo Almuerzo Rosarista",
        "descripcion": "Incluye bebida + arroz con pollo + postre",
        "descuento": 30,
        "fecha_fin": "2025-04-20"
    },
    {
        "titulo": "Café + Empanada",
        "descripcion": "Perfecto para tu break entre clases",
        "descuento": 15,
        "fecha_fin": "2025-04-18"
    },
]

    hoy = timezone.now().date()
    ofertas = Oferta.objects.filter(fecha_inicio__lte=hoy, fecha_fin__gte=hoy)
    return render(request, 'ofertas.html', {'ofertas': ofertas})

    