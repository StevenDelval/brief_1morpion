def afficher_grille(grille):
    """
    Fonction qui affiche la grille du jeu
    :param grille: (dict) Dictionnaire qui représente la grille
    """
    print("     0 | 1 | 2 |\n")
    for cle in grille:
        print(cle+" ","| ",end="")
        for elt in grille[cle]:
            print(elt,end=" | ")
        print("\n")
        

def est_gagnante(grille):
    """
    Fonction qui vérifie si quelqu'un a gagné sur cette grille
    :param grille : (dict) La grille du morpion 
    :return: (boolean) Renvoie vrai si quelqu'un a gagné, False sinon
    """

    #Vérification des lignes 
    
    for cle, ligne in grille.items():
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != "-":
            return True
    
    #Vérification des colonnes
    
    for i in range(3):
        if grille["A"][i]  == grille["B"][i]  == grille["C"][i] and grille["A"][i]  != "-":
            return True
    
    #Vérification des diagonales

    if grille["A"][0]  == grille["B"][1]  == grille["C"][2] and grille["A"][0]  != "-":
        return True
    if grille["A"][2]  == grille["B"][1]  == grille["C"][1] and grille["A"][2]  != "-":
        return True

    #Si aucun de ces cas est gagnant
    return False


def est_pleine(grille):
    """
    Fonction qui vérifie si la grille est pleine
    :param grille: (dict) La grille du morpion
    :return: (boolean) Renvoie vrai si la grille est pleine, False sinon
    """
    for cle,ligne in grille.items():
        if "-" in ligne:
            return False
    return True


def jouer_coup(grille,joueur,coup):
    """
    Fonction qui permet de jouer un coup
    :param grille: (dict) La grille du morpion
    :param joueur: (str) Le caractère qui va être placé sur la grille
    :param coup: (str) chaine de caractères qui contient en position 0 une lettre entre A,B ou C et en position 1 0,1ou 2
    :return : Renvoie le nouveau plateau de jeu si le coup est valide. False sinon
    """
    if coup[0] in grille and int(coup[1]) in range(3):
        if grille[coup[0]][int(coup[1])] == "-":
            grille[coup[0]][int(coup[1])]=joueur
            return grille
    return False
    

#Programme principal    

plateau={
    "A" : ["-","-","-"],
    "B" : ["-","-","-"], 
    "C" : ["-","-","-"]
}

fin= False

joueur="X"

while not fin:
    afficher_grille(plateau)
    coup = input("({}) Entrez votre coup: (Les lignes vont de A à C et les colonnes de 0 à 2 inclus et qui n'est pas déjà occupé : ".format(joueur))
    grille2 = jouer_coup(plateau,joueur,coup) # grille2 le nouveau plateau si le coups est valide, False sinon
    while grille2 == False:
        # On demande à l'utilisateur de rentre une valeur tant qu'il n'a pas donné une valeur correcte
        coup = input("({}) Entrez votre coup: (Les lignes vont de A à C et les colonnes de 0 à 2 inclus et qui n'est pas déjà occupé : ".format(joueur))
        grille2 = jouer_coup(plateau,joueur,coup)
    plateau = grille2

    gagnee = est_gagnante(plateau)
    pleine = est_pleine(plateau)

    fin = gagnee or pleine

    if gagnee:
        print("Félicitation joueur {} !".format(joueur))
    elif pleine:
        print("Egalité !")
    else:
        if joueur == "X":
            joueur = "O"
        else:
            joueur = "X"
