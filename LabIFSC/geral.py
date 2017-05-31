#!/usr/bin/env python

# Referências: https://en.wikipedia.org/wiki/Conversion_of_units#Energy e http://physics.nist.gov/cuu/Constants/Table/allascii.txt

UNIDADES = {}

# Molares
Unidade({"mol": 1}, Medida("6.022140857(74)×10^23"), Medida(0), "mol")
# Temperatura
Unidade({"temperatura": 1}, Medida(1), Medida(0), "Kelvin", "K")
Unidade({"temperatura": 1}, Medida(1), Medida("+273.15"), "Celsius", "C")
Unidade({"temperatura": 1}, Medida(5/9), Medida("-459.67"), "Fahrenheit", "F")
Unidade({"temperatura": 1}, Medida(5/9), Medida(0), "Rankine", "R")
# Tempo e frequência
Unidade({"tempo": 1}, Medida(1), Medida(0), "segundo", "s")
Unidade({"tempo": 1}, Medida(60), Medida(0), "minuto", "min")
Unidade({"tempo": 1}, Medida(3600), Medida(0), "hora", "h")
Unidade({"tempo": 1}, Medida(86400), Medida(0), "dia", "d")
Unidade({"tempo": 1}, Medida(1209600), Medida(0), "fortnight", "ftn")
Unidade({"tempo": -1}, Medida(1), Medida(0), "Hertz", "Hz")
# Massa
Unidade({"massa": 1}, Medida(1), Medida(0), "kilograma", "kg")
Unidade({"massa": 1}, Medida(1E-3), Medida(0), "grama", "g")
Unidade({"massa": 1}, Medida(1E6), Medida(0), "tonelada métrica", "ton")
Unidade({"massa": 1}, Medida(6.4), Medida(0), "pedra", "st")
Unidade({"massa": 1}, Medida(0.45), Medida(0), "libra", "lb")
Unidade({"massa": 1}, Medida(28E-3), Medida(0), "onça", "oz")
Unidade({"massa": 1}, Medida(0.065E-3), Medida(0), "grão", "gr")
Unidade({"massa": 1}, Medida(0.2E-3), Medida(0), "quilate", "ct")
Unidade({"massa": 1}, Medida(40.8233133), Medida(0), "firkin", "fir")
# Comprimento
Unidade({"comprimento": 1}, Medida(1), Medida(0), "metro", "m")
Unidade({"comprimento": 1}, Medida(1E-10), Medida(0), "ångstrom", "Å")
Unidade({"comprimento": 1}, Medida(0.00254), Medida(0), "polegada", "in")
Unidade({"comprimento": 1}, Medida(0.3048), Medida(0), "pés", "ft")
Unidade({"comprimento": 1}, Medida(0.9144), Medida(0), "jarda", "yd")
Unidade({"comprimento": 1}, Medida(2.54e-05), Medida(0), "thou", "thou")
Unidade({"comprimento": 1}, Medida(1609.344), Medida(0), "milha internacional", "mi")
Unidade({"comprimento": 1}, Medida(1852), Medida(0), "milha náutica", "nmi")
Unidade({"comprimento": 1}, Medida(0.0003528), Medida(0), "ponto tipográfico", "pt")
Unidade({"comprimento": 1}, Medida(1.7018), Medida(0), "smoot", "sm")
Unidade({"comprimento": 1}, Medida(201.168), Medida(0), "furlong", "fur")
# Área
# Volume
# Corrente
Unidade({"corrente": 1}, Medida(1), Medida(0), "A")
# Energia
Unidade({"massa": 1, "comprimento": 2, "tempo": -2}, Medida(1), Medida(0), "Joule", "J")
Unidade({"massa": 1, "comprimento": 2, "tempo": -2}, Medida(4.184), Medida(0), "caloria", "cal")
Unidade({"massa": 1, "comprimento": 2, "tempo": -2}, Medida(1055.06), Medida(0), "british thermal unit", "BTU") # Padrão ISO
Unidade({"massa": 1, "comprimento": 2, "tempo": -2}, Medida("1.602176565(35)×10−19"), Medida(0), "elétron-volt", "eV")
Unidade({"massa": 1, "comprimento": 2, "tempo": -2}, Medida(1E-7), Medida(0), "erg", "erg")
Unidade({"massa": 1, "comprimento": 2, "tempo": -2}, Medida(4.184E9), Medida(0), "tonelada de TNT", "tTNT")