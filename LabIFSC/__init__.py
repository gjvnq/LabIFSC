#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gabriel Queiroz"
__credits__ = ["gabriel Queiroz", "Pedro Ilídio"]
__license__ = "GPL"
__version__ = "0.1.4"
__email__ = "gabrieljvnq@gmail.com"
__status__ = "Production"

from .geral import TODAS_AS_UNIDADES, MAPA_DE_DIMENSOES, PREFIXOS_SI_LONGOS, PREFIXOS_SI_CURTOS, PREFIXOS_SI, analisa_numero, analisa_unidades, calcula_dimensao, parse_dimensions, acha_unidade, unidades_em_texto
from .medida import Medida, M
from .unidade import Unidade
from .lista_de_unidades import registra_unidades
from .matematica import soma, cos, sin, tan, cot, sec, csc, arc_cos, arc_sin, arc_tan, log, log10, log2, ln, sqrt, cbrt
from .tabela import media, desvio_padrao, linearize, compare


__all__ = [
    "TODAS_AS_UNIDADES", "MAPA_DE_DIMENSOES", "PREFIXOS_SI_LONGOS", "PREFIXOS_SI_CURTOS", "PREFIXOS_SI", "analisa_numero", "analisa_unidades", "calcula_dimensao", "parse_dimensions", "acha_unidade", "unidades_em_texto",
    "Medida", "M",
    "Unidade",
    "registra_unidades",
    "soma", "cos", "sin", "tan", "cot", "sec", "csc", "arc_cos", "arc_sin", "arc_tan", "log", "log10", "log2", "ln", "sqrt", "cbrt",
    "media", "desvio_padrao", "linearize", "compare"
]

def init():
    global TODAS_AS_UNIDADES
    registra_unidades()

init()
