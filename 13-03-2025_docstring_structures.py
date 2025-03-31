class Noeud:
     """
    A class to represent a noeud

    Attributes
    ----------
    nom : int
        name of the noeud
    suivant: Noeud
        

    Methods
    -------
    get_suivant():
        return the next noeud.
    """
    def __init__(self,nom:int, suivant:Noeud):
        self.nom=nom,
        self.suivant=suivant
    
    def get_suivant(self)-> Noeud:
        return self.suivant
    def set_suivant(self, noeud:Noeud)->None:
        self.suivant=suivant
    def get_nom(self)-> Noeud:
        """
        Cette méthode retourne la valeur du noeud
            Parameters :
                NONE
            Returns:
                self.noeud = la valeur du noeud
        """
        return self.nom
    def set_nom(self, nom:int)->None:
        """
        Cette méthode met à jour la valeur du noeud
            Parameters :
                nom -> valeur du noeud
            Returns:
                None
        """
        self.nom=nom
    