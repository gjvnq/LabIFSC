#!/usr/bin/env python

from .geral import unidades_em_texto

def ajusta_unidade(val, unidade_ref):
    try:
        if unidade_ref == u"∅":
            unidade_ref = unidades_em_texto(val.unidades_originais)
    except AttributeError:
        pass
    if unidade_ref != u"∅":
        try:
            val = val.converta(unidade_ref)
        except AttributeError:
            pass
        except:
            raise Exception("falha ao converter unidades de {} em {}".format(val.__repr__(), unidade_ref))
    return val, unidade_ref

def plote(linhas=[], arquivo="plot.pdf", titulo_x="", titulo_y="", titulo="", lgd_y_hack=-0.25, lgd_ncol=2, tamanho_horizontal=20, tamanho_vertical=15):
    print(linhas)
    try:
        import matplotlib.pyplot as plt
    except:
        raise RuntimeError("matplotlib não está instalado e ela é necessária para gerar gráficos")

    # Prepare o básico
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Cuidados com unidades
    unidade_x = u"∅"
    unidade_y_esquerda = u"∅"
    unidade_y_direita = u"∅"

    # Plote cada um dos gráficos de linha
    for l in linhas:
        x, y = l["x"], l["y"]
        xerr, yerr = [], []
        legenda = ""
        tipo = ""
        if "nome" in l:
            legenda = l["nome"]
        if "tipo" in l:
            tipo = l["tipo"]

        # Converta as unidades por precaução e anote os erros
        for i in range(len(x)):
            x[i], unidade_x = ajusta_unidade(x[i], unidade_x)
            y[i], unidade_y_esquerda = ajusta_unidade(y[i], unidade_y_esquerda)
            try:
                xerr.append(x[i].incerteza)
            except:
                xerr.append(0)
            try:
                yerr.append(y[i].incerteza)
            except:
                yerr.append(0)
        if tipo == "continuo":
            ax.errorbar(
                x, y,
                label=legenda)
        else:    
            ax.errorbar(
                x, y, marker="o", linestyle="--",
                xerr=xerr, yerr=yerr, elinewidth=1, capsize=3,
                label=legenda)

    # Arrume os títulos
    if unidade_x != u"∅":
        if titulo_x == "":
            titulo_x = "{}".format(
                unidade_x)
        else:
            titulo_x = "{} ({})".format(
                titulo_x,
                unidade_x)
    if unidade_y_esquerda != u"∅":
        if titulo_y == "":
            titulo_y = "{}".format(
                unidade_y_esquerda)
        else:
            titulo_y = "{} ({})".format(
                titulo_y,
                unidade_y_esquerda)

    # Coloque os títulos
    ax.set_title(titulo)
    ax.set_xlabel(titulo_x)
    ax.set_ylabel(titulo_y)

    # Retire as barras de erro das legendas
    handles, labels = ax.get_legend_handles_labels()
    handles = [h[0] for h in handles]

    # Toques finais e salve
    fig.set_size_inches(tamanho_horizontal/2.54, tamanho_vertical/2.54)
    plt.grid(True)
    lgd = plt.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, lgd_y_hack), ncol=lgd_ncol)
    fig.savefig(arquivo, bbox_extra_artists=(lgd,), bbox_inches='tight')