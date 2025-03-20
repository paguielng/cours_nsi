#Recherche maximum(1ere) :

def recherche_maximum(tab):
    ind = tab[0]
    for i in tab:
        if i > ind:
           ind = i
    return ind

OU

def maximum_tableau(tab:list)->int:
    max = tab[0]
    for i in range(len(tab)) : 
        if max < tab[i] : max = tab[i] 
    return max

