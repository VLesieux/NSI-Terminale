t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]


def mini(releve,date):
    """
    Renvoie la plus petite valeur de relevé et la date correspondante
    param : releve : list
    param : annees : list
    return : tuple
    >>> mini(t_moy, annees)
    (12.5, 2016)
    """
    minimum=releve[0]
    indice=0
    for i in range(len(releve)):
        if releve[i]<minimum:
            minimum=releve[i]
            indice=i
    return (minimum,date[indice])

def inverse_chaine(chaine):
    """
    Renverse la chaîne de caractère
    param : chaine : str
    return : str
    >>> inverse_chaine('bac')
    'cab'
    """
    result = ''
    for caractere in chaine:
       result = caractere+result
    return result

def est_palindrome(chaine):
    """
    Renvoie True si chaine est un palindrome, False sinon
    >>> est_palindrome('NSI')
    False
    >>> est_palindrome('ISN NSI')
    True    
    """
    inverse = inverse_chaine(chaine)
    return chaine==inverse
    
def est_nbre_palindrome(nbre):
    """
    Renvoie True si nbre est un palindrome, False sinon
    >>> est_nbre_palindrome(214312)
    False
    >>> est_nbre_palindrome(213312)
    True 
    """
    chaine = str(nbre)
    return est_palindrome(chaine)

















if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

