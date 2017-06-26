#!/usr/bin/env python

from .tabela import linearize, media
from .geral import unidades_em_texto

def ajusta_unidade(val, unidade_ref):
    try:
        if unidade_ref[0] == u"∅":
            unidade_ref = [unidades_em_texto(val.unidades_originais)]
    except AttributeError:
        pass
    if unidade_ref[0] != u"∅":
        try:
            val = val.converta(unidade_ref)
        except AttributeError:
            pass
        except:
            raise Exception("falha ao converter unidades de {} em {}".format(val.__repr__(), unidade_ref))
    return val, unidade_ref[0]

def plote(linhas=[], arquivo="plot.pdf", titulo_x="", titulo_y="", titulo_y2="", titulo="", lgd_y_hack=-0.25, lgd_ncol=2, tamanho_horizontal=20, tamanho_vertical=15, cor_x="black", cor_y="black", cor_y2="black"):
    try:
        import matplotlib.pyplot as plt
    except:
        raise RuntimeError("matplotlib não está instalado e ela é necessária para gerar gráficos")

    # Prepare o básico
    fig = plt.figure()
    ax_line_left  = fig.add_subplot(111)
    ax_line_right = ax_line_left.twinx()

    # Cuidados com unidades | listast para editar por referência
    unidade_x = [u"∅"]
    unidade_y_esquerda = [u"∅"]
    unidade_y_direita = [u"∅"]

    # Plote cada um dos gráficos de linha
    for l in linhas:
        try:
            x, y = l["x"], l["y"]
            ax = ax_line_left
            unidade_y = unidade_y_esquerda
        except:
            x, y = l["x"], l["y2"]
            ax = ax_line_right
            unidade_y = unidade_y_direita
        xerr, yerr = [], []
        max_x = float("-inf")
        min_x = float("+inf")
        legenda = ""
        tipo = ""
        cor = None
        linearize_flag = False
        media_flag = False
        if "nome" in l:
            legenda = l["nome"]
        if "tipo" in l:
            tipo = l["tipo"]
        if "linearize" in l:
            linearize_flag = l["linearize"]
        if "média" in l:
            media_flag = l["média"]
        if "cor" in l:
            cor = l["cor"]

        # Converta as unidades por precaução e anote os erros
        for i in range(len(x)):
            max_x = max(x[i], max_x)
            min_x = min(x[i], min_x)
            x[i], unidade_x[0] = ajusta_unidade(x[i], unidade_x)
            y[i], unidade_y[0] = ajusta_unidade(y[i], unidade_y)
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
                x, y, marker="o", linestyle="--", color=cor,
                xerr=xerr, yerr=yerr, elinewidth=1, capsize=3,
                label=legenda)

        if linearize_flag == True:
            lin = linearize(x, y)
            a = lin["a"]
            b = lin["b"]
            r2 = lin["R²"]
            lin_x = [min_x, max_x]
            lin_y = [a*min_x+b, a*max_x+b]
            ax.errorbar(
                lin_x, lin_y,
                label="(Linearização) "+legenda+" R² = {:.3f}".format(r2.nominal))
        if media_flag == True:
            y_avg = media(y)
            ax.axhspan(
                hatch='/',
                fill=False,
                zorder=-99,
                ymin=y_avg-y_avg.incerteza,
                ymax=y_avg+y_avg.incerteza,
                label="(Média) "+legenda)

    # Arrume os títulos
    if unidade_x[0] != u"∅":
        if titulo_x == "":
            titulo_x = "{}".format(
                unidade_x[0])
        else:
            titulo_x = "{} ({})".format(
                titulo_x,
                unidade_x[0])
    if unidade_y_esquerda[0] != u"∅":
        if titulo_y == "":
            titulo_y = "{}".format(
                unidade_y_esquerda[0])
        else:
            titulo_y = "{} ({})".format(
                titulo_y,
                unidade_y_esquerda[0])
    if unidade_y_direita[0] != u"∅":
        if titulo_y2 == "":
            titulo_y2 = "{}".format(
                unidade_y_direita[0])
        else:
            titulo_y2 = "{} ({})".format(
                titulo_y2,
                unidade_y_direita[0])

    # Coloque os títulos
    ax_line_left.set_title(titulo)
    ax_line_left.set_xlabel(titulo_x, color=cor_x)
    ax_line_left.set_ylabel(titulo_y, color=cor_y)
    ax_line_right.set_ylabel(titulo_y2, color=cor_y2)

    # Retire as barras de erro das legendas
    handles_left, labels_left = ax_line_left.get_legend_handles_labels()
    handles_left_old = handles_left
    handles_left = []
    for h in handles_left_old:
        try:
            handles_left.append(h[0])
        except:
            handles_left.append(h)
    handles_right, labels_right = ax_line_right.get_legend_handles_labels()
    handles_right_old = handles_right
    handles_right = []
    for h in handles_right_old:
        try:
            handles_right.append(h[0])
        except:
            handles_right.append(h)

    # Toques finais e salve
    fig.set_size_inches(tamanho_horizontal/2.54, tamanho_vertical/2.54)
    plt.grid(True)
    extra_artists = []
    lgd_left = plt.legend(handles_left, labels_left, loc='lower left', bbox_to_anchor=(0.5, lgd_y_hack), ncol=lgd_ncol)
    lgd_right = plt.legend(handles_right, labels_right, loc='lower right', bbox_to_anchor=(0.5, lgd_y_hack), ncol=lgd_ncol)
    if len(lgd_left.get_texts()) > 0:
        extra_artists.append(lgd_left)
    if len(lgd_right.get_texts()) > 0:
        extra_artists.append(lgd_right)
    fig.savefig(arquivo+".pdf", bbox_extra_artists=tuple(extra_artists), bbox_inches='tight')
    fig.savefig(arquivo+".png", bbox_extra_artists=tuple(extra_artists), bbox_inches='tight', dpi=300)
