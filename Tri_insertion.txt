# Tri par insertion :

def tri_insertion(tab):
    for j in range(1, len(tab)):
        cle = tab[j]
        i = j-1
        while i >= 0 and tab[i] > cle:
            tab[i+1] = tab[i]
            i = i-1
        tab[+1] = cle
    return tab
