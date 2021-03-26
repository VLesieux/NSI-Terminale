
def moyenne(tab):
    """
    Renvoie la moyenne des éléments du tableau si non vide sinon renvoie 'erreur'
    param : list
    return : float ou "erreur"
    >>> moyenne([5,3,8])
    5.333333333333333
    >>> moyenne([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> moyenne([])
    'erreur'
    """
    if len(tab)==0:
        return 'erreur'
    else:
        resultat=0
        for valeur in tab:
            resultat+=valeur
        return resultat/len(tab)



def tri(tab):
    """
    Renvoie une table triée
    param : tab : list
    return : list
    >>> tri([0,1,0,1,0,1,0,1,0])
    [0, 0, 0, 0, 0, 1, 1, 1, 1]
    """
    #i est le premier indice de la zone non triee, j le dernier indice. 
    #Au debut, la zone non triee est le tableau entier.
    i= 0
    j= len(tab)-1
    while i != j :
        if tab[i]== 0:
            i= i+1
        else :
            tab[j],tab[i] = tab[i],tab[j]
            j= j -1
    return tab













if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)