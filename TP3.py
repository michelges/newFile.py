#Programme nombres aléatoires

import random
nbre_alea = random.randint(0,9)

rep_user = None

while rep_user != nbre_alea:
    rep_user = int(input("veuillez saisir une valeur de votre choix svp comprise entre 0 et 9 \n"))
    if rep_user < nbre_alea:
        print("Dommage ! Réessayez à nouveau, \n") 
    elif rep_user > nbre_alea:
        print("Vous y êtes presque \n")
    else:
        print("Bravo !!! Vous avez trouvé. Félicitation !")
