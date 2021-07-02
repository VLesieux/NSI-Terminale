## déjà sujet 10

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

def recherche(gene, seq_adn):
    """
    Renvoie True si on trouve gene dans seq_adn et False sinon
    param : gene : str
    param : seq_adn : str
    >>> recherche("AATC", "GTACAAATCTTGCC")
    True
    >>> recherche("AGTC", "GTACAAATCTTGCC")
    False
    """
#    n = len(seq_adn)
#    g = len(gene)
#    i = 0
#    trouve = False
#    while i < n and trouve == False :
#        j = 0
#        while j < g and gene[j] == seq_adn[i+j]:
#            j+=1
#        if j == g:
#            trouve = True
#        i+=1
#    return trouve
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j=j+1
        if j == g:
            trouve = True
        i=i+1
    return trouve

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

