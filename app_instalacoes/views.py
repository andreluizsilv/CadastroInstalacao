from django.shortcuts import render, redirect
from .metragem import calculate_metragens, calculate_metragem_adicionadas, calculate_metragem_taxa, calculate_wave
from .models import Instalacao
from django.http import HttpResponseRedirect
import openpyxl
from datetime import datetime
import os

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


def salvar_cadastro(request):
    if request.method == "POST":
        pedido = int(request.POST.get('pedido'))
        vendedor = str(request.POST.get('vendedor'))
        metragem = float(request.POST.get('metragem'))
        valor_unitario = float(request.POST.get('valor_unitario'))
        valor_total = float(request.POST.get('valor_total'))

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

def gerar_excel(request):
    # Consulta para obter as datas do modelo Instalacao
    datas_criadas = Instalacao.objects.values_list('data_criacao', flat=True).distinct()

    # Obter a data formatada para incluir no nome do arquivo
    data_formatada_atual = datetime.now().strftime('%d-%m-%y')

    # Especificar o caminho completo para a pasta onde você deseja salvar o arquivo
    pasta_destino = os.path.join(os.path.dirname(__file__), 'excel')

    # Criar o diretório se ele não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    # Inicializar a flag de redirecionamento
    redirecionou = False

    for data in datas_criadas:
        # Converter a data para o formato apropriado, se necessário
        data_formatada = data.strftime('%d-%m-%t') if isinstance(data, datetime) else data

        # Criando uma nova página para cada data
        instalacoes_page = openpyxl.Workbook()

        # Obtendo a folha ativa
        sheet = instalacoes_page.active

        # Criando as Linhas (Cabeçalho de modo fixo)
        sheet.append([
            'pedido',
            'vendedor',
            'metragem',
            'valor_unitario',
            'valor_total',
        ])

        # Criando as Linhas (dados) para cada data
        dados_data = Instalacao.objects.filter(data_criacao=data)
        for dado in dados_data:
            sheet.append([
                dado.pedido,
                dado.vendedor,
                dado.metragem,
                dado.valor_unitario,
                dado.valor_total,
            ])

        # Salvar a planilha com o nome baseado na data no diretório específico
        caminho_arquivo = os.path.join(pasta_destino, f'teste_com_dados_do_bd_{data_formatada}.xlsx')
        instalacoes_page.save(caminho_arquivo)

        # Atualizar a flag de redirecionamento
        redirecionou = True

    # Redirecionar para a página excel.html após o loop se o redirecionamento ocorreu
    if redirecionou:
        return render(request, 'excel.html', {'datas_criadas': datas_criadas})
    else:
        # Se o loop não for executado (sem datas_criadas), redirecione para a página inicial ('home')
        return HttpResponseRedirect('home')