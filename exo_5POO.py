# Créé par NGANJI, le 22/02/2025 en Python 3.7
class Date:
    def __init__(self, jour:int, mois:int, annee:int):
        self.jour = jour
        self.mois = mois
        self.annee = annee

        def afficher(self):
            nom_mois = ["janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout" ,"septembre", "octobre", "novembre", "decembre"]
            return f"{str(self.jour)} / {str(nom_mois[self.mois - 1])} / {str(self.annee)}"

        def est_avant(self, d):
            if self.annee > d.annee or self.annee == d.annee and (self.mois < d.mois or self.mois == d.mois and self.jour < d.jour):
                return True
            else:
                return False

d = Date(8, 12, 1997)