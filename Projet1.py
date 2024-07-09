#j'importe ce module pour arreter la boucle infinie while True
import sys

print("BIENVENU SUR MA PLATE-FORME CALCULATRICE\n")

#Ici je crée une boucle infinie dont en chaque doit commencer à parcourir tous les codes qui sera en-dessous
#Boucle While
while True:
    #demande à l'utilisateur
    nombre1 = int(input("Entrez le premier nombre 👇\n"))
    nombre2 = int(input("Entrez le deuxieme nombre 👇\n"))

#Ici je cree le Menu qui doit permettre à l'utilisateur de choisir l'operateur qu'il a besoin d'utiliser
    MENU = input("""Choisissez un opérateur au choix ci-dessous : 👇
    1. Addition
    2. Soustraction
    3. Multiplication
    4. Division
    5. Exponentiation ou la puissance
    6. Division entière
    7. Quitter
    \n""")

#La ligne de code ci-dessous va recupérer le numéro de MENU de chaque opérateur
    choix = input('Entrez votre choix entre "1", "2", "3", "4", "5", "6", "7"\n')

#Ici je fais maintenant avec les conditions de recupérer chaque operateur selon le choix de l'utilisateur
    if choix == "1":
        resultat = nombre1 + nombre2
        print(f"Resultat est :{resultat}")
    elif choix == "2":
        resultat = nombre1 - nombre2
        print(f"Resultat est :{resultat}")
    elif choix == "3":
        resultat = nombre1 * nombre2
        print(f"Resultat est :{resultat}")
    elif choix == "4":
        if nombre2 == 0:
            print("Impossible de diviser un nombre")
        else:
            resultat = nombre1 / nombre2
            round_numbre = round(resultat, 2)
            print(f"Resultat est : {round_numbre}")
    elif choix == "5":
        resultat = nombre1 ** nombre2
        print(f"Resultat est :{resultat}")
    elif choix == "6":
        resultat = nombre1 // nombre2
        print(f"Resultat est :{resultat}")
    elif choix == "7":
        print("Merci pour votre confiance")
        sys.exit()
    else:
        print("Choix invalide")
        


