"""
Module d'étude de la suite de Syracuse.

Ce module permet de générer la suite de Syracuse, de calculer ses
propriétés (temps de vol, altitude) et de l'afficher graphiquement.
"""

#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Affiche le graphique de la suite de Syracuse avec Plotly.

    Args:
        lsyr (list): La liste des valeurs de la suite.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    # Correction R1721 : Utilisation directe de list(range())
    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n: int) -> list[int]:
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list[int]: la suite de Syracuse de source n
    """
    l = [n]
    current = n
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = current * 3 + 1
        l.append(current)
    return l


def temps_de_vol(l: list[int]) -> int:
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list[int]): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    return len(l) - 1


def temps_de_vol_en_altitude(l: list[int]) -> int:
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list[int]): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    altitude_initiale = l[0]
    n = 0
    for x in l[1:]:
        if x < altitude_initiale:
            break
        n += 1
    return n


def altitude_maximale(l: list[int]) -> int:
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list[int]): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    return max(l)


#### Fonction principale


def main() -> None:
    """
    Fonction principale.
    Calcule et affiche les propriétés de la suite de Syracuse pour n=15.
    """
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(f"Temps de vol : {temps_de_vol(lsyr)}")
    print(f"Temps de vol en altitude : {temps_de_vol_en_altitude(lsyr)}")
    print(f"Altitude maximale : {altitude_maximale(lsyr)}")


if __name__ == "__main__":
    main()
