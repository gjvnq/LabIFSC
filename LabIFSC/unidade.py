#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .geral import TODAS_AS_UNIDADES, parse_dimensions, acha_unidade, dimensao_em_texto, gera_expoente, sigla_prefixo, nome_prefixo, sigla_prefixo_latex, comando_siunitx_prefixo

class Unidade:
    nome = ""
    simbolo = ""
    simbolo_latex = ""
    simbolo_siunitx = ""
    # As dimensões são (comprimento, ângulo, massa, tempo, temperatura, corrente, mol)
    dimensao = (0, 0, 0, 0, 0, 0, 0)
    # Valor que deve ser multiplicado para obter o valor no MKS
    cte_multiplicativa = None
    # Valor que deve ser adicionado para obter o valor no MKS
    cte_aditiva = None
    unidade_pai = None
    expoente_pai = None

    def __init__(self, nome, simbolo, simbolo_latex, dimensao, cte_multiplicativa, cte_aditiva, simbolo_siunitx=None):
        self.nome = str(nome).replace(" ", "_")
        self.simbolo = str(simbolo)
        self.simbolo_latex = str(simbolo_latex)

        if simbolo_siunitx is None or simbolo_siunitx == "":
            self.simbolo_siunitx = str(simbolo_latex)
        else:
            self.simbolo_siunitx = str(simbolo_siunitx)

        self.cte_multiplicativa = cte_multiplicativa
        self.cte_aditiva = cte_aditiva
        if isinstance(dimensao, tuple):
            self.dimensao = dimensao
        else:
            self.dimensao = parse_dimensions(dimensao)

        self.unidade_pai = self
        self.expoente_pai = 1

        # Registre unidade
        global TODAS_AS_UNIDADES
        TODAS_AS_UNIDADES[nome.lower()] = self
        if simbolo not in TODAS_AS_UNIDADES:
            TODAS_AS_UNIDADES[simbolo] = self

    def __hash__(self):
        return hash(self.nome)

    def __str__(self):
        return self.nome

    def __eq__(self, other):
        if isinstance(other, Unidade):
            return self.nome == other.nome
        return False
    def nova_unidade_por_expoente(self, e):
        global TODAS_AS_UNIDADES

        # Veja os casos especiais
        if e == 1:
            return self
        if e == 0:
            return None
        if self.simbolo+gera_expoente(e) in TODAS_AS_UNIDADES:
            return TODAS_AS_UNIDADES[self.simbolo+gera_expoente(e)]
        if self.nome+"^"+str(e) in TODAS_AS_UNIDADES:
            return TODAS_AS_UNIDADES[self.nome+"^"+str(e)]
        if self != self.unidade_pai and self.expoente_pai != 1:
            return self.unidade_pai.nova_unidade_por_expoente(self.expoente_pai*e)

        # Decida como será o símbolo para o siunitx
        simbolo_siunitx = ""
        if self.simbolo_siunitx != "":
            simbolo_siunitx = self.simbolo_siunitx
            if abs(e) == 2:
                simbolo_siunitx += "\\squared"
            elif abs(e) == 3:
                simbolo_siunitx += "\\cubed"
            else:
                simbolo_siunitx += "\\tothe{{{}}}".format(abs(e))

        # Gere a nova unidade
        cte_m = self.cte_multiplicativa**e
        cte_a = self.cte_aditiva
        dim = tuple([x*e for x in self.dimensao])
        u = Unidade(self.nome+"^"+str(e), self.simbolo+gera_expoente(e), self.simbolo_latex+"^"+str(e), dim, cte_m, cte_a, simbolo_siunitx)
        u.unidade_pai = self
        u.expoente_pai = e
        return u

    def nova_unidade_por_prefixo(self, cte):
        global TODAS_AS_UNIDADES

        # Veja os casos especiais
        if cte == 1:
            return self
        if cte == 0:
            return None
        simbolo = nome_prefixo(cte)+self.simbolo
        if simbolo in TODAS_AS_UNIDADES:
            return TODAS_AS_UNIDADES[simbolo]
        simbolo = sigla_prefixo(cte)+self.simbolo
        if simbolo in TODAS_AS_UNIDADES:
            return TODAS_AS_UNIDADES[simbolo]
        if self != self.unidade_pai:
            return self.unidade_pai.nova_unidade_por_expoente(self.expoente_pai*e)

        # Decida como será o símbolo para o siunitx
        simbolo_siunitx = ""
        if self.simbolo_siunitx != "":
            simbolo_siunitx = comando_siunitx_prefixo(cte)+self.simbolo_siunitx

        # Gere a nova unidade
        cte_m = self.cte_multiplicativa*cte
        cte_a = self.cte_aditiva*cte
        u = Unidade(nome_prefixo(cte)+self.nome, simbolo, sigla_prefixo_latex(cte)+self.simbolo_latex, self.dimensao, cte_m, cte_a, simbolo_siunitx)
        u.unidade_pai = self
        u.expoente_pai = 1
        return u

    def __repr__(self):
        try:
            return "<{}:*{}:+{}:{}>".format(self.nome, self.cte_multiplicativa.nominal, self.cte_aditiva.nominal, dimensao_em_texto(self.dimensao))
        except:
            return "<{}:*?:+?:{}>".format(self.nome, dimensao_em_texto(self.dimensao))