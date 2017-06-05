#!/usr/bin/env python
# -*- coding: utf-8 -*-

TODAS_AS_UNIDADES = {}

MAPA_DE_DIMENSOES = {
    "L": 0, # Comprimento | Padrão: metro
    "A": 1, # Ângulo | Padrão: radianos
    "M": 2, # Massa | Padrão: quilograma
    "T": 3, # Tempo | Padrão: segundo
    "K": 4, # Temperatura | Padrão: kelvin
    "I": 5, # Corrente | Padrão: Ampère
    "N": 6,  # "Quantidade" | Padrão: mol
    0: "L",
    1: "A",
    2: "M",
    3: "T",
    4: "K",
    5: "I",
    6: "N"
}

PREFIXOS_SI_LONGOS = {
    "exa":   10**18,
    "peta":  10**15,
    "tera":  10**12,
    "giga":  10**9,
    "mega":  10**6,
    "kilo":  10**3,
    "quilo": 10**3,
    "hecto": 10**2,
    "deca":  10**1,
    "":      10**0,
    "deci":  10**-1,
    "centi": 10**-2,
    "milli": 10**-3,
    "micro": 10**-6,
    "nano":  10**-9,
    "pico":  10**-12,
    "femto": 10**-15,
    "atto":  10**-18,
    "kibi":   2**10,
    "mebi":   2**20,
    "gibi":   2**30,
    "tebi":   2**40,
    "pebi":   2**50,
    "exbi":   2**60,
    "zebi":   2**70,
    "yobi":   2**80
}

PREFIXOS_SI_CURTOS = {
    "E":  10**18,
    "P":  10**15,
    "T":  10**12,
    "G":  10**9,
    "M":  10**6,
    "k":  10**3,
    "h":  10**2,
    "da": 10**1,
    "":   10**0,
    "d":  10**-1,
    "c":  10**-2,
    "m":  10**-3,
    "μ":  10**-6,
    "n":  10**-9,
    "p":  10**-12,
    "f":  10**-15,
    "a":  10**-18,
    "Ki":  2**10,
    "Mi":  2**20,
    "Gi":  2**30,
    "Ti":  2**40,
    "Pi":  2**50,
    "Ei":  2**60,
    "Zi":  2**70,
    "Yi":  2**80
}

PREFIXOS_SI = dict(list(PREFIXOS_SI_CURTOS.items()) + list(PREFIXOS_SI_LONGOS.items()))

def analisa_numero(num):
    try:
        return float(num), 0.0
    except:
        try:
            return analisa_numero_forma_concisa(num)
        except:
            return analisa_numero_forma_mais_ou_menos(num)

# Analisa números do tipo: (13.415±0.001)*10^9 ; (13.415+/-0.001)E9 ; (13.415 \pm 0.001)*10^9
def analisa_numero_forma_mais_ou_menos(txt):
    txt = txt.replace("(", "").replace(")", "").replace("{", "").replace("}", "").replace(" ", "").replace("+-", "±").replace("+/-", "±").replace("\\pm", "±").replace("×", "").replace("x", "").replace("10^", "E").replace(",", ".").replace("'", "")
    base = ""
    incerteza = ""
    expoente = ""
    num_char = set(["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."])
    modo = 0 # 0-Base; 1-Incerteza; 2-Expoente
    for i, c in enumerate(txt):
        if modo == 0:
            if c in num_char:
                base += c
            elif c == "±":
                modo = 1
            elif c == "E":
                modo = 2
            else:
                raise Exception("caractere {} não em esperado (modo = {}, i = {}, txt = {})".format(c, modo, i, txt))
        elif modo == 1:
            if c in num_char:
                incerteza += c
            elif c == "E":
                modo = 2
            else:
                raise Exception("caractere {} não em esperado (modo = {}, i = {}, txt = {})".format(c, modo, i, txt))
        elif modo == 2:
            if c  == "E":
                pass
            elif c in num_char:
                expoente += c
            else:
                raise Exception("caractere {} não em esperado (modo = {}, i = {}, txt = {})".format(c, modo, i, txt))
        else:
            raise Exception("caractere {} não em esperado (modo = {} (?), i = {}, txt = {})".format(c, modo, i, txt))
    try:
        base = float(base)
    except:
        raise Exception("base = '{}' deve ser conversível em float".format(base))
    try:
        incerteza = float(incerteza)
    except:
        if len(incerteza) != 0:
            raise Exception("incerteza = '{}' deve ser conversível em float".format(incerteza))
        else:
            incerteza = 0.0
    try:
        expoente = float(expoente)
    except:
        if len(expoente) != 0:
            raise Exception("expoente = '{}' deve ser conversível em float".format(expoente))
        else:
            expoente = 0.0
    base *= 10**(expoente)
    incerteza *= 10**(expoente)
    return base, incerteza

