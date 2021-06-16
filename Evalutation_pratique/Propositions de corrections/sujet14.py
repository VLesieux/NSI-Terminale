def recherche(elt,tab):
    """
    Renvoie le tableau des indices de elt dans tab sinon []
    param : elt : int
    param : tab : list
    return : list
    >>> recherche(3, [3, 2, 1, 3, 2, 1])
    [0, 3]
    >>> recherche(4, [1, 2, 3])
    []    
    """
    indices=[]
    for i in range(len(tab)):
        if tab[i]==elt:
            indices.append(i)
    return indices
        


resultats = {'Dupont':{'DS1' : [15.5, 4],
                       'DM1' : [14.5, 1],
                       'DS2' : [13, 4],
                       'PROJET1' : [16, 3],
                       'DS3' : [14, 4]},
             'Durand':{'DS1' : [6 , 4],
                       'DM1' : [14.5, 1],
                       'DS2' : [8, 4],
                       'PROJET1' : [9, 3],
                       'IE1' : [7, 2],
                       'DS3' : [8, 4],
                       'DS4' :[15, 4]}}


def moyenne(nom):
    """
    renvoie la moyenne coefficientée pour un élève
    param : nom : str
    return : float
    >>> moyenne('Dupont')
    14.5
    """
    if nom in resultats.keys():
        notes = resultats[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs  in notes.values():
            note , coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round( total_points / total_coefficients , 1 )
    else:
        return -1














if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

