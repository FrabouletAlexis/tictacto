
def initialiseGrille(grille):
    for compteur in range (0,8):
        grille[compteur]=" "

def afficheGrille (grille):
    for i in range (0,2):
        print(grille[3*i],grille[3*i+1],grille[3*i+2],"\n")
input()