# Analisa números do tipo: 13.415(01)*10^9 ; 13.415(18)E9 ; 13.415(137)×10^9
def analisa_numero_forma_concisa(txt):
    txt = txt.replace(" ", "").replace("−", "-").replace("*", "").replace("×", "").replace("x", "").replace("10^", "E").replace(",", ".").replace("'", "")
    base = ""
    incerteza = ""
    expoente = ""
    num_char = set(["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."])
    modo = 0 # 0-Base; 1-Incerteza; 2-Expoente
    for i, c in enumerate(txt):
        if modo == 0:
            if c in num_char:
                base += c
            elif c == "(":
                modo = 1
            elif c == "E":
                modo = 2
            else:
                raise Exception("caractere {} não em esperado (modo = {}, i = {}, txt = {})".format(c, modo, i, txt))
        elif modo == 1:
            if c in num_char:
                incerteza += c
            elif c == ")":
                modo = 2
            else:
                raise Exception("caractere {} não em esperado (modo = {}, i = {}, txt = {})".format(c, modo, i, txt))
        elif modo == 2:
            if c  == "E":
                pass
            elif c in num_char:
                expoente += c
            else:
                raise Exception("caractere {} não em esperado (modo = {}, i = {}, txt = {})".format(c, modo, i, txt))
        else:
            raise Exception("caractere {} não em esperado (modo = {} (?), i = {}, txt = {})".format(c, modo, i, txt))
    # Arrume o posicionamento da incerteza
    tmp = ""
    for j in range(len(base)-len(incerteza)):
        if base[j] == ".":
            tmp += "."
        else:
            tmp += "0"
    incerteza = tmp + incerteza
    try:
        base = float(base)
    except:
        raise Exception("base = '{}' deve ser conversível em float".format(base))
    try:
        incerteza = float(incerteza)
    except:
        if len(incerteza) != 0:
            raise Exception("incerteza = '{}' deve ser conversível em float".format(incerteza))
        else:
            incerteza = 0.0
    try:
        expoente = float(expoente)
    except:
        if len(expoente) != 0:
            raise Exception("expoente = '{}' deve ser conversível em float".format(expoente))
        else:
            expoente = 0.0
    base *= 10**(expoente)
    incerteza *= 10**(expoente)
    return base, incerteza

