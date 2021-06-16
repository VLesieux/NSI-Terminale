def maxi(liste):
    """
    Renvoie le plus grand élément de la liste et son indice de première apparition
    param : liste
    return : tuple
    >>> maxi([1,5,6,9,1,2,3,7,9,8])
    (9, 3)
    """
    maximum=liste[0]
    for valeur in liste:
        if valeur>=maximum:
            maximum=valeur
    for i in range(len(liste)):
        if liste[i]==maximum:
            return (maximum,i)
    








if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
