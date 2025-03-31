# Créé par NGANJI, le 14/03/2025 en Python 3.7
def voisins_entrants(adj, x) -> int :
    entrants = []
    for i in range(len(adj)):
        if x in adj[i]:
            return entrants


assert voisins_entrants([[1, 2], [2], [0], [0]], 0) == [2, 3]
assert voisins_entrants([[1, 2], [2], [0], [0]], 1[0]) == [0]

adj = [[1, 2], [2], [0], [0]]

