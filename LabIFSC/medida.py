#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .geral import acha_unidade, calcula_dimensao, analisa_numero, dimensao_em_texto

class Medida:
    unidades_originais = [] # Tuplas (objeto unidade, expoente) na ordem em que foram entradas  
    dimensao = (0, 0, 0, 0, 0, 0, 0)
    nominal = 0.0
    incerteza = 0.0

    def __init__(self, valor, unidade_txt=None):
        # Analise o valor
        if isinstance(valor, Medida):
            self.nominal = valor.nominal
            self.incerteza = valor.incerteza
        elif isinstance(valor, str):
            self.nominal, self.incerteza = analisa_numero(valor)
        elif isinstance(valor, tuple) and len(valor) == 2:
            self.nominal, self.incerteza = float(valor[0]), float(valor[1])
        else:
            try:
                self.nominal = float(valor)
            except:
                raise Exception("não foi possível extrair o valor e a incerteza")

        # Veja as unidades
        self.unidades_originais = []
        if unidade_txt != None:
            unidade_txt = unidade_txt.split(" ")
            for unidade in unidade_txt:
                self.unidades_originais.append(acha_unidade(unidade))
        self.dimensao = calcula_dimensao(self.unidades_originais)

    def _checa_dim(self, other):
        print(self.dimensao, other.dimensao)
        if self.dimensao != other.dimensao:
            raise Exception("dimensões físicas incomaptíveis: {} vs {}".format(dimensao_em_texto(self.dimensao), dimensao_em_texto(other.dimensao)))

    def __eq__(self, other):
        if not isinstance(other, Medida):
            raise Exception("medidas só podem ser comparadas com outras medidas")
        self._checa_dim(other)
        return abs(self.nominal - other.nominal) <= 2 * (self.incerteza + other.incerteza)
    def __ne__(self, other):
        if not isinstance(other, Medida):
            raise Exception("medidas só podem ser comparadas com outras medidas")
        self._checa_dim(other)
        return abs(self.nominal - other.nominal) > 3 * (self.incerteza + other.incerteza)
    def __add__(self, other):
        pass
    def __sub__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __floordiv__(self, other):
        pass
    def __mod__(self, other):
        pass
    def __divmod__(self, other):
        pass
    def __pow__(self, other):
        pass
    def __div__(self, other):
        pass
    def __abs__(self):
        pass
    def __complex__(self):
        pass
    def __int__(self):
        pass
    def __float__(self):
        pass
    def __radd__(self, other):
        pass
    def __rsub__(self, other):
        pass
    def __rmul__(self, other):
        pass
    def __rfloordiv__(self, other):
        pass
    def __rmod__(self, other):
        pass
    def __rdivmod__(self, other):
        pass
    def __rpow__(self, other):
        pass
    def __rdiv__(self, other):
        pass