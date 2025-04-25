from django.views import View
from django.shortcuts import render, redirect
from mi_admin.models import Reserva

class BotonReservas(View):
    def get(self, request):
        numero_id = request.session.get('numero_id')
        if not numero_id:
            return redirect('login')

        reservas = Reserva.objects.filter(usuario__numero_id=numero_id)
        return render(request, 'boton_reservas.html', {'reservas': reservas})
