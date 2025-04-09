from django.contrib import messages
from django.shortcuts import render, redirect
from mi_admin.models import usuarios, Reserva
from django.views import View
from django.utils import timezone
from datetime import timedelta


class Reservas(View):
    def get(self, request):
        # Muestra la página de reservas
        usuario = usuarios.objects.get(id=request.session.get("usuario_id"))
        reservas = Reserva.objects.filter(usuario=usuario).order_by('-fecha_reserva')

        messages.success(request, "Bienvenido a tus reservas. 😊")
        messages.info(request, "Aquí podrás ver y hacer tus reservas.")
        messages.warning(request, "IMPORTANTE: Las reservas se deben hacer como mínimo 3 horas antes y máximo un día antes de la fecha de la reserva.")

        return render(request, 'reservas.html', {'reservas': reservas})

    def post(self, request):
        # Procesa la reserva
        usuario = usuarios.objects.get(numero_id=request.session.get("usuario_id"))
        fecha_reserva = request.POST.get("fecha_reserva")

        try:
            fecha_reserva_dt = timezone.datetime.strptime(fecha_reserva, '%Y-%m-%dT%H:%M')
            ahora = timezone.now()

            if fecha_reserva_dt < ahora + timedelta(hours=3):
                messages.error(request, "La reserva debe hacerse al menos 3 horas antes.")
                return redirect("reservas")

            if fecha_reserva_dt > ahora + timedelta(days=1):
                messages.error(request, "La reserva debe hacerse máximo un día antes.")
                return redirect("reservas")

            # Crear y guardar la reserva
            nueva_reserva = Reserva(usuario=usuario, fecha_reserva=fecha_reserva_dt)
            nueva_reserva.save()

            messages.success(request, "¡Reserva realizada con éxito! 🎉")
            return redirect("reservas")

        except ValueError:
            messages.error(request, "Formato de fecha inválido.")
            return redirect("reservas")