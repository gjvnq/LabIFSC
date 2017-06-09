#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from copy import copy

def media(x, erro="desvio padrão"):
    try:
        x = list(x)
    except:
        raise ValueError("x deve ser uma lista ou algo conversível em lista")

    acumulador = copy(x[0])
    acumulador *= 0
    for elemento in x:
        acumulador += elemento
    acumulador /= len(x)

    try:
        avg = copy(acumulador)
        avg.inicializa("0", acumulador.unidades_originais)
    except:
        erro = "nenhum"

    avg = copy(acumulador)
    erro_val = 0.0
    if erro == "nenhum":
        return avg
    elif erro == "desvio padrão":
        erro_val = desvio_padrao(x)
        avg.inicializa((acumulador.nominal, erro_val), acumulador.unidades_originais)
        return avg
    elif erro == "propagação":
        return avg
    else:
        raise ValueError("mecanismo de erro desconhecido: {}".format(erro))


def desvio_padrao(x):
    try:
        x = list(x)
    except:
        raise ValueError("x deve ser uma lista ou algo conversível em lista")

    try:
        avg = sum(list(map(lambda x: x.nominal, x)))/len(x)
    except:
        avg = sum(x)/len(x)

    acumulador = 0.0
    for elemento in x:
        acumulador += (elemento.nominal - avg)**2
    acumulador /= max(len(x)-1, 1)
    acumulador = math.sqrt(acumulador)
    return acumulador

def linearize(x, y):
    pass

# Compara todos os pares (xi, xj) e os retorna em três grupos de acordo com a função de igualdade e desigualdade
def compare(x):
    pass