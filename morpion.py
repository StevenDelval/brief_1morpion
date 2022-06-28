grille={
    "A1":"-","A2":"-","A3":"-",
    "B1":"-","B2":"-","B3":"-",
    "C1":"-","C2":"-","C3":"-"
}                                                                                                                                                                         
 

def afficher_grille(grille):
    """Afficher la grille du morpion."""
    print("_  ","|","1","|","2","|","3","|",sep="",end="\n\n")
    for ligne in ["A","B","C"]:
        print(ligne+" ","|",end="")
        for colonne in ["1","2","3"]:
            print(grille[ligne+colonne],end="|")
        print("\n")

def verification_grille(grille,joueurs,numero):
    """Vérifie si un joueur a gagner ou s'il y a égalité.
    param: joueurs (liste) liste des joueurs
    param: numero (int) numero du joueur entre 0 et 1
    return: (boolean) vrai si la grille n'est pas terminer et faux si un joueur a gagner ou si égalité 
    """


    #Sur une ligne
    for ligne in ["A","B","C"]:   
        if grille[ligne+"1"]==grille[ligne+"2"]==grille[ligne+"3"]!="-":
            print ("{0} a gagné sur la ligne {1}".format(joueurs[numero],ligne))
            return False


    #Sur une colonne
    for colonne in ["1","2","3"]:
        if grille["A"+colonne]==grille["B"+colonne]==grille["C"+colonne]!="-":
            print ("{0} a gagné sur la colonne {1}".format(joueurs[numero],colonne))
            return False


    #Sur les diagonales
    if grille["A"+"1"]==grille["B"+"2"]==grille["C"+"3"]!="-":
        print ("{} a gagné sur la diagonale".format(joueurs[numero]))
        return False
    if grille["A"+"3"]==grille["B"+"2"]==grille["C"+"1"]!="-":
        print ("{} a gagné sur la diagonale".format(joueurs[numero]))
        return False     


    #Verifie si toute les cases sont vide
    nombre_case_vide=0
    for ligne in ["A","B","C"]:
        for colonne in ["1","2","3"]:
            if grille[ligne+colonne]=="-":
                nombre_case_vide+=1
    if nombre_case_vide==0:
        print ("Egalité")
        return False     

    
    return  True

joueurs=[]
joueurs.append(input("Nom du joueur n°1 : ") or "joueur n°1")
joueurs.append(input("Nom du joueur n°2 : ") or "joueur n°2")
numero=0
afficher_grille(grille)
while verification_grille(grille,joueurs,(numero-1)%2):
    
    case_joueur=(input("{} choisissez votre case : ".format(joueurs[numero])))
    if case_joueur in grille:
        if grille[case_joueur]=="-":
            if numero ==0:
                grille[case_joueur]="X"
            else :
                grille[case_joueur]="O"
            numero = (numero+1)%2
        else:
            print("Le coup {} n'est pas possible car un joueur là déjà prise".format(case_joueur))
            continue   
    else:
        
        print("Le coup {} n'est pas possible car il n'est pas dans la grille".format(case_joueur))
        continue
        
    

    afficher_grille(grille)

