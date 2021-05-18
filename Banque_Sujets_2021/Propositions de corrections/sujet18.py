def insere(a, tab):
    """
    Insère la valeur a dans le tableau ordonné et renvoie le nouveau tableau
    param : a : int
    param : tab : list
    return : list
    >>> insere(3,[1,2,4,5])
    [1, 2, 3, 4, 5]
    >>> insere(10,[1,2,7,12,14,25])
    [1, 2, 7, 10, 12, 14, 25]
    >>> insere(1,[2,3,4])
    [1, 2, 3, 4]
    """
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l)-2
    while a < tab[i] and i>-1: 
      l[i+1] = l[i]
      l[i] = a
      i = i-1
    return l






















if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

