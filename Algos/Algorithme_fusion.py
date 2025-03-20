# Algorithme de fusion :

def tri_fusion(tab:list, deb: int, fin: int)  -> None:
	"""- rechercher le **milieu** du tableau, - **appel récursif** sur chaque **sous-tableau** - **fusionner** les tableaux lors de la remontée d’appel"""
	if deb<fin:
		# rechercher le **milieu** du tableau
        	milieu=(deb+fin)//2
        	# appel récursif sur chaque sous-tableau
        	tri_fusion(tab,deb,milieu)
        	tri_fusion(tab,milieu+1,fin)
        	# fusionner les tableaux lors de la remontée d’appel
        	fusionner(tab,deb,fin)


def fusionner(tab: list, deb: int, fin: int)-> None:
    # Créer un tableau temporaire res vide.
    res=[]
    # Trouver le milieu de la partie à trier.
    milieu=(deb+fin)//2
    i=deb
    j=milieu+1
    # Tant que les parties gauches et droites n’ont pas été entièrement parcourues :
    while i<=milieu and j<=fin:
        # Si l’élément en cours de gauche est inférieur à celui de droite :
        if tab[i]<tab[j]:
            # insérer l’élément en cours de gauche dans res
            res.append(tab[i])
            i+=1
        # sinon
        else:#    insérer l’élément de droite dans res
            res.append(tab[j])
            j+=1
        # Ajouter les éléments restants de la partie non parcourue entièrement. 
        
        
        for i1 in range(i,milieu+1):
            res.append(tab[i1])
        for j1 in range(j,fin+1):
            res.append(tab[j1])
        #copier res dans la partie de tab.
        for k in range(len(res)):
            tab[deb+k]=res[k]
    def fusionner(tab: list, deb: int, fin: int)-> None:
    # Créer un tableau temporaire res vide.
    res=[]
    # Trouver le milieu de la partie à trier.
    milieu=(deb+fin)//2
    i=deb
    j=milieu+1
    # Tant que les parties gauches et droites n’ont pas été entièrement parcourues :
    while i<=milieu and j<=fin:
        # Si l’élément en cours de gauche est inférieur à celui de droite :
        if tab[i]<tab[j]:
            # insérer l’élément en cours de gauche dans res
            res.append(tab[i])
            i+=1
        # sinon
        else:#    insérer l’élément de droite dans res
            res.append(tab[j])
            j+=1
        # Ajouter les éléments restants de la partie non parcourue entièrement. 
        
        
        for i1 in range(i,milieu+1):
            res.append(tab[i1])
        for j1 in range(j,fin+1):
            res.append(tab[j1])
        #copier res dans la partie de tab.
        for k in range(len(res)):
            tab[deb+k]=res[k]
