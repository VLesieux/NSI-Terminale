def recherche(tab,n):
    """
    Recherche de façon dichotomique l'indice de n dans tab sinon renvoie -1
    param : tab : list
    param : n : int
    return : int ou -1
    >>> recherche([2, 3, 4, 5, 6], 5)
    3
    >>> recherche([2, 3, 4, 6, 7], 5)
    -1    
    """
    a=0
    b=len(tab)-1
    while a<=b:
        m=(a+b)//2
        if tab[m]==n:
            return m
        elif tab[m]<n:
            a=m+1
        else:
            b=m-1
    return -1



ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    """
    Renvoie le nouveau message codé avec le codage de César utilisant le décalage decalage
    param : message : str
    param : decalage : int
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5)
    'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
    """
#    resultat = ''
#    for lettre in message :
#        if lettre in ALPHABET :
#            indice = ( position_alphabet(lettre)+decalage)%26
#            resultat = resultat + ALPHABET[indice]
#        else:
#            resultat = resultat + lettre
#    return resultat
    resultat = ''
    for indice in message :
        if lettre in ALPHABET :
            indice = ( decalage )%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = -1
    return resultat

def recherche(gene, seq_adn):
    """
    vérifie si gene est présent dans seq_adn
    param : gene : str
    param : seq_adn : str
    return : bool
    >>> recherche("AATC", "GTACAAATCTTGCC")
    True
    >>> recherche("AGTC", "GTACAAATCTTGCC")
    False
    """
    n=len(seq_adn)
    g=len(gene)
    i=0
    trouve=False
    while i<n and trouve==False:
        j=0
        while j<g and gene[j]==seq_adn[i+j]:
            j+=1
        if j==g:
            trouve=True
        i+=1
    return trouve














if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

