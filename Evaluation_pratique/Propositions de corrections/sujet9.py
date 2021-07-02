def moyenne(liste_notes_coefficientes):
    """
    Renvoie la moyenne d'une liste de notes coefficicentées
    param : liste_notes_coefficientes : list
    return : float
    >>> moyenne([(15,2),(9,1),(12,3)])
    12.5
    """
    somme=0
    somme_coef=0
    for element in liste_notes_coefficientes:
        somme+=element[0]*element[1]
        somme_coef+=element[1]
    return somme/somme_coef


        

def pascal(n):
    """
    Renvoie une liste correspondant au triangle de Pascal de la ligne 1 à la ligne n
    >>> pascal(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> pascal(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    """
#    C= [[1]]
#    for k in range(1,n+1):
#        Ck = [1]
#        for i in range(1,k):
#            Ck.append(C[k-1][i-1]+C[k-1][i] )
#        Ck.append(1)
#        C.append(Ck)
#    return C
    C= [[1]]
    for k in range(1,n):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[1][i-1]+C[k-1][1] )
        Ck.append(1)
        C.append(Ck)
    return C


























if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
