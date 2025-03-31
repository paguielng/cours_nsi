# Créé par NGANJI, le 17/02/2025 en Python 3.7
class Livre:
    def __init__(self, titre:str, auteur:str, prix:float):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix;

    def afficher(self)->str:
        return f"{self.titre} a été écrit par {self.auteur} et coute {self.prix}"

Livre("Le guide du voyageur galactique","Douglas Adams", 6.42)  print(livre1.afficher()) #instance
