# Créé par NGANJI, le 17/02/2025 en Python 3.7
class Rectangle:

    def __init__(self, longueur, largeur)->None:
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self)->float:
        return 2*(self.longueur + self.largeur)

    def aire(self)->float:
        return self.longueur*self.largeur

    def est_carre(self):
        if self.longueur**2+self.largeur**2 == self.hypothenus:
            return True
        else:
            return False

