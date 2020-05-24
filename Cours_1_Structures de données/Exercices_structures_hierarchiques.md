## Exercices structures hierarchiques

**Exercice 1** :  On donne ci-dessous un tableau caractérisant un arbre.

<table>
<tr>
<td>Noeud</td><td>Étiquette</td><td>Noeud du SAG</td><td>Noeud du SAD</td>
</tr>
<tr>
<td>1</td><td>*</td><td>2</td><td>3</td>
</tr>
<tr>
<td>2</td><td>+</td><td>4</td><td>5</td>
</tr>
<tr>
<td>3</td><td>-</td><td>6</td><td>7</td>
</tr>
<tr>
<td>4</td><td>3</td><td> </td><td> </td>
</tr>
<tr>
<td>5</td><td>/</td><td>8</td><td>9</td>
</tr>
<tr>
<td>6</td><td>8</td><td> </td><td> </td>
</tr>
<tr>
<td>7</td><td>*</td><td>10</td><td>11</td>
</tr>
<tr>
<td>8</td><td>4</td><td> </td><td> </td>
</tr>
<tr>
<td>9</td><td>2</td><td> </td><td> </td>
</tr>
<tr>
<td>10</td><td>2</td><td> </td><td> </td>
</tr>
<tr>
<td>11</td><td>3</td><td> </td><td> </td>
</tr>
</table>

1. Représenter l'arbre correspondant.
2. Quelle est la hauteur de cet arbre ?
3. Cet arbre est-il binaire, complet, dégénéré ?
4. Quel est le résultat de cette suite d'opérations mathématiques ? On parcourt l'arbre étiqueté de la gauche vers la droite, en évaluant en premier les opérations concernant les feuilles les plus basses.

**Exercice 2** : On donne la suite d'instructions suivantes :
A=CREER_ARBRE(2,CREER_ARBRE_FEUILLE(4),CREER_ARBRE_FEUILLE(3))
B=CREER_ARBRE(5,CREER_ARBRE_VIDE(),CREER_ARBRE_FEUILLE(6))
C=CREER_ARBRE(1,A,B)

1. Réprésenter la situation sous la forme d'un arbre.
2. Donner l'arbre correspondant à l'instruction : T=SAD(C).
3. Quelle est la valeur retournée par l'instruction suivante : r=RACINE(B).

