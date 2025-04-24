import random

# Classe représentant une cellule du labyrinthe avec des murs au nord, est, sud, ouest
class Cellule:
    def __init__(self, murNord, murEst, murSud, murOuest):
        self.murs = {'N': murNord, 'E': murEst, 'S': murSud, 'O': murOuest}

# Classe représentant le labyrinthe entier
class Labyrinthe:
    def __init__(self, hauteur, longueur):
        self.hauteur = hauteur
        self.longueur = longueur
        self.grille = self.construire_grille(hauteur, longueur)  # Création de la grille initiale

    # Méthode pour construire la grille initiale du labyrinthe avec tous les murs fermés
    def construire_grille(self, hauteur, longueur):
        grille = []
        for i in range(hauteur):
            ligne = []
            for j in range(longueur):
                cellule = Cellule(True, True, True, True)
                ligne.append(cellule)
            grille.append(ligne)
        return grille

    # Crée un passage entre deux cellules adjacentes en retirant les murs correspondants
    def creer_passage(self, c1_lig, c1_col, c2_lig, c2_col):
        cellule1 = self.grille[c1_lig][c1_col]
        cellule2 = self.grille[c2_lig][c2_col]
        if c1_lig - c2_lig == 1 and c1_col == c2_col:  # cellule2 est au nord de cellule1
            cellule1.murs['N'] = False
            cellule2.murs['S'] = False
        elif c1_lig == c2_lig and c1_col == c2_col + 1:  # cellule2 est à l'ouest
            cellule1.murs['O'] = False
            cellule2.murs['E'] = False
        elif c1_lig == c2_lig and c1_col == c2_col - 1:  # cellule2 est à l'est
            cellule1.murs['E'] = False
            cellule2.murs['O'] = False
        elif c1_lig == c2_lig - 1 and c1_col == c2_col:  # cellule2 est au sud
            cellule1.murs['S'] = False
            cellule2.murs['N'] = False

    # Méthode récursive pour créer un labyrinthe en divisant l'espace (type "division récursive")
    def creer_labyrinthe(self, ligne, colonne, hauteur, longueur):
        if hauteur == 1:
            # Cas ligne unique : passage horizontal
            for k in range(longueur - 1):
                self.creer_passage(ligne, colonne + k, ligne, colonne + k + 1)
        elif longueur == 1:
            # Cas colonne unique : passage vertical
            for k in range(hauteur - 1):
                self.creer_passage(ligne + k, colonne, ligne + k + 1, colonne)
        else:
            if longueur > hauteur:
                milieu = longueur // 2
                self.creer_labyrinthe(ligne, colonne, hauteur, milieu)
                self.creer_labyrinthe(ligne, colonne + milieu, hauteur, longueur - milieu)
                # Crée une ouverture entre les deux sous-labyrinthes horizontaux
                passage = ligne + random.randint(0, hauteur - 1)
                self.creer_passage(passage, colonne + milieu - 1, passage, colonne + milieu)
            else:
                milieu = hauteur // 2
                self.creer_labyrinthe(ligne, colonne, milieu, longueur)
                self.creer_labyrinthe(ligne + milieu, colonne, hauteur - milieu, longueur)
                # Crée une ouverture entre les deux sous-labyrinthes verticaux
                passage = colonne + random.randint(0, longueur - 1)
                self.creer_passage(ligne + milieu - 1, passage, ligne + milieu, passage)

    # Affiche le labyrinthe dans la console avec des +, -, | pour les murs
    def afficher(self):
        for i in range(len(self.grille)):
            ligne_haut = ""
            ligne_milieu = ""
            for j in range(len(self.grille[0])):
                if self.grille[i][j].murs['N']:
                    ligne_haut += "+---"
                else:
                    ligne_haut += "+   "
                if self.grille[i][j].murs['O']:
                    ligne_milieu += "|   "
                else:
                    ligne_milieu += "    "
            ligne_haut += "+"
            if self.grille[i][-1].murs['E']:
                ligne_milieu += "|"
            else:
                ligne_milieu += " "
            print(ligne_haut)
            print(ligne_milieu)
        # Affiche la ligne du bas du labyrinthe
        print("+---" * len(self.grille[0]) + "+")

    # Trouve un chemin de (0, 0) à (fin) avec un DFS
    def trouver_solution(self):
        hauteur, longueur = self.hauteur, self.longueur
        start = (0, 0)
        end = (hauteur - 1, longueur - 1)
        chemin = []

        def dfs(lig, col, visite):
            if (lig, col) == end:
                chemin.append((lig, col))
                return True
            visite.add((lig, col))
            directions = [('N', -1, 0), ('E', 0, 1), ('S', 1, 0), ('O', 0, -1)]
            for direction, dl, dc in directions:
                if not self.grille[lig][col].murs[direction]:
                    nl, nc = lig + dl, col + dc
                    if 0 <= nl < hauteur and 0 <= nc < longueur and (nl, nc) not in visite:
                        if dfs(nl, nc, visite):
                            chemin.append((lig, col))
                            return True
            return False

        dfs(0, 0, set())
        chemin.reverse()
        return chemin

    # Affiche le labyrinthe avec la solution marquée par des étoiles "*"
    def afficher_avec_solution(self, chemin):
        chemin_set = set(chemin)
        for i in range(self.hauteur):
            ligne_haut = ""
            ligne_milieu = ""
            for j in range(self.longueur):
                if self.grille[i][j].murs['N']:
                    ligne_haut += "+---"
                else:
                    ligne_haut += "+   "
                if self.grille[i][j].murs['O']:
                    ligne_milieu += "|"
                else:
                    ligne_milieu += " "
                if (i, j) in chemin_set:
                    ligne_milieu += " * "
                else:
                    ligne_milieu += "   "
            ligne_haut += "+"
            if self.grille[i][-1].murs['E']:
                ligne_milieu += "|"
            else:
                ligne_milieu += " "
            print(ligne_haut)
            print(ligne_milieu)
        print("+---" * self.longueur + "+")

# Code principal pour créer, afficher et résoudre un labyrinthe
if __name__ == "__main__":
    lab = Labyrinthe(5, 5)
    lab.creer_labyrinthe(0, 0, 5, 5)
    # Ouvre l'entrée et la sortie
    lab.grille[0][0].murs['O'] = False
    lab.grille[4][4].murs['E'] = False

    solution = lab.trouver_solution()
    lab.afficher_avec_solution(solution)
