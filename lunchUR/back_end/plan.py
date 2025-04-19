from django.views import View
from django.shortcuts import render
import random

class PlanNutricional(View):
    def get(self, request):
        return render(request, 'planes_nutricionales.html')

    def post(self, request):
        peso = float(request.POST.get("peso"))
        estatura_cm = float(request.POST.get("estatura"))
        estatura_m = estatura_cm / 100
        edad = int(request.POST.get("edad"))
        actividad = request.POST.get("actividad_fisica")  # 'baja', 'moderada', 'alta'

        imc = peso / (estatura_m ** 2)

        if imc < 18.5:
            objetivo = "subir"
        elif 18.5 <= imc < 25:
            if actividad == "alta":
                objetivo = "subir"
            else:
                objetivo = "Mantener el peso"
        elif 25 <= imc < 30:
            objetivo = "Bajar de peso"
        else:
            objetivo = "Bajar de peso"
            
            
        #Definiremos algunas comidas base que van a servir para todos los objetivos.  
        comidas_base = {
            "desayuno": [
                "Avena con fruta y yogur", "Tostadas integrales con huevo", "Smoothie de banana y mantequilla de maní"
            ],
            "almuerzo": [
                "Pollo con arroz y verduras", "Pescado al horno con camote", "Lentejas con quinoa y ensalada"
            ],
            "cena": [
                "Ensalada con huevo y aguacate", "Tortilla de espinaca", "Crema de verduras con pan integral"
            ]
        }

        if objetivo == "subir peso":
            comidas_base["snack"] = ["Batido proteico", "Frutos secos con yogur", "Pan con aguacate y huevo"]
        elif objetivo == "bajar peso":
            comidas_base["snack"] = ["Zanahoria con hummus", "Manzana con canela", "Yogur bajo en grasa"]
        else:
            comidas_base["snack"] = ["Fruta fresca", "Té verde y galletas integrales", "Smoothie verde"]

        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        plan = []

        for dia in dias_semana:
            plan.append({
                "dia": dia,
                "desayuno": random.choice(comidas_base["desayuno"]),
                "almuerzo": random.choice(comidas_base["almuerzo"]),
                "cena": random.choice(comidas_base["cena"]),
                "snack": random.choice(comidas_base["snack"]),
            })

        return render(request, 'planes_nutricionales.html', {
            "plan": plan,
            "objetivo": objetivo.capitalize()
        })
