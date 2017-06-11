#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy
from math import floor, log, ceil
from .geral import acha_unidade, calcula_dimensao, analisa_numero, dimensao_em_texto, fator_de_conversao_para_si, unidades_em_texto, converte_unidades, analisa_unidades, simplifica_unidades, gera_expoente, adimensional, get_unidades

def M(val, incerteza = None, unidade = None):
    # Talvez seja uma lista de números para converter
    if isinstance(val, list):
        ret = []
        for x in val:
            try:
                ret.append(Medida((x, incerteza), unidade=unidade))
            except:
                ret.append(Medida(x, unidade=unidade))
        return ret
    # Tente o de sempre
    try:
        return Medida((val, incerteza), unidade=unidade)
    except:
        return Medida(val, unidade=unidade)

class Medida:
    unidades_originais = [] # Tuplas (objeto unidade, expoente) na ordem em que foram entradas  
    dimensao = (0, 0, 0, 0, 0, 0, 0)
    nominal = 0.0
    incerteza = 0.0
    si_nominal = 0.0
    si_incerteza = 0.0

    def __init__(self, valor, unidade=None):
        self.inicializa(valor, unidade_txt=unidade)

    def inicializa(self, valor, unidade_txt=None):
        # Analise o valor
        if isinstance(valor, Medida):
            self.nominal = valor.nominal
            self.incerteza = valor.incerteza
        elif isinstance(valor, str):
            self.nominal, self.incerteza = analisa_numero(valor)
        elif isinstance(valor, tuple) and len(valor) == 2:
            self.nominal, self.incerteza = float(valor[0]), abs(float(valor[1]))
        else:
            try:
                self.nominal = float(valor)
            except:
                raise Exception("não foi possível extrair o valor e a incerteza")

        # Veja as unidades
        if isinstance(unidade_txt, list):
            self.unidades_originais = copy(unidade_txt)
        elif unidade_txt != None:
            self.unidades_originais = analisa_unidades(unidade_txt)
        self.dimensao = calcula_dimensao(self.unidades_originais)

        # Converta para o SI
        mul_nom, mul_err, add_nom, add_err = fator_de_conversao_para_si(self.unidades_originais)
        self.si_nominal = self.nominal * mul_nom + add_nom
        self.si_incerteza = (self.nominal * mul_err + mul_nom * self.incerteza)  + add_err

    def checa_dim(self, outro):
        # Aplique a regra
        if self.dimensao != outro.dimensao:
            raise ValueError("dimensões físicas incompatíveis: {} vs {} ({} vs. {})".format(dimensao_em_texto(self.dimensao), dimensao_em_texto(outro.dimensao), self, outro))
    def _eh_medida(self, outro):
        if not isinstance(outro, Medida):
            raise TypeError("medidas só podem ser comparadas com outras medidas")
    def _torne_medida(self, outro, converter):
        m = outro
        if not isinstance(outro, Medida):
            m = Medida(outro)
        if converter:
            return m.converta(self.unidades_originais, ignore=True)
        else:
            return m

    def converta(self, unidades, ignore=False):
        if isinstance(unidades, str):
            unidades = analisa_unidades(unidades)
        m = Medida(1, unidades)
        if not ignore:
            self.checa_dim(m)
        nom, err = converte_unidades(self.nominal, self.incerteza, self.unidades_originais, unidades)
        return Medida((nom, err), unidades)

    def __str__(self):
        return "{}".format(self)

    def __repr__(self):
        return "<{}±{} {} = {}±{} {}>".format(self.nominal, self.incerteza, unidades_em_texto(self.unidades_originais), self.si_nominal, self.si_incerteza, dimensao_em_texto(self.dimensao))

    def __eq__(self, outro):
        self._eh_medida(outro)
        self.checa_dim(outro)
        return abs(self.si_nominal - outro.si_nominal) <= 2 * (self.si_incerteza + outro.si_incerteza)
    def __ne__(self, outro):
        self._eh_medida(outro)
        self.checa_dim(outro)
        return abs(self.si_nominal - outro.si_nominal) > 3 * (self.si_incerteza + outro.si_incerteza)
    def __add__(self, outro):
        unidades = get_unidades(outro)
        outro = self._torne_medida(outro, True)
        if not adimensional(self):
            unidades = self.unidades_originais
        m = Medida((self.nominal+outro.nominal, self.incerteza+outro.incerteza), unidades)
        return m
    def __sub__(self, outro):
        unidades = get_unidades(outro)
        outro = self._torne_medida(outro, True)
        if not adimensional(self):
            unidades = self.unidades_originais
        m = Medida((self.nominal-outro.nominal, self.incerteza+outro.incerteza), unidades)
        return m
    def __mul__(self, outro):
        outro = self._torne_medida(outro, False)
        nom = self.nominal * outro.nominal
        err = self.nominal * outro.incerteza + self.incerteza * outro.nominal
        m = Medida((nom, err), simplifica_unidades(self.unidades_originais, outro.unidades_originais))
        return m
    def __div__(self, outro):
        outro = self._torne_medida(outro, False)
        nom = self.nominal / outro.nominal
        err = ((self.nominal * outro.incerteza) + self.incerteza * outro.nominal)/outro.nominal**2
        m = Medida((nom, err), simplifica_unidades(self.unidades_originais, outro.unidades_originais, inverte=True))
        return m
    def __floordiv__(self, outro):
        m = self.__div__(outro)
        nom = floor(m.nominal)
        err = abs(m.nominal-nom) + m.incerteza
        return Medida((nom, err), m.unidades_originais)
    def __truediv__(self, outro):
        return self.__div__(outro)
    def __mod__(self, outro):
        pass
    def __divmod__(self, outro):
        outro = self._torne_medida(outro, False)
        a = self.__floordiv__(1)
        b = outro.__floordiv__(1)
        unidades = simplifica_unidades(self.unidades_originais, outro.unidades_originais, inverte=True)

        q_nom, r_nom = divmod(int(a.nominal), int(b.nominal))
        err = ((self.nominal * outro.incerteza) + self.incerteza * outro.nominal)/outro.nominal**2
        err *= 1/outro.nominal
        return Medida((q_nom, err), unidades), Medida((r_nom, err), unidades)
    def __pow__(self, outro):
        if isinstance(outro, Medida):
            raise NotImplementedError("a exponenciação entre medidas não está implementada")
        else:
            unidades = self.unidades_originais
            if outro == int(outro):
                unidades = simplifica_unidades(self.unidades_originais*outro)
            return Medida((self.nominal**outro, outro*self.nominal**(outro-1)*self.incerteza), unidades)
    def __abs__(self):
        m = Medida((abs(self.nominal), self.incerteza), self.unidades_originais)
        return m
    def __int__(self):
        return int(self.nominal)
    def __float__(self):
        return float(self.nominal)
    def __complex__(self):
        return complex(self.nominal)
    def __radd__(self, outro):
        return Medida(outro).__add__(self)
    def __rsub__(self, outro):
        return Medida(outro).__sub__(self)
    def __rmul__(self, outro):
        return Medida(outro).__mul__(self)
    def __rfloordiv__(self, outro):
        return Medida(outro).__floordiv__(self)
    def __rmod__(self, outro):
        return Medida(outro).__mod__(self)
    def __rdivmod__(self, outro):
        return Medida(outro).__divmod__(self)
    def __rpow__(self, outro):
        outro = float(outro)
        return Medida((
            outro**self.nominal,
            outro**self.nominal * log(outro) * self.incerteza))
    def __rdiv__(self, outro):
        return Medida(outro).__div__(self)

    def __format__(self, fmt):
        fmt = fmt.split(",")
        modo = fmt[0]
        exp = 0
        rouding = "ifsc"
        if len(fmt) >= 2:
            rouding = fmt[1]
        if len(fmt) >= 3:
            exp = int(fmt[2])
        expf = str(exp)
        self_nom = self.nominal*10**(-exp)
        self_err = self.incerteza*10**(-exp)
        nom = ""
        sep = ""
        err = ""
        uni = ""
        base = "{nom}±{err} {uni}"
        base_exp = "({nom}±{err})×10{expf} {uni}"

        if modo == "repr":
            return self.__repr__()

        if rouding == "ifsc" or rouding == "-":
            n = 0
            nom = self_nom
            err = self_err
            # Arredonde o erro para a maior casa significativa
            if err != 0.0:
                while err < 1.0:
                    n -= 1
                    err *= 10
                while err >= 10.0:
                    n += 1
                    err /= 10
                err = round(err)*10**n
                # Arredonde o valor nominal de acrodo
                if n <= 0:
                    nom = round(nom, -n)
                else:
                    nom = round(nom*10**(-n))*10**n
            # Converta para string tomando cuidado com zeros desnecessários
            if err == int(err) and err != 0.0:
                err = str(int(err))
                nom = str(int(nom))
            elif err != 0.0:
                err = "{:.6f}".format(err).rstrip('0') # Isso evita com que 0.0000001 cause problemas
                if err[-1] == ".":
                    err = err + "0"
                nom = "{:.6f}".format(nom) # Isso evita com que 0.0000001 cause problemas
            else:
                err = "0"
                nom = "{}".format(nom)
            if err != 0.0:
                # Verifique se não faltam zeros no nominal
                while nom.find(".") >= 0 and err.find(".") >= 0 and len(nom)-nom.find(".") < len(err)-err.find("."):
                    nom += "0"
                # Verifique se não há zeros em excesso no nominal
                while nom.find(".") >= 0 and err.find(".") >= 0 and len(nom)-nom.find(".") > len(err)-err.find("."):
                    nom = nom[:-1]
        elif rouding == "full":
            nom = str(self_nom)
            err = str(self_err)
        else:
            raise ValueError("{} não é um parâmetro válido de arredondamento".format(rouding))
        sep = "±"
        uni = unidades_em_texto(self.unidades_originais)
        if modo == "latex":
            uni = unidades_em_texto(self.unidades_originais, estilo="latex")
            base = "{nom}\\pm{err}\\textrm{{ {uni}}}"
            base_exp = "({nom}\\pm{err})\cdot10^{{{expn}}}\\textrm{{ {uni}}}"
        elif modo == "siunitx":
            uni = unidades_em_texto(self.unidades_originais, estilo="siunitx")
            base = "\\SI{{{nom}+-{err}}}{{{uni}}}"
            base_exp = "\\SI{{{nom}E{expn}+-{err}E{expn}}}{{{uni}}}"
        elif modo == "txt":
            uni = unidades_em_texto(self.unidades_originais, estilo="latex")
            base = "{nom}+/-{err} {uni}"
            base_exp = "({nom}+/-{err})*10^{expf} {uni}"
        else:
            expf = gera_expoente(exp)

        # Prepare para imprimir
        d = {}
        d["nom"] = nom
        d["err"] = err
        d["uni"] = uni
        d["expn"] = exp
        d["expf"] = expf

        if exp == 0:
            return base.format(**d)
        else:
            return base_exp.format(**d)

        