from django.shortcuts import render, redirect
from django.contrib import messages
from mi_admin.models import usuarios
import random
from django.views import View

class CrearPlan(View):
    def get(self, request):
        return render(request, 'crear_plan.html')

    def post(self, request):
        peso = float(request.POST.get("peso"))
        estatura = float(request.POST.get("estatura"))
        edad = int(request.POST.get("edad"))
        actividad = request.POST.get("actividad")

        # Cálculo simple de IMC
        imc = peso / ((estatura / 100) ** 2)
        objetivo = "mantener"

        if imc < 18.5:
            objetivo = "subir"
        elif imc > 24.9:
            objetivo = "bajar"

        comidas = {
            "subir": ["Desayuno energético", "Almuerzo proteico", "Cena con carbohidratos"],
            "bajar": ["Desayuno ligero", "Ensalada con proteína", "Cena con vegetales"],
            "mantener": ["Desayuno balanceado", "Almuerzo saludable", "Cena moderada"]
        }

        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        plan_semanal = [{"dia": d, "comida": random.choice(comidas[objetivo])} for d in dias]

        context = {
            "plan": {
                "objetivo": objetivo,
                "semanal": plan_semanal
            }
        }

        return render(request, 'crear_plan.html', context)