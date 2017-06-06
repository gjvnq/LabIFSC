#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from LabIFSC import Medida

def test_unidade_1():
    m1 = Medida(1, "m")
    m2 = Medida(1, "kg")
    with pytest.raises(Exception) as excinfo:
        m1 == m2
    assert "dimensões físicas incompatíveis: L1 vs M1" in str(excinfo)
    with pytest.raises(Exception) as excinfo:
        m1 != m2
    assert "dimensões físicas incompatíveis: L1 vs M1" in str(excinfo)

def test_unidade_2():
    m1 = Medida(0.3048, "m")
    m2 = Medida(1, "ft")
    assert m1 == m2
    assert not m1 != m2

def test_unidade_3():
    m1 = Medida(0.3049, "m")
    m2 = Medida(1, "ft")
    assert m1 != m2
    assert not m1 == m2