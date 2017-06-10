#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from .matematica import soma, sqrt
from copy import copy

def media(x, incerteza="desvio padrão"):
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
        incerteza = "nenhum"

    avg = copy(acumulador)
    incerteza_val = 0.0
    if incerteza == "nenhum":
        return avg
    elif incerteza == "desvio padrão":
        incerteza_val = desvio_padrao(x)
        avg.inicializa((acumulador.nominal, incerteza_val), acumulador.unidades_originais)
        return avg
    elif incerteza == "propagação":
        return avg
    else:
        raise ValueError("mecanismo de incerteza desconhecido: {}".format(incerteza))


def desvio_padrao(x):
    try:
        x = list(x)
    except:
        raise ValueError("x deve ser uma lista ou algo conversível em lista")

    avg = soma(x)/len(x)

    acumulador = 0.0
    for elemento in x:
        acumulador += (elemento.nominal - avg.nominal)**2
    acumulador /= max(len(x)-1, 1)
    acumulador = math.sqrt(acumulador)
    return acumulador

def linearize(x, y, imprimir=False):
    if len(x) == 0 or len(y) == 0 or len(x) != len(y):
        raise ValueError("As listas para os valores de 'x' e 'y' tem que ser não nulas ter o mesmo tamanho.")
    x_avg = sum(x)/len(x)
    y_avg = sum(y)/len(y)

    a = sum(list(map(lambda x, y: (x-x_avg)*y, x, y)))
    a /= sum(list(map(lambda x: (x-x_avg)**2, x)))

    b = y_avg - a * x_avg

    dy = sqrt(sum(map(lambda x, y: (a*x + b - y)**2, x, y))/(len(x)-2))

    da = dy/sqrt(sum(map(lambda x: (x-x_avg)**2, x)))

    db = sqrt(sum(map(lambda x: x**2, x))/(len(x)*sum(map(lambda x: (x-x_avg)**2, x))))

    if imprimir:
        print("a  = {}".format(a))
        print("b  = {}".format(b))
        print("Δy = {}".format(dy))
        print("Δa = {}".format(da))
        print("Δb = {}".format(db))

    return {"a": a, "b": b, "Δy": dy, "Δa": da, "Δb": db}

# Compara todos os pares (xi, xj) e os retorna em três grupos de acordo com a função de igualdade e desigualdade
def compare(x):
    pass