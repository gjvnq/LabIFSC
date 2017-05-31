#!/usr/bin/env python

class Medida:
    valor = 0.0
    unidade = []
    incerteza = 0.0

    def __eq__(self, other):
        if not isinstance(other, Medida):
            raise Exception("medidas só podem ser comparadas com outras medidas")
        return abs(self.valor - other.value) < 2 * (self.incerteza + other.incerteza)
    def __ne__(self, other):
        if not isinstance(other, Medida):
            raise Exception("medidas só podem ser comparadas com outras medidas")
        return abs(self.valor - other.value) > 3 * (self.incerteza + other.incerteza)