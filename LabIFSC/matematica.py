#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from .medida import Medida

__all__ = ["cos", "sin", "tan", "cot", "sec", "csc", "arc_cos", "arc_sin", "arc_tan", "log", "log10", "log2", "ln", "sqrt", "cbrt"]

def soma(x):
    try:
        return sum(x)
    except:
        m = Medida(
            (sum(list(map(lambda x: x.nominal, x))),
            sum(list(map(lambda x: x.incerteza, x)))), x[0].unidades_originais)
        return m

def torna_medida(x):
    if not isinstance(x, Medida):
        return Medida(x)
    return x

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
    err  = (1.0/math.cos(x.nominal))**2
    err *= x.incerteza
    return Medida((nom, err))

def cot(x):
    x    = torna_medida(x)
    nom  = (1.0/math.tan(x.nominal))
    err  = (1.0/math.sin(x.nominal))**2
    err *= x.incerteza
    return Medida((nom, err))

def sec(x):
    x    = torna_medida(x)
    nom  = math.tan(x.nominal)
    err  = (1.0/math.cos(x.nominal))*math.tan(x.nominal)
    err *= x.incerteza
    return Medida((nom, err))

def csc(x):
    x    = torna_medida(x)
    nom  = math.tan(x.nominal)
    err  = (1.0/math.sin(x.nominal))*(1.0/math.tan(x.nominal))
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
    return Medida((nom, err), x.unidades_originais)

def log2(x):
    return log(x, 2)

def log10(x):
    return log(x, 10)

def ln(x):
    return log(x, math.exp(1))

def sqrt(x):
    return x**0.5

def cbrt(x):
    return x**(1.0/3.0)