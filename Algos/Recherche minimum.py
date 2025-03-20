# Recherche minimum(1ere):

def recherche_minimum(tab):
    ind = tab[0]
    for i in tab:
        if i < ind:
           ind = i
    return ind
