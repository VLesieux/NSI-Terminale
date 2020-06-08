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

1. Proposer une implémentation sous forme de classe de la structure abstraite Pile vue dans le cours précédent.
2. Faire de même pour la structure File.

