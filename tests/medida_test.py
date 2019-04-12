#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from math import fabs
from LabIFSC import M, Medida, unidades_em_texto

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
    assert m3.nominal == 1.3048
    assert m3.incerteza == 0.13048
    assert unidades_em_texto(m3.unidades_originais) == "m"
    assert m4.nominal == 4.2808398950131235
    assert m4.incerteza == 0.4280839895013123
    assert unidades_em_texto(m4.unidades_originais) == "ft"

def test_medida_si_1():
    m = Medida("1+-0.1", "ft").SI()

    assert m.nominal - 0.3048 < 1E-4
    assert m.incerteza - 0.03048 < 1E-4
    assert unidades_em_texto(m.unidades_originais) == "m"

def test_medida_si_2():
    m = Medida("1+-0.1", "ft²").SI()

    assert m.nominal - 0.092903 < 1E-4
    assert m.incerteza - 0.0092903 < 1E-4
    assert unidades_em_texto(m.unidades_originais) == "m²"

def test_medida_si_3():
    m = Medida("1+-0.1", "ft² deg lb h °F A mol^-1").SI()

    assert unidades_em_texto(m.unidades_originais) == "m² rad kg s K A mol⁻¹"

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

def test_medida_div_2():
    m1 = Medida("5+-2", "kg")
    m2 = 0.5
    m3 = m1/m2
    m4 = m2/m1
    assert m3.nominal == 10.0
    assert m3.incerteza == 4.0
    assert unidades_em_texto(m3.unidades_originais) == "kg"
    assert m4.nominal == 0.1
    assert m4.incerteza == 0.04
    assert unidades_em_texto(m4.unidades_originais) == "kg⁻¹"

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

def test_medida_pow_1():
    m = Medida("4+/-0.1", "m^2")**0.5
    assert m.nominal == 2
    assert m.incerteza == 0.025
    assert unidades_em_texto(m.unidades_originais) == "m"

def test_medida_pow_2():
    m = Medida("4+/-0.1", "m^2")**2
    assert m.nominal == 16
    assert m.incerteza == 0.8
    assert unidades_em_texto(m.unidades_originais) == "m⁴"

def test_medida_pow_3():
    m1 = Medida("2+/-0.1", "m^2")
    m2 = Medida("3+/-0.5", "")
    m3 = m1**m2
    assert m3.nominal == 2**3
    assert m3.incerteza == 3.9725887222397813
    assert unidades_em_texto(m3.unidades_originais) == "m⁶"

def test_medida_pow_4():
    m1 = Medida("2+/-0.1", "m^2")
    m2 = Medida("3.1+/-0.5", "")
    m3 = m1**m2
    assert m3.nominal == 2**3.1
    assert m3.incerteza == 4.300586108569011
    assert unidades_em_texto(m3.unidades_originais) == "m²"

def test_medida_pow_5():
    m1 = Medida("-2+/-0.1", "m^2")
    m2 = Medida("-3+/-0.5", "")
    m3 = m1**m2
    assert m3.nominal == (-2)**-3
    assert m3.incerteza == 0.06207169878499658
    assert unidades_em_texto(m3.unidades_originais) == "m⁻⁶"

def test_medida_array_1():
    m = M([1,2,3,4,5], incerteza=0.5, unidade="ft")
    assert len(m) == 5
    for i in range(len(m)):
        assert m[i].nominal == i + 1
        assert m[i].incerteza == 0.5
        assert m[i].si_nominal == 0.3048*(i + 1)
        assert m[i].si_incerteza == 0.1524

def test_medida_array_2():
    m = Medida("100+-10", "libra")
    l = M([1,2,m,4,5], incerteza=0.5, unidade="ft")
    print(l)
    assert len(l) == 5
    for i in range(len(l)):
        if i == 2:
            continue
        assert l[i].nominal == i + 1
        assert l[i].incerteza == 0.5
        assert l[i].si_nominal == 0.3048*(i + 1)
        assert l[i].si_incerteza == 0.1524
    assert l[2].nominal == 100
    assert l[2].incerteza == 10
    assert fabs(l[2].si_nominal - 45.359237) < 0.001
    assert fabs(l[2].si_incerteza - 4.5359237) < 0.001