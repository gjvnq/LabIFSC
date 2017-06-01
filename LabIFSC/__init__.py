#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .variaveis import TODAS_AS_UNIDADES
from .medida import Medida, analisa_numero, analisa_unidades
from .unidade import Unidade, acha_unidade
from .lista_de_unidades import registra_unidades

__all__ = ["Medida", "Unidade", "TODAS_AS_UNIDADES", "analisa_numero", "registra_unidades", "acha_unidade", "analisa_unidades"]

def init():
    global TODAS_AS_UNIDADES
    registra_unidades()