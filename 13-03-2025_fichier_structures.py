# Créé par NGANJI, le 13/03/2025 en Python 3.7

class Noeud:
    def __init__(self, nom: int, suivant: object):
        self.nom = nom
        self.suivant = suivant

    def get_nom(self) -> int:
        return self.nom

    def set_nom(self, n: int) -> None:
        self.nom = n

    def get_suivant(self) -> object:
        return self.suivant

    def set_suivant(self, s: object) -> None:
        self.suivant = s


class Pile:
    '''
    Classe Pile constructeur qui initialisera l’attribut sommet à None.
    '''
    def __init__(self, sommet):
        self.sommet = None

    def est_vide(self):
        return self.sommet is None

    def empiler(self, n:int):
        self.sommet = Noeud(n, self.sommet)

    def depiler(self) -> int:
        if not self.est_vide():
            retour = self.sommet.v
            self.sommet = self.sommet.suivant
            return retour

class File:

    def __init__(self)-> None:
        self.premier = None
        self.dernier = None

    def est_vide(self):
        return self.premier is None

    def enfiler(self, n: int) -> None:
        nouveau = Noeud(n, None)
        if self.est_vide():
            self.premier = nouveau
        else:
            self.dernier.set_suivant(nouveau)
            self.dernier = nouveau

    def defiler(self) -> int:
          res = -1
          if not self.est_vide():
              res = self.premier.get_nom()
              self.premier = self.premier.get_suivant()
           return res