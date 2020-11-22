tab = [ [5], [8, 10 ], [11, 3, 4], [6, 10, 7, 12 ]]

def gain_max(t,l,r):
    """Renvoie le gain maximal
    : param tableau : liste
    : return : int
    >>> gain_max(tab,0,0)
    34
    """
    n=len(t)
    if l==n-1:
        return t[l][r]
    else:
        return t[l][r]+max(gain_max(t,l+1,r),gain_max(t,l+1,r+1))
    

def somme(liste):
    
    valeurs={}
    liste_maximum=[]
    for i in range(len(liste)):
        calcul=0
        for j in range(len(liste[0])):
            calcul+=liste[i][j]
        if calcul!=0:
            valeurs[(i,j)]=calcul
            liste_maximum.append(calcul)
    return valeurs
    
    
    
    
    
    
#def maximum_par_niveau(liste):
#    n=0
#    chemin=[]
    
            
            
        
    
    


def gain_max_mem(t,l,r,mem=None):
    """Renvoie le gain maximal
    : param tableau : liste
    : return : int
    >>> gain_max_mem(tab,0,0)
    34
    """
    n=len(t)
    if mem == None:
        mem = [[0 for _ in range(n)] for _ in range(n)]
    if mem[l][r] !=0:
        res=mem[l][r]
    else:
        if l<n-1:
            res=t[l][r]+max(gain_max_mem(t,l+1,r),gain_max_mem(t,l+1,r+1))
        else:
            res=t[l][r]
        mem[l][r]=res
#        print(mem)
    return res







    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)