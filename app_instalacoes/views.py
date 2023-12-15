from django.shortcuts import render
from django.http import HttpResponse
from .metragem import *
from .models import Instalacao

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
        valores = request.POST.get('metragem_fracionaro')
        if valores != 0:
            valores = list(metragem_adicionadas(float(valores)))
            for valor in valores:
                metragem = valores[0]
                valor_unitario = valores[1]
                valor_total = valores[2]
        valores = request.POST.get('metragem_wave')
        if valores != 0:
            valores = list(wave(float(valores)))
            for valor in valores:
                metragem = valores[0]
                valor_unitario = valores[1]
                valor_total = valores[2]
        valores = request.POST.get('taxa')
        if valores != 0:
            valores = list(metragem_taxa(float(valores)))
            for valor in valores:
                metragem = valores[0]
                valor_unitario = valores[1]
                valor_total = valores[2]

        # Salvar instalação no Banco de dados
        cadastro_instalacao = Instalacao()
        cadastro_instalacao.pedido = pedido
        cadastro_instalacao.vendedor = vendedor
        cadastro_instalacao.metragem = metragem
        cadastro_instalacao.valor_unitario = valor_unitario
        cadastro_instalacao.valor_total = valor_total
        cadastro_instalacao.save()

        # Exibir todos as instalação em nova pagina

        return  HttpResponse("Estou Aqui!")
