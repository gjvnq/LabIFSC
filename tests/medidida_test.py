#!/usr/bin/env python

from LabIFSC import Medida

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