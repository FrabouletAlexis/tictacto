#Fontion#
def initialiseGrille(grille):
    for compteur in range (0,8):
        grille[compteur]=" "

def afficheGrille (grille):
    for i in range (0,3):
        print(grille[3*i],grille[3*i+1],grille[3*i+2])

def ajouteSymbole(grille,joueur):
    choixIncorrect==True
    while( choixIncorrect==True):
        i= int(input("Sur quelle ligne voulez-vous jouer ?"))
        j= int(input("Sur quelle colonne voulez-vous ?"))
        if (grille[3*i+j]!=" "):
            grille [3*i+j] = joueur
            choixIncorrect==False

def testeVictoireVerticale(grille):
    compteur=0
    while (compteur<3):
        if (grille[compteur]!=" ") and (grille[compteur]==grille[compteur+3]) and (grille[compteur]==grille[compteur+6]):
            return True
    return False

def testeVictoireHorizontale (grille):
    compteur=0
    while (compteur<3):
        if (grille[compteur] != " ") and (grille[compteur*3] == grille [compteur*3+1]) and (grille[compteur*3] == grille[compteur*3+2]):
            return True
    return False

def testeVictoireDiagonale (grille):
    compteur=0
    if (grille[compteur] !=" ") and (grille [4]==grille[0]) and (grille[4]==grille [6]):
        return True
    elif (grille[compteur] !=" ") and (grille [4]==grille[2]) and (grille[4]==grille [6]):
        return True
    return False

def testeJeuNul (victoire,tour):
    if (tour==9) and (victoire==False):
        return True
    return False  

#Prog#

grille=["*","*","*","*","*","*","*","*","*","*"]
afficheGrille(grille)
    
input()