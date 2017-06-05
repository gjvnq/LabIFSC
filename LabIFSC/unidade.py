#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .geral import TODAS_AS_UNIDADES, parse_dimensions, acha_unidade

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