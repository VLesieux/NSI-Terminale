def conv_bin(n):
    """
    Renvoie un couple (b,bit)
    b est une liste d'entiers correspondant à la représentation binaire de n
    bit correspond aux nombre de bits qui constituent b
    param : n : int
    return : tuple
    >>> conv_bin(9)
    ([1, 0, 0, 1], 4)
    >>> conv_bin(13)
    ([1, 1, 0, 1], 4)
    """

    nb_binaire=[]
    while n!=0:
        nb_binaire.append(n%2)
        n=n//2
    nb_binaire.reverse()
    return nb_binaire, len(nb_binaire)

#    T=[n%2]
#    while n//2 >0:
#        n=n//2
#        T.append(n%2)
#    T.reverse()
#    return (T,len(T))



    
def tri_bulles1(T):
    """
    Renvoie la liste triée dans l'ordre croissant
    param : T : list
    return : list
    >>> tri_bulles1([3, 8, 1, 5])
    [1, 3, 5, 8]
    """
    n = len(T)
    for i in range(n-1,0,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


def tri_bulles2(T):
    """
    Renvoie la liste triée dans l'ordre croissant
    param : T : list
    return : list
    >>> tri_bulles2([3, 8, 1, 5])
    [1, 3, 5, 8]
    """
    n = len(T)
    for i in range(n-1):
        for j in range(n-i-1):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


def conv_bin_g(n):
    """
    renvoie le nombre binaire de n
    >>> conv_bin_g(9)
    ([1, 0, 0, 1], 4)
    """
    nb_binaire=[]
    while n!=0:
        nb_binaire.append(n%2)
        n=n//2
    return nb_binaire, len(nb_binaire)

##marche pas marina

#def tri_bulles_marina(T):
#    '''
#    Renvoie la liste triée par ordre croissant
#    
#    param : T : list
#    return : list
#    >>> tri_bulles_marina([3, 8, 1, 5])
#    [1, 3, 5, 8]
#    '''
#    n = len(T)
#    for i in range(0,len(T),-1):
#        for j in range(i):
#            if T[j] > T[i]:
#                T[i] = T[j]
#                T[j] = T[i]
#                T[j+1] = temp
#    return T












if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
