def recherche(tab,n):
    """
    renvoie l'indice de la dernière occurence de n sinon longueur du tableau
    param : tab : list
    param : n : int
    return : int
    >>> recherche([5,3],1)
    2
    >>> recherche([2,4],2)
    0
    >>> recherche([2,3,5,2,4],2)
    3    
    """
    variable=len(tab)
    for i in range(len(tab)):
        if tab[i]==n:
            variable=i
    return variable
    
from math import sqrt   # import de la fonction racine carrée

def distance(point1, point2): 
    """
    Calcule et renvoie la distance entre deux points.
    param : point 1 : tuple
    param : point 2 : tuple
    return : float
    >>> distance((1, 0), (5, 3))
    5.0    
    """
    return sqrt((point1[1]-point2[1])**2 + (point1[0]-point2[0])**2)


def plus_courte_distance(tab, depart):
    """
    Renvoie le point du tableau tab se trouvant à la plus     
    courte distance du point depart.
    param : tab : list
    param : depart : tuple
    return : tuple
    >>> plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0))
    (2, 5)    
    """
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart)<min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)