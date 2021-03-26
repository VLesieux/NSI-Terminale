def fibonacci(n):
    """
    Renvoie l'élémet d'indice n de la suite
    param : n : int
    return : int
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(25)
    75025
    >>> fibonacci(45)
    1134903170
    """
    a=1
    b=1
    c=1
    if n==1 or n==2:
        return c
    i=3
    while i<=n:
        c=a+b
        a=b
        b=c
        i+=1
    return c

def Fibonacci_iteratif(n):
    """
    renvoie le nième terme de la suite de Fibonacci
    param : n : int
    return : int
    >>> Fibonacci_iteratif(2)
    1
    >>> Fibonacci_iteratif(3)
    2
    >>> Fibonacci_iteratif(4)
    3
    """
    u,v=0,1
    for i in range(n-1):
        u,v=v,u+v
    return v

def Fibonacci_recursif(n):
    """
    renvoie le nième terme de la suite de Fibonacci
    param : n : int
    return : int
    >>> Fibonacci_recursif(2)
    1
    >>> Fibonacci_recursif(3)
    2
    >>> Fibonacci_recursif(4)
    3
    """
    if n==0 or n==1:
        return n
    else:
        return Fibonacci_recursif(n-1)+Fibonacci_recursif(n-2)

liste_eleves = ['a','b','c','d','e','f','g','h','i','j']
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def meilleures_notes():
    """
    Renvoie note maxi,nb eleves ayant note, liste eleves
    >>> meilleures_notes()
    (80, 3, ['c', 'f', 'h'])
    """
    note_maxi = 0
    nb_eleves_note_maxi = 0
    liste_maxi = []
    
    for compteur in range(len(liste_eleves)):
        if liste_notes[compteur] == note_maxi:
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[compteur])
        if liste_notes[compteur] > note_maxi:
            note_maxi = liste_notes[compteur]
            nb_eleves_note_maxi = 1
            liste_maxi = [liste_eleves[compteur]]
            
    return (note_maxi,nb_eleves_note_maxi,liste_maxi)



if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
