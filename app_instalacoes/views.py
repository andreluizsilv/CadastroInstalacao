from django.shortcuts import render
from .metragem import calculate_metragens, calculate_metragem_adicionadas, calculate_metragem_taxa, calculate_wave
from .models import Instalacao


def home(request):
    return render(request,'home.html')
def pedido_cadastrados(request):
    if request.method == "GET":
        # Recupere todos os cadastros do banco de dados
        cadastros = Instalacao.objects.all()
        return render(request, 'pedido_cadastrados.html', {'cadastros': cadastros})
    elif request.method == "POST":
        pedido = request.POST.get('pedido')
        vendedor = request.POST.get('vendedor')

        valores_inteiro = request.POST.get('metragem_inteiro')
        if valores_inteiro != '0':
            valores_inteiro = list(calculate_metragens(float(valores_inteiro)))
            for valor in valores_inteiro:
                metragem = valores_inteiro[0]
                valor_unitario = valores_inteiro[1]
                valor_total = valores_inteiro[2]

        metragem_fracionaro = request.POST.get('metragem_fracionaro')
        if metragem_fracionaro != '0':
            metragem_fracionaro = list(calculate_metragem_adicionadas(float(metragem_fracionaro)))
            for valor in metragem_fracionaro:
                metragem = metragem_fracionaro[0]
                valor_unitario = metragem_fracionaro[1]
                valor_total = metragem_fracionaro[2]

        metragem_wave = request.POST.get('metragem_wave')
        if metragem_wave != '0':
            metragem_wave = list(calculate_wave(float(metragem_wave)))
            for valor in metragem_wave:
                metragem = metragem_wave[0]
                valor_unitario = metragem_wave[1]
                valor_total = metragem_wave[2]

        taxa = request.POST.get('taxa')
        if taxa != '0':
            taxa = list(calculate_metragem_taxa(float(taxa)))
            for valor in taxa:
                metragem = taxa[0]
                valor_unitario = taxa[1]
                valor_total = taxa[2]

        # Não salve no banco de dados ainda, retorne os dados em um contexto
        novo_cadastro = {
            'pedido': pedido,
            'vendedor': vendedor,
            'metragem': metragem,
            'valor_unitario': valor_unitario,
            'valor_total': valor_total
        }

        return render(request, 'cadastro_confirmado.html', novo_cadastro)

# Em views.py
from django.shortcuts import redirect
from .models import Instalacao

def salvar_cadastro(request):
    if request.method == "POST":
        pedido = request.POST.get('pedido')
        vendedor = request.POST.get('vendedor')
        metragem = request.POST.get('metragem')
        valor_unitario = request.POST.get('valor_unitario')
        valor_total = request.POST.get('valor_total')

        # Salvar instalação no Banco de dados
        cadastro_instalacao = Instalacao(
            pedido=pedido,
            vendedor=vendedor,
            metragem=metragem,
            valor_unitario=valor_unitario,
            valor_total=valor_total
        )

        cadastro_instalacao.save()

        return redirect('home')  # Redirecione para a página inicial ou para onde desejar
def inst_cadastradas(request):
    cadastros = Instalacao.objects.all()
    return render(request, 'pedido_cadastrados.html', {'cadastros': cadastros})