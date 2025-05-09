# Initiation à la Programmation Orientée Objet


## Introduction

En 1995, l'ingénieur américain Grady Booch propose 5 étapes dans l'établissement d'une conception orientée objet.

- Identifier les objets et les attributs ; identifier pour cela les propriétés caractéristiques de l'objet
- Identifier les opérations ; identifier les actions que l'objet subit ou exerce sur son environnement
- Établir la visibilité ; l'objet étant identifié par ses caractéristiques et ses opérations, on définira ses relations avec les autres objets, à savoir quels objets le voient et quels objets sont vus par lui.
- Établir l'interface : dès que la visibilité est acquise, on définit l'interface précise de l'objet avec le monde extérieur 
- Implémenter les objets : la dernière étape consiste à implanter les objets en écrivant le code.


## Les classes

Dans la programmation orientée objet, les différents objets utilisés peuvent être construits indépendamment les uns des autres (par exemple par des programmeurs différents) sans qu'il n'y ait de risque d'interférence.  

Ce résultat est obtenu grâce au concept d'**encapsulation** : les fonctionnalités internes et les variables qu'il utilise pour effectuer son travail sont en quelque sorte enfermées dans l'objet. Les autres objets et le monde extérieur ne peuvent y accéder qu'à travers des procédures bien définies, c'est ce qu'on appelle l'**interface** de l'objet.   

Une classe est une description d'un ensemble d'objets ayant une structure de données commune : les **attributs** et pouvant réaliser des actions : les **méthodes**. On considère en fait une classe comme un **nouveau type de données**. On appelle **instance de la classe** un objet du type de la classe qui la représente.  

L'intérêt de créer une classe est de pouvoir la modifier indépendamment du reste du programme en masquant leur complexité. Une donnée peut être déclarée en **accès public** (les autres objets peuvent accéder à la valeur de cette donnée ou la modifier) ou en **accès privé** (les autres objets n'ont pas le droit d'accéder directement à la valeur de cette donnée).  

Chaque classe doit définir une ou plusieurs méthodes appelées constructeurs. Un **constructeur** est une méthode invoquée lors de la création d'un objet. Cette méthode effectue les opérations nécessaires à l'initialisation de l'objet.


## Exemple d'implémentation d'une classe

En Python, on déclare une classe à l'aide du mot-clé **class**.

Pour déterminer et initialiser les attributs d'un objet que l'on crée, on utilise la méthode particulière appelée **constructeur** ; son nom est imposé : __init__.  

Les attributs privés sont précédés du **double** underscore.
La variable self, dans les méthodes d'un objet, désigne l'objet auquel s'appliquera la méthode.

```
class Carte:
    """
    Une carte est caractérisée par :
    - sa valeur (7,8,9,10,11,12,13,14) pour un jeu de 32 cartes
    - sa couleur (Pique, Trèfle, Coeur, Carreau)
    - sa figure, déduite de la valeur: Aucune, Valet, Dame, Roi, As.
    """
    def __init__(self,val,coul):
        """
        écriture du constructeur de la classe Carte (avec une majuscule)
        """
        self.__valeur=val
        self.__couleur=coul
        if val==11:
            self.__figure="Valet"
        elif val==12:
            self.__figure="Dame"
        elif val==13:
            self.__figure="Roi"
        elif val==14:
            self.__figure="As"
        else:
            self.__figure="Aucune"

    def GetValeur(self):
        """
        Retourne la valeur d'une carte
        """
        return self.__valeur
    
    def GetCouleur(self):
        """
        Retourne la couleur d'une carte
        """
        return self.__couleur
    
    def GetFigure(self):
        """
        Retourne la couleur d'une carte
        """
        return self.__figure
    
    
    def _SetFigure(self,val):
        """
        Méthode privée pour changer la figure en fonction de la nouvelle valeur
        pour la cohérence
        """
        if val==11:
            self.__figure="Valet"
        elif val==12:
            self.__figure="Dame"
        elif val==13:
            self.__figure="Roi"
        elif val==14:
            self.__figure="As"
        else:
            self.__figure="Aucune"   

    def SetValeur(self,val):
        """
        Retourne Vrai si la valeur de la carte a été changée par val
        et Faux sinon dans le cas où val n'est pas dans le bon domaine
        """
        if 7<=val<=14:
            self.__valeur=val
            self._SetFigure(val)
            return True
        else:
            return False
    
    def SetCouleur(self,coul):
        """
        Retourne Vrai si la couleur de la carte a été changée par coul et Faux sinon
        
        """        
        liste_couleurs=['Carreau','Coeur','Pique','Trèfle']
        if coul in liste_couleurs:
            self.__couleur=coul
            return True
        else:
            return False
            
    def Describe(self):
        """
        Renvoie les informations sur la carte
        
        """           
        
        return (self.__valeur,self.__couleur,self.__figure)
    

ma_carte=Carte(11,"Trèfle")#création d'un objet, on parle d'instance de la classe. Dans ce contexte, instance est un anglicisme, qui signifie « cas », « exemple ».

```     

À essayer dans la console : 

