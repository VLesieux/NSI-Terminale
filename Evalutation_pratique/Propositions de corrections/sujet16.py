def moyenne(tab):
    """
    Renvoie la moyenne des nombres flottants dans le tableau non vide
    param : tab : list
    return : float
    >>> moyenne([1.0])
    1.0
    >>> moyenne([1.0, 2.0, 4.0])
    2.3333333333333335    
    """
    resultat=0
    for valeurs in tab:
        resultat+=valeurs
    return resultat/len(tab)



def dec_to_bin(a):
    """
    Renvoie l'écriture binaire d'un nombre donné en écriture décimale
    param : a : int
    return : str
    >>> dec_to_bin(83)
    '1010011'
    >>> dec_to_bin(127)
    '1111111'    
    """
    bin_a = str(a%2)
    a = a//2
    while a >0 :
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a















if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

