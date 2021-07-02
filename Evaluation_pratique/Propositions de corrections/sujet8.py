def recherche(caractere,mot):
    """
    Renvoie le nombre d'occurences de caractere dans mot
    param : caractere : str
    param : mot : str
    >>> recherche('e', "sciences")
    2
    >>> recherche('i',"mississippi")
    4
    >>> recherche('a',"mississippi")
    0    
    """
    compteur=0
    for lettre in mot:
        if lettre==caractere:
            compteur+=1
    return compteur



Pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution=[], i=0):
    """
    Renvoie la liste des pieces à rendre selon l'algorithme glouton
    param : arendre : int
    param : solution : list
    param : i
    return : list
    >>> rendu_glouton(68,[],0)
    [50, 10, 5, 2, 1]
    >>> rendu_glouton(291,[],0)
    [100, 100, 50, 20, 20, 1]
    """
    if arendre == 0:
       return solution
    p = Pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution,i)
    else :
        return rendu_glouton(arendre, solution, i+1)



















if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
