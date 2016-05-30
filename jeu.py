# -*- coding: utf-8 -*-

# Fonctions contenant les règles du jeu ainsi que le contexte
def contexte():
    print("\n\nContexte et regles du jeu: \n")
    print("Vous etes dans un labyrinthe poursuivi par un farfadet douteu, ")
    print("vous essayez de lui echapper depuis des heures quand soudain... ")
    print("Apparait devant vos yeux 3 passages distincts.")
    print("Vous devez choisir un des passages avant que le farfadet ne vous rattrape.")
    print("Un d'entres eux vous fera sortir du labyrinthe saint et sauf,")
    print("un autre vous menera directement dans le chaudron du farfadet,")
    print("et le dernier donne sur 3 nouveaux passage ou les possibilites sont les memes.")
    print("A vous de jouez!! Bonne chance\n\n")
#Fonctions affichant les differents passages
def passages():
    print(" __________        __________        __________ ")
    print(" |        |        |        |        |        | ")
    print(" |        |        |        |        |        | ")
    print(" |    1   |        |    2   |        |    3   | ")
    print(" |        |        |        |        |        | ")
    print(" |        |        |        |        |        | ")
#Declaration (dans un tableau) des différents choix possibles
tableau=[]
tableau.append("\nVous avez faim? Dommage, ce soir c'est vous que l'on mange! Game over.")
tableau.append("\n3 nouveaux passages, ressayez.. C'est peut etre votre jour de chance.")
tableau.append("\nBravo! Suivez la lumiere et vous sortirez du labyrinthe.")

#Programme principal
contexte()
jouer=True
while jouer==True:
    passages()
    rep=input("\nQuel passage desirez-vous prendre? ")
    if rep==1 or rep==2 or rep==3:
        print(tableau[rep-1])
        if rep==1 or rep==3:
            jouer=False
    else:
        print("Vous n'avez choisi aucun passage existant.")
        print("Merci d'avoir participé, au revoir!")
        jouer=False
