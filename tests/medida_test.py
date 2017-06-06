#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
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

def test_medida_add_4():
    m1 = Medida(1, "m")
    m2 = Medida("2+/-0.1", "kg")
    with pytest.raises(Exception) as excinfo:
        m = m1 + m2
    assert "dimensões físicas incompatíveis: L1 vs M1" in str(excinfo)

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

def test_medida_mul_1():
    m1 = Medida("1+-0.1", "kg^2/m^3")
    print(m1.dimensao)
    m2 = Medida("1+-0.1", "lb/kg")
    print(m2.dimensao)
    m3 = m1*m2
    m4 = m2*m1
    assert m3.nominal == 1
    assert m3.incerteza == 0.2
    assert unidades_em_texto(m3.unidades_originais) == "kg lb m⁻³"
    assert m4.nominal == 1
    assert m4.incerteza == 0.2
    assert unidades_em_texto(m4.unidades_originais) == "kg lb m⁻³"

def test_medida_div_1():
    m1 = Medida("3", "kg/m")
    m2 = Medida("2", "L*Pa/m")
    m3 = m1/m2
    m4 = m2/m1
    assert m3.nominal == 3.0/2.0
    assert m3.incerteza == 0
    assert unidades_em_texto(m3.unidades_originais) == "kg L⁻¹ Pa⁻¹"
    assert m4.nominal == 2.0/3.0
    assert m4.incerteza == 0
    assert unidades_em_texto(m4.unidades_originais) == "L Pa kg⁻¹"

def test_medida_abs_1():
    m1 = Medida("-3+-1", "kg/m")
    m2 = abs(m1)
    assert m2.nominal == 3
    assert m2.incerteza == 1
    assert unidades_em_texto(m2.unidades_originais) == "kg m⁻¹"

def test_medida_divmod_1():
    m1 = Medida("11+-1", "kg/m")
    m2, m3 = divmod(m1, 2)
    assert m2.nominal == 5
    assert m2.incerteza == 0.25
    assert unidades_em_texto(m2.unidades_originais) == "kg m⁻¹"
    assert m3.nominal == 1
    assert m3.incerteza == 0.25
    assert unidades_em_texto(m3.unidades_originais) == "kg m⁻¹"

