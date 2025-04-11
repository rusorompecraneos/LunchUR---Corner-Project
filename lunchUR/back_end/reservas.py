from django.contrib import messages
from django.shortcuts import render, redirect
from mi_admin.models import usuarios, Reserva
from django.views import View
from django.utils import timezone
from datetime import timedelta


class Reservas(View):
    def get(self, request):
        
        # Validación de sesión
        numero_id = request.session.get("numero_id")
        if not numero_id:
            messages.error(request, "Debes iniciar sesión para ver tus reservas.")
            return redirect("login")

        try:
            usuario = usuarios.objects.get(numero_id=numero_id)
        except usuarios.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")
            return redirect("login")

        # Obtener reservas del usuario
        reservas = Reserva.objects.filter(usuario=usuario).order_by('-fecha_reserva')

        # Mensajes de bienvenida
        messages.success(request, "Bienvenido a tus reservas 😊")
        messages.info(request, "Aquí podrás ver y hacer tus reservas.")
        messages.warning(
            request,
            "IMPORTANTE: Las reservas deben hacerse mínimo 3 horas antes y máximo 1 día antes."
        )

        return render(request, 'reservas.html', {'reservas': reservas})

    def post(self, request):
        usuario_id = request.session.get("usuario_id")
        if not usuario_id:
            messages.error(request, "Debes iniciar sesión para hacer una reserva.")
            return redirect("login")

        try:
            usuario = usuarios.objects.get(id=usuario_id)
        except usuarios.DoesNotExist:
            messages.error(request, "Usuario no válido.")
            return redirect("login")

        fecha_reserva = request.POST.get("fecha_reserva")

        try:
            # Convertir string a datetime
            fecha_reserva_dt = timezone.datetime.strptime(fecha_reserva, '%Y-%m-%dT%H:%M')
            fecha_reserva_dt = timezone.make_aware(fecha_reserva_dt)  # Marcar como "timezone-aware"
            ahora = timezone.now()

            # Validaciones de tiempo
            if fecha_reserva_dt < ahora + timedelta(hours=3):
                messages.error(request, "La reserva debe hacerse al menos 3 horas antes.")
                return redirect("reservas")

            if fecha_reserva_dt > ahora + timedelta(days=1):
                messages.error(request, "La reserva debe hacerse máximo con 1 día de anticipación.")
                return redirect("reservas")

            # Verificar si ya hay una reserva para ese momento exacto
            if Reserva.objects.filter(fecha_reserva=fecha_reserva_dt).exists():
                messages.error(request, "Esta hora ya está reservada.")
                return redirect("reservas")

            # Crear y guardar la reserva
            nueva_reserva = Reserva(usuario=usuario, fecha_reserva=fecha_reserva_dt)
            nueva_reserva.save()

            messages.success(request, "¡Reserva realizada con éxito! 🎉")
            return redirect("reservas")

        except ValueError:
            messages.error(request, "Formato de fecha inválido.")
            return redirect("reservas")
