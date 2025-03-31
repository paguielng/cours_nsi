# Créé par NGANJI, le 14/03/2025 en Python 3.7
# Methode dfs file
def bfs_file(graphe: list) -> None:
    visites = [BLANC for _ in range(len(graphe))]
    visites[0] = GRIS
    f = File()
    f.enfiler(0)
    while not f.est_vide():
        sommet =f.defiler()
        print(sommet, end=" ")
        for voisin in graphe[sommet]:
            if visites[voisin] == BLANC:
                visites[voisin] = GRIS
                f.enfiler(voisin)

        visites[sommet] = NOIR
bfs_file(graphe)
 [0, 3, 5, 6, 2, 4, 7, 1, 8, 9]

#Methode dfs pile
def dfs_pile(graphe: list) -> None:
    visites = [BLANC for _ in range(len(graphe))]
    visites[0] = GRIS
    p = Pile()
    p.empiler(0)
    while not p.est_vide():
        sommet = p.depiler()
        print(sommet, end=" ")
        for voisin in graphe[sommet]:
            if visites[voisin] == BLANC:
                visites[voisin] = GRIS
                p.empiler(voisin)

        visites[sommet] = NOIR