# Analisa um texto que representa unidades. Note que os símbolos devem ser separados por espaços, asteríscos ou uma barra; e que o carcatere do expoente é opicional.
# Ex: "kg m-1 A^-2", "km / m A^2", "kg3/m*A2"
# Se houverem prefixos incomuns, usa-se dois-pontos (:):
# Ex: "kilo:T", "k:T", "quilo:Tesla" | "kilo:byte", "k:byte", "kb" (base 10) | "kibi:byte", "ki:byte" (base 2)
def analisa_unidades(txt):
    txt = txt.replace(" ", "*").replace("**", "*").replace("^", "")+"*Z0"
    if len(txt.split("/")) > 2:
        raise Exception("apenas uma barra (/) pode ser utilizada ao especificar uma unidade. Após a barra todos os expoentes são multiplicados por -1")
    mul_cte = 1 # Fator multiplicativo para os expoentes. Serve apenas para regular o sinal
    modo = 0 # 0-Nome da unidade; 1-Expoente da unidade
    num_char = list("+-0123456789")
    sep_char = list("*/")
    nome_unidade = ""
    expoente_txt = ""
    tokens = []
    # Analise o textp
    for i, c in enumerate(txt):
        stop_flag = False
        #print(i, c, modo, nome_unidade, expoente_txt)
        if modo == 0:
            if c in num_char:
                modo = 1
            elif c in sep_char:
                stop_flag = True
                expoente_txt = "1"
            else:
                nome_unidade += c
        if modo == 1:
            if c in num_char:
                expoente_txt += c
            else:
                modo = 0
                stop_flag = True
        
        if stop_flag == True:
            tokens.append((nome_unidade, expoente_txt, mul_cte))
            nome_unidade = ""
            expoente_txt = ""
            if c == "/":
                mul_cte *= -1
    # Processe os tokens
    for tok in tokens:
        tmp = tok[0].split(":")
        prefix = ""
        base = ""
        if len(tmp) == 1:
            base = tmp[0]
        elif len(tmp) == 2:
            prefix = tmp[0]
            base = tmp[1]
        else:
            raise Exception("cada token de unidade não pode ter mais do que um dois-pontos")

        if prefix in PREFIXOS_SI:
            prefix = PREFIXOS_SI[prefix]
        else:
            raise Exception("prefixo desconhecido em '{}'".format(tok[0]))
        if base in TODAS_AS_UNIDADES:
            base = TODAS_AS_UNIDADES[base]
        else:
            raise Exception("unidade desconhecida em '{}'".format(tok[0]))
    return tokens

def calcula_dimensao(unidades):
    dim = [0, 0, 0, 0, 0, 0, 0]
    for unidade in unidades:
        for i, val in enumerate(unidade.dimensao):
            dim[i] += val
    return tuple(dim)

def parse_dimensions(txt):
    mode = 0 # 0 - Letra | 1 - Número
    num = ""
    dim = ""
    txt = txt.replace(" ", "")
    ans = [0, 0, 0, 0, 0, 0, 0]
    for i, c in enumerate(txt):
        # Se estamos lendo letras
        if mode == 0:
            if c in MAPA_DE_DIMENSOES:
                dim = c
                num = ""
                mode = 1
            else:
                raise Exception("{} não é uma dimensão física conhecida".format(c))
        elif mode == 1:
            if i == len(txt)-1:
                # Terminamos de ler o expoente da dimensão
                num += c
                num = int(num)
                ans[MAPA_DE_DIMENSOES[dim]] += num
            elif c in MAPA_DE_DIMENSOES:
                try:
                    # Terminamos de ler o expoente da dimensão
                    if len(num) == 0:
                        num = 1
                    else:
                        num = int(num)
                    ans[MAPA_DE_DIMENSOES[dim]] += num
                    dim = c
                    num = ""
                    mode = 1
                except:
                    raise Exception((num, ans, dim, c, i, txt))
            else:
                num += c
        else:
            raise Exception("{} não é um modo válido para parse_dimensions (c={} i={} txt='{}')".format(mode, c, i, txt))
    return tuple(ans)

def acha_unidade(nome):
    global TODAS_AS_UNIDADES
    nome = nome.lower()
    if nome in TODAS_AS_UNIDADES:
        return TODAS_AS_UNIDADES[nome]
    else:
        raise Exception("unidade '{}' não encontrada".format(nome))

def dimensao_em_texto(dim):
    txt = ""
    for i, v in enumerate(dim):
        if v != 0:
            txt += MAPA_DE_DIMENSOES[i] + str(v)
    return txt