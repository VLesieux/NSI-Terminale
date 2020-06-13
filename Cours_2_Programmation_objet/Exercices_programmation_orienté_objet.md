## Exercices programmation orienté objet

**Exercice 1** :  

On souhaite caractériser la notion de point telle qu'elle existe en deux dimensions : aussi bien en coordonnées cartésiennes qu'en coordonnées polaires.
Une version simplifiée est la suivante.

```python
import math
x=float(input("abscisse : "))
y=float(input("ordonnée : "))
if (x>0):
    θ=math.atan(y/x)
if (x<0) and (y>=0):
    θ=math.atan(y/x)+math.pi
if (x<0) and (y<0):
    θ=math.atan(y/x)-math.pi
if (x==0) and (y>0):
    θ=math.pi/2
if (x==0) and (y<0):
    θ=-math.pi/2
if (x==0) and (y==0):
    θ=0
θ=180*θ/math.pi
r=math.sqrt(x**2+y**2)
print("le rayon r vaut :",r," et l'angle θ(degré) vaut : ",θ)
```
Réaliser une classe Point pour réaliser ceci : 

```python
>>> A=Point(-2,5)
>>> A.convertis()
le rayon r vaut : 5.385164807134504  et l'angle θ(degré) vaut :  111.80140948635182
>>> B=Point(5,5)
>>> B.convertis()
le rayon r vaut : 7.0710678118654755  et l'angle θ(degré) vaut :  45.0
```

On créera deux méthodes privées `get_θ` et `get_r` et une méthode publique `convertis`.

**Exercice 2** : 


1. Proposer une implémentation sous forme de classe de la structure abstraite Pile vue dans le  [cours précédent](https://github.com/VLesieux/NSI-Terminale/blob/master/Cours_1_Structures%20de%20donn%C3%A9es/1.Cours_Structures_donn%C3%A9es_lin%C3%A9aires_et_dictionnaires.md) . On utilisera le type liste pour typer les attributs privés et des méthodes publiques pour manipuler ceux-ci.

Réaliser une classe Pile pour réaliser ceci : 

```python
>>> ma_pile=Pile()
>>> ma_pile.empiler(5)
>>> ma_pile.empiler(12)
>>> ma_pile.montrer()
[5, 12]
>>> ma_pile.depiler()
12
>>> ma_pile.montrer()
[5]
```


2. Faire de même pour la structure File.

Réaliser une classe File pour réaliser ceci : 

```python
>>> ma_file=File()
>>> ma_file.enfiler(5)
>>> ma_file.enfiler(12)
>>> ma_file.montrer()
[5, 12]
>>> ma_file.defiler()
5
>>> ma_file.montrer()
[12]
```

**Exercice 3** : 

Le domino est un jeu très ancien composé de 28 pièces toutes différentes. Sur chacune de ces pièces, il y a deux côtés constitués de 0 (blanc) à 6 points. Lorsque deux côtés possèdent le même nombre de points, on l'appelle domino double.

1. Proposer une classe Domino permettant de représenter une pièce. Les objets seront initialisés par les valeurs portées par les des deux côtés (gauche et droite). On définit des méthodes `est_double` et `est_blanc` pour tester si le domino est double ou blanc. On implémentera également une méthode `compte` pour compter le nombre de points sur un domino. On ajoutera une méthode `affiche` qui affiche les valeurs des deux faces de manière horizontale pour un domino classique et de manière verticale pour un domino double.

2. Proposer une classe JeuDeDomino permettant de manipuler le jeu de domino complet. On créera une méthode pour mélanger le jeu et pour distribuer selon 2 joueurs.

	On utilisera la méthode random.shuffle(mylist)
   
```python
>>> import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
>>> mylist
['banana', 'apple', 'cherry']
```
   

3. En utilisant cette classe, on affichera le jeu des 2 joueurs.
```python
>>> mon_jeu=JeuDeDomino()
>>> mon_jeu.montre()
Joueur 1
- - - - - - - - -
|               |
|   6   |   3   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   6   |   5   |
|               |
- - - - - - - - -
- - - -
|      |
|   0  |  
|- - - |
|   0  |  
|      |
- - - -
- - - -
|      |
|   5  |  
|- - - |
|   5  |  
|      |
- - - -
- - - - - - - - -
|               |
|   6   |   1   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   5   |   4   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   3   |   1   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   5   |   0   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   3   |   2   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   5   |   1   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   5   |   3   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   6   |   0   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   4   |   0   |
|               |
- - - - - - - - -
- - - -
|      |
|   4  |  
|- - - |
|   4  |  
|      |
- - - -
-------------------------------
Joueur 2
- - - - - - - - -
|               |
|   1   |   0   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   2   |   1   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   6   |   4   |
|               |
- - - - - - - - -
- - - -
|      |
|   2  |  
|- - - |
|   2  |  
|      |
- - - -
- - - - - - - - -
|               |
|   3   |   0   |
|               |
- - - - - - - - -
- - - -
|      |
|   6  |  
|- - - |
|   6  |  
|      |
- - - -
- - - - - - - - -
|               |
|   6   |   2   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   5   |   2   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   2   |   0   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   4   |   2   |
|               |
- - - - - - - - -
- - - -
|      |
|   3  |  
|- - - |
|   3  |  
|      |
- - - -
- - - -
|      |
|   1  |  
|- - - |
|   1  |  
|      |
- - - -
- - - - - - - - -
|               |
|   4   |   1   |
|               |
- - - - - - - - -
- - - - - - - - -
|               |
|   4   |   3   |
|               |
- - - - - - - - -
```

Indication :
Pour obtenir les 28 pièces sans répétition du symétrique :
```python
jeu=[]
for i in range(7):
    for j in range(i+1):
        jeu.append((i,j))
print(jeu)
>>> %Run Domino.py
[(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
```

