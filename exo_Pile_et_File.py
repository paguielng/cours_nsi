# Créé par NGANJI, le 13/03/2025 en Python 3.7
class Maillon:

    def __init__(self,s,v):
        self.valeur = v
        self.suivant = s

class Pile:
    def __init__(self):
        self.sommet= None

    def est_vide(self):
        return self.sommet is None

    def empiler(self,v):
        self.sommet = Maillon(val, self.sommet)

    def depiler(self):
        if not self.est_vide():
            retour = self.sommet.valeur
            self.sommet = self.sommet.suivant
            return retour

class Pile_lst:

    def __init__(self, lst):
        self.lst = lst

    def est_vide(self):
        return len(self.lst) == 0

    def empiler(self, v):
        self.lst.append(v)

    def depiler(self):
        if not self.est_vide():
            return lst.pop(-1)
        return "vide!"



class File:
    def __init__(self):
        self.sommet= None
        self.fin = None

    def est_vide(self):
        return self.sommet is None

    def empiler(self,v):
        self.sommet = Maillon(val, self.sommet)

    def depiler(self):
        if not self.est_vide():
            retour = self.sommet.valeur
            self.sommet = self.sommet.suivant
            return retour


class File_lst:

    def __init__(self, lst):
        self.lst = lst

    def est_vide(self):
        return len(self.lst) == 0

    def empiler(self, v):
        self.lst.append(v)

    def depiler(self):
        if not self.est_vide():
            return lst.pop(0)
        return "vide!"

