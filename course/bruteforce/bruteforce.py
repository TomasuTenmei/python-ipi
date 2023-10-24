import random

caracteres = [chr(c) for c in range(ord('a'), ord('z') + 1)] + [chr(c) for c in range(ord('A'), ord('Z') + 1)]
caracteres += ['(' ,')' ,'[' ,']' ,':' ,';' ,'!']
caracteres += [str(i) for i in range(10)]

def new_pass_world(longueur):
    
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    
    return mot_de_passe

def bruteforce(longueur_max = 1, prefixe =""):
    
    liste_mdp = []
    
    if longueur_max == 0:
        
        liste_mdp.append(prefixe)
        return
    
    for char in caracteres:
        
        bruteforce(longueur_max - 1, prefixe + char)
        
    return liste_mdp

def bruteforce_mdp(mdp, prefixe = ""):
    
    pass

def door_lock(text, mdp):
    
    if text == mdp:
        
        return True
    
    return False

def nb_combinaison(longueur_max):
    
    nb_caracteres = len(caracteres)
    value = nb_caracteres ** longueur_max
    
    print(str(nb_caracteres) + " ^ " + str(longueur_max) + " = " + str(value))


mot_de_passe = new_pass_world(6)
retour = False

liste = bruteforce(3)
print(liste)

#while retour == False:
