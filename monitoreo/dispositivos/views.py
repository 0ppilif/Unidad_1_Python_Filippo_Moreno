from django.shortcuts import render

def inicio(request):
    dispositivos = [
        {"nombre": "Medidor Electrico", "consumo": 30},
        {"nombre": "Refrigeradores", "consumo": 45},
        {"nombre": "Aire Acondicionado", "consumo": 300},
        {"nombre": "Estufa", "consumo": 150}
    ]
    
    consumo_maximo = 100

    return render(request, "dispositivos/inicio.html", {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo
        })
