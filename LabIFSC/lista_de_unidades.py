#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Referências: https://en.wikipedia.org/wiki/Conversion_of_units e http://physics.nist.gov/cuu/Constants/Table/allascii.txt

import math
from .medida import Medida
from .unidade import Unidade

def registra_unidades():
    PI = Medida("3.14159(1)")

    # Comprimento
    Unidade("Ångstrom", "Å", "Å", "L1", Medida(1E-9), Medida(0))
    Unidade("unidade astronômica", "AU", "AU", "L1", Medida(149597870700), Medida(0))
    Unidade("raio de Bohr do hidrogênio", "a0", "a_0", "L1", Medida("5.2917721092(17)×10^−11"), Medida(0))
    Unidade("côvado", "côv", "côv", "L1", Medida("0.52635(285)"), Medida(0))
    Unidade("fermi", "fm", "fm", "L1", Medida(1E-15), Medida(0))
    Unidade("pé métrico", "pém", "pém", "L1", Medida(math.sqrt(0.1)), Medida(0))
    Unidade("pé internacional", "ft", "ft", "L1", Medida(0.3048), Medida(0), simbolo_siunitx="\\foot")
    Unidade("furlong", "fur", "fur", "L1", Medida(201.168), Medida(0))
    Unidade("mão", "mão", "mão", "L1", Medida(0.1016), Medida(0))
    Unidade("polegada internacional", "in", "in", "L1", Medida(0.0254), Medida(0))
    Unidade("dia-luz", "dLuz", "dLuz", "L1", Medida(2.59020683712E13), Medida(0))
    Unidade("hora-luz", "hLuz", "hLuz", "L1", Medida(1.0792528488E12), Medida(0))
    Unidade("minuto-luz", "minLuz", "minLuz", "L1", Medida(1.798754748E10), Medida(0))
    Unidade("segundo-luz", "sLuz", "sLuz", "L1", Medida(299792458), Medida(0))
    Unidade("line", "ln", "ln", "L1", Medida(0.0254/12), Medida(0))
    Unidade("metro", "m", "m", "L1", Medida(1), Medida(0))
    Unidade("mickey", "mickey", "mickey", "L1", Medida(1.27E-4), Medida(1))
    Unidade("micron", "µ", "\mu", "L1", Medida(1.27E-4), Medida(0))
    Unidade("thou", "mil", "mil", "L1", Medida(2.54E-4), Medida(0))
    Unidade("milha internacional", "mi", "mi", "L1", Medida(1609.344), Medida(0))
    Unidade("légua nautica", "nl", "nl", "L1", Medida(5556), Medida(0))
    Unidade("milha náutica internacional", "nmi", "nmi", "L1", Medida(1852), Medida(0))
    Unidade("parsec", "pc", "pc", "L1", Medida("3.085677581(1)×10^16"), Medida(0))
    Unidade("ponto tipográfico", "pt", "pt", "L1", Medida(0.0254/12), Medida(0))
    Unidade("unidade x de cobre", "xu(Cu Kα1)", "xu(Cu K\\alpha1)", "L1", Medida("1.00207699(28)×10^−13"), Medida(0))
    Unidade("unidade x de molibdênio", "xu(Mo Kα1)", "xu(Mo K\\alpha1)", "L1", Medida("1.00209955(53)×10^−13"), Medida(0))
    Unidade("jarda internacional", "yd", "yd", "L1", Medida(0.9144), Medida(0))

    # Área
    Unidade("hectare", "ha", "ha", "L2", Medida(1E4), Medida(0))
    # Unidade("pé quadrado", "!ft²", "!ft^2", "L2", Medida(9.290304E-2), Medida(0))
    Unidade("polegada quadrada", "in²", "in^2", "L2", Medida(6.4516E-4), Medida(0))
    Unidade("quilômetro quadrado", "km²", "km^2", "L2", Medida(1E6), Medida(0))
    Unidade("metro quadrado", "m²", "m^2", "L2", Medida(1), Medida(0))
    Unidade("milha quadrada", "mi²", "mi^2", "L2", Medida(2.589988110336E6), Medida(0))
    Unidade("jarda quadrada", "yd²", "yd^2", "L2", Medida(0.83612736), Medida(0))

    # Volume
    Unidade("barril imperial", "bl(imp)", "bl(imp)", "L3", Medida(0.16365924), Medida(0))
    Unidade("barril de petróleo", "bbl", "bbl", "L3", Medida(0.158987294928), Medida(0))
    Unidade("balde", "bkt", "bkt", "L3", Medida(0.01818436), Medida(0))
    Unidade("metro cúbico", "m³", "m^3", "L3", Medida(1), Medida(0))
    Unidade("taça de desjejum", "c(dj)", "c(dj)", "L3", Medida(284.130625E-6), Medida(0))
    Unidade("taça canadense", "c(CA)", "c(CA)", "L3", Medida(227.3045E-6), Medida(0))
    Unidade("taça métrica", "c(m)", "c(m)", "L3", Medida(250.0E-6), Medida(0))
    Unidade("taça americana costumária", "c(US)", "c(US)", "L3", Medida(236.5882365E-6), Medida(0))
    Unidade("taça americana nutricional", "c(USn)", "c(USn)", "L3", Medida(2.4E-4), Medida(0))
    Unidade("colher de sobremesa imperial", "gi(imp)", "gi(imp)", "L3", Medida("11.8387760416(1)*10^-4"), Medida(0))
    Unidade("gota métrica", "gt", "gt", "L3", Medida(50E-9), Medida(0))
    Unidade("galão imperial", "gal(imp)", "gal(imp)", "L3", Medida(4.54609E-3), Medida(0))
    Unidade("litro", "L", "L", "L3", Medida(0.001), Medida(0))
    Unidade("onça flúida imperial", "fl oz(imp)", "fl oz(imp)", "L3", Medida(28.4130625E-6), Medida(0))
    Unidade("onça flúida americana costumária", "fl oz(US)", "fl oz(US)", "L3", Medida(29.5735295625E-6), Medida(0))
    Unidade("onça flúida americana nutricional", "fl oz(USn)", "fl oz(USn)", "L3", Medida(3E-5), Medida(0))
    Unidade("colher de sopa australiana métrica", "tbsp(AU)", "tbsp(AU)", "L3", Medida(20E-6), Medida(0))
    Unidade("colher de sopa canadense", "tbsp(CA)", "tbsp(CA)", "L3", Medida(14.20653125E-6), Medida(0))
    Unidade("colher de sopa imperial", "tbsp(imp)", "tbsp(imp)", "L3", Medida(17.7581640625E-6), Medida(0))
    Unidade("colher de sopa métrica", "tbsp(m)", "tbsp(m)", "L3", Medida(15E-6), Medida(0))
    Unidade("colher de sopa americana costumária", "tbsp(US)", "tbsp(US)", "L3", Medida(14.78676478125E-6), Medida(0))
    Unidade("colher de sopa americana nutricional", "tbsp(USn)", "tbsp(USn)", "L3", Medida(1.5E-4), Medida(0))
    Unidade("colher de chá canadense", "tbsp(CA)", "tbsp(CA)", "L3", Medida("4.735510416(1)×10^−6"), Medida(0))
    Unidade("colher de chá imperial", "tbsp(imp)", "tbsp(imp)", "L3", Medida("5.91938802083(1)×10^−6"), Medida(0))
    Unidade("colher de chá métrica", "tbsp(m)", "tbsp(m)", "L3", Medida(5E-6), Medida(0))
    Unidade("colher de chá americana costumária", "tbsp(US)", "tbsp(US)", "L3", Medida(4.92892159375E-6), Medida(0))
    Unidade("colher de chá americana nutricional", "tbsp(USn)", "tbsp(USn)", "L3", Medida(5E-6), Medida(0))

    # Ângulos planares
    Unidade("milésimo angular", "µ", "µ", "A1", Medida("0.981748(1)E-3"), Medida(0))
    Unidade("minuto de arco", "'", "'", "A1", Medida("0.290888(1)E-3"), Medida(0))
    Unidade("segundo de arco", "''", "''", "A1", Medida("4.848137(1)E-6"), Medida(0))
    Unidade("grau", "°", "deg", "A1", Medida("17.453293(1)E-3"), Medida(0))
    Unidade("radiano", "rad", "rad", "A1", Medida(1), Medida(0))

    # Ângulos sólidos
    Unidade("grau quadrado", "(°)²", "deg^2", "A2", Medida("0.30462(1)E-3"), Medida(0))
    Unidade("esferorradiano", "sr", "sr", "A2", Medida(1), Medida(0))

    # Massa
    Unidade("unidade massa atômica", "u", "u", "M1", Medida("1.660538921(73)×10^−27"), Medida(0))
    Unidade("massa do elétron em repouso", "mₑ", "m_e", "M1", Medida("9.10938291(40)×10^−31"), Medida(0))
    Unidade("saca de café", "scafé", "scafé", "M1", Medida(60), Medida(0))
    Unidade("quilate", "ct", "ct", "M1", Medida(200E-3), Medida(0))
    Unidade("Dalton", "Da", "Da", "M1", Medida("1.660538921(73)×10^−27"), Medida(0))
    Unidade("elétron-Volt", "eV", "eV", "M1", Medida("1.78266184(45)×10^−36"), Medida(0))
    Unidade("grama", "g", "g", "M1", Medida(1E-3), Medida(0))
    Unidade("quilograma", "kg", "kg", "M1", Medida(1), Medida(0))
    Unidade("onça americana nutricional", "oz", "oz", "M1", Medida(28E-3), Medida(0))
    Unidade("libra", "lb", "lb", "M1", Medida(0.45359237), Medida(0))
    Unidade("pedra", "st", "st", "M1", Medida(6.35029318), Medida(0))
    Unidade("tonelada", "ton", "ton", "M1", Medida(1000), Medida(0))

    # Densidade
    Unidade("quilograma por metro cúbico", "kg/m³", "kg/m^3", "M1L-3", Medida(1), Medida(0))
    Unidade("grama por mililitro", "g/mL", "g/mL", "M1L-3", Medida(1000), Medida(0))
    Unidade("quilograma por litro", "kg/L", "kg/L", "M1L-3", Medida(1000), Medida(0))
    
    # Tempo
    Unidade("dia", "d", "d", "T1", Medida("86.4E3"), Medida(0))
    Unidade("dia sideral", "ds", "d_s", "T1", Medida("86.1641(1)E3"), Medida(0))
    Unidade("hora", "h", "h", "T1", Medida(60*60), Medida(0))
    Unidade("minuto", "min", "min", "T1", Medida(60), Medida(0))
    Unidade("fortnight", "fn", "fn", "T1", Medida("1.2096E6"), Medida(0))
    Unidade("mês comercial", "mês", "mês", "T1", Medida("2.592E6"), Medida(0))
    Unidade("mês médio", "mêsm", "mêsm", "T1", Medida("2.6297(1)E6"), Medida(0))
    Unidade("segundo", "s", "s", "T1", Medida(1), Medida(0))
    Unidade("ano comum", "ano", "ano", "T1", Medida("31.536E6"), Medida(0))
    Unidade("ano Greogirano médio", "anog", "anog", "T1", Medida("31.556952E6"), Medida(0))
    Unidade("ano sideral", "sano", "ano_s", "T1", Medida("31.5581497632(1)E6"), Medida(0))

    # Frequência
    Unidade("Hertz", "Hz", "Hz", "T-1", Medida(1), Medida(0))
    Unidade("revoluções por minuto", "rpm", "rpm", "A1T-1", Medida("0.104719755(1)"), Medida(0))

    # Velocidade
    Unidade("metro por segundo", "m/s", "m/s", "L1T-1", Medida(1), Medida(0))

    # Fluxo
    Unidade("metro cúbico por segundo", "m²/s", "m^2/s", "L3T-1", Medida(1), Medida(0))

    # Aceleração
    Unidade("metro por segundo quadrado", "m/s²", "m/s^2", "L1T-2", Medida(1), Medida(0))

    # Força
    Unidade("Newton", "N", "N", "M1L1T-2", Medida(1), Medida(0))

    # Pressão
    Unidade("Pascal", "Pa", "Pa", "M1L-1T-2", Medida(1), Medida(0))

    # Torque
    Unidade("Newton metro", "N·m", "N\\cdot{}m", "M1L2T-2", Medida(1), Medida(0))

    # Calor e Energia
    Unidade("caloría internacional", "cal", "cal", "M1L2T-2", Medida(4.1868), Medida(0))
    Unidade("Joule", "J", "J", "M1L2T-2", Medida(1), Medida(0))
    Unidade("erg", "erg", "erg", "M1L2T-2", Medida(1E-7), Medida(0))
    Unidade("British Thermal Unit (ISO)", "BTU", "BTU", "M1L2T-2", Medida(1.0545E3), Medida(0))

    # Potência
    Unidade("Watt", "W", "W", "ML2T-3", Medida(1), Medida(0))

    # Corrente
    Unidade("Ampère", "A", "A", "I1", Medida(1), Medida(0))

    # Carga
    Unidade("Coulomb", "C", "C", "I1T1", Medida(1), Medida(0))

    # Dipolo
    Unidade("Coulomb metro", "C·m", "C\\cdot{}m", "I1T2L1", Medida(1), Medida(0))

    # Potencial elétrico
    Unidade("Volt", "V", "V", "ML2A-1T-3", Medida(1), Medida(0))

    # Resistência elétrica
    Unidade("Ohm", "Ω", "\ohm", "M1L2A-2T-3", Medida(1), Medida(0))

    # Capacitância
    Unidade("Farad", "F", "F", "A2T4M-1L-2", Medida(1), Medida(0))

    # Temperature
    Unidade("Kelvin", "K", "K", "K", Medida(1), Medida(0))
    Unidade("Celsius", "°C", "\degree{}C", "K", Medida(1), Medida(273.15))
    Unidade("Fahrenheit", "°F", "\degree{}F", "K", Medida(5/9), Medida(255.37222222222223))