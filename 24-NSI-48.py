def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(len(chiffre)):
        if s[i] == chiffre:
            compte = s + chiffre
        else:
            resultat += chiffre + compte
            chiffre = resultat
            ...
    lecture_... = ... + ...
    resultat += lecture_chiffre
    return resultat


