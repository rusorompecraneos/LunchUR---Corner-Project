from django.contrib import messages
from django.shortcuts import render, redirect
from mi_admin.models import usuarios, Reserva, menus
from django.views import View
from django.utils import timezone
from datetime import timedelta
import random


class Reservas_Almuerzos(View):
    def get(self, request):
        numero_id = request.session.get("numero_id")
        if not numero_id:
            messages.error(request, "Debes iniciar sesión para ver tus reservas.")
            return redirect("login")

        try:
            usuario = usuarios.objects.get(numero_id=numero_id)
        except usuarios.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")
            return redirect("login")

        reservas = Reserva.objects.filter(usuario=usuario).order_by('-fecha_reserva')
        menus_disponibles = menus.objects.all()
        
        
        

        messages.success(request, "Bienvenido a tus reservas 😊")
        messages.info(request, "Aquí podrás ver y hacer tus reservas.")
        messages.warning(
            request,
            "IMPORTANTE: Las reservas deben hacerse mínimo 3 horas antes y máximo 1 día antes."
        )

        return render(request, 'reservas.html', {
            'reservas': reservas,
            'menus': menus_disponibles
        })

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
        menu_id = request.POST.get("menu")

        if not menu_id:
            messages.error(request, "Debes seleccionar un menú.")
            return redirect("reservas")

        try:
            fecha_reserva_dt = timezone.datetime.strptime(fecha_reserva, '%Y-%m-%dT%H:%M')
            fecha_reserva_dt = timezone.make_aware(fecha_reserva_dt)
            ahora = timezone.now()

            if fecha_reserva_dt < ahora + timedelta(hours=3):
                messages.error(request, "La reserva debe hacerse al menos 3 horas antes.")
                return redirect("reservas")

            if fecha_reserva_dt > ahora + timedelta(days=1):
                messages.error(request, "La reserva debe hacerse máximo con 1 día de anticipación.")
                return redirect("reservas")

            if Reserva.objects.filter(fecha_reserva=fecha_reserva_dt).exists():
                messages.error(request, "Esta hora ya está reservada.")
                return redirect("reservas")

            menu = menus.objects.get(id=menu_id)

            
            # AQUI VAMOS AGREGAR LA ALETORIDAD DEL NUMERO:
            numero_reserva = random.randint(0, 80)
            
            nueva_reserva = Reserva(
                usuario=usuario,
                fecha_reserva=fecha_reserva_dt,
                menu=menu,
                estado='CONFIRMADA',
                numero_aleatorio=numero_reserva
            )
            nueva_reserva.save()

            messages.success(request, "¡Reserva realizada con éxito! 🎉")
            return redirect("reservas")

        except ValueError:
            messages.error(request, "Formato de fecha inválido.")
            return redirect("reservas")

        except menus.DoesNotExist:
            messages.error(request, "El menú seleccionado no existe.")
            return redirect("reservas")