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

### Funções Trigonométricas

## Conversão de Unidades

## Sequências e Tabelas

## Gráficos
