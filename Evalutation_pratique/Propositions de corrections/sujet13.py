def recherche_minimum(tab,n):
    """
    Renvoie le plus petit élément de tab à partir du rang n
    param : tab : list
    return : int
    >>> recherche_minimum([100,-52,6,-9,12],0)
    -52
    >>> recherche_minimum([100,-52,6,-9,12],2)
    -9
    """
    minimum=tab[n]
    for i in range(n,len(tab)):
        if tab[i]<minimum:
            minimum=tab[i]
    return minimum

def tri_selection(tab):
    """
    Renvoie le tableau trié par ordre croissant
    param : tab : list
    return : list
    >>> tri_selection([1,52,6,-9,12])
    [-9, 1, 6, 12, 52]    
    """
    for i in range(len(tab)-1):
        for j in range(i,len(tab)):
            if tab[j]==recherche_minimum(tab,i):
                tab[i],tab[j]=tab[j],tab[i]
    return tab

## Version synthétique

def tri_selection_synthetique(tab):
    """
    param : t : list
    return : list
    >>> tri_selection_synthetique([1,52,6,-9,12])
    [-9, 1, 6, 12, 52] 
    """
#    for i in range(len(t)-1):
#        minimum=i
#        for j in range(i+1,len(t)):
#            if t[j]<t[minimum]:
#                minimum=j
#        t[i],t[minimum]=t[minimum],t[i]
#    return t
    for i in range(len(tab)):
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
    return tab

def plus_ou_moins():
    """
    simule un jeu du "plus ou moins" : le joueur doit trouver le nombre avant 10 essais
    """
    nb_mystere = randint(1,99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 9 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print ("Perdu ! Le nombre était ", nb_mystere)
        
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

