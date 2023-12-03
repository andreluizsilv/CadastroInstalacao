from django.shortcuts import render
from django.http import HttpResponse
from .metragem import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def pedido_cadastrados(request):
    if request.method == "GET":
        return render(request, 'home.html')
    elif request.method == "POST":
        pedido = request.POST.get('pedido')
        vendedor = request.POST.get('vendedor')
        valores = request.POST.get('metragem_inteiro')
        if valores != 0:
            valores = list(metragens(float(valores)))
            for valor in valores:
                metragem = valores[0]
                valor_unitario = valores[1]
                valor_total = valores[2]

        print(f'Pedido: {pedido} Vendedor: {vendedor} metragem: {metragem} valor unitario: {valor_unitario} valor Total: {valor_total} ')
        return  HttpResponse("Estou Aqui!")
