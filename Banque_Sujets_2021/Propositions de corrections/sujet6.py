def rendu(somme_a_rendre):
    """
    Renvoie une liste de 3 entiers pour (5,2,1)
    param : somme_a_rendre : int
    return : list
    >>> rendu(13)
    [2, 1, 1]
    >>> rendu(64)
    [12, 2, 0]
    >>> rendu(89)
    [17, 2, 0]
    """
    n1=somme_a_rendre//5
    n2=(somme_a_rendre%5)//2
    n3=(somme_a_rendre%5)%2
    return [n1,n2,n3]
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)