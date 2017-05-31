#!/usr/bin/env python

MAPA_DE_DIMENSOES = {
    "comprimento": 0,
    "ângulo": 1,
    "massa": 2,
    "tempo": 3,
    "temperatura": 4,
    "corrente": 5,
    "mol": 6
}

class Unidade:
    nome = ""
    símbolo = ""
    símbolo_latex = ""
    # As dimensões são (comprimento, ângulo, massa, tempo, temperatura, corrente, mol)
    dimensao = (0, 0, 0, 0, 0, 0, 0)
    # Valor que deve ser multiplicado para obter o valor no MKS
    cte_multiplicativa = None
    # Valor que deve ser adicionado para obter o valor no MKS
    cte_aditiva = None

    def __init__(self, dimensoes, cte_multiplicativa, cte_aditiva, nome, símbolo=None, símbolo_latex=None):
        self.nome = str(nome)
        self.símbolo = str(símbolo)
        self.símbolo_latex = str(símbolo_latex)
        if símbolo == None:
            self.símbolo = self.nome
        if símbolo_latex == None:
            self.símbolo_latex = self.símbolo

        self.constante
        self.incerteza = parse_number(valor)
        for nome, val in list(constante.items()):
            if nome in MAPA_DE_DIMENSOES:
                self.dimensao[MAPA_DE_DIMENSOES[nome]] = int(round(val))
            else:
                raise Exception("{} não é uma dimensão física suportada".format(nome))