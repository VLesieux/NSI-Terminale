def multiplication(n1,n2):
    """
    Renvoie le produit n1*n2
    param : n1 : int
    param : n2 : int
    return : int
    >>> multiplication(3,5)
    15
    >>> multiplication(-4,-8)
    32
    >>> multiplication(-2,6)
    -12
    >>> multiplication(-2,0)
    0    
    """
    resultat=0
    if n2<0:
        n1=-n1
        n2=-n2
    for i in range(n2):
        resultat+=n1
    return resultat

def dichotomie(tab, x):
    """
    Renvoie True si x dans tab sinon False
    param : tab : list
    param : x : int
    return : bool
    c.u : tab est trié
    >>> dichotomie([15,16,18,19,23,24,28,29,31,33],28)
    True
    >>> dichotomie([15,16,18,19,23,24,28,29,31,33],27)
    False    
    """
    debut=0
    fin=len(tab)-1
    while debut<=fin:
        m=(debut+fin)//2
        if x==tab[m]:
            return True
        if x>tab[m]:
            debut=m+1
        else:
            fin=m-1
    return False
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)