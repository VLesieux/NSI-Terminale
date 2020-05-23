## Exercices structures de données linéaires

**Exercice 1** :  On se donne la séquence d'instructions suivantes:

```python
L1=CREER_LISTE_VIDE(5)
INSERER(L1,1,1)
INSERER(L1,2,2)
INSERER(L1,3,3)
INSERER(L1,4,4)
L2=CREER_LISTE_VIDE(5)
INSERER(L2,LIRE(L1,1),1)
INSERER(L2,LIRE(L1,2),1)
INSERER(L2,LIRE(L1,3),1)
INSERER(L2,LIRE(L1,4),1)
```

Établir à la main les valeurs de L1 et de L2 après cette suite d'instructions. Quelle est l'opération effectuée ?

**Exercice 2** : On se donne la séquence d'instructions suivantes:

```python
F=CREER_FILE_VIDE(5)
ENFILER(F,4)
ENFILER(F,1)
ENFILER(F,3)
DEFILER(F)
ENFILER(F,8)
DEFILER(F)
```

Établir à la main la valeur de la file F après cette suite d'instructions.

**Exercice 3** : On suppose que l'on a déjà une file F1 qui contient les éléments suivants saisis dans l'ordre alphabétique F1=('A','B','C','D','E').

1) Quel est l'élément issu du défilage de F1 ?

On réalise maintenant une pile P1 qui contient les mêmes éléments saisis dans l'ordre alphabétique.

2) Quel est l'élément issu du dépilage de P1 ?

3) Montrer qu'avec deux piles on peut avoir la même gestion qu'avec une file. Écrire la suite d'instructions nécessaires.

**Exercice 4** : La Notation Polonaire Inversée NPI permet de réaliser des opérations mathématiques sans utiliser de parenthèses. Ici nous nous limiterons à des nombres entiers naturels et aux opérations +,-,* et /. Dans cette notation, les opérateurs sont écrits après les opérandes.

Par exemple, l'expression : 13*(3+2) se saisit en notation NPI : 3 _ 2 _ + _ 13 _ *_

1) Montrer qu'une file semble plus adaptée qu'une pile pour calculer le résultat de la  saisie. Expliquer néanmoins le problème posé par le stockage du résultat intermédiaire dans la file.

2) On suppose que l'on dispose d'une fonction INVERSER_PILE(), proposer un algorithme utilsant une pile permettant de renvoyer le résultat correspondant à l'expression saisie en notation NPI.

**Exercice 5** : En utilisant les méthodes append() et pop() associées aux listes

1) proposer une implémentation des opérations classiques des piles, à savoir CREER_PILE, EMPILER, DEPILER, EST_VIDE.

2)  proposer une implémentation des opérations classiques des files, à savoir CREER_FILE,ENFILER, DEFILER, EST_VIDE.

**Exercice 6** : Dans un logiciel de calcul formel ou dans un éditeur de texte, on trouve une gestion dynamique du parenthésage. Proposer une solution informatique pour programmer une fonction VERIFIER_PARENTHESES(chaine) qui reçoit comme argument une chaîne de caractères constituée uniquement de parenthèses ouvrantes et fermantes, qui renvoie à l'utilisateur un message en cas d'erreur, ou qui lui renvoie les couples d'indices correspondant aux parenthèses ouvrantes et fermantes.
Par exemple :

```python
>>> VERIFIER_PARENTHESES('(())()')
'(1,2)(0,3)(4,5)'
>>> VERIFIER_PARENTHESES('(()()')
Le parenthésage n'est pas correct
```
On utilisera l'implémentation de la pile de l'exercice précédent.



