
def initialiseGrille(grille):
    for compteur in range (0,8):
        grille[compteur]=" "

def afficheGrille (grille):
    for i in range (0,2):
        print(grille[3*i],grille[3*i+1],grille[3*i+2],"\n")

def ajouteSymbole(grille,joueur):
    choixIncorrect=True
    while( choixIncorrect=True):
        i= int(input("Sur quelle ligne voule-vous jouer ?"))
        j= int(input("Sur quelle colonne voule-vous ?"))
        if (grille[3*i+j]!=" "):
            grille [3*i+j] = joueur
            choixIncorrect=False
            
input()