#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .geral import acha_unidade, calcula_dimensao, analisa_numero, dimensao_em_texto, fator_de_conversao_para_si, unidades_em_texto, converte_unidades, analisa_unidades, simplifica_unidades

class Medida:
    unidades_originais = [] # Tuplas (objeto unidade, expoente) na ordem em que foram entradas  
    dimensao = (0, 0, 0, 0, 0, 0, 0)
    nominal = 0.0
    incerteza = 0.0
    si_nominal = 0.0
    si_incerteza = 0.0

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
        if isinstance(unidade_txt, list):
            self.unidades_originais = unidade_txt
        elif unidade_txt != None:
            self.unidades_originais = analisa_unidades(unidade_txt)
        self.dimensao = calcula_dimensao(self.unidades_originais)

        # Converta para o SI
        mul_nom, mul_err, add_nom, add_err = fator_de_conversao_para_si(self.unidades_originais)
        self.si_nominal = self.nominal * mul_nom + add_nom
        self.si_incerteza = (self.nominal * mul_err + mul_nom * self.incerteza)  + add_err

    def _checa_dim(self, other):
        if self.dimensao != other.dimensao:
            raise Exception("dimensões físicas incomaptíveis: {} vs {}".format(dimensao_em_texto(self.dimensao), dimensao_em_texto(other.dimensao)))
    def _eh_medida(self, other):
        if not isinstance(other, Medida):
            raise Exception("medidas só podem ser comparadas, somadas ou subitraídas com outras medidas")
    def _torne_medida(self, other):
        if not isinstance(other, Medida):
            return Medida(other)
        return other

    def __str__(self):
        return "{}±{} {}".format(self.nominal, self.incerteza, unidades_em_texto(self.unidades_originais))

    def __repr__(self):
        return "<{}±{} {} = {}±{} {}>".format(self.nominal, self.incerteza, unidades_em_texto(self.unidades_originais), self.si_nominal, self.si_incerteza, dimensao_em_texto(self.dimensao))

    def __eq__(self, other):
        self._eh_medida(other)
        self._checa_dim(other)
        return abs(self.si_nominal - other.si_nominal) <= 2 * (self.si_incerteza + other.si_incerteza)
    def __ne__(self, other):
        self._eh_medida(other)
        self._checa_dim(other)
        return abs(self.si_nominal - other.si_nominal) > 3 * (self.si_incerteza + other.si_incerteza)
    def __add__(self, other):
        self._eh_medida(other)
        self._checa_dim(other)
        nom, err = converte_unidades(other.nominal, other.incerteza, other.unidades_originais, self.unidades_originais)
        return Medida((self.nominal+nom, self.incerteza+err), self.unidades_originais)
    def __sub__(self, other):
        self._eh_medida(other)
        self._checa_dim(other)
        nom, err = converte_unidades(other.nominal, other.incerteza, other.unidades_originais, self.unidades_originais)
        return Medida((self.nominal-nom, self.incerteza+err), self.unidades_originais)
    def __mul__(self, other):
        other = self._torne_medida(other)
        nom = self.nominal * other.nominal
        err = self.nominal * other.incerteza + self.incerteza * other.nominal
        m = Medida((nom, err), simplifica_unidades(self.unidades_originais+other.unidades_originais))
        print(self.__repr__(), "*", other.__repr__(), "=", m.__repr__())
        return m

    def __floordiv__(self, other):
        pass
    def __mod__(self, other):
        pass
    def __divmod__(self, other):
        pass
    def __pow__(self, other):
        if isinstance(other, Medida):
            raise Exception("não implementado")
        else:
            return Medida((self.nominal**other, other*self.nominal**(other-1)*self.incerteza), self.unidades_originais)
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