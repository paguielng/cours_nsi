class Menu:
    def __init__(self):
        self.entree = None
        self.plat = None
        self.accompagnement = None
        self.dessert = None

    def prendre_entree(self, choix: str) -> None:
        self.entree = choix

    def prendre_plat(self, choix: str) -> None:
        self.plat = choix

    def prendre_accompagnement(self, choix: str) -> None:
        self.accompagnement = choix

    def prendre_dessert(self, choix: str) -> None:
        self.dessert = choix

    def calculer_note(self) -> int:
        somme = 0
        if self.entree is not None:
            somme += 8
        if self.plat is not None:
            somme = somme + 10
        if self.accompagnement is not None:
            somme = somme + 3
        if self.dessert is not None:
            somme = somme + 8
            return somme



repas = Menu()
repas.prendre_plat("steak")
repas.prendre_accompagnement("frites")
repas.prendre_dessert("glace")
print(repas.calculer_note())
