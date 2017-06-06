# LabIFSC
Uma biblioteca em python para propagação de erro e conversão de unidades utilizando os métodos (um tanto insólitos) que os professores de lab de física do IFSC-USP insistem.

**AVISO**: está biblioteca ainda não está pronta.

# Instalação

No momento a biblioteca não está disponível do pip, porém é possível utilizá-la simplesmente colocando a pasta ```LabIFSC``` dentro da pasta em que o seu script está. Exemplo:

```
─┬ Minha pasta qualquer
 ├─ Relatório.tex
 ├─ Relatório.pdf
 ├─ Foto1.jpg
 ┊
 ├─ meu script.py
 └┬ LabIFSC
  ├─ __init__.py
  ├─ geral.py
  ├─ lista_de_unidades.py
  ├─ matematica.py
  ├─ medida.py
  ├─ tabela.py
  └─ unidade.py
```

# Uso

## O Básico

Para utilizar essa biblioteca:
```python
from LabIFSC import *
```

A principal classe é a ```Medida```. Ela pode ser inicializada das seguintes formas:

```python
# A unidade é sempre opcional
m = Medida((130, 27), "m")  # Medida((valor nominal, erro), unidade)
m = Medida("130+-27", "m")  # Medida(valor+-erro, unidade)
m = Medida("130+/-27", "m") # Medida(valor+/-erro, unidade)
m = Medida("130±27", "m")   # Medida(valor±erro, unidade)
m = Medida("130(27)", "m")  # Medida(valor(erro), unidade)
```

Uma instância de Medida tem os seguintes atributos:

```python
m = Medida("130±27", "ft")
print(m.nominal)      # 130.0
print(m.incerteza)    # 27.0
print(m.si_nominal)   # 39.64
print(m.si_incerteza) # 8.2296
```

Os valores prefixados com ```si_``` estão em unidades do MKS, ou seja: metro, radiano, quilograma, segundo, kelvin, Ampère e mol. Mais detalhes serão apresentados adiante na parte de unidades.

## Comparações

As comparações entre medidas não comparam os valores em si, mas sim verificam se as medidas são estatisticamente equivalentes.

A equação que determina se duas medidas são equivalentes é: ```|x₁ - x₂| ≤ 2(σ₁ + σ₂)```. Já a equação~que determina não equivalência é ```|x₁ - x₂| > 3(σ₁ + σ₂)```.

Cuidado deve ser tomado já que duas medidas podem não ser iguais nem diferentes.

```python
m1 = Medida("100+/-7")
m2 = Medida("110+/-3")
m1 == m2 # True
m1 != m2 # False
```

```python
m1 = Medida("100+/-7")
m2 = Medida("125+/-3")
m1 == m2 # False
m1 != m2 # False
```

```python
m1 = Medida("100+/-7")
m2 = Medida("131+/-3")
m1 == m2 # False
m1 != m2 # True
```

## Propagação de Erro

A propagação de erro é feita automaticamente nas seguintes operções: ```+```, ```-```, ```*```, ```/```, ```**```.

```python
m1 = Medida("20+/-1")
m2 = Medida("4+/-2")
print(m1+m2) # 24±3
print(m1-m2) # 16±3
print(m1*m2) # 80±40
print(m1/m2) # 5±3
print(m1**4) # 160000±30000
print(3**m2) # 81±200
print(m1**m2) # Erro
```

Infelizmente, não há propagação de erro automática nas funções da biblioteca ```math```, porém, a LabIFSC provê as seguintes funções com propagação de erro:

```python
m1 = Medida("20+/-1.5")
print(cos(m1))     # 0±1
print(sin(m1))     # 0.9±0.6
print(tan(m1))     # 2±9
print(cot(m1))     # 0±2
print(sec(m1))     # 2±8
print(csc(m1))     # 2.2±0.7
print(arc_cos(m1)) # 0.8±0.1 rad
print(arc_sin(m1)) # 0.8±0.1 rad
print(arc_tan(m1)) # 0.6±0.1 rad
print(log(m1))     # 2.73±0.07
print(log10(m1))   # 1.30±0.03
print(log2(m1))    # 4.3±0.1
print(ln(m1))      # 3±0.08
print(sqrt(m1))    # 4.5±0.2
print(cbr(m1))     # 2.71±0.0
```

## Unidades

Todas as medidas podem ter um parâmetro adicional de unidade após o valor. Por exemplo:

```python
m1 = Medida("1+/-0.001", "m")
m2 = Medida("1+/-0.001", "ft")
m3 = Medida("1+/-0.02", "s")
```

(O arquivo ```LabIFSC/lista_de_unidades.py``` contém todas as unidades suportadas por esta biblioteca.)

As contas de soma e subtração sempre ficam nas unidades do primeiro argumento nas operações desde que as dimensões físicas sejam iguais. No caso contrário, tem-se um erro. Já as contas de multiplicação e divisão combinam as unidades.

```python
print(m1+m2) #   2.610±0.001 m
print(m2+m1) #   5.586±0.004 ft
print(m1-m2) #  -0.610±0.001 m
print(m2-m1) #  -3.586±0.004 ft
print(m1*m2) # 1±0.002 ft m
print(m2*m1) # 1±0.002 ft m
print(m1/m2) # 1±0.002 m ft⁻¹
print(m2/m1) # 1±0.002 ft m⁻¹
print(m1*m3) # 1±0.02 m s
print(m1/m3) # 1±0.02 m s⁻¹

print(m1+m3) # ValueError: dimensões físicas incompatíveis: L1 vs T1
```

Para converter as unidades:

```python
m4 = m1*m2/m3
print(m4.converta("m^2 s^-1")) # 1.610±0.007 m² s⁻¹
print(m4.converta("m^2/s"))    # 1.610±0.007 m² s⁻¹
print(m4.converta("m^2/kg"))   # ValueError: dimensões físicas incompatíveis: L2T-1 vs L2M-1
```

## Sequências e Tabelas

## Gráficos