```    
>>> ma_carte.Describe()
(11, 'Trèfle', 'Valet')
>>> ma_carte.GetValeur()
11
>>> ma_carte.GetCouleur()
'Trèfle'
>>> ma_carte.GetFigure()
'Valet'
>>> ma_carte.SetValeur(13)
True
>>> ma_carte.SetCouleur('Pique')
True
>>> ma_carte.Describe()
(13, 'Pique', 'Roi')
```
La classe `Carte` peut ainsi être utilisée comme un module dans un autre fichier Python.
Si le fichier précédent s'appelle `exemple_classe.py`, on peut rappeler la classe Carte dans un nouveau fichier de la manière suivante :

```
from exemple_classe import Carte

ma_carte=Carte(11,"Trèfle")

>>> ma_carte.Describe()
(11, 'Trèfle', 'Valet')
```

Nous allons maintenant créer une nouvelle classe appelée `JeuDeCarte``. L'objet `jeu_de_carte` sera un objet agrégé, c'est-à-dire constitué de 32 ou 52 cartes, objets de type Carte.

```
from exemple_classe import Carte

import random

class JeuDeCarte:
    """
    Classe définissant un jeu de cartes caractérisé par
    - son nombre de cartes
    - son paquet de cartes
    """
    def __CreerPaquet(self):
        """
        Méthode privée pour créer le paquet de cartes classé par valeur
        et couleur ; il est donc non mélangé
        """
        monpaquet=[]
        if self.__Nbcartes==32:
            num_debut=7
        else:
            num_debut=2
        for coul in ["Carreau","Coeur","Trèfle","Pique"]:
            for i in range(num_debut,15,1):
                new_carte=Carte(i,coul)
                monpaquet.append(new_carte)
        return monpaquet
    
    def __init__(self,nb):
        """
        Constructeur de la classe JeuDeCarte
        """
        self.__Nbcartes=nb
        self.__Paquet=self.__CreerPaquet()
        
    def GetNbcarte(self):
        """
        Retourne le nombre de carte du jeu de cartes
        """
        return self.__Nbcartes
    
    def GetPaquet(self):
        """
        Retourne le paquet de cartes
        """
        return self.__Paquet
        
    def Description_non_melange(self):
        for i in range(len(self.__Paquet)):
            print(self.__Paquet[i].Describe())
    
    def Description_melange(self):
        random.shuffle(self.__Paquet)
        for i in range(len(self.__Paquet)):
            print(self.__Paquet[i].Describe())      

```   

À essayer dans la console : 

```     
    
    >>> mon_jeu=JeuDeCarte(32)
    >>> mon_jeu.Description_non_melange()
(7, 'Carreau', 'Aucune')
(8, 'Trèfle', 'Aucune')
(10, 'Carreau', 'Aucune')
(12, 'Carreau', 'Dame')
(14, 'Pique', 'Aucune')
(8, 'Coeur', 'Aucune')
(10, 'Coeur', 'Aucune')
(11, 'Trèfle', 'Valet')
(11, 'Carreau', 'Valet')
(12, 'Pique', 'Dame')
(14, 'Carreau', 'Aucune')
(9, 'Carreau', 'Aucune')
(14, 'Coeur', 'Aucune')
(13, 'Pique', 'Roi')
(8, 'Pique', 'Aucune')
(11, 'Pique', 'Valet')
(9, 'Trèfle', 'Aucune')
(14, 'Trèfle', 'Aucune')
(12, 'Coeur', 'Dame')
(7, 'Trèfle', 'Aucune')
(13, 'Coeur', 'Roi')
(8, 'Carreau', 'Aucune')
(13, 'Trèfle', 'Roi')
(7, 'Pique', 'Aucune')
(12, 'Trèfle', 'Dame')
(11, 'Coeur', 'Valet')
(10, 'Trèfle', 'Aucune')
(7, 'Coeur', 'Aucune')
(10, 'Pique', 'Aucune')
(9, 'Coeur', 'Aucune')
(9, 'Pique', 'Aucune')
(13, 'Carreau', 'Roi')
	>>> mon_jeu.Description_melange()
(7, 'Carreau', 'Aucune')
(8, 'Trèfle', 'Aucune')
(10, 'Carreau', 'Aucune')
(12, 'Carreau', 'Dame')
(14, 'Pique', 'Aucune')
(8, 'Coeur', 'Aucune')
(10, 'Coeur', 'Aucune')
(11, 'Trèfle', 'Valet')
(11, 'Carreau', 'Valet')
(12, 'Pique', 'Dame')
(14, 'Carreau', 'Aucune')
(9, 'Carreau', 'Aucune')
(14, 'Coeur', 'Aucune')
(13, 'Pique', 'Roi')
(8, 'Pique', 'Aucune')
(11, 'Pique', 'Valet')
(9, 'Trèfle', 'Aucune')
(14, 'Trèfle', 'Aucune')
(12, 'Coeur', 'Dame')
(7, 'Trèfle', 'Aucune')
(13, 'Coeur', 'Roi')
(8, 'Carreau', 'Aucune')
(13, 'Trèfle', 'Roi')
(7, 'Pique', 'Aucune')
(12, 'Trèfle', 'Dame')
(11, 'Coeur', 'Valet')
(10, 'Trèfle', 'Aucune')
(7, 'Coeur', 'Aucune')
(10, 'Pique', 'Aucune')
(9, 'Coeur', 'Aucune')
(9, 'Pique', 'Aucune')
(13, 'Carreau', 'Roi')
```


