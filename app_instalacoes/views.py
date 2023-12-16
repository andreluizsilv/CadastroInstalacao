from django.shortcuts import render
from django.http import HttpResponse
from .metragem import metragem_taxa, metragem_adicionadas, metragens, wave
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

        valores_inteiro = request.POST.get('metragem_inteiro')
        if valores_inteiro != '0':
            valores_inteiro = list(metragens(float(valores_inteiro)))
            for valor in valores_inteiro:
                metragem = valores_inteiro[0]
                valor_unitario = valores_inteiro[1]
                valor_total = valores_inteiro[2]

        metragem_fracionaro = request.POST.get('metragem_fracionaro')
        if metragem_fracionaro != '0':
            metragem_fracionaro = list(metragem_adicionadas(float(metragem_fracionaro)))
            for valor in metragem_fracionaro:
                metragem = metragem_fracionaro[0]
                valor_unitario = metragem_fracionaro[1]
                valor_total = metragem_fracionaro[2]

        metragem_wave = request.POST.get('metragem_wave')
        if metragem_wave != '0':
            metragem_wave = list(wave(float(metragem_wave)))
            for valor in metragem_wave:
                metragem = metragem_wave[0]
                valor_unitario = metragem_wave[1]
                valor_total = metragem_wave[2]

        taxa = request.POST.get('taxa')
        if taxa != '0':
            taxa = list(metragem_taxa(float(taxa)))
            for valor in taxa:
                metragem = taxa[0]
                valor_unitario = taxa[1]
                valor_total = taxa[2]

        # Salvar instalação no Banco de dados
        cadastro_instalacao = Instalacao(
            pedido=pedido,
            vendedor=vendedor,
            metragem=metragem,
            valor_unitario=valor_unitario,
            valor_total=valor_total
        )

        cadastro_instalacao.save()





        # Exibir todos as instalação em nova pagina
        instalacoes_cadastradas = {
            'cadastros': Instalacao.objects.all()
        }

        
        return render(request, 'cadastros.html', instalacoes_cadastradas)
