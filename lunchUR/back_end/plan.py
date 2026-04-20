from django.views import View
from django.shortcuts import render
import random

# Clase para determinar el objetivo del usuario. 
class PlanNutricional(View):
    def get(self, request):
        return render(request, 'planes_nutricionales.html')
    # Funcion en la que definimos 
    def post(self, request):
        peso = float(request.POST.get("Peso"))
        estatura_cm = float(request.POST.get("Estatura"))
        estatura_m = estatura_cm / 100
        edad = int(request.POST.get("Edad"))
        actividad = request.POST.get("Actividad_fisica")  # 'baja', 'moderada', 'alta'

        imc = peso / (estatura_m ** 2)

        if imc < 18.5:
            objetivo = "Subir de peso"
        elif 18.5 <= imc < 25:
            if actividad == "alta":
                objetivo = "Subir de peso"
            else:
                objetivo = "Mantener el peso"
        elif 25 <= imc < 30:
            objetivo = "Bajar de peso"
        else:
            objetivo = "Bajar de peso"
            
            
        #Definiremos algunas comidas base que van a servir para todos los objetivos.  
        comidas_base = {
            "Desayuno": [
                "Avena con fruta y yogur", "Tostadas integrales con huevo", "Smoothie de banana y mantequilla de maní", "Omelette de vegetales", "Yogur griego con frutos rojos y granola"
            ],
            "Almuerzo": [
                "Bowl gladiador", "Mega muscle plato", "Tortilla saludable", "Menu marino", "Ensalada energetica", "Pasta tradicional", "Clasico casero"
            ],
            "Cena": [
                "Ensalada con huevo y aguacate", "Tortilla de espinaca", "Crema de verduras con pan integral", "Tacos de lechuga", "Salmón al horno con espárragos"
            ]
        }
        # Definimos los objetivos que existen y un menu para cada objetivo. 
        if objetivo == "subir peso":
            comidas_base["Snack"] = ["Batido proteico", "Frutos secos con yogur", "Pan con aguacate y huevo", "Rebanada de pan y 2 huevos", "Yogur natural con semillas y miel"]
        elif objetivo == "bajar peso":
            comidas_base["Snack"] = ["Zanahoria con hummus", "Manzana con canela", "Yogur bajo en grasa", "Palitos de zanahoria o pepino con hummus"]
        else:
            comidas_base["Snack"] = ["Fruta fresca", "Té verde y galletas integrales", "Smoothie verde", "Una fruta de tu preferencia", "Tostadas de arroz con aguacate"]

        dias_semana = ["Lunes:", "Martes:", "Miércoles:", "Jueves:", "Viernes:", "Sábado:", "Domingo:"]
        plan = []

        # Hacemos el for, para recorrer la lista de dias de la semana y de menus. 
        for dia in dias_semana:
            plan.append({
                "dia": dia,
                "desayuno": random.choice(comidas_base["Desayuno"]),
                "almuerzo": random.choice(comidas_base["Almuerzo"]),
                "cena": random.choice(comidas_base["Cena"]),
                "snack": random.choice(comidas_base["Snack"]),
            })

        return render(request, 'planes_nutricionales.html', {
            "plan": plan,
            "objetivo": objetivo.capitalize()
        })
