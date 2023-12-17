# Constantes globais
VALOR_UNITARIO_1 = 38.5
VALOR_UNITARIO_2 = 18.59
VALOR_UNITARIO_3 = 20.69
VALOR_UNITARIO_4 = 22.89
VALOR_UNITARIO_5 = 21.97


def calculate_metragens(metragem):
    if metragem < 1.99:
        valor_unitario = VALOR_UNITARIO_1
        valor_total = VALOR_UNITARIO_1
        return metragem, valor_unitario, valor_total
    elif metragem <= 2.49:
        valor_unitario = VALOR_UNITARIO_2
    elif metragem <= 2.99:
        valor_unitario = VALOR_UNITARIO_3
    else:
        valor_unitario = VALOR_UNITARIO_4

    valor_total = metragem * valor_unitario
    return metragem, valor_unitario, valor_total

def calculate_metragem_adicionadas(metragem):
    valor_unitario = VALOR_UNITARIO_2
    valor_total = metragem * valor_unitario
    return metragem, valor_unitario, valor_total

def calculate_metragem_taxa(taxa):
    metragem = 0
    valor_unitario = taxa
    valor_total = taxa
    return metragem, valor_unitario, valor_total

def calculate_wave(metragem):
    valor_total = metragem * VALOR_UNITARIO_5
    return metragem, VALOR_UNITARIO_5, valor_total
