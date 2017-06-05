#!/usr/bin/env python
# -*- coding: utf-8 -*-

from LabIFSC import Medida, unidades_em_texto

def test_medida_eq_1():
    m1 = Medida((0.0, 0.0))
    m2 = Medida((0.0, 0.0))
    assert m1 == m2
    assert not m1 != m2

def test_medida_eq_2():
    m1 = Medida((0.0, 0.0))
    m2 = Medida((1.0, 0.0))
    assert not m1 == m2
    assert m1 != m2

def test_medida_eq_3():
    m1 = Medida((0, 0.5))
    m2 = Medida((1, 0.5))
    assert m1 == m2
    assert not m1 != m2

def test_medida_eq_4():
    m1 = Medida((0, 0.5))
    m2 = Medida((2.1, 0.5))
    assert not m1 == m2
    assert not m1 != m2

def test_medida_repr_1():
    m = Medida(1, "ft")
    assert m.__repr__() == "<1.0±0.0 ft = 0.3048±0.0 L1>"

def test_medida_add_1():
    m1 = Medida(1, "m")
    m2 = Medida(2, "m")
    m = m1+m2
    assert m.nominal == 3
    assert m.incerteza == 0

def test_medida_add_2():
    m1 = Medida(1, "m")
    m2 = Medida("2+/-0.1", "m")
    m = m1+m2
    assert m.nominal == 3
    assert m.incerteza == 0.1

def test_medida_add_3():
    m1 = Medida("1+-0.1", "m")
    m2 = Medida("1+-0.1", "ft")
    m3 = m1+m2
    m4 = m2+m1
    assert m3.nominal == 2.6096
    assert m3.incerteza == 0.13048
    assert unidades_em_texto(m3.unidades_originais) == "m"
    assert m4.nominal == 5.585639895013123
    assert m4.incerteza == 0.4280839895013123
    assert unidades_em_texto(m4.unidades_originais) == "ft"

def test_medida_sub_1():
    m1 = Medida(1, "m")
    m2 = Medida(2, "m")
    m = m1-m2
    assert m.nominal == -1
    assert m.incerteza == 0

def test_medida_sub_2():
    m1 = Medida("1+/-0.1", "m")
    m2 = Medida("2+/-0.01", "m")
    m = m1-m2
    assert m.nominal == -1
    assert m.incerteza == 0.11