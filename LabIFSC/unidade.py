#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .variaveis import TODAS_AS_UNIDADES

MAPA_DE_DIMENSOES = {
    "L": 0, # Comprimento | Padrão: metro
    "A": 1, # Ângulo | Padrão: radianos
    "M": 2, # Massa | Padrão: quilograma
    "T": 3, # Tempo | Padrão: segundo
    "K": 4, # Temperatura | Padrão: kelvin
    "I": 5, # Corrente | Padrão: Ampère
    "N": 6  # "Quantidade" | Padrão: mol
}

def parse_dimensions(txt):
    mode = 0 # 0 - Letra | 1 - Número
    num = ""
    dim = ""
    txt = txt.replace(" ", "")
    ans = [0, 0, 0, 0, 0, 0, 0]
    for i, c in enumerate(txt):
        # Se estamos lendo letras
        if mode == 0:
            if c in MAPA_DE_DIMENSOES:
                dim = c
                num = ""
                mode = 1
            else:
                raise Exception("{} não é uma dimensão física conhecida".format(c))
        elif mode == 1:
            if i == len(txt)-1:
                # Terminamos de ler o expoente da dimensão
                num += c
                num = int(num)
                ans[MAPA_DE_DIMENSOES[dim]] += num
            elif c in MAPA_DE_DIMENSOES:
                # Terminamos de ler o expoente da dimensão
                num = int(num)
                ans[MAPA_DE_DIMENSOES[dim]] += num
                dim = c
                num = ""
                mode = 1
            else:
                num += c
        else:
            raise Exception("{} não é um modo válido para parse_dimensions (c={} i={} txt='{}')".format(mode, c, i, txt))
    return tuple(ans)

def acha_unidade(nome):
    nome = nome.lower()
    if nome in TODAS_AS_UNIDADES:
        return TODAS_AS_UNIDADES[nome]
    else:
        raise Exception("unidade '{}' não encontrada".format(nome))

class Unidade:
    nome = ""
    simbolo = ""
    simbolo_latex = ""
    # As dimensões são (comprimento, ângulo, massa, tempo, temperatura, corrente, mol)
    dimensao = (0, 0, 0, 0, 0, 0, 0)
    # Valor que deve ser multiplicado para obter o valor no MKS
    cte_multiplicativa = None
    # Valor que deve ser adicionado para obter o valor no MKS
    cte_aditiva = None

    def __init__(self, nome, simbolo, simbolo_latex, dimensao, cte_multiplicativa, cte_aditiva):
        self.nome = str(nome)
        self.simbolo = str(simbolo)
        self.simbolo_latex = str(simbolo_latex)

        self.cte_multiplicativa = cte_multiplicativa
        self.cte_aditiva = cte_aditiva
        self.dimensao = parse_dimensions(dimensao)

        # Registre unidade
        global TODAS_AS_UNIDADES
        TODAS_AS_UNIDADES[nome.lower()] = self
        if simbolo.lower() not in TODAS_AS_UNIDADES:
            TODAS_AS_UNIDADES[simbolo] = self

    def __hash__(self):
        return hash(self.nome)