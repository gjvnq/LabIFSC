#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from .geral import torna_medida
from .medida import Medida

__all__ = ["cos", "sin", "tan", "cot", "sec", "csc", "arc_cos", "arc_sin", "arc_tan", "log", "log10", "log2", "ln"]

def cos(x):
    x    = torna_medida(x)
    nom  = math.cos(x.nominal)
    err  = math.sin(x.nominal)
    err *= x.incerteza
    return Medida((nom, err))

def sin(x):
    x    = torna_medida(x)
    nom  = math.sin(x.nominal)
    err  = math.cos(x.nominal)
    err *= x.incerteza
    return Medida((nom, err))

def tan(x):
    x    = torna_medida(x)
    nom  = math.tan(x.nominal)
    err  = math.sec(x.nominal)**2
    err *= x.incerteza
    return Medida((nom, err))

def cot(x):
    x    = torna_medida(x)
    nom  = math.cot(x.nominal)
    err  = math.csc(x.nominal)**2
    err *= x.incerteza
    return Medida((nom, err))

def sec(x):
    x    = torna_medida(x)
    nom  = math.tan(x.nominal)
    err  = math.sec(x.nomial)*math.tan(x.nomial)
    err *= x.incerteza
    return Medida((nom, err))

def csc(x):
    x    = torna_medida(x)
    nom  = math.tan(x.nominal)
    err  = math.csc(x.nomial)*math.cot(x.nomial)
    err *= x.incerteza
    return Medida((nom, err))

def arc_cos(x):
    x    = torna_medida(x)
    nom  = math.acos(x.nominal)
    err  = 1/math.sqrt(1 - x.nominal**2)
    err *= x.incerteza
    return Medida((nom, err), "rad")

def arc_sin(x):
    x    = torna_medida(x)
    nom  = math.asin(x.nominal)
    err  = 1/math.sqrt(1 - x.nominal**2)
    err *= x.incerteza
    return Medida((nom, err), "rad")

def arc_tan(x):
    x    = torna_medida(x)
    nom  = math.atan(x.nominal)
    err  = 1/math.sqrt(1 - x.nominal**2)
    err *= x.incerteza
    return Medida((nom, err), "rad")

def log(x, b):
    x    = torna_medida(x)
    nom  = math.log(x.nominal, b)
    err  = math.log(math.exp(1), b)/x.nominal
    err *= x.incerteza
    return Medida((nom, err), x.unidades)

def log2(x):
    return log(x, 2)

def log10(x):
    return log(x, 10)

def ln(x):
    return log(x, math.exp(1))