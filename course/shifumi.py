import random

dictShifumi = {1:"Pierre", 2:"Feuille", 3:"Ciseaux"}
victoriesOrdinateur = 0
victoriesPlayer = 0

while victoriesOrdinateur < 2 and victoriesPlayer < 2:

    ordi = dictShifumi[random.randint(1, 3)]
    player = input("Pierre, Feuille ou Ciseaux ? ")

    print("Vous avez choisi Pierre tandis que l'ordinateur a choisi", ordi)

    if player == "Pierre":

        if ordi == "Pierre":

            print("Egalité !")

        elif ordi == "Feuille":

            print("Perdu !")
            victoriesOrdinateur += 1

        else:

            print("Gagné !")
            victoriesPlayer += 1

    elif player == "Feuille":

            if ordi == "Pierre":

                print("Gagné !")
                victoriesPlayer += 1
                

            elif ordi == "Feuille":

                print("Egalité !")

            else:

                print("Perdu !")
                victoriesOrdinateur += 1

    elif player == "Ciseaux":

            if ordi == "Pierre":

                print("Perdu !")
                victoriesOrdinateur += 1

            elif ordi == "Feuille":

                print("Gagné !")
                victoriesPlayer += 1

            else:

                print("Egalité !")

    else:

        print("Vous n'avez pas choisi Pierre, Feuille ou Ciseaux !")
        
if victoriesOrdinateur == 2:
    
    print("Vous avez perdu le BO3 !")
    
else:
    
    print("Vous avez gagné le BO3 !")