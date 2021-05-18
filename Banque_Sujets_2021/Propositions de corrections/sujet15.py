def rechercheMinMax(tab):
    """
    Renvoie la plus petite et la plus grande valeur du tableau sous la forme d'un dictionnaire
    à 2 clés 'min' et 'max'
    param : tab : list
    return : dict
    >>> tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
    >>> rechercheMinMax(tableau)
    {'min': -2, 'max': 9}    
    """
    minimum=tab[0]
    maximum=tab[0]
    for i in range(len(tab)):
        if tab[i]<minimum:
            minimum=tab[i]
        if tab[i]>maximum:
            maximum=tab[i]
    return {'min':minimum,'max':maximum}






if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

