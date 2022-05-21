from django.shortcuts import render


ingredientes = ['Harina', 'Manteca', 'Azúcar', 'Levadura', 'Huevo', 'Sal']
proporciones = [0.5, 0.3, 0.18, 0.02, 1, 0.01] # Receta para 24 medialunas aprox.

def index(request):
    return render(request, 'costo/index.html', {'ingredientes': ingredientes})


def calcular(request):
    costos = dict(request.POST)['costos']
    cantidades = dict(request.POST)['cantidades']

    total = 0
    for i in range(len(costos)):
        total += proporciones[i] * float(costos[i]) / float(cantidades[i])


    return render(request,
                  'costo/resultado.html',
                  {'total_24': round(total, 2),
                   'total_1':  round(total/24, 2)
                  }   
    )

